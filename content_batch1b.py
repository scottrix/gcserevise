#!/usr/bin/env python3
"""Batch 1b: wave-2 depth for the same 15 AQA maths foundation topics.
Run: python3 content_batch1b.py"""
from expand_topics import run_wave2

KF = lambda body: (
    '<section class="section">\n'
    '<h2>📌 Key Facts to Memorise</h2>\n' + body + '\n</section>')
CTX = lambda body: (
    '<section class="section">\n'
    '<h2>🗺️ In the Exam</h2>\n' + body + '\n</section>')
W2 = lambda q, steps, marks: (
    '<section class="section">\n'
    '<h2>🧮 Worked Examples — Harder Exam Style</h2>\n'
    '<div class="example">\n'
    f'<p><strong>{q}</strong></p>\n{steps}\n'
    f'<p><em>{marks}</em></p>\n</div>\n</section>')

BATCH = {}

BATCH["N7-integer-indices.html"] = dict(
    keyfacts=KF('<ul>'
        '<li>Multiplying: <strong>ADD</strong> the indices (aᵐ × aⁿ = aᵐ⁺ⁿ)</li>'
        '<li>Dividing: <strong>SUBTRACT</strong> the indices (aᵐ ÷ aⁿ = aᵐ⁻ⁿ)</li>'
        '<li>Power of a power: <strong>MULTIPLY</strong> the indices ((aᵐ)ⁿ = aᵐⁿ)</li>'
        '<li>Memory hook: the operation between the powers tells you what to do to the indices</li>'
        '<li>Zero index: a⁰ = 1 for any a ≠ 0</li>'
        '</ul>'),
    context=CTX('<p>Index laws appear in <strong>Paper 1 (non-calculator)</strong> and <strong>Paper 2/3</strong>, '
        'typically as a 1–2 mark "simplify" opener, or 3 marks when combined with substitution. '
        'They also hide inside expansion and standard-form questions, so a weak index law costs marks twice.</p>'
        '<p>Links to: standard form (N9), substitution (A2), quadratic expansion (A11).</p>'),
    worked2=W2("Simplify (2x²y)³ × 4xy², giving your answer in index form.",
        '<p>Cube the bracket first — every factor inside: 2³ = 8, (x²)³ = x⁶, y³ stays y³</p>'
        '<p>So (2x²y)³ = 8x⁶y³</p>'
        '<p>Now multiply: 8x⁶y³ × 4xy² = (8 × 4)(x⁶ × x)(y³ × y²) = 32x⁷y⁵</p>'
        '<p><strong>Answer: 32x⁷y⁵</strong></p>',
        "M1 for cubing 2 and applying (x²)³ = x⁶; A1 for 32x⁷y⁵. "
        "Forgetting to cube the 2 (giving 2x⁶y³ × 4xy² = 8x⁷y⁵) is the targeted trap."))

BATCH["R4-simplifying-ratio.html"] = dict(
    keyfacts=KF('<ul>'
        '<li>Simplify a ratio: divide every part by the same number (HCF gives simplest form)</li>'
        '<li>Ratio with units: convert to the SAME unit first</li>'
        '<li>Sharing: total parts → value of one part (total ÷ parts) → multiply</li>'
        '<li>Ratio to fraction: part ÷ TOTAL parts (e.g. 3 : 5 → 3/8)</li>'
        '<li>Equivalent ratios: multiply or divide BOTH parts by the same number</li>'
        '</ul>'),
    context=CTX('<p>Ratio appears on every Foundation paper, usually 3–4 marks: one "simplify", one "share", '
        'and often a recipe-scaling or best-buy twist in Paper 2/3 (calculator).</p>'
        '<p>Links to: fractions of amounts (R3), proportion (R7), scale drawings (G).</p>'),
    worked2=W2("Golden syrup, flour and sugar are mixed in the ratio 2 : 5 : 3. A recipe uses 250 g of flour. How much golden syrup and sugar are needed?",
        '<p>Flour = 5 parts = 250 g → 1 part = 250 ÷ 5 = 50 g</p>'
        '<p>Golden syrup = 2 parts = 2 × 50 = <strong>100 g</strong></p>'
        '<p>Sugar = 3 parts = 3 × 50 = <strong>150 g</strong></p>',
        "M1 for 250 ÷ 5, A1 for both answers. Recipe-scaling wording ('A recipe uses…') is the standard ratio context."))

