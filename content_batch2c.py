#!/usr/bin/env python3
"""Batch 2c: A5, N9, N8, R10, R6, A15, A20, R5, R16 (with 3 answer corrections)."""
from content_waves import W_SEC, EX, SOL_HEAD, KF, CTX, W2, run, run2

B = {}

B["A5-rearranging-formulae.html"] = dict(
    marker="Q7: Rearrange y = 4(x − 3) to make x the subject",
    worked=W_SEC("Rearranging = solving an equation where the 'answer' is a letter. Reverse the operations acting on the target letter, one layer at a time.",
        EX("Rearrange T = 5c + 8 to make c the subject.",
            '<p>Subtract 8: T − 8 = 5c &nbsp;→&nbsp; Divide by 5: <strong>c = (T − 8)/5</strong></p>',
            "M1 for subtracting 8 first, A1 for the division. Undo in reverse order: +8 was LAST, so it comes off FIRST.") +
        EX("Rearrange V = πr²h to make r the subject.",
            '<p>÷ πh: V/(πh) = r² &nbsp;→&nbsp; Square root: <strong>r = √(V/(πh))</strong></p>',
            "M1 for dividing by πh, A1 for the root. The root undoes the SQUARE — last-in-first-out again."))
    + '<p><strong>Exam wording to expect:</strong> "Make … the subject", "Rearrange … to give an equation for …".</p>',
    questions=["Q7: Rearrange y = 4(x − 3) to make x the subject", "Q8: Rearrange A = 2(lw + wh) to make w the subject"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> a − 2 = 3b → <strong>b = (a − 2)/3</strong></p>'
        '<p><strong>Q2.</strong> Divide by m: <strong>a = F/m</strong></p>'
        '<p><strong>Q3.</strong> Divide by 2π: <strong>r = C/(2π)</strong></p>'
        '<p><strong>Q4.</strong> Subtract u², divide by 2a: <strong>s = (v² − u²)/(2a)</strong></p>'
        '<p><strong>Q5.</strong> P/2 = l + w → <strong>w = P/2 − l</strong></p>'
        '<p><strong>Q6.</strong> ax − bx = 8 → x(a − b) = 8 → <strong>x = 8/(a − b)</strong> — factorise when x appears twice</p>'
        '<p><strong>Q7.</strong> y/4 = x − 3 → <strong>x = y/4 + 3</strong></p>'
        '<p><strong>Q8.</strong> A/(2l) − wh = lw → hmm, divide first: A/2 = lw + wh = w(l + h) → '
        '<strong>w = A/(2(l + h))</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Undo operations in reverse order (last applied, first undone)</li>'
        '<li>Same operation to BOTH sides — the formula stays balanced</li>'
        '<li>Target appears twice → factorise it out: ax + bx = x(a + b)</li>'
        '<li>Powers: root both sides to undo squares (± at Higher)</li>'
        '<li>Brackets: divide the whole side by the factor, or expand first</li>'
        '</ul>'),
    context=CTX('<p>Rearranging: 2–3 marks on every paper — it is the gateway skill for science '
        'formulas, geometry and compound measures. Two-variable targets (Q6 style) mark the '
        'grade-5 boundary.</p>'
        '<p>Links to: solving equations (A17), substitution (A2), compound measures (R1).</p>'),
    worked2=W2("The formula for converting Celsius to Fahrenheit is F = 1.8C + 32. Rearrange to make C the subject, then convert 95°F to Celsius.",
        '<p>Subtract 32: F − 32 = 1.8C &nbsp;→&nbsp; Divide by 1.8: <strong>C = (F − 32)/1.8</strong></p>'
        '<p>95°F: C = (95 − 32)/1.8 = 63/1.8 = <strong>35°C</strong></p>',
        "M1 for the rearrangement, A1 for C = (F − 32)/1.8, A1 for 35°C. "
        "Applied rearrangements (conversion, physics) are the standard exam context."))

