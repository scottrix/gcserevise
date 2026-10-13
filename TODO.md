# GCSE Revise — Progress Tracker (generated from the filesystem)

**Last updated:** see the counts below — regenerate with the audit commands at the bottom.

## Current state (real numbers, not estimates)

| Metric | Count | Source |
|---|---|---|
| Subjects | 37 | `subjects.json` |
| Topic pages (all boards/tiers) | 3,632 | `find topics -type f -name '*.html' \| wc -l` |
| Unit / subject dirs | 407 | `ls topics \| wc -l` |
| Indexed in search | 3,632 | `search-index.json` (regenerated from filesystem) |
| Sitemap URLs | 3,709 | `sitemap.xml` (regenerated via `sitemap_gen.py`) |
| Past-paper pages | 37 | `*-past-papers.html` |
| Exam-question JSONs | 977 | `exam-questions/` |
| Flashcard JSONs | 977 | `flashcards/` |
| Smart-lesson JSONs | 974 | `smart-lessons/` |
| Target-test JSONs | 111 | `target-tests/` (backfill target: 977) |
| Mock-exam files | 175 | `mock-exams/` |
| Placeholder Q&A | 0 | grep for generic strings |
| Boards in JSON | AQA 30 / Edexcel 30 / OCR 25 / Eduqas 23 / CCEA 22 | `subjects.json` |

## Status by area (from the improvement brief)

| Area | Status | Notes |
|---|---|---|
| Search index + sitemap + dashboard | ✅ DONE | Regenerated from filesystem — every topic reachable |
| Homepage board counts | ✅ DONE | Derived from `subjects.json`, not hand-written |
| Affiliate/HTML integrity | ✅ DONE | Verified intact (300-file sample + site-wide tag balance) |
| Placeholder Q&A | ✅ DONE | 0 hits sitewide |
| Subject pages: static all-board sections | ✅ DONE (2026-10-12) | Build-time render of every board's section per subject page (P0-2 of the brief) |
| Maths foundation depth | ✅ DONE (2026-10-12) | All 97 AQA foundation topics ≥1,800 real words (batches 1+2a–2i: worked examples, model answers, key facts, exam context, drills; 4 wrong answers corrected). OCR higher maths (97 files) NOT yet expanded — out of P1 scope, tracked below |
| Required-practical coverage 1:1 | ✅ DONE (2026-10-12) | All four boards × separate sciences 100% (36 files mention practicals); 36 boxes added total (AQA 9; Edexcel Core Practical / OCR PAG / CCEA Practical Investigation — names only, no board numbering we cannot verify) |
| Board-diff pass | ⬜ TODO | Diff same-slug files across boards; inject genuine spec differences; board-difference boxes |
| Interactive backfill | ⬜ TODO | `target-tests/` 111 → 977; map `mock-exams/` to papers |
| Past-paper deep links | ⬜ TODO | Spec PDF + specimen papers + mark schemes per board (not just board homepages) |
| TODO/analysis docs | ✅ DONE | This file replaces the stale tracker; analysis doc updated |

## Audit commands (rerun to regenerate the numbers)

```
cd /home/scott/src/gcserevise
find topics -type f -name '*.html' | wc -l
python3 -c "import json;d=json.load(open('search-index.json'));print(len(d['subjects']),len(d['topics']))"
python3 -c "import re;print(len(re.findall(r'<loc>',open('sitemap.xml').read())))"
grep -rl "Demonstrate clear conceptual understanding" topics | wc -l
ls exam-questions | wc -l; ls flashcards | wc -l; ls target-tests | wc -l; ls smart-lessons | wc -l; ls mock-exams | wc -l
```

## Legacy purge (2026-10-12)
The live-site mirror (`github/gcserevise`) served 1,215 old flat-layout topic
files deleted from this repo on 2026-09-13 (deploy-manifest fix). All were
superseded duplicates of the current nested per-board pages (spot-checked by
title match; 1,013 exact filename counterparts, remainder renamed re-homes).
Purged from the mirror; both trees now serve identical 3,632 topic pages.
Music AoS4 pages' og:url/canonical/share links repointed from the dead
`topics/mu-aos4-classical-since-1910/` path to `topics/music/{board}/` in both
repos. `sitemap_gen.py` and `build_search_index.py` now live in this repo;
index entries carry proper id/name/subject/board fields.

## P1 completion note (2026-10-12)
- Depth: all P1 subjects at ≥1,800 real words per topic (maths foundation, English Language,
  English Literature, Chemistry, Biology, Physics, Combined Science).
- Practicals: every science topic file mentions/contains practical coverage on all boards.
- Known remaining gaps OUTSIDE P1: OCR higher maths (97 topics ~1,400 words — same expansion
  treatment recommended as next batch), and maths tier completeness (AQA has no higher set,
  OCR has no foundation set — 97+97 counterpart files missing).