BATCH["N1-ordering-numbers.html"] = dict(
    keyfacts=KF('<ul>'
        '<li>On a number line, LEFT = smaller — always</li>'
        '<li>With negatives: −8 < −2 (the further from zero, the smaller)</li>'
        '<li>Compare decimals place by place: 0.08 < 0.7 (8 hundredths < 7 tenths)</li>'
        '<li>Mixed forms: convert everything to decimals (or a common denominator) first</li>'
        '<li>Useful conversions: 1/2 = 0.5, 1/4 = 0.25, 3/4 = 0.75, 1/5 = 0.2, 1/8 = 0.125</li>'
        '</ul>'),
    context=CTX('<p>Ordering is a 1–2 mark question that opens many Paper 1 papers. It also feeds '
        'inequality number lines and estimating. Getting it wrong is expensive relative to the effort.</p>'
        '<p>Links to: inequalities (A22), decimals-fractions (N10), negative numbers (N2).</p>'),
    worked2=W2("Write these in order of size, smallest first: −0.4, −0.45, 0.4, −0.04",
        '<p>All the negatives come first, ordered by distance from zero: −0.45 (furthest) then −0.4, then −0.04.</p>'
        '<p>Positives last: 0.4</p>'
        '<p><strong>Answer: −0.45, −0.4, −0.04, 0.4</strong></p>',
        "B1 for all four in order. The −0.04 vs −0.4 pair is the designed trap: "
        "−0.04 is closer to zero, so it is LARGER than −0.4."))

BATCH["A22-inequalities.html"] = dict(
    keyfacts=KF('<ul>'
        '<li>Flip the symbol when multiplying or dividing by a NEGATIVE (only then)</li>'
        '<li>Number lines: open circle for < or >, filled (closed) circle for ≤ or ≥</li>'
        '<li>"List the integer values" → count integers strictly inside, respecting circle type</li>'
        '<li>x² > a² → x < −a or x > a (two regions); x² < a² → between (−a < x < a)</li>'
        '<li>Answers keep the inequality symbol — never write "="</li>'
        '</ul>'),
    context=CTX('<p>Linear inequalities are worth 2–3 marks on Paper 1/2; quadratic inequalities (higher '
        'content, but tested at Foundation in the region form) add 2 more. Number-line drawing is '
        'often worth its own mark.</p>'
        '<p>Links to: solving equations (A17), quadratics (A11/A12), number lines (N1).</p>'),
    worked2=W2("The perimeter of a rectangle is less than 30 cm. Its length is x cm and its width is 4 cm. Write an inequality for x and solve it.",
        '<p>Perimeter = 2(x + 4) &nbsp;→&nbsp; 2(x + 4) < 30</p>'
        '<p>Divide both sides by 2: x + 4 < 15</p>'
        '<p>Subtract 4: <strong>x < 11</strong></p>',
        "M1 for forming 2(x + 4) < 30, A1 for x < 11. "
        "'Form and solve' inequality questions also award a mark for correct context — lengths must also satisfy x > 0."))

BATCH["N6-powers-and-roots.html"] = dict(
    keyfacts=KF('<ul>'
        '<li>Squares up to 15²: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225</li>'
        '<li>Cubes up to 5³: 1, 8, 27, 64, 125 (and 10³ = 1000)</li>'
        '<li>Square root undoes a square: √(a²) = a</li>'
        '<li>Estimating roots: bracket between two perfect squares, then narrow down</li>'
        '<li>Powers of 10: 10⁴ = 10,000 (number of zeros = index)</li>'
        '</ul>'),
    context=CTX('<p>Squares/cubes recall earns 1 mark on Paper 1 nearly every year. Estimation of roots '
        'is a 2-mark non-calculator favourite. Powers feed standard form and index laws.</p>'
        '<p>Links to: index laws (N7), standard form (N9), Pythagoras (G), area problems (G).</p>'),
    worked2=W2("A cube has a volume of 216 cm³. Find the length of one edge.",
        '<p>Edge × edge × edge = 216, so edge = ³√216</p>'
        '<p>Try 5: 5³ = 125 (too small). Try 6: 6 × 6 × 6 = 216 ✓</p>'
        '<p><strong>Answer: 6 cm</strong></p>',
        "B1 for 6. Cube volumes reversing to edge length is the standard cube-root context at Foundation."))

