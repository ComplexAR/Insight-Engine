#!/usr/bin/env python3
"""Pre-flight for the live cross-lab run.
  OFFLINE (run now):  python3 preflight.py         # imports, prompt, mock dispatch+parse, gates, key presence
  LIVE SMOKE:         set the resolved provider's API key, then:  python preflight.py --live   # tiny call: endpoint + shape + JSON parse
Run the smoke BEFORE spending on a full adjudication."""
import os, sys, json

# Resolve adjudication prefs -> CROSSLAB_* env (provider / model / base-url / key-env / lineage),
# BEFORE importing crosslab so it reads them at import (keeps crosslab.py pure). A shell env var
# always wins; else the standing preference; else the adapter's built-in default.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    import crosslab_env
    crosslab_env.resolve()
except Exception:
    pass

from crosslab import CrossLabAdjudicator, MockAdjudicator, EgressBlocked

def offline():
    ok=True; print("[offline pre-flight]")
    try:
        for _n in ("adjudicate.txt", "adversarial.txt"):
            p=open(os.path.join(os.path.dirname(__file__),"prompts",_n),encoding="utf-8").read()
            print(f"  {_n} loads ".ljust(32,".")+f" OK ({len(p)} chars)")
    except Exception as e: print("  prompts ....................... FAIL", e); ok=False
    try:
        r=MockAdjudicator(provider="openai", egress_policy="redacted").dispatch({"facts":"x"},"P {{blind_package}}")
        assert r["_rung"]=="A-crosslab"; print("  mock dispatch + parse ......... OK")
    except Exception as e: print("  mock dispatch ................. FAIL", e); ok=False
    try:
        MockAdjudicator(provider="openai", egress_policy="full").dispatch({},"p",privileged=True); print("  privileged gate ............... FAIL"); ok=False
    except EgressBlocked: print("  privileged gate ............... OK (blocks egress)")
    try:
        r=MockAdjudicator(provider="openai", egress_policy="redacted").dispatch({},"p",privileged=True,override_privileged=True)
        assert r.get("_rung")=="A-crosslab"; print("  privileged OVERRIDE ........... OK (deliberate act dispatches)")
    except Exception as e: print("  privileged override ........... FAIL", e); ok=False
    try:
        MockAdjudicator(provider="openai", egress_policy="off").dispatch({},"p"); print("  egress-off gate ............... FAIL"); ok=False
    except EgressBlocked: print("  egress-off gate ............... OK (blocks)")
    import crosslab as _cl, urllib.error as _ue, io as _io
    _saved=_cl.urllib.request.urlopen; _hadkey=os.environ.get("OPENAI_API_KEY"); os.environ["OPENAI_API_KEY"]="sk-selftest"
    def _raise_http(code):
        def f(req, timeout=None): raise _ue.HTTPError(_cl.OPENAI_URL, code, "x", {}, _io.BytesIO(b"{}"))
        return f
    try:
        _c=CrossLabAdjudicator(provider="openai", egress_policy="redacted"); _tagok=True
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
        _gc=CrossLabAdjudicator(provider="openai", egress_policy="redacted")
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
        # "Other" OpenAI-compatible mode (A4)
        _other_ok=True
        os.environ["CROSSLAB_OTHER_API_KEY"]="sk-selftest"; os.environ["CROSSLAB_OTHER_LINEAGE"]="mistral"
        _oc={}
        def _cap2(req, timeout=None):
            _oc['url']=req.full_url; _oc['auth']=req.get_header("Authorization"); _oc['data']=req.data; _oc['ctype']=req.get_header("Content-type"); raise _ue.URLError("cap")
        _cl.urllib.request.urlopen=_cap2
        try: CrossLabAdjudicator(provider="other", base_url="https://api.example.com/v1", model="some-model", egress_policy="redacted").dispatch({"f":"x"},"P {{blind_package}}")
        except RuntimeError: pass
        _expb={"model":"some-model","messages":[{"role":"user","content":_cl.build_blind_text({"f":"x"},"P {{blind_package}}")}]}
        _other_ok=_other_ok and _oc.get('url')=="https://api.example.com/v1/chat/completions" and _oc.get('auth')=="Bearer sk-selftest" and _oc.get('ctype')=="application/json" and _oc.get('data')==json.dumps(_expb).encode()
        try: CrossLabAdjudicator(provider="other", base_url="http://x/v1", model="m", egress_policy="redacted").dispatch({"f":"x"},"p"); _other_ok=False
        except _cl.EgressBlocked as _e: _other_ok=_other_ok and "[no-base-url]" in str(_e)
        try: CrossLabAdjudicator(provider="other", base_url="https://api.example.com/v1", model="", egress_policy="redacted").dispatch({"f":"x"},"p"); _other_ok=False
        except _cl.EgressBlocked as _e: _other_ok=_other_ok and "[no-model]" in str(_e)
        os.environ.pop("CROSSLAB_OTHER_LINEAGE",None)
        try: CrossLabAdjudicator(provider="other", base_url="https://api.example.com/v1", model="m", egress_policy="redacted").dispatch({"f":"x"},"p"); _other_ok=False
        except _cl.EgressBlocked as _e: _other_ok=_other_ok and "[lineage-undeclared]" in str(_e)
        os.environ["CROSSLAB_OTHER_LINEAGE"]="mistral"
        try: CrossLabAdjudicator(provider="other", base_url="https://api.anthropic.com/v1", model="m", egress_policy="redacted").dispatch({"f":"x"},"p"); _other_ok=False
        except _cl.EgressBlocked as _e: _other_ok=_other_ok and "[same-lineage]" in str(_e)
        os.environ.pop("CROSSLAB_OTHER_API_KEY",None); os.environ.pop("CROSSLAB_OTHER_LINEAGE",None)
        print("  other OpenAI-compat mode (A4)  "+("OK" if _other_ok else "FAIL")); ok=ok and _other_ok
        # provider routing + mismatch (A6)
        import crosslab_env as _ce
        _route_ok=(_ce.infer_provider("gpt-5.6-sol")=="openai" and _ce.infer_provider("gemini-3.5-flash")=="google"
                   and _ce.infer_provider("grok-4.5")=="xai" and _ce.infer_provider("mystery-1") is None)
        os.environ["GEMINI_API_KEY"]="sk-selftest"
        try: CrossLabAdjudicator(provider="google", model="gpt-5.6-sol", egress_policy="redacted").dispatch({"f":"x"},"p"); _route_ok=False
        except _cl.EgressBlocked as _e: _route_ok=_route_ok and "[provider-model-mismatch]" in str(_e)
        os.environ.pop("GEMINI_API_KEY",None)
        print("  provider routing + mismatch (A6)  "+("OK" if _route_ok else "FAIL")); ok=ok and _route_ok
        # pluggable adapter files (A7): opt-in, path-contained, shape + lineage validated
        import tempfile as _tf
        _ad_ok=True
        os.environ.pop("CROSSLAB_ADAPTER_FILES",None); os.environ["CROSSLAB_OTHER_ADAPTER"]="myadapter"
        try: CrossLabAdjudicator(provider="other", model="m", egress_policy="redacted").dispatch({"f":"x"},"p"); _ad_ok=False
        except _cl.EgressBlocked as _e: _ad_ok=_ad_ok and "[adapter-off]" in str(_e)
        os.environ["CROSSLAB_ADAPTER_FILES"]="on"; os.environ["CROSSLAB_OTHER_ADAPTER"]="../evil"
        try: CrossLabAdjudicator(provider="other", model="m", egress_policy="redacted").dispatch({"f":"x"},"p"); _ad_ok=False
        except _cl.EgressBlocked as _e: _ad_ok=_ad_ok and "[adapter-path]" in str(_e)
        try: _cl._validate_adapter({"key_env":"K"}, "x"); _ad_ok=False
        except _cl.EgressBlocked as _e: _ad_ok=_ad_ok and "[adapter-shape]" in str(_e)
        _dir=_tf.mkdtemp(); _sd=_cl._adapters_dir; _cl._adapters_dir=lambda: _dir
        try:
            _good=('PROVIDER={"key_env":"MYKEY","label":"My Lab","default_model":"m1","lineage":"mylab",'
                   '"model_prefixes":(),"endpoint":lambda m,b:"https://api.mylab.test/v1/chat/completions",'
                   '"headers":lambda k:{"Authorization":"Bearer "+k},'
                   '"body":lambda m,t,e:{"model":m,"messages":[{"role":"user","content":t}]},'
                   '"extract_text":lambda r:r["choices"][0]["message"]["content"],'
                   '"classify":lambda e,m,u:"CROSSLAB-FAILED [api]"}\n')
            open(os.path.join(_dir,"myadapter.py"),"w",encoding="utf-8").write(_good)
            open(os.path.join(_dir,"evil2.py"),"w",encoding="utf-8").write(_good.replace('"lineage":"mylab"','"lineage":"anthropic"'))
            os.environ["MYKEY"]="sk-selftest"; os.environ.pop("CROSSLAB_ADAPTER_SHA",None); os.environ["CROSSLAB_OTHER_ADAPTER"]="myadapter"
            _oc2={}
            def _cap3(req,timeout=None): _oc2['url']=req.full_url; raise _ue.URLError("cap")
            _cl.urllib.request.urlopen=_cap3
            try: CrossLabAdjudicator(provider="other", egress_policy="redacted").dispatch({"f":"x"},"p")
            except RuntimeError: pass
            _ad_ok=_ad_ok and _oc2.get('url')=="https://api.mylab.test/v1/chat/completions"
            os.environ["CROSSLAB_OTHER_ADAPTER"]="nope"
            try: CrossLabAdjudicator(provider="other", egress_policy="redacted").dispatch({"f":"x"},"p"); _ad_ok=False
            except _cl.EgressBlocked as _e: _ad_ok=_ad_ok and "[adapter-missing]" in str(_e)
            os.environ["CROSSLAB_OTHER_ADAPTER"]="myadapter"; os.environ["CROSSLAB_ADAPTER_SHA"]="deadbeef"
            try: CrossLabAdjudicator(provider="other", egress_policy="redacted").dispatch({"f":"x"},"p"); _ad_ok=False
            except _cl.EgressBlocked as _e: _ad_ok=_ad_ok and "[adapter-changed]" in str(_e)
            os.environ.pop("CROSSLAB_ADAPTER_SHA",None)
            os.environ["CROSSLAB_OTHER_ADAPTER"]="evil2"
            try: CrossLabAdjudicator(provider="other", egress_policy="redacted").dispatch({"f":"x"},"p"); _ad_ok=False
            except _cl.EgressBlocked as _e: _ad_ok=_ad_ok and "[same-lineage]" in str(_e)
        finally:
            _cl._adapters_dir=_sd
            for _k in ("CROSSLAB_ADAPTER_FILES","CROSSLAB_OTHER_ADAPTER","CROSSLAB_ADAPTER_SHA","MYKEY"): os.environ.pop(_k,None)
        print("  pluggable adapters (A7) ...... "+("OK" if _ad_ok else "FAIL")); ok=ok and _ad_ok
    finally:
        _cl.urllib.request.urlopen=_saved
        if _hadkey is None: os.environ.pop("OPENAI_API_KEY",None)
        else: os.environ["OPENAI_API_KEY"]=_hadkey
    _adj=CrossLabAdjudicator(); _ke=_adj.key_env
    print(f"  cross-lab provider/model ..... {_adj.provider} / {_adj.model}")
    key=bool(os.environ.get(_ke))
    print(f"  {_ke} set ............ {'yes' if key else 'NO — set it before --live'}")
    print("  =>", "READY for --live" if (ok and key) else ("offline OK; set "+_ke+" for --live" if ok else "OFFLINE CHECKS FAILED"))
    return ok

def live_smoke():
    adj=CrossLabAdjudicator(egress_policy="redacted", effort="low")
    print(f"[live smoke — {adj.provider}/{adj.model} — minimal, low-token, low-effort]")
    prompt='Reply with ONLY this JSON, nothing else: {"ok": true, "saw_task": true}\n{{blind_package}}'
    try:
        r=adj.dispatch({"smoke":"ping"}, prompt, privileged=False)
        print("  parsed response:", json.dumps(r))
        good = r.get("ok") or r.get("saw_task")
        print("  =>", "endpoint + API shape + JSON parse OK" if good else "parsed, but shape unexpected — inspect above / adjust crosslab.py body")
    except Exception as e:
        print("  live smoke FAILED:", e)
        print("  => on an HTTP 4xx about the request body, adjust that provider's adapter body in crosslab.py to match its CURRENT API docs.")

if __name__=="__main__":
    if "--live" in sys.argv:
        _ke=CrossLabAdjudicator().key_env
        if not os.environ.get(_ke): print("set %s first." % _ke); sys.exit(1)
        live_smoke()
    else: offline()
