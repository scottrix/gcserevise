#!/usr/bin/env python3
"""Batch 1 content: 15 thinnest AQA maths foundation topics.
Run: python3 content_batch1.py   (from repo root)"""
from expand_topics import run

Q = lambda t: f'<strong>{t}</strong>'
W_SEC = lambda title, body: (
    '<section class="section">\n'
    '<h2>🧮 Worked Examples — Exam Style</h2>\n'
    f'<p>{title}</p>\n{body}\n</section>')
EX = lambda q, steps, marks: (
    '<div class="example">\n'
    f'<p><strong>{q}</strong></p>\n{steps}\n'
    f'<p><em>{marks}</em></p>\n</div>')
SOL_SEC = (
    '<section class="section">\n'
    '<h2>📋 Model Answers — Full Working</h2>\n'
    '<p>Every mark in GCSE maths comes from the working, not just the answer. '
    'These model answers show the lines a mark scheme expects to see.</p>\n'
    '<div class="example">')

BATCH = {}

# ---------------------------------------------------------------- N7-integer-indices
BATCH["N7-integer-indices.html"] = dict(
    marker="Simplify: b⁷ ÷ b²",
    worked=W_SEC("Index laws are among the most reliable marks on the paper — the rules never change, so examiners reuse the same question shapes every year.", 
        EX("Simplify 3a² × 4a³",
            '<p>Multiply the numbers, then apply the multiplication law to the letters:</p>'
            '<p>3 × 4 = 12 &nbsp;and&nbsp; a² × a³ = a²⁺³ = a⁵</p>'
            '<p><strong>Answer: 12a⁵</strong></p>',
            "M1 for adding the indices; A1 for 12a⁵. Common slip: multiplying the indices to get a⁶.") +
        EX("Given 2ⁿ = 32, find the value of n",
            '<p>List powers of 2 until you reach 32:</p>'
            '<p>2, 4, 8, 16, 32 &nbsp;→&nbsp; 32 = 2⁵</p>'
            '<p><strong>n = 5</strong></p>',
            "This is AO2 (reverse thinking): instead of evaluating a power, you identify the power. B1 for 5."))
    + '<p><strong>Exam wording to expect:</strong> "Simplify", "Give your answer in index form", or a table completing 2ⁿ values.</p>',
    questions=[
        "Q7: Simplify: b⁷ ÷ b²",
        "Q8: Simplify: 2m³ × 3m²",
        "Q9: Evaluate: (2³)²",
    ],
    solutions=SOL_SEC +
        '<p><strong>Q1.</strong> Same base, so ADD the indices: a⁴ × a⁶ = a⁴⁺⁶ = <strong>a¹⁰</strong></p>'
        '<p><strong>Q2.</strong> Power of a power: MULTIPLY the indices: (x³)⁵ = x³ˣ⁵ = <strong>x¹⁵</strong></p>'
        '<p><strong>Q3.</strong> Same base, so SUBTRACT the indices: 7⁸ ÷ 7³ = 7⁸⁻³ = <strong>7⁵</strong></p>'
        '<p><strong>Q4.</strong> A negative index means reciprocal: 5⁻² = 1/5² = <strong>1/25</strong></p>'
        '<p><strong>Q5.</strong> Fractional index: cube root first, then square. ³√27 = 3, then 3² = <strong>9</strong>. '
        'Writing (³√27)² earns the method mark even if the arithmetic slips.</p>'
        '<p><strong>Q7.</strong> b⁷ ÷ b² = b⁷⁻² = <strong>b⁵</strong></p>'
        '<p><strong>Q8.</strong> Multiply coefficients and add indices: 2 × 3 = 6, m³ × m² = m⁵, so <strong>6m⁵</strong></p>'
        '<p><strong>Q9.</strong> (2³)² = 2⁶ = <strong>64</strong></p>\n</div>\n</section>')

