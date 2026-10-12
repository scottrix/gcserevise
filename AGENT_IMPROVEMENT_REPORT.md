# GCSE Revise — Site Improvement Brief (for AI agent)

**Site live:** https://scottrix.github.io/gcserevise
**Canonical repo:** `/home/scott/src/gcserevise`
**Mirror repo (must apply same edits):** `/home/scott/src/github/gcserevise`
**Date of audit:** 2026-09-27
**Goal:** Make this the best UK GCSE revision resource — better than savemyexams.com, physicsandmathstutor.com, BBC Bitesize. Revision (concise, exam-focused, grade-9 sufficient) NOT lessons (teaching from scratch).

---

## 1. Current state (verified)

- `subjects.json`: 37 subjects, correct 5-board model (AQA / Edexcel / OCR / Eduqas / CCEA — note: Eduqas correctly separated here, unlike alevelrevise which conflates WJEC/Eduqas). Schema per subject: `{id, name, category, boards[], papers, topicDirs{BOARD:[dirs]}}`. **`topics[]` arrays are all empty** — JSON carries no topic list; `topicDirs` is the source of truth for organisation.
- `topics/`: **3,632 files in 407 dirs**. Path format: `topics/{subject-id}/{board-lower}/{tier?}/{topic-slug}.html` (e.g. `topics/biology/aqa/B1-cell-structure.html`, `topics/mathematics/aqa/foundation/A1-algebraic-notation.html`, `topics/biology/ocr/higher/B18-photosynthesis.html`). Tier split (foundation/higher) exists for maths/sciences.
- Homepage claims "37 Subjects / 5 Exam Boards / 600+ Topics" — files (3,632 incl. board/tier duplicates) vs unique topic names (~1,001). Claim is defensible if counted per-board, but misleading vs unique topics.
- Sampled page size ~1,400–2,900 words incl. boilerplate → roughly **1,200–2,000 words real content** per topic. Far deeper than alevelrevise (~350). Estimated total ~9M words. This is already near savemyexams depth per page.
- Topic template: head meta (board-specific title/description/canonical) + header + breadcrumb + topic header with badges + board `<select>` (`updateTopicBoard()` — switches to same topic on other board) + disclaimer + sections + footer + theme script. Board-specific URLs are real (AQA vs Edexcel B1 both exist, ~2,142 vs ~2,145 words, non-identical).
- Subject pages (e.g. `biology.html`): per-board sections (`<section id="biology-aqa">…22 Topics…</section>`) + board `<select>` (`updateSubjectUrl()`). Meta claims e.g. "88 topics across all major exam boards".
- 37 `*-past-papers.html` pages (one per subject). `exam-questions/` 977 JSON, `flashcards/` 977 JSON, `smart-lessons/` 974, `target-tests/` 111, `mock-exams/` 175 files.
- Zero broken internal `topics/`/`*.html` hrefs in root-page sample. Zero "Demonstrate clear conceptual understanding" placeholders. Affiliate HTML intact in 300-file sample (unlike alevelrevise).
- `SAVE_MY_EXAMS_ANALYSIS.md` exists (board-specific + 7 content types plan). `TODO.md` is **stale** ("Not Started" everywhere — false).

## 2. Defects to fix (prioritised)

### P0-1. Search + sitemap cover only ~1/3 of content
- `search-index.json`: 37 subjects but only **1,218 topics** vs 3,632 files.
- `sitemap.xml`: **1,254 URLs** vs 3,632 files + 77 root pages → ~2,400 topic files unindexed.
- **Task:** Regenerate both from filesystem (`topics/**/*.html` + subject pages + past-paper pages). Search index entry per file: `{u (relative url), t (title), s (subject), b (board), tier?}`. Keep `dashboard-data.json` in sync. Acceptance: counts match filesystem; every topic reachable via search.

