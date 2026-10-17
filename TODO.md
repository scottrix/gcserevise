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
| P2 MFL technique + grammar bank | ✅ DONE (2026-10-14) | Technique layer (Exam Technique, 90/150-word frames, photo-card) now on all 68 MFL files across 4 boards (was AQA-only); French grammar bank CREATED: 4 new topics (FR25 tenses, FR26 articles/adjectives, FR27 pronouns/negation, FR28 prepositions/questions/modals) × 4 boards, 1,876–1,972 words each; search-index 3,648 topics, french.html 28 links exact |
| P2 history option coverage | 🟡 VERIFIED (2026-10-14) | Covered: Germany 1890–1945 (H1–H10), Conflict & Tension/Versailles+League (H11–H16), Elizabeth (H26–H32) — the named options all exist on all 5 boards. Uncovered popular options (Health & People / Medicine c1250+, Norman England, America 1840–95, Russia, Cold War) = future content batches; each is 8–10 topics × 1,800+ words |
| P2 geography case studies + fieldwork | ✅ VERIFIED (2026-10-14) | 145/145 files carry case studies + fieldwork; named studies present (Amazon 234 refs, Lagos 57, Bristol 58, Haiti 31, Holderness 16, Dorset 7) |
| P2 computer science pseudocode + SQL | ✅ VERIFIED (2026-10-14) | Pseudocode/trace tables in 37/37 files; dedicated CS36-sql.html (2,090–2,158 words, 45 SELECT examples) on all 4 boards |
| Interactive backfill | ✅ DONE (2026-10-14) | target-tests 111 → 976 (all exam-q topics covered); mocks mapped to papers (paperStructure + renderer); empty sections hidden. Note: ~2,576 topic pages beyond the 976 still have NO interactive data (flashcards/exam-q/TT) — hidden when absent; filling them is a future content batch |
| History medicine option set | ✅ BUILT (2026-10-14) | 9 new topics (H40 medieval, H41 renaissance, H42 industrial, H43 modern, H44 surgery, H45 public health, H46 individuals, H47 factors, H48 Western Front) × 4 boards (aqa/edexcel/ocr/eduqas; CCEA has no medicine option — excluded), 36 pages, ~1,100–1,550 words each with factor-grid technique + worked 16-mark essay plans; history.html 151 links exact; index 3,684 topics; deeper per-page expansion queued |
| P4 target-tests backfill | ✅ DONE (2026-10-14) | 866 new target-test JSONs generated from the exam-questions data (Quick Check 10min/70% + Exam-Style Practice 20min/60% + Extended Practice 25min where extended questions exist); all 976 topic-question sets now have a target test; every file validated (questions + correctAnswer present) |
| P4 mock paper mapping | ✅ DONE (2026-10-14) | paperStructure field added to all 175 mock files (real paper names/counts/durations per board+tier: Maths 3 papers AQA/OCR, 2 Eduqas, CCEA modules; Sciences 2 per board with topic splits; Combined 6; English 2; MFL 4 skills; NEA subjects' components); mock-exams.js renders 'Your real exam structure' in the setup UI and after each load |
| P4 hide empty containers | ✅ DONE (2026-10-14) | flashcards.js / exam-questions.js / target-tests.js hide the whole section (heading included) when no data loads or the dataset is empty — no more bare 'coming soon' headings on the 2,576 data-less topic pages |
| P3 single-board spec verification | ✅ DONE (2026-10-14) | Spec Focus box on all 261 single-board topic pages (astronomy 1AS0, ancient-history J198, classical-civ J199, dance 8236, engineering 8852, statistics 8382/1ST0; geology/film/electronics named without unverified codes) + Exam Board & Specification section on each of the 10 subject pages; Law honestly flagged: AQA 4160 withdrawn, no board offers GCSE Law — pages kept as A-Level Law foundation |
| P3 coursework NEA frames | ✅ DONE (2026-10-14) | Coursework & NEA Guide section on all 11 NEA-bearing subject pages (art, music, drama, D&T, food, PE, media, dance, film, electronics, engineering): component weightings, frame/structure per NEA (portfolio AOs, choreographic log, NEA1 science linkage, A&E structure, SoI, circuit-simulation evidence...), timeline and top pitfalls |
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