# ---------------------------------------------------------------- R4-simplifying-ratio
BATCH["R4-simplifying-ratio.html"] = dict(
    marker="Share £63 between two people",
    worked=W_SEC("Ratio questions at Foundation are worth 3–5 marks and always reward one habit: find the value of ONE part first.",
        EX("Share £63 between Amy and Ben in the ratio 4 : 5",
            '<p>Steps: 4 + 5 = 9 parts &nbsp;→&nbsp; £63 ÷ 9 = £7 per part</p>'
            '<p>Amy: 4 × £7 = £28 &nbsp;&nbsp; Ben: 5 × £7 = £35</p>'
            '<p>Check: £28 + £35 = £63 ✓</p>'
            '<p><strong>Answer: Amy £28, Ben £35</strong></p>',
            "M1 for 63 ÷ 9, M1 for one correct share, A1 for both. The final check line is free insurance against slips.") +
        EX("A fruit bowl has apples and bananas in the ratio 3 : 7. There are 40 pieces of fruit. How many are bananas?",
            '<p>3 + 7 = 10 parts. 40 ÷ 10 = 4 per part.</p>'
            '<p>Bananas: 7 × 4 = <strong>28</strong></p>'
            '<p>Ratio method check: 3 × 4 = 12 apples, 12 + 28 = 40 ✓</p>',
            "M1 for 40 ÷ 10, A1 for 28. If asked for the fraction of bananas it would be 7/10 — read the question twice."))
    + '<p><strong>Exam wording to expect:</strong> "Share … in the ratio …", "How many … does … get?", or a part-empty table.</p>',
    questions=[
        "Q6: Simplify: 250 g : 0.5 kg",
        "Q7: Share 48 sweets between two children in the ratio 5 : 3",
    ],
    solutions=SOL_SEC +
        '<p><strong>Q1.</strong> Highest common factor of 16 and 24 is 8: 16 ÷ 8 : 24 ÷ 8 = <strong>2 : 3</strong></p>'
        '<p><strong>Q2.</strong> HCF of 45, 30, 15 is 15: <strong>3 : 2 : 1</strong></p>'
        '<p><strong>Q3.</strong> Decimals: multiply by 10 → 15 : 25 : 40, then ÷ 5 → <strong>3 : 5 : 8</strong></p>'
        '<p><strong>Q4.</strong> Convert units FIRST: 1.5 m = 150 cm, so 75 : 150 → ÷75 → <strong>1 : 2</strong>. '
        'The unit conversion is usually worth a mark — always show it.</p>'
        '<p><strong>Q5.</strong> Multiply BOTH parts by the same number: ×2 → 4 : 10, ×3 → 6 : 15, ×4 → 8 : 20 (any three).</p>'
        '<p><strong>Q6.</strong> 0.5 kg = 500 g, so 250 : 500 → <strong>1 : 2</strong></p>'
        '<p><strong>Q7.</strong> 5 + 3 = 8 parts, 48 ÷ 8 = 6 per part: <strong>30 sweets and 18 sweets</strong></p>\n</div>\n</section>')

# ---------------------------------------------------------------- N1-ordering-numbers
BATCH["N1-ordering-numbers.html"] = dict(
    marker="Which is larger: 2/3 or 0.66?",
    worked=W_SEC("Ordering questions look easy and are where careless marks die. Two habits fix it: convert everything to the same form, and remember that with negatives, the bigger-looking number is smaller.",
        EX("Write in order, smallest first: −3.5, −3.05, 3.05, −3",
            '<p>Negatives first (smallest = most negative): −3.5 < −3.05 < −3, then positives last.</p>'
            '<p><strong>Answer: −3.5, −3.05, −3, 3.05</strong></p>',
            "B1 all four correct. Trap: −3.05 looks smaller than −3.5 but sits closer to zero, so it is LARGER.") +
        EX("Write in order of size, smallest first: 7/8, 0.9, 4/5, 0.85",
            '<p>Convert all to decimals: 7/8 = 0.875, 0.9, 4/5 = 0.8, 0.85</p>'
            '<p>Order: 0.8 < 0.85 < 0.875 < 0.9</p>'
            '<p><strong>Answer: 4/5, 0.85, 7/8, 0.9</strong></p>',
            "M1 for converting fractions to decimals (or all to fractions with a common denominator), A1 for the correct order."))
    + '<p><strong>Exam wording to expect:</strong> "Write … in order of size, starting with the smallest" — nearly always 1 mark, no working shown in the mark scheme but you may still use the margin.</p>',
    questions=[
        "Q6: Order from smallest to largest: −1, −1.5, −0.5, 0",
        "Q7: Which is larger: 2/3 or 0.66?",
    ],
    solutions=SOL_SEC +
        '<p><strong>Q1.</strong> Most negative is smallest: <strong>−8, −2, 0, 4, 6</strong></p>'
        '<p><strong>Q2.</strong> Compare place by place: 0.08 (8 hundredths) < 0.7 < 0.71 < 0.8 → '
        '<strong>0.08, 0.7, 0.71, 0.8</strong></p>'
        '<p><strong>Q3.</strong> Convert to /10: 1/2 = 5/10, 2/5 = 4/10, 3/10 → <strong>3/10, 2/5, 1/2</strong></p>'
        '<p><strong>Q4.</strong> −5 is further from zero on the negative side, so <strong>−5 < −2</strong></p>'
        '<p><strong>Q5.</strong> Convert to decimals: 1.5, 1.333…, 1.25, 1.75 → <strong>1.25, 1⅓, 1.5, 1¾</strong></p>'
        '<p><strong>Q6.</strong> <strong>−1.5, −1, −0.5, 0</strong></p>'
        '<p><strong>Q7.</strong> 2/3 = 0.666… (recurring), which is greater than 0.66, so <strong>2/3 is larger</strong>. '
        'Write 0.666… or 0.6̇ to justify — a bare "2/3" may not earn the mark.</p>\n</div>\n</section>')