BATCH["R3-fractions-of-amounts.html"] = dict(
    keyfacts=KF('<ul>'
        '<li>Fraction OF amount: divide by the denominator (bottom), multiply by the numerator (top)</li>'
        '<li>Reverse: "3/4 of the number is 54" → 1/4 = 54 ÷ 3, then × 4</li>'
        '<li>Fraction of a ratio group: part ÷ total parts (4 : 7 → apples are 4/11)</li>'
        '<li>Simplify before multiplying when you can — smaller numbers, fewer slips</li>'
        '<li>Check direction: "of" shrinks, "is … of" rebuilds</li>'
        '</ul>'),
    context=CTX('<p>Fractions of amounts: 2–3 marks, every paper, both calculator and non-calculator. '
        'The reverse version is the AO2 twist worth the extra mark.</p>'
        '<p>Links to: ratio (R4), percentages of amounts (R9/N12), probability fractions (P).</p>'),
    worked2=W2("A 480 g bag of sweets is shared in the ratio 2 : 3 : 5 between Ali, Ben and Cara. Ben eats 2/3 of his share. How many grams does Ben have left?",
        '<p>Ben\u2019s share: 3 parts of 10 → 480 ÷ 10 = 48, then 48 × 3 = 144 g</p>'
        '<p>Ben eats: 2/3 of 144 = 144 ÷ 3 × 2 = 96 g</p>'
        '<p>Left: 144 − 96 = <strong>48 g</strong></p>',
        "M1 for the ratio share (144), M1 for 2/3 of 144, A1 for 48. "
        "Multi-step fraction-of-amount chains like this are worth 4–5 marks at Foundation."))

BATCH["G21-exact-trig-values.html"] = dict(
    keyfacts=KF('<p>Memorise the table (angles 0°, 30°, 45°, 60°, 90°):</p>'
        '<table>'
        '<tr><th></th><th>0°</th><th>30°</th><th>45°</th><th>60°</th><th>90°</th></tr>'
        '<tr><td>sin</td><td>0</td><td>1/2</td><td>√2/2</td><td>√3/2</td><td>1</td></tr>'
        '<tr><td>cos</td><td>1</td><td>√3/2</td><td>√2/2</td><td>1/2</td><td>0</td></tr>'
        '<tr><td>tan</td><td>0</td><td>1/√3 (=√3/3)</td><td>1</td><td>√3</td><td>—</td></tr>'
        '</table>'
        '<p>Memory hooks: sin climbs 0, 1, 2, 3 over √-denominators (√0, √1, √2, √3, √4)/2; cos is sin reversed; tan = sin ÷ cos.</p>'),
    context=CTX('<p>Exact values are "write down" 1-mark questions on Paper 1 (non-calculator). They '
        'also gate trig-graph and exact-area questions later, so the table pays off repeatedly.</p>'
        '<p>Links to: trigonometry ratios (R12/G), trig graphs (A12), Pythagoras (G).</p>'),
    worked2=W2("A right-angled triangle has a 30° angle and a hypotenuse of 10 cm. Write down the exact length of the side opposite the 30° angle.",
        '<p>sin 30° = opposite ÷ hypotenuse</p>'
        '<p>sin 30° = 1/2, so opposite = 10 × 1/2 = <strong>5 cm</strong></p>',
        "M1 for using sin 30° = 1/2 (exact form), A1 for 5. "
        "Writing 0.5 instead of 1/2 still scores here, but quoting 1/2 keeps 'exact' habits intact."))