B["N9-standard-form.html"] = dict(
    marker="Q6: Write 3.6 × 10⁵ as an ordinary number",
    worked=W_SEC("Standard form: A × 10ⁿ with 1 ≤ A < 10. Big numbers → positive power; small numbers → negative power.",
        EX("Write 240,000 in standard form.",
            '<p>A = 2.4 (between 1 and 10); the decimal moved 5 places → <strong>2.4 × 10⁵</strong></p>',
            "B1 for 2.4 × 10⁵. 24 × 10⁴ is NOT standard form — A must be under 10.") +
        EX("Calculate (2 × 10³) × (3 × 10⁴), giving your answer in standard form.",
            '<p>Multiply the A parts: 2 × 3 = 6. Add the powers: 10³ × 10⁴ = 10⁷</p>'
            '<p><strong>6 × 10⁷</strong></p>',
            "M1 for 6 × 10⁷, A1. If the A-part lands ≥ 10 (e.g. 12 × 10⁷), convert: 1.2 × 10⁸."))
    + '<p><strong>Exam wording to expect:</strong> "Write … in standard form", "as an ordinary number", "giving your answer in standard form".</p>',
    questions=["Q6: Write 3.6 × 10⁵ as an ordinary number", "Q7: Calculate (8 × 10⁻³) ÷ (2 × 10²), giving your answer in standard form."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> Decimal 6 places right → <strong>7.5 × 10⁶</strong></p>'
        '<p><strong>Q2.</strong> 8.2, decimal 5 places LEFT → <strong>8.2 × 10⁻⁵</strong></p>'
        '<p><strong>Q3.</strong> Negative power moves left: <strong>0.047</strong></p>'
        '<p><strong>Q4.</strong> 3 × 4 = 12; 10⁵ × 10⁶ = 10¹¹ → 12 × 10¹¹ = <strong>1.2 × 10¹²</strong></p>'
        '<p><strong>Q5.</strong> 9 ÷ 3 = 3; 10⁸ ÷ 10² = 10⁶ → <strong>3 × 10⁶</strong></p>'
        '<p><strong>Q6.</strong> <strong>360,000</strong></p>'
        '<p><strong>Q7.</strong> 8 ÷ 2 = 4; 10⁻³ ÷ 10² = 10⁻⁵ → <strong>4 × 10⁻⁵</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Standard form: A × 10ⁿ, 1 ≤ A < 10</li>'
        '<li>Positive n = big number; negative n = small number</li>'
        '<li>×: multiply the A parts, ADD the powers · ÷: divide A, SUBTRACT powers</li>'
        '<li>Adding/subtracting in standard form: convert to the SAME power first</li>'
        '<li>Adjust out-of-range A: 45 × 10³ = 4.5 × 10⁴ · 0.3 × 10⁴ = 3 × 10³</li>'
        '</ul>'),
    context=CTX('<p>Standard form: 2–4 marks per paper — conversions (1), arithmetic (2–3). '
        'It carries real-world data (planets, bacteria, populations) in Papers 2/3.</p>'
        '<p>Links to: powers (N6), index laws (N7), estimation (N14).</p>'),
    worked2=W2("Work out (6 × 10⁸) ÷ (1.5 × 10⁻²), giving your answer in standard form.",
        '<p>6 ÷ 1.5 = 4</p>'
        '<p>10⁸ ÷ 10⁻² = 10⁸⁻⁽⁻²⁾ = 10¹⁰ (subtracting a negative power ADDS)</p>'
        '<p><strong>4 × 10¹⁰</strong></p>',
        "M1 for 4, M1 for the power subtraction, A1 for 4 × 10¹⁰. "
        "Dividing BY a negative power is the designed trap — 10⁸ ÷ 10⁻² is not 10⁶."))