# ---------------------------------------------------------------- A22-inequalities
BATCH["A22-inequalities.html"] = dict(
    marker="Solve: 7 − 2x ≥ 3",
    worked=W_SEC("Inequality solving follows exactly the same steps as equation solving — with one extra rule the examiner is testing: flip the symbol when multiplying or dividing by a negative.",
        EX("Solve 5x + 3 ≥ 2x − 9",
            '<p>Collect x terms on one side, numbers on the other:</p>'
            '<p>5x − 2x ≥ −9 − 3 &nbsp;→&nbsp; 3x ≥ −12</p>'
            '<p>Divide by 3 (positive — no flip): <strong>x ≥ −4</strong></p>',
            "M1 for valid rearrangement, A1 for x ≥ −4. Writing the answer as an equation (x = −4) loses the final mark — keep the symbol.") +
        EX("List the integer values that satisfy −2 ≤ x < 3",
            '<p>x can equal −2 (filled circle — ≤) but not 3 (open circle — <).</p>'
            '<p><strong>Answer: −2, −1, 0, 1, 2</strong></p>',
            "B1 all five values. Sketching the number line first, with the circles, makes the boundary values obvious."))
    + '<p><strong>Exam wording to expect:</strong> "Solve the inequality", "List the integer values …", or "Show your answer on the number line".</p>',
    questions=[
        "Q7: Solve: 7 − 2x ≥ 3",
        "Q8: Solve: 4(x − 1) < 2x + 6",
    ],
    solutions=SOL_SEC +
        '<p><strong>Q1.</strong> 4x − 7 > 13 → 4x > 20 (add 7) → <strong>x > 5</strong> (divide by 4)</p>'
        '<p><strong>Q2.</strong> 2x + 5 ≤ x + 8 → x ≤ 3 (subtract x, subtract 5)</p>'
        '<p><strong>Q3.</strong> −3x > 12 → divide by −3 and FLIP: <strong>x < −4</strong>. '
        'Forgetting the flip is the single most common error on this topic.</p>'
        '<p><strong>Q4.</strong> −3 < x ≤ 2 → open at −3, filled at 2 → <strong>−2, −1, 0, 1, 2</strong></p>'
        '<p><strong>Q5.</strong> x² − 9 > 0 → (x + 3)(x − 3) > 0. Sketch y = x²: above the x-axis '
        'means x < −3 or x > 3 → <strong>x < −3 or x > 3</strong></p>'
        '<p><strong>Q6.</strong> x² + 5x + 6 < 0 → (x + 2)(x + 3) < 0 → between the roots → '
        '<strong>−3 < x < −2</strong></p>'
        '<p><strong>Q7.</strong> 7 − 2x ≥ 3 → −2x ≥ −4 → divide by −2, FLIP → <strong>x ≤ 2</strong></p>'
        '<p><strong>Q8.</strong> 4x − 4 < 2x + 6 → 2x < 10 → <strong>x < 5</strong></p>\n</div>\n</section>')

# ---------------------------------------------------------------- N6-powers-and-roots
BATCH["N6-powers-and-roots.html"] = dict(
    marker="Q6: Calculate: √225",
    worked=W_SEC("Square and cube numbers are free marks — but only if you have memorised them up to 15² and 5³. Estimation questions reward bracketing between perfect squares.",
        EX("A square garden has an area of 169 m². Find the length of one side.",
            '<p>Side × side = 169, so side = √169.</p>'
            '<p>Check nearby squares: 12² = 144 (too small), 13² = 169 ✓</p>'
            '<p><strong>Answer: 13 m</strong></p>',
            "B1 for 13. Units matter: m not m² — the side is a length.") +
        EX("Estimate √90",
            '<p>Bracket between perfect squares: 81 < 90 < 100, so 9 < √90 < 10.</p>'
            '<p>90 is closer to 81 than to 100? 90 − 81 = 9 and 100 − 90 = 10, so try ≈ 9.5.</p>'
            '<p>9.5² = 90.25 — just over, so <strong>√90 ≈ 9.49</strong> (accept 9.4–9.5).</p>',
            "M1 for 81 < 90 < 100, A1 for an estimate between 9.4 and 9.5. The answer to 1 d.p. is 9.5."))
    + '<p><strong>Exam wording to expect:</strong> "Write down the value of …" (memorised squares/cubes), or "Estimate …" (never a calculator answer).</p>',
    questions=[
        "Q6: Calculate: √225",
        "Q7: Write down the first five square numbers",
    ],
    solutions=SOL_SEC +
        '<p><strong>Q1.</strong> 7² = 7 × 7 = <strong>49</strong>; 11² = 11 × 11 = <strong>121</strong></p>'
        '<p><strong>Q2.</strong> √81 = <strong>9</strong> (9 × 9 = 81); √196 = <strong>14</strong> (14 × 14 = 196)</p>'
        '<p><strong>Q3.</strong> 6³ = 6 × 6 × 6 = <strong>216</strong>; ³√125 = <strong>5</strong> (5 × 5 × 5 = 125)</p>'
        '<p><strong>Q4.</strong> 7² = 49 and 8² = 64, and 50 sits almost exactly between them: '
        '<strong>√50 ≈ 7.1</strong> (actual 7.07…). Method mark for using 49 < 50 < 64.</p>'
        '<p><strong>Q5.</strong> 2⁵ = 32 and 3⁴ = 81, so 32 − 81 = <strong>−49</strong>. '
        'Do each power FIRST, then subtract — 2⁵⁻⁴ is the classic misread.</p>'
        '<p><strong>Q6.</strong> √225 = <strong>15</strong></p>'
        '<p><strong>Q7.</strong> 1, 4, 9, 16, <strong>25</strong></p>\n</div>\n</section>')