BATCH["R7-proportion.html"] = dict(
    keyfacts=KF('<ul>'
        '<li>Direct proportion (∝): both rise together — y = kx</li>'
        '<li>Inverse proportion: one rises as the other falls — y = k/x</li>'
        '<li>Unitary method: find the value of ONE item first, then scale</li>'
        '<li>Best buys: compare price per unit (or amount per £) — same unit both sides</li>'
        '<li>Direction check before answering: doubling workers HALVES the time</li>'
        '</ul>'),
    context=CTX('<p>Proportion questions: 3–5 marks, usually Paper 2/3 (calculator): best buys, recipes, '
        'exchange rates, workers-and-days. The "show it is inversely proportional" version appears at Higher.</p>'
        '<p>Links to: ratio (R4), compound measures (R11), percentages (R9).</p>'),
    worked2=W2("8 pens cost £3.60. Work out the cost of 13 pens.",
        '<p>1 pen: £3.60 ÷ 8 = £0.45</p>'
        '<p>13 pens: 13 × £0.45 = <strong>£5.85</strong></p>',
        "M1 for £3.60 ÷ 8, A1 for £5.85. "
        "If the numbers divide awkwardly (e.g. cost of 13 from a 12-pack price), find the price of 1 item via the HCF-friendly route instead."))

BATCH["A2-substitution.html"] = dict(
    keyfacts=KF('<ul>'
        '<li>Substitute with BRACKETS: 3x² at x = −3 means 3(−3)², never 3 −3²</li>'
        '<li>Order of operations: powers before multiplication, multiplication before addition</li>'
        '<li>(−3)² = +9 but −3² = −9 — the bracket changes everything</li>'
        '<li>Formula questions give you the formula — copy it, do not rely on memory</li>'
        '<li>Two-step formulas (v = u + at): substitute all values, then compute in BIDMAS order</li>'
        '</ul>'),
    context=CTX('<p>Substitution: 2–3 marks on nearly every Paper 1, plus the front end of every '
        'formula-sheet question on Papers 2/3. Negative-value substitution is the discriminating version.</p>'
        '<p>Links to: index laws (N7), formulas and sequences (A23), compound measures (R11).</p>'),
    worked2=W2("The cost £C of hiring a van for d days is C = 45 + 20d. Find the cost of 3 days, and the number of days affordable with £165.",
        '<p>Cost: C = 45 + 20 × 3 = 45 + 60 = <strong>£105</strong></p>'
        '<p>Reverse: 165 = 45 + 20d → 120 = 20d → d = <strong>6 days</strong></p>',
        "M1 for 20 × 3, A1 for 105; M1 for 165 − 45 = 120, A1 for 6. "
        "Formula questions often ask forward AND reverse — the reverse is just equation solving (A17)."))

BATCH["G1-geometric-notation.html"] = dict(
    keyfacts=KF('<ul>'
        '<li>⊥ perpendicular (meets at 90°) · ∥ parallel (never meets, marked with arrows)</li>'
        '<li>△ triangle · ∠ angle · ≅ congruent (identical) · ∼ similar (same shape)</li>'
        '<li>Angle ∠ABC: the MIDDLE letter is the vertex where the angle sits</li>'
        '<li>Polygon names by sides: 5 pentagon, 6 hexagon, 7 heptagon, 8 octagon, 10 decagon</li>'
        '<li>Regular = all sides AND all angles equal</li>'
        '<li>Cube: 6 faces, 12 edges, 8 vertices</li>'
        '</ul>'),
    context=CTX('<p>Notation itself is 1–2 marks a year, but the vocabulary gates the geometry marks: '
        '"using congruent triangles", "the vertex B", "regular hexagon" all assume it. '
        'Properties-of-shapes recall (faces/edges/vertices) is a reliable 1-mark line.</p>'
        '<p>Links to: angle rules (G4), transformations (G), 3D shapes and nets (G).</p>'),
    worked2=W2("A prism has an L-shaped cross-section. State the meaning of the word cross-section, and name the prism type.",
        '<p>Cross-section: the face revealed by slicing the prism parallel to its ends — '
        'the same shape all the way through.</p>'
        '<p>A prism is named by its cross-section, so this is an <strong>L-shaped prism</strong> '
        '(a non-convex hexagonal prism).</p>',
        "B1 for the meaning, B1 for the name. "
        "Volume-of-prism questions open with exactly this vocabulary, so the definition is load-bearing."))

