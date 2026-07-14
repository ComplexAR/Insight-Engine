# Phase-synced highlight map for the narrated explainer.
#
# For each slide number, a list with ONE card-index per narration sentence
# (sentences are split by render_video.split_sentences, which is deterministic
# and round-trips). The value is the index of the card to outline in red during
# that sentence, into that slide's card list (draw order, as recorded in
# card_geometry.json), or -1 for "no highlight".
#
# render_video.py asserts len(HIGHLIGHT[slide]) == number of sentences on that
# slide, and that every card index is in range. So if the narration is ever
# edited, the render FAILS LOUDLY until this map is updated -- the highlight can
# never silently drift out of sync, or be dropped on a version bump, again.
#
# Slides not present here play with no highlight (title, close, single-card).

HIGHLIGHT = {
    # 2 - the map: 4 quadrant cards (idea/pipeline/interface/model) + banner(4).
    2:  [-1, -1, 0, 1, 2, 3, 4, -1],
    # 3 - Insight | Engine | banner. Insight=card0, Engine=card1, banner=card2.
    3:  [-1, 0, 0, 0, 1, 1, 1, 1, 2],
    # 4 - three "features" columns (0,1,2) + trap banner(3).
    4:  [-1, -1, -1, 0, 1, 2, -1, 3, 3, -1],
    # 5 - two jobs (reveal=0, verify=1) + the rule banner(2).
    5:  [-1, 0, 0, 0, 0, 1, 1, 2, 2, 2, -1],
    # 6 - the 12-step map. Cards 0..11 = STEP 1..12 (row-major draw order).
    6:  [-1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 7, 0],
    # 7 - full-method(0) | short-answer(1) | banner(2).
    7:  [-1, -1, 1, 0, 0, -1],
    # 8 - the five scoping questions card(0) + fill-assumption banner(1).
    8:  [-1, 0, 0, 0, 0, 0, 0, 0, 1],
    # 9 - four probe cards (0..3) + "make invisible visible" banner(4).
    9:  [-1, -1, 0, 1, 2, 3, -1, 4, -1, -1, -1],
    # 10 - V(0) N(1) | tiers V1/V2/V3 (2,3,4) | independence(5) | grade-lock banner(6).
    10: [-1, -1, -1, 0, 1, 2, 5, 5, 5, 6],
    # 11 - three buckets (0,1,2) | tiering(3) | independence(4) | banner(5).
    11: [-1, -1, 0, 1, 2, 3, 3, 4, 5],
    # 12 - three outcome columns (0,1,2) + two banners (3,4).
    12: [-1, -1, -1, -1, 0, 1, 2, 3, 4],
    # 13 - when-it-runs(0) | limits(1) | false-precision banner(2).
    13: [-1, -1, 0, 0, 1, 1, 1, 2],
    # 14 - the questions(0) | the three rules(1) | banner(2).
    14: [-1, 0, 0, 1, -1, 2],
    # 15 - grade-lock(0) | resilience(1) | banner(2).
    15: [-1, 0, 0, 0, 1, 1, 2],
    # 17 - six brief-part cards (0..5) + banner(6).
    17: [-1, 0, 0, 1, 3, 6],
    # 18 - mechanism(0) | ladder(1) | banner(2).
    18: [-1, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    # 19 - sharpens(0) | adds-little(1) | banner(2).
    19: [-1, 1, 0, 0, 2, 2, -1],
    # 20 - switchable(0) | governance+monitor(1) | banner(2).
    20: [0, 1, 1, 1, 1, -1, -1, -1],
    # 21 - execution model(0) | adjudication model(1) | honest-framing banner(2).
    21: [-1, 0, 0, 1, 1, 2, 2, -1],
    # 22 - scaffolding survives(0) | what degrades(1) | banner(2).
    22: [-1, 0, 0, 1, 1, 2, 2, 2, 2],
    # 23 - five command cards: analyse(0) verify(1) render(2) track(3) adjudicate(4).
    23: [-1, -1, -1, 0, 1, 2, 3, 4, -1],
    # 24 - render card(0) + banner(1).
    24: [-1, 0, 0, 0, 1],
    # 25 - track card(0) + banner(1).
    25: [0, 0, 1, -1, -1],
}

# ::IE-RENDER-EOF::