# ---------------------------------------------------------------- R3-fractions-of-amounts
BATCH["R3-fractions-of-amounts.html"] = dict(
    marker="Q6: Find 7/10 of £90",
    worked=W_SEC("Fractions of amounts come in two shapes: 'fraction OF amount' (divide then multiply) and 'fraction IS amount' (unitary method backwards). Learn both directions.",
        EX("A class of 32 students: 3/8 walk to school. How many walk?",
            '<p>1/8 of 32 = 32 ÷ 8 = 4. &nbsp;Then 3/8 = 3 × 4 = <strong>12 students</strong>.</p>'
            '<p>Order matters: divide by the bottom FIRST, then multiply by the top — '
            'the numbers stay small and friendly.</p>',
            "M1 for 32 ÷ 8, A1 for 12. Writing 32 × 3/8 as one step is fine but show the ÷8 line to bank the method mark.") +
        EX("2/5 of a train journey is 14 miles. How long is the whole journey?",
            '<p>2/5 = 14 miles → 1/5 = 14 ÷ 2 = 7 miles → whole journey (5/5) = 7 × 5 = <strong>35 miles</strong>.</p>'
            '<p>Check: 2/5 of 35 = 35 ÷ 5 × 2 = 14 ✓</p>',
            "M1 for 14 ÷ 2 (unitary method), A1 for 35. Reverse 'fraction of' questions appear every year — recognise the phrase '… is 14'."))
    + '<p><strong>Exam wording to expect:</strong> "Find … of …", "What fraction of … is …?", or a reverse: "… of the total is 24, how many altogether?"</p>',
    questions=[
        "Q6: Find 7/10 of £90",
        "Q7: 5/6 of a number is 45. Find the number.",
    ],
    solutions=SOL_SEC +
        '<p><strong>Q1.</strong> 240 ÷ 8 = 30, then 30 × 5 = <strong>150</strong></p>'
        '<p><strong>Q2.</strong> 18/45 → ÷9 top and bottom → <strong>2/5</strong></p>'
        '<p><strong>Q3.</strong> 15/25 → ÷5 → <strong>3/5</strong></p>'
        '<p><strong>Q4.</strong> Total parts 4 + 7 = 11; apples are 4 parts → <strong>4/11</strong>. '
        'The denominator is ALL the parts, not just the other item.</p>'
        '<p><strong>Q5.</strong> 3/4 of the number = 54 → 1/4 = 54 ÷ 3 = 18 → whole = 18 × 4 = <strong>72</strong>. '
        'Check: 72 ÷ 4 × 3 = 54 ✓</p>'
        '<p><strong>Q6.</strong> 90 ÷ 10 = 9, 9 × 7 = <strong>£63</strong></p>'
        '<p><strong>Q7.</strong> 1/6 = 45 ÷ 5 = 9 → number = 9 × 6 = <strong>54</strong></p>\n</div>\n</section>')

# ---------------------------------------------------------------- G21-exact-trig-values
BATCH["G21-exact-trig-values.html"] = dict(
    marker="Q6: Write down the exact value of cos 0°",
    worked=W_SEC("Exact trig values are 'write down' marks — but only from the table or the two special triangles. Never reach for a calculator: √3/2 typed as 0.866… scores zero.",
        EX("Write down the exact value of cos 30°",
            '<p>From the table: cos 30° = <strong>√3/2</strong>.</p>'
            '<p>Where it comes from: half an equilateral triangle of side 2 gives sides 1, 2, √3 — '
            'cos 30° = adjacent/hypotenuse = √3/2.</p>',
            "B1 for √3/2. Writing 0.866 scores 0 — the question says exact.") +
        EX("Write down the exact value of tan 30°",
            '<p>Same half-equilateral triangle: tan 30° = opposite/adjacent = 1/√3.</p>'
            '<p>Rationalised: 1/√3 = <strong>√3/3</strong> (multiply top and bottom by √3).</p>',
            "B1 for 1/√3 or √3/3 — both forms are accepted. 0.577 is not."))
    + '<p><strong>Exam wording to expect:</strong> "Write down the exact value of …" — the word exact bans decimals. Memorise the table for 0°, 30°, 45°, 60°, 90°.</p>',
    questions=[
        "Q6: Write down the exact value of cos 0°",
        "Q7: Write down the exact value of tan 60°",
    ],
    solutions=SOL_SEC +
        '<p><strong>Q1.</strong> sin 60° = <strong>√3/2</strong> (from the table, or the half-equilateral triangle)</p>'
        '<p><strong>Q2.</strong> tan 45° = <strong>1</strong> — the isosceles right triangle has equal legs</p>'
        '<p><strong>Q3.</strong> sin 30° = 1/2 and cos 60° = 1/2, so 1/2 × 1/2 = <strong>1/4</strong></p>'
        '<p><strong>Q4.</strong> (√2/2)² + (√2/2)² = 1/2 + 1/2 = <strong>1</strong> — this is sin²+cos² = 1, worth knowing</p>'
        '<p><strong>Q5.</strong> sin 45° = opposite/hypotenuse → √2/2 = opp/8 → opp = 8 × √2/2 = <strong>4√2 cm</strong></p>'
        '<p><strong>Q6.</strong> cos 0° = <strong>1</strong></p>'
        '<p><strong>Q7.</strong> tan 60° = <strong>√3</strong></p>\n</div>\n</section>')