BATCH["R11-compound-measures.html"] = dict(
    keyfacts=KF('<ul>'
        '<li>Speed = distance ÷ time (units: km/h, m/s)</li>'
        '<li>Density = mass ÷ volume (g/cm³)</li>'
        '<li>Pressure = force ÷ area (N/m² = Pa)</li>'
        '<li>Triangle method: cover the one you want; rearrange algebraically for the method mark</li>'
        '<li>Conversions: km/h ÷ 3.6 = m/s; m/s × 3.6 = km/h; 30 min = 0.5 h</li>'
        '</ul>'),
    context=CTX('<p>Compound measures: 3–4 marks on Papers 2/3 (calculator). Unit conversion inside the '
        'question (km/h → m/s, grams → kg) is where the marks are protected or lost.</p>'
        '<p>Links to: units (N13/G14), ratio and proportion (R7), graphs of journeys (A14).</p>'),
    worked2=W2("A car journey of 132 km takes 1 hour 30 minutes on the motorway and 30 minutes through town. Calculate the average speed for the WHOLE journey in km/h.",
        '<p>Total distance = 132 km. Total time = 1.5 + 0.5 = 2 hours.</p>'
        '<p>Average speed = 132 ÷ 2 = <strong>66 km/h</strong></p>',
        "M1 for total time 2 h, A1 for 66. "
        "Average speed is TOTAL distance ÷ TOTAL time — never the average of the two speeds."))

BATCH["N10-decimals-fractions.html"] = dict(
    keyfacts=KF('<ul>'
        '<li>0.5 = 1/2 · 0.25 = 1/4 · 0.75 = 3/4 · 0.2 = 1/5 · 0.1 = 1/10</li>'
        '<li>Eighths: 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875</li>'
        '<li>To convert: tenths → /10, hundredths → /100, thousandths → /1000, then simplify</li>'
        '<li>Recurring with one repeating digit → /9; two digits → /99 (0.5̇ = 5/9, 0.1̇2̇ = 12/99)</li>'
        '<li>"Simplest form" = divide top and bottom by the HCF</li>'
        '</ul>'),
    context=CTX('<p>Conversions: 1–2 marks on Paper 1, and the eighth-values are assumed inside '
        'fractions-of-amounts and percentages questions on all papers.</p>'
        '<p>Links to: ordering (N1), percentages (N12/R9), recurring decimals (Higher N10).</p>'),
    worked2=W2("Show that 0.7̇2̇ can be written as 8/11.",
        '<p>Let x = 0.727272… (72 repeating)</p>'
        '<p>Two repeating digits → multiply by 100: 100x = 72.7272…</p>'
        '<p>Subtract: 100x − x = 72.72… − 0.72… = 72, so 99x = 72</p>'
        '<p>x = 72/99 = ÷9 → <strong>8/11</strong> ✓</p>',
        "M1 for forming 100x, M1 for the subtraction 99x = 72, A1 for 8/11. "
        "In a 'show that' question the final line must END at the given answer — stop exactly there."))

BATCH["N12-fractions-percentages-operators.html"] = dict(
    keyfacts=KF('<ul>'
        '<li>Multiplier table: +25% ×1.25 · +10% ×1.1 · +5% ×1.05 · −20% ×0.8 · −15% ×0.85</li>'
        '<li>Percentage change = change ÷ ORIGINAL × 100</li>'
        '<li>Fraction of amount: ÷ bottom, × top</li>'
        '<li>Common fraction-percentages: 50% = 1/2 · 25% = 1/4 · 12.5% = 1/8 · 10% = 1/10</li>'
        '<li>Chained changes multiply: +20% then −10% = ×1.2 × 0.9 = ×1.08 (net +8%)</li>'
        '</ul>'),
    context=CTX('<p>Percentages of amounts: 3–5 marks per paper — VAT, interest, discounts, depreciation. '
        'The chained-change version and reverse-percentage appear on Papers 2/3 (calculator).</p>'
        '<p>Links to: fractions of amounts (R3), interest and growth (R9), reverse percentages (Higher R9).</p>'),
    worked2=W2("A phone priced at £240 is discounted by 15% in a sale. The sale price then rises by 15%. Explain why the final price is not £240.",
        '<p>Sale price: 240 × 0.85 = £204</p>'
        '<p>Rise: 204 × 1.15 = <strong>£234.60</strong></p>'
        '<p>Why not £240: the 15% rise applies to the SMALLER sale price (£204), so it adds only '
        '£30.60, while the discount removed £36. The percentage is of different bases.</p>',
        "M1 for 0.85 and 1.15 multipliers, A1 for £234.60, B1 for the explanation. "
        "The explanation line is explicitly asked — 'the percentages are of different amounts' scores."))