B["N8-surds.html"] = dict(
    marker="Q6: Simplify: √50",
    worked=W_SEC("Surds keep answers EXACT. Simplify by finding the largest square factor; multiply under one root; rationalise by multiplying by the conjugate.",
        EX("Simplify √48.",
            '<p>Largest square factor: 48 = 16 × 3</p>'
            '<p>√48 = √16 × √3 = <strong>4√3</strong></p>',
            "M1 for 16 × 3, A1 for 4√3. Choosing 4 × 12 gives 2√12 — right idea, not finished; simplify again.") +
        EX("Rationalise 5/√3.",
            '<p>Multiply top and bottom by √3: 5√3/(√3 × √3) = <strong>5√3/3</strong></p>',
            "M1 for × √3/√3, A1 for 5√3/3. √3 × √3 = 3 clears the root from the denominator."))
    + '<p><strong>Exam wording to expect:</strong> "Simplify", "Give your answer in the form a√b", "rationalise the denominator".</p>',
    questions=["Q6: Simplify: √50", "Q7: Simplify: √27 + √12"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> 75 = 25 × 3 → <strong>5√3</strong></p>'
        '<p><strong>Q2.</strong> 3√2 − 2√2 = <strong>√2</strong> (like surds combine like terms)</p>'
        '<p><strong>Q3.</strong> 2 × 3 = 6 outside; √5 × √10 = √50 = 5√2 → 6 × 5√2 = <strong>30√2</strong></p>'
        '<p><strong>Q4.</strong> 3√5/5</p>'
        '<p><strong>Q5.</strong> Multiply by the conjugate (1 − √3): 2(1 − √3)/(1 − 3) = 2(1 − √3)/(−2) = <strong>√3 − 1</strong></p>'
        '<p><strong>Q6.</strong> 50 = 25 × 2 → <strong>5√2</strong></p>'
        '<p><strong>Q7.</strong> 3√3 + 2√3 = <strong>5√3</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>√(ab) = √a × √b — split off square factors: √72 = 6√2</li>'
        '<li>Only LIKE surds add: 2√5 + 3√5 = 5√5; √2 + √3 stays put</li>'
        '<li>√a × √a = a &nbsp;·&nbsp; √a ÷ √b = √(a/b)</li>'
        '<li>Rationalise single-root: × √b/√b. Bracket denominator: × conjugate (a − √b)/(a − √b)</li>'
        '<li>Square factors to spot: 4, 9, 16, 25, 36, 49, 64, 100</li>'
        '</ul>'),
    context=CTX('<p>Surds are Higher-tier content sitting in this folder — they appear on Higher '
        'Papers 1/2 (non-calculator friendly): 2–3 marks, plus exact trig-value answers (G21).</p>'
        '<p>Links to: exact trig values (G21), Pythagoras (G20), indices (N7).</p>'),
    worked2=W2("Rationalise and simplify: 6/(3 − √3).",
        '<p>Multiply by (3 + √3)/(3 + √3): numerator 6(3 + √3) = 18 + 6√3</p>'
        '<p>Denominator: 3² − (√3)² = 9 − 3 = 6 (difference of two squares)</p>'
        '<p>(18 + 6√3)/6 = <strong>3 + √3</strong></p>',
        "M1 for the conjugate, M1 for 9 − 3 = 6, A1 for 3 + √3. "
        "The difference-of-two-squares denominator is the standard conjugate result — quote it."))

B["R10-direct-inverse-proportion.html"] = dict(
    marker="Q6: y ∝ x². When x = 3, y = 18. Find y when x = 6",
    worked=W_SEC("Proportion questions: (1) write the model, (2) find k from one pair, (3) rewrite the equation, (4) answer. Forwards or backwards — same recipe.",
        EX("y ∝ x. When x = 12, y = 30. Find x when y = 20.",
            '<p>y = kx: 30 = 12k → k = 2.5 → y = 2.5x</p>'
            '<p>20 = 2.5x → <strong>x = 8</strong></p>',
            "M1 for k, A1 for 8. The reverse direction (find x) is just equation solving on the same model.") +
        EX("A recipe for 6 people uses 300 g of rice. How much for 9 people?",
            '<p>Direct proportion: 1 person = 50 g → 9 × 50 = <strong>450 g</strong></p>',
            "M1 for the unitary step, A1 for 450. Recipes, currency and fuel are the standard contexts."))
    + '<p><strong>Exam wording to expect:</strong> "y is proportional to x", "Find an equation for y in terms of x", tables to classify.</p>',
    questions=["Q6: y ∝ x². When x = 3, y = 18. Find y when x = 6.", "Q7: P is inversely proportional to V. When V = 4, P = 30. Find P when V = 8."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> k = 42 ÷ 7 = 6 → y = 6 × 10 = <strong>60</strong></p>'
        '<p><strong>Q2.</strong> k = 6 × 5 = 30 → y = 30/15 = <strong>2</strong></p>'
        '<p><strong>Q3.</strong> Work = 4 × 9 = 36 worker-days → 36 ÷ 6 = <strong>6 days</strong></p>'
        '<p><strong>Q4.</strong> 60 mph × 7 = <strong>420 miles</strong></p>'
        '<p><strong>Q5.</strong> x × y = 24, 24, 24.02 — constant product → <strong>inverse</strong></p>'
        '<p><strong>Q6.</strong> k = y/x² = 18/9 = 2 → y = 2 × 36 = <strong>72</strong></p>'
        '<p><strong>Q7.</strong> k = PV = 120 → P = 120/8 = <strong>15</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Direct: y = kx (product not constant; graph = straight line through origin)</li>'
        '<li>Inverse: y = k/x (product x × y constant; graph = hyperbola)</li>'
        '<li>Direct square: y = kx²; inverse square: y = k/x²</li>'
        '<li>Classify from a table: check y/x, y/x², x × y — the one that stays constant names the model</li>'
        '<li>Always find k BEFORE answering — k is the method mark</li>'
        '</ul>'),
    context=CTX('<p>Proportion: 3–5 marks, Papers 2/3. Tables-for-classification test AO2; '
        'worded problems (workers, recipes, pressure-volume) test modelling.</p>'
        '<p>Links to: multiplicative reasoning (R6), graphs (R8), equations (R13).</p>'))

