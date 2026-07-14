# Spoken-only pronunciation fixes for the narrated explainer.
#
# These respellings are applied to the text sent to the TTS engine ONLY. They do
# NOT change the on-screen deck text or Insight-Engine-Explainer-Narration.md,
# which stay verbatim. They exist because edge-tts mispronounces certain novel or
# compound tokens, and that correction must live in the committed pipeline so it
# can never be lost on a re-render / version bump again.
#
# TUNED_FOR pins the voice+rate these respellings were confirmed against by ear
# (render_video guard G3b refuses to run under a different voice/rate, because a
# respelling is only known-good for the voice it was tuned on).
TUNED_FOR = ("en-GB-RyanNeural", "+40%")

# (regex source, spoken replacement). Whole-word, case-sensitive; list both cases.
LEXICON = [
    (r"\bCowork\b",       "Co-work"),
    (r"\bcowork\b",       "co-work"),
    (r"\bdecorrelated\b", "dee-correlated"),
    (r"\bDecorrelated\b", "Dee-correlated"),
]

# One-way ratchet: lowercased tokens known to be mispronounced by the TTS. Guard
# G3 fails the render unless EVERY occurrence of each of these in the narration is
# matched by a LEXICON pattern. So a hard word re-introduced by a future edit is
# either already covered or it stops the render loudly -- it can never silently
# revert to the mispronunciation. Add to this list whenever a new hard word is
# found; never remove an entry while the word can still appear.
HARD_TOKENS = ["cowork", "decorrelated"]

# ::IE-RENDER-EOF::