# ---------------------------------------------------------------- R7-proportion
BATCH["R7-proportion.html"] = dict(
    marker="y is inversely proportional to x",
    worked=W_SEC("Direct proportion: both quantities rise together (y = kx). Inverse: one rises as the other falls (y = k/x). Exam questions expect you to find k first, then answer.",
        EX("y is directly proportional to x. When x = 4, y = 10. Find y when x = 14.",
            '<p>y = kx → 10 = 4k → k = 2.5</p>'
            '<p>So y = 2.5x → y = 2.5 × 14 = <strong>35</strong></p>',
            "M1 for finding k, A1 for 35. Writing the proportional statement first (y = kx) banks the method mark even if k goes wrong.") +
        EX("4 workers build a wall in 6 days. How long would 8 workers take (same rate)?",
            '<p>More workers → fewer days, so this is INVERSE proportion.</p>'
            '<p>Total work = 4 × 6 = 24 worker-days. 24 ÷ 8 = <strong>3 days</strong>.</p>',
            "M1 for 4 × 6, A1 for 3. Doubling workers halves the time — sanity-check the direction before answering."))
    + '<p><strong>Exam wording to expect:</strong> "y is (inversely) proportional to x", symbol ∝, or "best value" money comparisons.</p>',
    questions=[
        "Q6: y ∝ x. When x = 2, y = 8. Find y when x = 9.",
        "Q7: 5 tins of soup cost £6.25. How much do 8 tins cost?",
    ],
    solutions=SOL_SEC +
        '<p><strong>Q1.</strong> y = kx, k = 18 ÷ 6 = 3 → y = 3 × 15 = <strong>45</strong></p>'
        '<p><strong>Q2.</strong> 8 : 12 = 2 : 3 and 12 : 18 = 2 : 3 → <strong>yes, in proportion</strong>. '
        'Cross-check: 8 × 18 = 144 = 12 × 12 ✓</p>'
        '<p><strong>Q3.</strong> 4 → 20 is × 5, so x = 7 × 5 = <strong>35</strong></p>'
        '<p><strong>Q4.</strong> Parts: 5 + 1 = 6. Cement = 1 part of 6 = <strong>1/6</strong></p>'
        '<p><strong>Q5.</strong> £4.50 ÷ 3 = £1.50 per kg → 7 × £1.50 = <strong>£10.50</strong></p>'
        '<p><strong>Q6.</strong> k = 8 ÷ 2 = 4 → y = 4 × 9 = <strong>36</strong></p>'
        '<p><strong>Q7.</strong> £6.25 ÷ 5 = £1.25 per tin → 8 × £1.25 = <strong>£10</strong></p>\n</div>\n</section>')

# ---------------------------------------------------------------- A2-substitution
BATCH["A2-substitution.html"] = dict(
    corrections=[("<li>18</li>", "<li>21</li>")],
    marker="Q7: Evaluate 3x² − 2x when x = −3",
    worked=W_SEC("Substitution is guaranteed marks if you follow two rules: put EVERY substituted number in brackets, and square the whole bracket when squaring negatives.",
        EX("Evaluate 3x² − 2x when x = −3",
            '<p>Substitute in brackets: 3(−3)² − 2(−3)</p>'
            '<p>Square first: (−3)² = 9, so 3 × 9 = 27</p>'
            '<p>−2(−3) = +6 &nbsp;→&nbsp; 27 + 6 = <strong>33</strong></p>',
            "M1 for 3 × 9 or correct handling of −2(−3) = +6, A1 for 33. Writing 3 −3² = 3 − 9 (no brackets) gives −30 — the classic error.") +
        EX("Use the formula v = u + at to find v when u = 5, a = −2, t = 8.",
            '<p>v = 5 + (−2)(8) = 5 + (−16) = 5 − 16 = <strong>−3</strong></p>'
            '<p>A negative answer can be correct — here it means the object is moving backwards.</p>',
            "M1 for correct substitution, A1 for −3. Formula questions tell you the equation — read it off the page, never work from memory."))
    + '<p><strong>Exam wording to expect:</strong> "Find the value of … when …", or a named formula (area, speed, v = u + at) to substitute into.</p>',
    questions=[
        "Q7: Evaluate 3x² − 2x when x = −3",
        "Q8: Use v = u + at to find v when u = 5, a = −2, t = 8",
    ],
    solutions=SOL_SEC +
        '<p><strong>Q1.</strong> 5x − 2 = 5(3) − 2 = 15 − 2 = <strong>13</strong></p>'
        '<p><strong>Q2.</strong> 2a + 3b = 2(4) + 3(5) = 8 + 15 = <strong>23</strong></p>'
        '<p><strong>Q3.</strong> 3x² = 3(4²) = 3 × 16 = <strong>48</strong>. Square FIRST, then multiply by 3 — '
        'not (3x)².</p>'
        '<p><strong>Q4.</strong> (m + 2)(n − 1) = (5 + 2)(4 − 1) = 7 × 3 = <strong>21</strong></p>'
        '<p><strong>Q5.</strong> A = ½bh = ½ × 10 × 7 = ½ × 70 = <strong>35</strong></p>'
        '<p><strong>Q6.</strong> x² + 2x − 3 with x = −2: (−2)² + 2(−2) − 3 = 4 − 4 − 3 = <strong>−3</strong></p>'
        '<p><strong>Q7.</strong> 3(−3)² − 2(−3) = 27 + 6 = <strong>33</strong></p>'
        '<p><strong>Q8.</strong> v = 5 + (−2)(8) = 5 − 16 = <strong>−3</strong></p>\n</div>\n</section>')

