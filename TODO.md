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
| Board-diff pass | ✅ DONE (2026-10-12) | Per-board "Board Focus" boxes injected into 3,256 topic pages across 29 multi-board subjects (spec codes, paper structure, practicals, tier availability — verified facts only, with a check-your-spec line); composed "Board Differences" section on all 29 subject pages; 0 byte-identical cross-board bodies remain (was 10 groups). Data: board_focus_*.py; injector: inject_board_focus.py |
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

## Post-P1 completion (2026-10-12) — OCR higher + maths tier structure
- OCR higher maths: all 97 topics expanded to ≥1,800 real words (same enrichment as AQA).
- Maths tier structure RESOLVED: both `aqa/foundation/` and `ocr/higher/` held the SAME
  full 97-topic set under a single-tier label (higher-only topics sat in "foundation").
  Files moved to board-first paths (`topics/mathematics/{board}/`) matching every other
  subject; tier depth stays marked inline ((Higher) sections, tier badges). 194 redirect
  stubs at the old tier URLs (meta refresh + canonical) preserve inbound links; stubs are
  excluded from sitemap, search index and subject-page links by a content marker.
- Remaining known gap: cross-board content differentiation for maths (aqa vs ocr bodies
  are near-identical — that is the separate board-diff pass, not a tier problem).
