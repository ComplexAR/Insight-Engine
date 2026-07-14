#!/usr/bin/env python3
"""Pre-flight for the live cross-lab run.
  OFFLINE (run now):  python3 preflight.py         # imports, prompt, mock dispatch+parse, gates, key presence
  LIVE SMOKE:         OPENAI_API_KEY=sk-... python3 preflight.py --live   # tiny ~free call: endpoint + API shape + JSON parse
Run the smoke BEFORE spending on a full adjudication."""
import os, sys, json

# Resolve the cross-lab model: an explicit CROSSLAB_MODEL env wins (per-run override); else fall
# back to the standing crosslab_model preference; else crosslab.py's built-in default. Set the env
# BEFORE importing crosslab so its DEFAULT_MODEL (read at import) picks it up - keeps crosslab.py
# pure (it never imports prefs).
if not os.environ.get("CROSSLAB_MODEL"):
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "prefs"))
        import prefs as _prefs
        _m = _prefs.get_value("crosslab_model")
        if _m:
            os.environ["CROSSLAB_MODEL"] = _m
    except Exception:
        pass

from crosslab import CrossLabAdjudicator, MockAdjudicator, EgressBlocked

def offline():
    ok=True; print("[offline pre-flight]")
    try:
        p=open(os.path.join(os.path.dirname(__file__),"prompts","adjudicate.txt"),encoding="utf-8").read()
        print(f"  adjudicate.txt loads .......... OK ({len(p)} chars)")
    except Exception as e: print("  adjudicate.txt ................ FAIL", e); ok=False
    try:
        r=MockAdjudicator(egress_policy="redacted").dispatch({"facts":"x"},"P {{blind_package}}")
        assert r["_rung"]=="A-crosslab"; print("  mock dispatch + parse ......... OK")
    except Exception as e: print("  mock dispatch ................. FAIL", e); ok=False
    try:
        MockAdjudicator(egress_policy="full").dispatch({},"p",privileged=True); print("  privileged gate ............... FAIL"); ok=False
    except EgressBlocked: print("  privileged gate ............... OK (blocks egress)")
    try:
        r=MockAdjudicator(egress_policy="redacted").dispatch({},"p",privileged=True,override_privileged=True)
        assert r.get("_rung")=="A-crosslab"; print("  privileged OVERRIDE ........... OK (deliberate act dispatches)")
    except Exception as e: print("  privileged override ........... FAIL", e); ok=False
    try:
        MockAdjudicator(egress_policy="off").dispatch({},"p"); print("  egress-off gate ............... FAIL"); ok=False
    except EgressBlocked: print("  egress-off gate ............... OK (blocks)")
    import crosslab as _cl, urllib.error as _ue, io as _io
    _saved=_cl.urllib.request.urlopen; _hadkey=os.environ.get("OPENAI_API_KEY"); os.environ["OPENAI_API_KEY"]="sk-selftest"
    def _raise_http(code):
        def f(req, timeout=None): raise _ue.HTTPError(_cl.OPENAI_URL, code, "x", {}, _io.BytesIO(b"{}"))
        return f
    try:
        _c=CrossLabAdjudicator(egress_policy="redacted"); _tagok=True
        for _code,_tag in [(401,"[auth 401]"),(404,"[model-unavailable 404]"),(429,"[quota 429]"),(500,"[api 500]")]:
            _cl.urllib.request.urlopen=_raise_http(_code)
            try: _c.dispatch({"f":"x"},"p"); _tagok=False
            except RuntimeError as _e: _tagok=_tagok and ("CROSSLAB-FAILED "+_tag) in str(_e)
        def _raise_url(req, timeout=None): raise _ue.URLError("down")
        _cl.urllib.request.urlopen=_raise_url
        try: _c.dispatch({"f":"x"},"p"); _tagok=False
        except RuntimeError as _e: _tagok=_tagok and "CROSSLAB-FAILED [network]" in str(_e)
        print("  tagged-error mapping .......... "+("OK (401/404/429/api/network)" if _tagok else "FAIL")); ok=ok and _tagok
        # golden request (A1): capture the constructed request without sending; assert byte-identical shape
        _cap={}
        def _capture(req, timeout=None):
            _cap['url']=req.full_url; _cap['data']=req.data
            _cap['auth']=req.get_header("Authorization") or ""
            _cap['ctype']=req.get_header("Content-type") or ""
            raise _ue.URLError("captured")
        _cl.urllib.request.urlopen=_capture
        _gc=CrossLabAdjudicator(egress_policy="redacted")
        try: _gc.dispatch({"f":"x"},"P {{blind_package}}")
        except RuntimeError: pass
        _expbody={"model":_gc.model,"reasoning":{"effort":"high"},"input":_cl.build_blind_text({"f":"x"},"P {{blind_package}}")}
        _goldok=(_cap.get('url')==_cl.OPENAI_URL and _cap.get('data')==json.dumps(_expbody).encode()
                 and _cap.get('auth')=="Bearer sk-selftest" and _cap.get('ctype')=="application/json")
        print("  golden request (openai) ...... "+("OK (url+headers+body byte-identical)" if _goldok else "FAIL")); ok=ok and _goldok
        # per-provider adapters (A2): mock-parse + tagged-error map for google/xai
        _prov_ok=True
        _fixtures={
            "openai": {"output":[{"content":[{"type":"output_text","text":"OK-openai"}]}]},
            "google": {"candidates":[{"content":{"parts":[{"text":"OK-google"}]}}]},
            "xai":    {"choices":[{"message":{"content":"OK-xai"}}]},
        }
        for _pv,_raw in _fixtures.items():
            _txt=_cl.PROVIDERS[_pv]["extract_text"](_raw)
            _rep=_cl._parse_report(json.dumps({"probe":_txt}),"m",_pv)
            _prov_ok=_prov_ok and _txt=="OK-"+_pv and _rep.get("_adjudicator_provider")==_pv and _rep.get("_rung")=="A-crosslab"
        print("  provider parse (openai/google/xai)  "+("OK" if _prov_ok else "FAIL")); ok=ok and _prov_ok
        _perr_ok=True
        for _pv,_kenv in [("google","GEMINI_API_KEY"),("xai","XAI_API_KEY")]:
            os.environ[_kenv]="sk-selftest"
            _ad=CrossLabAdjudicator(provider=_pv, egress_policy="redacted")
            for _code,_tag in [(401,"[auth 401]"),(404,"[model-unavailable 404]"),(429,"[quota 429]"),(500,"[api 500]")]:
                _cl.urllib.request.urlopen=_raise_http(_code)
                try: _ad.dispatch({"f":"x"},"p"); _perr_ok=False
                except RuntimeError as _e: _perr_ok=_perr_ok and ("CROSSLAB-FAILED "+_tag) in str(_e)
            os.environ.pop(_kenv,None)
        print("  provider errors (google/xai) ....... "+("OK" if _perr_ok else "FAIL")); ok=ok and _perr_ok
        # same-lineage hard guard (A3): rung A must refuse the analyser's Anthropic lineage
        _g=_cl._same_lineage_reason
        _guard_ok=(bool(_g("anthropic","gpt")) and bool(_g("openai","claude-opus-5")) and bool(_g("openai","opus"))
                   and bool(_g("openai","x","https://api.anthropic.com/v1")) and bool(_g("openai","x","","anthropic"))
                   and bool(_g("openai","x","","claude")) and (not _g("openai","gpt-5.6-sol"))
                   and (not _g("xai","grok-4.5")) and (not _g("google","gemini-3.5-flash"))
                   and (not _g("openai","opusfoo")) and bool(_g("openai","x","api.anthropic.com")))
        os.environ["OPENAI_API_KEY"]="sk-selftest"
        try:
            CrossLabAdjudicator(provider="openai", model="claude-opus-5", egress_policy="redacted").dispatch({"f":"x"},"p")
            _guard_ok=False
        except _cl.EgressBlocked as _e:
            _guard_ok=_guard_ok and ("CROSSLAB-BLOCKED [same-lineage]" in str(_e))
        print("  same-lineage guard (A3) ...... "+("OK (blocks Anthropic, allows others)" if _guard_ok else "FAIL")); ok=ok and _guard_ok
    finally:
        _cl.urllib.request.urlopen=_saved
        if _hadkey is None: os.environ.pop("OPENAI_API_KEY",None)
        else: os.environ["OPENAI_API_KEY"]=_hadkey
    print(f"  cross-lab model .............. {CrossLabAdjudicator().model}")
    key=bool(os.environ.get("OPENAI_API_KEY"))
    print(f"  OPENAI_API_KEY set ............ {'yes' if key else 'NO — set it before --live'}")
    print("  =>", "READY for --live" if (ok and key) else ("offline OK; set OPENAI_API_KEY for --live" if ok else "OFFLINE CHECKS FAILED"))
    return ok

def live_smoke():
    print("[live smoke — minimal, low-token, low-effort]")
    adj=CrossLabAdjudicator(egress_policy="redacted", effort="low")
    prompt='Reply with ONLY this JSON, nothing else: {"ok": true, "saw_task": true}\n{{blind_package}}'
    try:
        r=adj.dispatch({"smoke":"ping"}, prompt, privileged=False)
        print("  parsed response:", json.dumps(r))
        good = r.get("ok") or r.get("saw_task")
        print("  =>", "endpoint + API shape + JSON parse OK" if good else "parsed, but shape unexpected — inspect above / adjust crosslab.py body")
    except Exception as e:
        print("  live smoke FAILED:", e)
        print("  => on an HTTP 4xx about the request body, adjust the body in crosslab.py to match CURRENT OpenAI Responses-API docs.")

if __name__=="__main__":
    if "--live" in sys.argv:
        if not os.environ.get("OPENAI_API_KEY"): print("set OPENAI_API_KEY first."); sys.exit(1)
        live_smoke()
    else: offline()