### P0-2. Subject pages show only default board statically
- `biology.html` static HTML contains only the AQA section (22 links); Edexcel/OCR/CCEA sections appear absent from static markup (grep finds 22 `topics/` hrefs vs 99 biology files on disk; same for `french.html`: 3 vs 12). Board switching depends on JS.
- No-JS users, crawlers, and validators see one board only. Meta "88 topics" unverifiable from static HTML.
- **Task:** Server-side (build-time) render ALL board sections into each subject page, hide non-selected with CSS/JS (not by omitting). Each section: `<section id="{subject}-{board}">` with full topic-card grid. Acceptance: `grep -c topics/` per subject page == file count for that subject; works with JS disabled.

### P0-3. Canonical / domain mismatch (SEO split, same as alevelrevise)
- Every canonical + `og:url`, `sitemap.xml`, `robots.txt` point at `https://www.scottrix.co.uk/gcserevise/...`, live site is `https://scottrix.github.io/gcserevise`.
- **Task:** Decide single canonical domain, apply to all pages/sitemap/robots/JSON-LD. Redirect the other.

### P0-4. Board-count claims need verification
- Homepage: AQA ~35, Edexcel ~40, OCR ~28, Eduqas ~22, CCEA ~41 subjects. CCEA offering 41 of 37 subjects is arithmetically suspicious; CCEA does not offer e.g. Film Studies, Media variants identically. Single-board subjects in JSON look right (Astronomy=Edexcel only, Geology=Eduqas only, Ancient History/Classical Civ=OCR only, Law/Dance=AQA only, Film/Electronics=Eduqas only) — good — but counts must be derived, not hand-written.
- **Task:** Compute homepage counts from `subjects.json` boards arrays at build time. Acceptance: numbers always match JSON.

### P0-5. Stale docs
- `TODO.md` says nothing started; `SAVE_MY_EXAMS_ANALYSIS.md` describes current state as "board-agnostic" (no longer true).
- **Task:** Rewrite `TODO.md` as generated progress tracker (per subject × board file counts + JS-data coverage). Update analysis doc to reflect board-specific reality.

## 3. Content quality work (the main job)

**Revision vs lesson rule:** assume taught once. Each topic: condensed spec-mapped notes (every spec bullet named + spec code), key terms, 1–2 worked exam Qs with mark-scheme logic, misconceptions/pitfalls, required-practical/fieldwork where applicable, exam technique (command words, AO1/AO2/AO3, timing, tiers), maths skills, ≥4 practice Qs with answers, 8–15 flashcards, diagrams as inline SVG (no external dependency).

**Depth audit (sampled):** Biology B1/B10–B13, French FR11–FR13 all substantive with board badges. Maths foundation topics thinner (~1,400 words) than sciences/languages (~2,300) — prioritise maths foundation expansion.

### Per-subject priorities
| Priority | Subjects | Action |
|---|---|---|
| P1 | Mathematics (foundation tier thin), English Language/Literature (verify 9-1 Paper 1/2 + set texts per board), Combined Science + Biology/Chemistry/Physics (required practicals 1:1 with spec, equations, maths skills) | Expand to ≥1,800 real words; add SVG diagrams, practical write-ups, tier tags |
| P2 | History (named options per board: Germany, Versailles, Nazi women etc. exist — verify option coverage), Geography (case studies + fieldwork), French/Spanish/German (theme vocab + photo-card + 90-word/150-word technique + grammar bank), Computer Science (pseudocode traces, SQL) | Fill option gaps; add exam-technique frames |
| P3 | Single-board specials (Astronomy, Geology, Ancient History, Classical Civ, Law, Dance, Film, Electronics, Engineering, Statistics) + creative/technical (Art, Music, Drama, D&T, Food, PE, Media, Citizenship, RS, Business, Econ, Psych, Soc, Latin) | Verify each matches its single spec exactly; coursework subjects must say so + give NEA frames |
| P4 | `target-tests/` only 111 vs 977 exam-questions/flashcards — backfill quizzes; `mock-exams/` 175 — map to papers (Maths 3, Eng 2, Sciences 2–6 per board incl. tiers) | Complete interactive layer; hide empty containers when no data |