B["R6-multiplicative-relationships.html"] = dict(
    marker="Q6: A map scale is 1 : 25000. Two towns are 6 cm apart on the map. Find the real distance in km",
    worked=W_SEC("Multiplicative reasoning is ratio thinking with numbers: find the multiplier between two values, then apply it (or its inverse).",
        EX("3 tins cost £2.10. How much do 7 tins cost?",
            '<p>Multiplier 3 → 7: 7/3 &nbsp;·&nbsp; £2.10 × 7/3 = £2.10 ÷ 3 × 7 = <strong>£4.90</strong></p>',
            "M1 for the unitary step, A1 for £4.90. One multiplier (7/3) does the work — ÷3 then ×7 is the same idea.") +
        EX("A map has scale 1 : 50000. How many km does 4 cm represent?",
            '<p>4 × 50000 = 200,000 cm = <strong>2 km</strong></p>',
            "M1 for × 50000, A1 for 2 km (the cm → km conversion is part of the mark)."))
    + '<p><strong>Exam wording to expect:</strong> "How many … for …?", map scales, currency conversions, ingredient scaling.</p>',
    questions=["Q6: A map scale is 1 : 25000. Two towns are 6 cm apart on the map. Find the real distance in km.", "Q7: 5 identical pens cost £3.75. How many pens can you buy with £9?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> Multiplier 30 ÷ 12 = <strong>2.5</strong></p>'
        '<p><strong>Q2.</strong> 25 : 40 = ÷5 → <strong>5 : 8</strong></p>'
        '<p><strong>Q3.</strong> 24 ÷ 4 = 6 m² per litre → 60 ÷ 6 = <strong>10 litres</strong></p>'
        '<p><strong>Q4.</strong> 85 × 1.17 = <strong>£99.45</strong> (99.45 euros)</p>'
        '<p><strong>Q5.</strong> 285 ÷ 15 = <strong>19 teachers</strong></p>'
        '<p><strong>Q6.</strong> 6 × 25000 = 150,000 cm = <strong>1.5 km</strong></p>'
        '<p><strong>Q7.</strong> £3.75 ÷ 5 = £0.75 each → £9 ÷ 0.75 = <strong>12 pens</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Multiplier = new ÷ old — apply the SAME multiplier to every connected quantity</li>'
        '<li>Inverse multiplier: to reverse a ×2.5, use ÷2.5 (or ×2/5)</li>'
        '<li>Map scale 1 : n → real distance = map distance × n</li>'
        '<li>Currency: × the rate one way, ÷ the rate back</li>'
        '<li>Check direction: more items → more money (direct), faster speed → less time (inverse)</li>'
        '</ul>'),
    context=CTX('<p>Multiplicative reasoning underpins best buys, exchange rates, recipes and maps: '
        '3–5 marks per paper. It is the arithmetic engine of the ratio/proportion strand.</p>'
        '<p>Links to: proportion (R7/R10), ratio (R4/R5), percentages (R9).</p>'))

