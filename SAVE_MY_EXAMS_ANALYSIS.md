# SaveMyExams vs GCSE Revise - Analysis & Improvement Plan

## SaveMyExams Structure (Strengths)

### Board-Specific Organization
- AQA, Edexcel, OCR (A/B), WJEC, WJEC Eduqas, CCEA - all separate
- Tier-specific: Foundation/Higher for Maths, Science
- Granular topic breakdown: 50+ topics per subject

### 7 Content Types per Topic (per board)
1. **Revision Notes** - Core content
2. **Exam Questions** (Topic Questions) - Board-specific past paper questions
3. **Flashcards** - Spaced repetition
4. **Smart Lessons** - Guided interactive lessons
5. **Target Tests** - Auto-graded quizzes
6. **Mock Exams** - Full timed papers
7. **Past Papers** - Full papers with mark schemes

### Navigation Hierarchy
```
/gcse/biology/aqa/18/
  ├── revision-notes/
  ├── topic-questions/
  ├── flashcards/
  ├── smart-lesson/
  ├── target-tests/
  ├── mock-exams/
  └── past-papers/
```

---

## Your GCSE Revise (Current State)

### Strengths
- Clean, fast, board-agnostic
- Good extended questions, misconceptions, problem-solving
- AO3 reasoning sections
- Model answers with mark schemes
- Video resources, past paper links, external links
- Full gcserevise-style layout with ads

### Gaps vs SaveMyExams
| Feature | Your Site | SaveMyExams |
|---------|-----------|-------------|
| Board-specific content | ❌ | ✅ (6 boards) |
| Tier-specific (F/H) | ❌ | ✅ Maths/Science |
| Exam questions by topic | Links only | ✅ Board-specific Qs |
| Flashcards | ❌ | ✅ Spaced repetition |
| Smart Lessons | ❌ | ✅ Guided lessons |
| Target Tests | ❌ | ✅ Auto-graded |
| Mock Exams | ❌ | ✅ Timed papers |
| Tier-specific (F/H) | ❌ | ✅ Maths/Science |
| Topic granularity | ~10/subject | 50+ per subject |

---

## Quick Wins (This Week)

### 1. Add "Exam Questions by Topic" section to existing topics
- Add board-specific past paper question links per topic
- Use official board past paper finder URLs

### 2. Add Board Badges
- Show which boards cover each topic
- AQA, Edexcel, OCR, WJEC, Eduqas, CCEA badges

### 3. Create "Past Papers" Landing Pages
- Per subject per board landing pages
- Links to official past paper finders

### 3. Add Tier Badges (Foundation/Higher)
- For Maths and Science topics
- Label "Foundation only" / "Higher only" content

### 3. Board Navigation on Subject Pages
- Subject landing pages show board selector
- Links to board-specific topic lists

---

## Implementation Plan

### Phase 1: Quick Wins (Week 1)
- [ ] Add board badges to topic pages
- [ ] Add "Exam Questions by Topic" links
- [ ] Add tier badges for Maths/Science
- [ ] Create Past Papers landing pages per subject/board

### Phase 2: Board-Specific Architecture (Week 2-3)
- [ ] Update subjects.json for board hierarchy
- [ ] Generate board-specific topic pages
- [ ] Add board selector to subject landing pages

### Phase 3: Content Types (Week 3-5)
- [ ] Flashcards system (spaced repetition)
- [ ] Exam questions by topic per board
- [ ] Target tests (auto-graded)

### Phase 3+ (Future)
- Smart Lessons
- Target Tests
- Mock Exams
- Tier-specific content (Foundation/Higher)

---

## File Structure Changes Needed

### Current
```
gcserevise/
├── topics/
│   ├── algebra/
│   │   └── A1-algebraic-notation.html
│   └── bio-cell/
│       └── cell-structure.html
```

### Target (Board-Specific)
```
gcserevise/
├── biology/
│   ├── aqa/
│   │   ├── cell-structure.html
│   │   └── ...
│   ├── edexcel/
│   ├── ocr-a/
│   └── ocr-b/
├── maths/
│   ├── aqa/
│   │   ├── foundation/
│   │   └── higher/
│   ├── edexcel/
│   │   ├── foundation/
│   │   └── higher/
│   └── ...
```

---

## Quick Win Implementation Details

### 1. Board Badges
Add to topic header:
```html
<div class="topic-meta">
  <span class="badge">AQA</span>
  <span class="badge">Edexcel</span>
  <span class="badge">OCR</span>
  <span class="badge">WJEC</span>
</div>
```

### 2. Exam Questions Section
```html
<section class="section">
<h2>📝 Exam Questions by Topic</h2>
<ul>
  <li><a href="https://www.aqa.org.uk/find-past-papers-and-mark-schemes">AQA Past Papers - Topic Questions</a></li>
  <li><a href="https://qualifications.pearson.com/...">Edexcel Past Papers - Topic Questions</a></li>
  <li><a href="https://www.ocr.org.uk/qualifications/past-paper-finder/">OCR Past Papers - Topic Questions</a></li>
</ul>
</section>
```

### 3. Tier Badges (Maths/Science)
```html
<span class="badge foundation">Foundation</span>
<span class="badge higher">Higher</span>
```

---

## Next Steps
1. **Today**: Implement quick wins (board badges, exam question links, tier badges)
2. **This week**: Create past papers landing pages
3. **Next week**: Start board-specific architecture