### Board-differentiation check (sampled AQA vs Edexcel B1: same length, non-identical — good)
- **Task:** Diff all same-slug files across boards; where content is copy-paste, inject genuine spec differences (paper structure, required practical numbers/names, equations given vs memorised, tier availability, set texts/options). Add per-subject "Board differences" box (copy the good `alevelrevise/biology.html` pattern). Acceptance: no two boards' pages for one topic are byte-identical unless specs truly identical (document why).

## 4. Layout / UX (already good — don't regress)
- Keep: dark mode (`style.css`), mobile nav, breadcrumbs, disclaimer banner, `sidebar.js`/`app.js`, theme/board localStorage keys, `*-past-papers.html` pattern linked from index subject cards (alevelrevise lacks these — consider backporting the pattern, not the files).
- Past-paper pages: verify each has **deep links** (spec PDF, specimen papers + mark schemes per board, exam timetable windows) not just board homepages.
- Subject-page section headings: verify they use real spec areas, not first-word auto-split (the alevelrevise bug).
- Duplicate slugs across boards/tiers (e.g. `p1-energy-stores-and-transfers.html` ×10) are correct per-URL (paths differ) — keep, but ensure `<link rel="canonical">` is per-file and titles include board+tier.

## 5. Sources (not just savemyexams)
Official spec + specimen mark schemes per board (AQA/Edexcel/OCR/Eduqas/CCEA); savemyexams (structure); physicsandmathstutor (topic Q banks); BBC Bitesize; Seneca; Chemguide/chemrevise; mathsgenie/Dr Frost; tutor2u; Massolit (lit); set-text editions. Never copy — synthesise, cite spec codes.

## 6. Execution order
1. P0 (search/sitemap regen, subject-page static board sections, canonical, counts, docs).
2. P1 subject expansion + practicals/diagrams.
3. Board-diff pass (diff → differentiate → board boxes).
4. P2–P4 + interactive backfill + past-paper deep links.
5. QA per subject (see below).
6. Mirror every edit to `/home/scott/src/github/gcserevise`.

## 7. Reproduce-audit commands
```
cd /home/scott/src/gcserevise
find topics -type f | wc -l; ls topics | wc -l
python3 -c "import json;d=json.load(open('search-index.json'));print(len(d['subjects']),len(d['topics']))"
python3 -c "import re;print(len(re.findall(r'<loc>',open('sitemap.xml').read())))"
grep -rl "Demonstrate clear conceptual understanding" topics | wc -l
ls exam-questions | wc -l; ls flashcards | wc -l; ls target-tests | wc -l; ls smart-lessons | wc -l; ls mock-exams | wc -l
diff <(ls topics/biology/aqa/B1-cell-structure.html) <(echo ok)
python3 - <<'EOF'
import re,glob
for s in ['french.html','biology.html']:
    h=open(s,errors='ignore').read()
    links=set(re.findall(r'href="(topics/[^"]+)"',h))
    import os
    allf=set('topics/'+f for f in glob.glob(f'topics/{s[:-5]}/**/*.html',recursive=True))
    print(s,'linked:',len(links),'existing:',len(allf))
EOF
```

## 8. Acceptance criteria
- [ ] search-index + sitemap + dashboard-data counts == filesystem (3,632 + roots).
- [ ] Every subject page statically lists every board's topics; works JS-off.
- [ ] Single canonical domain everywhere.
- [ ] Homepage board counts generated from JSON.
- [ ] Zero placeholder Q&A; maths foundation ≥1,800 real words; every science topic has practical coverage.
- [ ] No byte-identical cross-board duplicates without documented reason; board-difference boxes present.
- [ ] Past-paper pages have deep spec/specimen links per board.
- [ ] Both repo copies identical for changed files.