B["A15-gradients-areas-under-graphs.html"] = dict(
    marker="Q6: A velocity-time graph rises in a straight line from 0 to 12 m/s over 6 seconds. Find the distance travelled",
    worked=W_SEC("Graphs encode rates and totals: gradient = rate of change; area under = total accumulated (distance from velocity, work done from force).",
        EX("A velocity-time graph is a straight line from (0, 0) to (20 s, 10 m/s). Find the acceleration and the distance travelled.",
            '<p>Acceleration = gradient = 10/20 = <strong>0.5 m/s²</strong></p>'
            '<p>Distance = area = ½ × 20 × 10 = <strong>100 m</strong></p>',
            "M1 for the gradient, A1 for 0.5; M1 for the triangle area, A1 for 100. Triangular areas: ½ × base × height."))
    + '<p><strong>Exam wording to expect:</strong> "Find the acceleration", "estimate the area under the graph", "What does the gradient represent?".</p>',
    questions=["Q6: A velocity-time graph rises in a straight line from 0 to 12 m/s over 6 seconds. Find the distance travelled.", "Q7: On a curved graph, how do you estimate the gradient at a point?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> Distance-time gradient = <strong>speed</strong></p>'
        '<p><strong>Q2.</strong> Velocity-time gradient = <strong>acceleration</strong></p>'
        '<p><strong>Q3.</strong> Area under velocity-time = <strong>distance travelled</strong></p>'
        '<p><strong>Q4.</strong> 200 ÷ 4 = <strong>50 mph</strong></p>'
        '<p><strong>Q5.</strong> Triangle: ½ × 10 × 30 = <strong>150 m</strong></p>'
        '<p><strong>Q6.</strong> Acceleration = 12/6 = 2 m/s²; distance = ½ × 6 × 12 = <strong>36 m</strong></p>'
        '<p><strong>Q7.</strong> Draw a <strong>tangent</strong> at the point and find its gradient (two grid-friendly points on the tangent)</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Gradient of distance-time = speed; of velocity-time = acceleration</li>'
        '<li>Area under velocity-time = distance; count grid squares for estimates (area of one square × squares)</li>'
        '<li>Straight sections: constant rate; curves: changing rate (tangent for instantaneous)</li>'
        '<li>Area below the x-axis counts as NEGATIVE distance (moving back)</li>'
        '<li>Units of area under: (m/s) × (s) = m</li>'
        '</ul>'),
    context=CTX('<p>Gradients and areas: 3–5 marks on Papers 2/3. Estimating curved areas by '
        'counting trapeziums/squares is the AO3 skill; interpreting gradients in context is AO2.</p>'
        '<p>Links to: instantaneous rates (R15), real-life graphs (A14), compound measures (R1).</p>'))

