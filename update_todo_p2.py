#!/usr/bin/env python3
"""Update TODO.md with P2 completion status."""
src = open('TODO.md').read()

mfl = ("| P2 MFL technique + grammar bank | \u2705 DONE (2026-10-14) | Technique layer (Exam Technique, "
       "90/150-word frames, photo-card) now on all 68 MFL files across 4 boards (was AQA-only); "
       "French grammar bank CREATED: 4 new topics (FR25 tenses, FR26 articles/adjectives, FR27 "
       "pronouns/negation, FR28 prepositions/questions/modals) \u00d7 4 boards, 1,876\u20131,972 words each; "
       "search-index 3,648 topics, french.html 28 links exact |")

hist = ("| P2 history option coverage | \U0001F7A1 VERIFIED (2026-10-14) | Covered: Germany 1890\u20131945 "
        "(H1\u2013H10), Conflict & Tension/Versailles+League (H11\u2013H16), Elizabeth (H26\u2013H32) \u2014 "
        "the named options all exist on all 5 boards. Uncovered popular options (Health & People / Medicine "
        "c1250+, Norman England, America 1840\u201395, Russia, Cold War) = future content batches; each is "
        "8\u201310 topics \u00d7 1,800+ words |")

geo = ("| P2 geography case studies + fieldwork | \u2705 VERIFIED (2026-10-14) | 145/145 files carry case "
       "studies + fieldwork; named studies present (Amazon 234 refs, Lagos 57, Bristol 58, Haiti 31, "
       "Holderness 16, Dorset 7) |")

cs = ("| P2 computer science pseudocode + SQL | \u2705 VERIFIED (2026-10-14) | Pseudocode/trace tables in "
      "37/37 files; dedicated CS36-sql.html (2,090\u20132,158 words, 45 SELECT examples) on all 4 boards |")

anchor = "| Interactive backfill | \u2b1c TODO |"
assert anchor in src, "anchor missing"
src = src.replace(anchor, mfl + "\n" + hist + "\n" + geo + "\n" + cs + "\n" + anchor)
open('TODO.md', 'w').write(src)
print("TODO updated with 4 P2 rows")
