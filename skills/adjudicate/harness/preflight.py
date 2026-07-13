#!/usr/bin/env python3
"""Pre-flight for the live cross-lab run.
  OFFLINE (run now):  python3 preflight.py         # imports, prompt, mock dispatch+parse, gates, key presence
  LIVE SMOKE:         OPENAI_API_KEY=sk-... python3 preflight.py --live   # tiny ~free call: endpoint + API shape + JSON parse
Run the smoke BEFORE spending on a full adjudication."""
import os, sys, json
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
    finally:
        _cl.urllib.request.urlopen=_saved
        if _hadkey is None: os.environ.pop("OPENAI_API_KEY",None)
        else: os.environ["OPENAI_API_KEY"]=_hadkey
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