B["A20-iteration.html"] = dict(
    marker="Q7: Use xₙ₊₁ = (5 − 2xₙ)^(1/2)? — no: use xₙ₊₁ = √(5 − xₙ) with x₁ = 1. Find x₂ and x₃",
    worked=W_SEC("Iteration feeds an answer back into the formula repeatedly. Set the calculator to Ans memory: type x₁, =, then the formula with Ans in place of xₙ, and press = repeatedly.",
        EX("Use xₙ₊₁ = √(xₙ + 6) with x₁ = 1. Find x₂, x₃ and x₄.",
            '<p>x₂ = √(1 + 6) = √7 ≈ 2.6458</p>'
            '<p>x₃ = √(2.6458 + 6) ≈ 2.9404</p>'
            '<p>x₄ = √(2.9404 + 6) ≈ <strong>2.9900</strong> (4 d.p.)</p>',
            "M1 for substituting, A1 for the sequence of values. Keep 4+ decimal places in the working; round only when asked."))
    + '<p><strong>Exam wording to expect:</strong> "Use the iterative formula … with x₁ = … to find x₂ and x₃", "show that the equation has a root between a and b".</p>',
    questions=["Q7: Use xₙ₊₁ = √(5 − xₙ) with x₁ = 1. Find x₂ and x₃", "Q8: Why does xₙ₊₁ = √(5 − xₙ) fail if x₃ were 6?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> x² + 2x − 4 = 0 → x² = 4 − 2x → <strong>x = √(4 − 2x)</strong> for x > 0</p>'
        '<p><strong>Q2.</strong> x₂ = 4/1 − 2 = <strong>2</strong>; x₃ = 4/2 − 2 = <strong>0</strong></p>'
        '<p><strong>Q3.</strong> x₂ = √4 = <strong>2</strong>; x₃ = √4 = <strong>2</strong>; x₄ = <strong>2</strong> — it has converged immediately</p>'
        '<p><strong>Q4.</strong> x₂ = ³√7 ≈ 1.913; x₃ = ³√(6.826) ≈ 1.897; x₄ ≈ 1.894 → <strong>x ≈ 1.89</strong> (2 d.p.)</p>'
        '<p><strong>Q5.</strong> x = 5 − x³ → <strong>xₙ₊₁ = 5 − xₙ³</strong></p>'
        '<p><strong>Q6.</strong> A limit L satisfies L = f(L) — e.g. 1.618 solves <strong>x² = x + 1</strong></p>'
        '<p><strong>Q7.</strong> x₂ = √4 = <strong>2</strong>; x₃ = √3 ≈ <strong>1.732</strong></p>'
        '<p><strong>Q8.</strong> You cannot square-root a negative: 5 − 6 = −1 → √(−1) is not real — the iteration leaves the valid domain</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>xₙ₊₁ = f(xₙ): substitute the PREVIOUS value, keep full decimals until the end</li>'
        '<li>Ans button: x₁ then =, formula with Ans, then = repeatedly</li>'
        '<li>Converge → values settle towards a limit (a root); diverge → values blow up or jump</li>'
        '<li>"To 2 d.p." → iterate until consecutive values agree at 2 d.p.</li>'
        '<li>Rearranging the same equation differently gives different iterations — some converge, some do not</li>'
        '</ul>'),
    context=CTX('<p>Iteration is Higher-tier content in this folder: 3–4 marks on Higher Paper 2/3, '
        'calculator essential. The sign-change/interval version ("show a root lies between a and b") '
        'pairs with it.</p>'
        '<p>Links to: solving quadratics (A18), rearranging (A5), graphs (A11).</p>'))

B["R5-dividing-in-a-ratio.html"] = dict(
    marker="Q6: £360 is shared between three people in the ratio 1 : 2 : 6. Find the largest share",
    worked=W_SEC("Sharing in a ratio: total parts → one part → multiply out. Difference questions: parts difference ↔ amount difference.",
        EX("Share £88 in the ratio 3 : 5.",
            '<p>8 parts → £88 ÷ 8 = £11 per part</p>'
            '<p>3 × 11 = <strong>£33</strong> and 5 × 11 = <strong>£55</strong></p>',
            "M1 for £11 per part, A1 for both amounts. The check (£33 + £55 = £88) is worth writing.") +
        EX("Two lengths are in ratio 4 : 9. The longer is 45 cm. Find the shorter.",
            '<p>9 parts = 45 → 1 part = 5 → 4 × 5 = <strong>20 cm</strong></p>',
            "M1 for 45 ÷ 9, A1 for 20. When ONE share is given (not the total), match that ratio number first."))
    + '<p><strong>Exam wording to expect:</strong> "Share/divide … in the ratio …", "The smaller share is …", "Their difference is …".</p>',
    questions=["Q6: £360 is shared between three people in the ratio 1 : 2 : 6. Find the largest share.", "Q7: Two amounts are in ratio 5 : 8. Their total is £78. Find the difference between them."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> 9 parts → £10 each → <strong>£20 and £70</strong></p>'
        '<p><strong>Q2.</strong> 10 parts → 21 g each → <strong>42 g, 63 g, 105 g</strong></p>'
        '<p><strong>Q3.</strong> 3 parts = £75 → 1 part = £25 → 7 parts = £175 → <strong>total £175</strong></p>'
        '<p><strong>Q4.</strong> Difference 4 parts = 24 → 1 part = 6 → <strong>42 and 66</strong></p>'
        '<p><strong>Q5.</strong> 8 parts = 120 → 15 each → sheep = 5 × 15 = <strong>75</strong></p>'
        '<p><strong>Q6.</strong> 9 parts → £40 each → largest = 6 × 40 = <strong>£240</strong></p>'
        '<p><strong>Q7.</strong> 13 parts = £78 → £6 each → difference = 3 parts = <strong>£18</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Sharing: total ÷ total parts = one part; multiply by each ratio number</li>'
        '<li>Given ONE share: divide by ITS ratio number to get one part</li>'
        '<li>Given the DIFFERENCE: difference of ratio numbers ↔ amount difference</li>'
        '<li>Total = sum of all shares — always check it adds back</li>'
        '<li>Ratio 1 : 2 : 6 — the numbers are PARTS, not amounts</li>'
        '</ul>'),
    context=CTX('<p>Ratio division: 3–5 marks on every paper — money shares, ingredients, teams. '
        'The one-share and difference versions are the AO2 twists.</p>'
        '<p>Links to: simplifying ratio (R4), fractions of amounts (R3), proportion (R7).</p>'))