# ---------------------------------------------------------------- G1-geometric-notation
BATCH["G1-geometric-notation.html"] = dict(
    marker="Write the notation for triangle ABC is similar to triangle DEF",
    worked=W_SEC("Geometric notation questions are pure recall marks. Learn the symbols as a matching set — and always name lines/angles in the right letter order.",
        EX("Line PQ is parallel to line RS. Write this in notation, and state the angle relationship.",
            '<p>Notation: <strong>PQ ∥ RS</strong></p>'
            '<p>Parallel lines never meet — marked with arrows on diagrams. Angles in a matching '
            '"Z" (alternate) or "F" (corresponding) position are equal.</p>',
            "B1 for the ∥ symbol used correctly. Angle facts linked to parallel lines are the usual follow-up question.") +
        EX("Write the angle ABC, and explain what the middle letter means.",
            '<p>Notation: <strong>∠ABC</strong> (or just ABC in exam text).</p>'
            '<p>The middle letter (B) is the VERTEX — the corner where the angle sits. '
            '∠ABC means the angle between ray BA and ray BC.</p>',
            "B1 for ∠ABC with B identified as the vertex. Angle names in proofs must match this letter order."))
    + '<p><strong>Exam wording to expect:</strong> "Write down the notation for …", or reading a diagram that uses the symbols.</p>',
    questions=[
        "Q6: Write the notation for: triangle ABC is similar to triangle DEF",
        "Q7: How many faces does a cube have?",
    ],
    solutions=SOL_SEC +
        '<p><strong>Q1.</strong> <strong>AB ⊥ CD</strong> — the ⊥ symbol means perpendicular (meets at 90°)</p>'
        '<p><strong>Q2.</strong> A pentagon has <strong>5 vertices</strong> (one per corner)</p>'
        '<p><strong>Q3.</strong> 45° is between 0° and 90° → <strong>acute</strong></p>'
        '<p><strong>Q4.</strong> A regular polygon has all sides and angles equal; 6 sides → '
        '<strong>regular hexagon</strong></p>'
        '<p><strong>Q5.</strong> A cube has <strong>12 edges</strong> (4 on top, 4 on bottom, 4 vertical)</p>'
        '<p><strong>Q6.</strong> <strong>△ABC ∼ △DEF</strong> — the ∼ symbol means similar (same shape, different size); '
        '≅ means congruent (identical)</p>'
        '<p><strong>Q7.</strong> <strong>6 faces</strong></p>\n</div>\n</section>')

# ---------------------------------------------------------------- R11-compound-measures
BATCH["R11-compound-measures.html"] = dict(
    marker="Q6: A crate weighs 300 N",
    worked=W_SEC("Speed, density and pressure are all 'compound measures': one unit divided by another. Learn the triangle (or rearrange every time) and convert units BEFORE calculating.",
        EX("A cyclist rides 42 km in 2 hours 30 minutes. Calculate the average speed in km/h.",
            '<p>Convert time first: 2 h 30 min = 2.5 h (30 ÷ 60).</p>'
            '<p>Speed = distance ÷ time = 42 ÷ 2.5 = <strong>16.8 km/h</strong></p>',
            "M1 for 2.5 (the conversion), A1 for 16.8. Dividing by 2 h 30 min as if it were 2.3 is the classic error.") +
        EX("A metal block has mass 810 g and density 2.7 g/cm³. Find its volume.",
            '<p>Density = mass ÷ volume → volume = mass ÷ density</p>'
            '<p>Volume = 810 ÷ 2.7 = <strong>300 cm³</strong></p>'
            '<p>Check: 2.7 × 300 = 810 ✓</p>',
            "M1 for rearranging, A1 for 300. Rearranging the triangle earns the method mark even with an arithmetic slip."))
    + '<p><strong>Exam wording to expect:</strong> "Calculate the average speed/density/pressure", "Convert … into …", or a best-value comparison.</p>',
    questions=[
        "Q6: A crate weighs 300 N and sits on an area of 1.5 m². Calculate the pressure.",
        "Q7: Convert 15 m/s into km/h",
    ],
    solutions=SOL_SEC +
        '<p><strong>Q1.</strong> Speed = 315 ÷ 3.5 = <strong>90 km/h</strong></p>'
        '<p><strong>Q2.</strong> Mass = density × volume = 1.2 × 150 = <strong>180 g</strong></p>'
        '<p><strong>Q3.</strong> km/h → m/s: divide by 3.6. 72 ÷ 3.6 = <strong>20 m/s</strong></p>'
        '<p><strong>Q4.</strong> Pressure = force ÷ area → area = 500 ÷ 2500 = <strong>0.2 m²</strong></p>'
        '<p><strong>Q5.</strong> Price per kg: £3.20 ÷ 0.4 = £8.00/kg; £4.50 ÷ 0.6 = £7.50/kg → '
        '<strong>600 g for £4.50</strong> is better value</p>'
        '<p><strong>Q6.</strong> Pressure = 300 ÷ 1.5 = <strong>200 Pa</strong></p>'
        '<p><strong>Q7.</strong> 15 × 3.6 = <strong>54 km/h</strong></p>\n</div>\n</section>')