BATCH["G4-quadrilaterals-triangles.html"] = dict(
    keyfacts=KF('<ul>'
        '<li>Triangle angles: 180° · Quadrilateral angles: 360°</li>'
        '<li>Isosceles: 2 equal sides, 2 equal base angles, 1 line of symmetry</li>'
        '<li>Equilateral: 3 equal sides, 60° each, 3 lines of symmetry</li>'
        '<li>Parallelogram: opposite sides parallel and equal; opposite angles equal; co-interior angles sum 180°</li>'
        '<li>Rhombus: equal sides, 2 symmetry lines (the diagonals), diagonals ⊥</li>'
        '<li>Kite: 2 pairs of adjacent equal sides; diagonals ⊥; 1 symmetry line</li>'
        '<li>Trapezium: one pair of parallel sides; co-interior angles on the parallel sides sum to 180°</li>'
        '</ul>'),
    context=CTX('<p>Angle properties: 2–4 marks per paper. "Give a reason for each stage of your working" '
        'is the standard instruction — reasons are named facts (base angles in an isosceles triangle '
        'are equal), not restated arithmetic.</p>'
        '<p>Links to: angles in parallel lines (G), polygon interior/exterior angles (G), constructions (G).</p>'),
    worked2=W2("In triangle ABC, AB = AC. Angle BAC = 36°. D lies on AC so that BD = BC. Work out angle ABD, giving reasons.",
        '<p>AB = AC → base angles equal: angle ABC = angle ACB = (180 − 36) ÷ 2 = 72°</p>'
        '<p>BD = BC → triangle BCD isosceles → angle BDC = angle BCD = 72°</p>'
        '<p>Angle DBC = 180 − 72 − 72 = 36°</p>'
        '<p>Angle ABD = angle ABC − angle DBC = 72 − 36 = <strong>36°</strong></p>',
        "M1 for base angles 72°, M1 for the isosceles step in BCD, A1 for 36°. "
        "This 'silver ratio' chain is a real AQA Foundation 4-marker — every line needs its reason."))

BATCH["G24-vectors.html"] = dict(
    keyfacts=KF('<ul>'
        '<li>Column vector (a above b): a = right (+) / left (−), b = up (+) / down (−)</li>'
        '<li>Add/subtract component by component; scalar multiply BOTH components</li>'
        '<li>Journey rule: AC = AB + BC (any route between the same two points is equal)</li>'
        '<li>Vector from P to Q = Q − P (end minus start)</li>'
        '<li>Parallel vectors: one is a scalar multiple of the other (both components, same factor)</li>'
        '</ul>'),
    context=CTX('<p>Column-vector arithmetic: 2–3 marks on Paper 1 (non-calculator). The parallel test '
        'and journey rule add the AO2 marks. Vectors reappear in transformations (translation by a vector).</p>'
        '<p>Links to: translation (G), coordinates (A8), midpoint and line segments (A).</p>'),
    worked2=W2("OP = (4, −3) and OQ = (−2, 5) as position vectors (from O). Find PQ as a column vector, and state whether PQ is parallel to (6, −8).",
        '<p>PQ = Q − O − (P − O) = OQ − OP = (−2 − 4, 5 − (−3)) = (−6, 8)</p>'
        '<p>Parallel test: is (−6, 8) = k × (6, −8)? k = −1 works for both components → '
        '<strong>yes, parallel</strong> (PQ points the opposite way along the same direction).</p>',
        "M1 for OQ − OP, A1 for (−6, 8), B1 for parallel with k = −1. "
        "A negative scalar still means parallel — same line direction, opposite sense."))

if __name__ == "__main__":
    run_wave2(BATCH)