B["R16-growth-decay.html"] = dict(
    corrections=[("£7109.62 (5000 × 1.045⁸)", "£7110.50 (5000 × 1.045⁸)")],
    marker="Q6: A car worth £15,000 depreciates by 15% per year. Find its value after 4 years",
    worked=W_SEC("Growth and decay = repeated percentage change: final = initial × multiplierⁿ. Appreciation ×(1 + r), depreciation ×(1 − r).",
        EX("A £800 investment grows at 6% per year for 3 years. Find the final value.",
            '<p>Multiplier 1.06 → 800 × 1.06³ = 800 × 1.191016 = <strong>£952.81</strong> (2 d.p.)</p>',
            "M1 for 1.06³, A1 for £952.81. Keep the power form until the end: 800 × 1.06 × 1.06 × 1.06.") +
        EX("A population of 40,000 shrinks by 7% each year. Find the population after 5 years.",
            '<p>Multiplier 0.93 → 40,000 × 0.93⁵ = 40,000 × 0.6956884 = <strong>27,828</strong> (nearest whole)</p>',
            "M1 for 0.93⁵, A1 for 27,828. Populations round to whole people — say 'approximately'."))
    + '<p><strong>Exam wording to expect:</strong> "compound interest", "depreciates by …%", "grows at …% per year".</p>',
    questions=["Q6: A car worth £15,000 depreciates by 15% per year. Find its value after 4 years.", "Q7: An investment doubles in 9 years. What single yearly multiplier achieves this (2 d.p.)?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> 5000 × 1.045⁸ = 5000 × 1.422101 = <strong>£7110.50</strong></p>'
        '<p><strong>Q2.</strong> 1200 × 0.8³ = 1200 × 0.512 = <strong>£614.40</strong></p>'
        '<p><strong>Q3.</strong> 3646.52/3000 = 1.215507 = 1.05⁴ → <strong>4 years</strong></p>'
        '<p><strong>Q4.</strong> 2000 × 1.03¹⁰ = 2000 × 1.343916 = <strong>2688</strong> (nearest whole)</p>'
        '<p><strong>Q5.</strong> 20 ÷ 5 = 4 halvings → 64 × (½)⁴ = 64/16 = <strong>4 g</strong></p>'
        '<p><strong>Q6.</strong> 15,000 × 0.85⁴ = 15,000 × 0.52200625 = <strong>£7830.09</strong></p>'
        '<p><strong>Q7.</strong> m⁹ = 2 → m = 2^(1/9) ≈ <strong>1.08</strong> — about 8% growth per year</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Final = initial × multiplierⁿ (n = periods)</li>'
        '<li>Growth: ×(1 + r/100) · Decay: ×(1 − r/100) — e.g. 4.5% → 1.045; 12% → 0.88</li>'
        '<li>Half-life: divide by 2 each period — n halvings → ×(½)ⁿ</li>'
        '<li>Finding time: trial-and-improve with the multiplier, or spot the power</li>'
        '<li>Money: 2 d.p.; populations/quantities: sensible rounding stated</li>'
        '</ul>'),
    context=CTX('<p>Growth/decay: 3–5 marks on Papers 2/3 — savings, car values, populations, '
        'radioactivity. The find-the-rate-or-time reverse is the top-difficulty version.</p>'
        '<p>Links to: percentages (R9), types of sequences (A24), standard form (N9).</p>'))

if __name__ == "__main__":
    run(B)
    run2(B)
