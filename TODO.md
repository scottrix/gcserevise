# GCSE Revise — Progress Tracker (generated from the filesystem)

**Last updated:** see the counts below — regenerate with the audit commands at the bottom.

## Current state (real numbers, not estimates)

| Metric | Count | Source |
|---|---|---|
| Subjects | 37 | `subjects.json` |
| Topic pages (all boards/tiers) | 3,632 | `find topics -type f -name '*.html' \| wc -l` |
| Unit / subject dirs | 407 | `ls topics \| wc -l` |
| Indexed in search | 3,632 | `search-index.json` (regenerated from filesystem) |
| Sitemap URLs | 3,710 | `sitemap.xml` (topics + root + past-paper pages) |
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
| Subject pages: static all-board sections | ⬜ TODO | Build-time render of every board's section per subject page (P0-2 of the brief) |
| Maths foundation depth | ⬜ TODO | Foundation-tier topics thin (~1,400 words) — expand to ≥1,800 |
| Required-practical coverage 1:1 | ⬜ TODO | Sciences: practical write-ups with numbers per board |
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