# ---------------------------------------------------------------- N10-decimals-fractions
BATCH["N10-decimals-fractions.html"] = dict(
    marker="Q6: Convert 0.125 to a fraction in its simplest form",
    worked=W_SEC("Terminating decimals become fractions by reading the place value (tenths, hundredths, thousandths) then simplifying. Recurring decimals need the algebra trick.",
        EX("Convert 0.375 to a fraction in its simplest form.",
            '<p>0.375 = 375/1000 (three decimal places → thousandths)</p>'
            '<p>Simplify: ÷ 125 top and bottom → <strong>3/8</strong></p>'
            '<p>Quick check: 1/8 = 0.125, so 3/8 = 0.375 ✓</p>',
            "M1 for 375/1000, A1 for 3/8. Knowing the eighths (0.125, 0.25, 0.375, 0.5 …) turns this into write-down marks.") +
        EX("Write 7/40 as a decimal.",
            '<p>40 = 5 × 8, so scale to a power of 10: 7/40 = 17.5/100 = <strong>0.175</strong></p>'
            '<p>Or divide: 7 ÷ 40 = 0.175 ✓</p>',
            "B1 for 0.175. Fractions with denominators of 2, 4, 5, 8, 10, 20, 25, 40 are the exam favourites."))
    + '<p><strong>Exam wording to expect:</strong> "Write … as a fraction in its simplest form" or "Show that 0.7̇2̇ = 8/11" (Higher — the &ldquo;show that&rdquo; format means every algebra line is marked).</p>',
    questions=[
        "Q6: Convert 0.125 to a fraction in its simplest form",
        "Q7: Write 5/8 as a decimal",
    ],
    solutions=SOL_SEC +
        '<p><strong>Q1.</strong> 0.35 = 35/100 → ÷5 → <strong>7/20</strong></p>'
        '<p><strong>Q2.</strong> 3 ÷ 20: 20 × 0.1 = 2, remainder 1 → 10/20 = 0.05 → total <strong>0.15</strong></p>'
        '<p><strong>Q3.</strong> 1 ÷ 6 = <strong>0.1666…</strong> = 0.16 recurring (the 6 repeats)</p>'
        '<p><strong>Q4.</strong> Let x = 0.555… Then 10x = 5.555…, so 10x − x = 5, 9x = 5 → '
        '<strong>x = 5/9</strong>. The rule: one repeating digit → denominator 9.</p>'
        '<p><strong>Q5.</strong> Let x = 0.121212… Then 100x = 12.1212…, so 99x = 12 → '
        'x = 12/99 → ÷3 → <strong>4/33</strong>. Two repeating digits → denominator 99.</p>'
        '<p><strong>Q6.</strong> 0.125 = 125/1000 → ÷125 → <strong>1/8</strong></p>'
        '<p><strong>Q7.</strong> 5 ÷ 8 = <strong>0.625</strong></p>\n</div>\n</section>')

# ---------------------------------------------------------------- N12-fractions-percentages-operators
BATCH["N12-fractions-percentages-operators.html"] = dict(
    marker="Q6: Find 12.5% of 640",
    worked=W_SEC("Percentage change questions chain two operations — and the trap is assuming +20% then −10% returns near the start. Multipliers do the bookkeeping.",
        EX("A jumper costs £45. The price increases by 20%, then the new price decreases by 10%. What is the final price?",
            '<p>Increase: ×1.20 → £45 × 1.20 = £54</p>'
            '<p>Decrease: ×0.90 → £54 × 0.90 = <strong>£48.60</strong></p>'
            '<p>Not £45 × 1.10 — the 10% comes off the NEW price.</p>',
            "M1 for 45 × 1.2, M1 for 54 × 0.9, A1 for £48.60. The net effect is ×1.08 (a rise), not ×1.10.") +
        EX("The value of a car rises from £80 to £92. Write the percentage increase.",
            '<p>Change = 92 − 80 = £12. Percentage = 12 ÷ 80 × 100 = <strong>15%</strong></p>'
            '<p>The rule: change ÷ ORIGINAL × 100 — divide by where you started.</p>',
            "M1 for 12/80, A1 for 15%. Dividing by 92 instead of 80 is the standard slip."))
    + '<p><strong>Exam wording to expect:</strong> "Find …% of …", "Increase/decrease by …%", "Express … as a percentage of …".</p>',
    questions=[
        "Q6: Find 12.5% of 640",
        "Q7: Express 18/45 as a percentage",
    ],
    solutions=SOL_SEC +
        '<p><strong>Q1.</strong> 54 ÷ 3 = 18, then 18 × 2 = <strong>£36</strong></p>'
        '<p><strong>Q2.</strong> 35% = 0.35 → 0.35 × 240 = <strong>84</strong></p>'
        '<p><strong>Q3.</strong> Increase by 15% → multiplier 1.15 → 180 × 1.15 = <strong>£207</strong>. '
        'One multiplication replaces the find-10%-and-add method.</p>'
        '<p><strong>Q4.</strong> Decrease by 30% → multiplier 0.70 → 250 × 0.7 = <strong>£175</strong></p>'
        '<p><strong>Q5.</strong> 45 ÷ 150 × 100 = <strong>30%</strong></p>'
        '<p><strong>Q6.</strong> 12.5% = 1/8 → 640 ÷ 8 = <strong>80</strong></p>'
        '<p><strong>Q7.</strong> 18/45 = 2/5 (÷9) = 40/100 → <strong>40%</strong></p>\n</div>\n</section>')

# ---------------------------------------------------------------- G4-quadrilaterals-triangles
BATCH["G4-quadrilaterals-triangles.html"] = dict(
    marker="Q6: Two angles of a triangle are 55° and 65°. Find the third angle.",
    worked=W_SEC("Angle questions on quadrilaterals lean on two facts: angles in a triangle sum to 180°, angles in a quadrilateral to 360° — plus the special properties of each shape.",
        EX("Two angles of a triangle are 55° and 65°. Find the third angle.",
            '<p>Angles in a triangle sum to 180°.</p>'
            '<p>55 + 65 = 120 → 180 − 120 = <strong>60°</strong></p>',
            "B1 for 60°. If the triangle is isosceles and one base angle is given, remember the OTHER base angle equals it.") +
        EX("A parallelogram has one angle of 70°. Write down the sizes of the other three angles.",
            '<p>Opposite angles are equal: one more angle = <strong>70°</strong>.</p>'
            '<p>Co-interior (allied) angles sum to 180°: the other two = 180 − 70 = <strong>110°</strong> each.</p>',
            "B1 for 70°, B1 for 110° and 110°. Sketching the parallelogram and labelling is accepted working."))
    + '<p><strong>Exam wording to expect:</strong> "Work out the size of angle …" (give reasons), "Write down" (properties recall), or symmetry counting.</p>',
    questions=[
        "Q6: Two angles of a triangle are 55° and 65°. Find the third angle.",
        "Q7: Work out the size of each interior angle of a regular pentagon.",
    ],
    solutions=SOL_SEC +
        '<p><strong>Q1.</strong> Apex 50° between the equal sides → two base angles equal: '
        '(180 − 50) ÷ 2 = <strong>65° each</strong></p>'
        '<p><strong>Q2.</strong> A rhombus has <strong>2</strong> lines of symmetry (its diagonals)</p>'
        '<p><strong>Q3.</strong> Kite diagonals meet at <strong>90°</strong> — always, by symmetry</p>'
        '<p><strong>Q4.</strong> Co-interior angles between parallel sides: 180 − 72 = <strong>108°</strong></p>'
        '<p><strong>Q5.</strong> All sides equal, angles not 90° → <strong>rhombus</strong></p>'
        '<p><strong>Q6.</strong> 180 − (55 + 65) = <strong>60°</strong></p>'
        '<p><strong>Q7.</strong> Sum = (5 − 2) × 180 = 540° → regular → 540 ÷ 5 = <strong>108° each</strong>. '
        'M1 for 540, A1 for 108.</p>\n</div>\n</section>')

# ---------------------------------------------------------------- G24-vectors
BATCH["G24-vectors.html"] = dict(
    marker="Given AB = (3 −1) and BC = (2 4), find AC",
    worked=W_SEC("Column vectors add/subtract component by component. The journey rule (A to C via B) and the scalar-multiple parallel test are the two exam favourites.",
        EX("Given AB = (3, −1) as a column vector and BC = (2, 4), find AC.",
            '<p>Journey rule: A → C = A → B then B → C</p>'
            '<p>AC = AB + BC = (3 + 2, −1 + 4) = <strong>(5, 3)</strong></p>',
            "M1 for adding the components, A1 for (5, 3). Column vectors are written vertically in the exam — practise the layout.") +
        EX("Is the vector (6, 9) parallel to the vector (2, 3)? Explain.",
            '<p>Parallel vectors are scalar multiples of each other.</p>'
            '<p>(6, 9) = 3 × (2, 3) — one multiplier works for BOTH components → <strong>yes, parallel</strong></p>',
            "B1 yes with B1 justification (×3). Both components must scale by the same factor."))
    + '<p><strong>Exam wording to expect:</strong> "Write (vector) as a column vector", "Find AB as a column vector", "Show that … is parallel to …".</p>',
    questions=[
        "Q6: Given AB = (3, −1) and BC = (2, 4) as column vectors, find AC",
        "Q7: Is (6, 9) parallel to (2, 3)? Explain.",
    ],
    solutions=SOL_SEC +
        '<p><strong>Q1.</strong> Add component by component: 5 + 3 = 8, −2 + 7 = 5 → <strong>(8, 5)</strong></p>'
        '<p><strong>Q2.</strong> Scalar multiply each component: 4 × 2 = 8, 4 × (−3) = −12 → <strong>(8, −12)</strong></p>'
        '<p><strong>Q3.</strong> Subtract component by component: 8 − 3 = 5, 5 − 9 = −4 → <strong>(5, −4)</strong></p>'
        '<p><strong>Q4.</strong> 2 × (4, 1) = (8, 2) and 3 × (−2, 5) = (−6, 15); add: '
        '(8 − 6, 2 + 15) = <strong>(2, 17)</strong></p>'
        '<p><strong>Q5.</strong> PQ = Q − P = (6 − 1, 2 − 4) = <strong>(5, −2)</strong>. '
        'End point minus start point — order matters and reversing gives the negative.</p>'
        '<p><strong>Q6.</strong> AC = (5, 3) — journey rule AB + BC</p>'
        '<p><strong>Q7.</strong> Yes: (6, 9) = 3 × (2, 3), same scalar for both components</p>\n</div>\n</section>')

if __name__ == "__main__":
    run(BATCH)
