#!/usr/bin/env python3
"""Batch 2g: A9, N3, G13, G12, G5, A25, R15, G9, G23 (G22 correction lives in 2h)."""
from content_waves import W_SEC, EX, SOL_HEAD, KF, CTX, W2, run, run2

B = {}

B["A9-straight-line-graphs.html"] = dict(
    marker="Q7: Plot the line y = ½x + 1 for x from −2 to 4",
    worked=W_SEC("Straight lines from equations: build a table, plot, draw with a ruler. Gradient-intercept reading works both ways.",
        EX("Draw the line y = 2x − 1 by completing a table for x = −1, 0, 1, 2.",
            '<p>y: −3, −1, 1, 3 — plot and join with a ruler.</p>'
            '<p>Sanity checks: crosses y-axis at (0, −1); rises 2 for every 1 right.</p>',
            "M1 for the table, A1 for the line. The y-intercept check catches most table errors before plotting.") +
        EX("Find the equation of the line through (0, 4) and (2, 10).",
            '<p>Gradient = (10 − 4)/2 = 3; intercept (0, 4) → <strong>y = 3x + 4</strong></p>',
            "M1 for the gradient, A1 for the equation. When one point is on the y-axis, c is just its y-value."))
    + '<p><strong>Exam wording to expect:</strong> "complete the table and draw the graph", "find the equation of the straight line".</p>',
    questions=["Q7: Plot the line y = ½x + 1 for x = −2, 0, 2, 4", "Q8: Which of these lines is steepest: y = x, y = 3 − x, y = ½x + 4?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> Gradient <strong>4</strong>, y-intercept <strong>−3</strong></p>'
        '<p><strong>Q2.</strong> (10 − 1)/(5 − 2) = <strong>3</strong></p>'
        '<p><strong>Q3.</strong> <strong>y = −2x + 5</strong></p>'
        '<p><strong>Q4.</strong> Gradient (11 − 3)/2 = 4, c = 3 → <strong>y = 4x + 3</strong></p>'
        '<p><strong>Q5.</strong> Parallel → same gradient 5, through (0, 1) → <strong>y = 5x + 1</strong></p>'
        '<p><strong>Q6.</strong> −1/3 → <strong>−⅓</strong></p>'
        '<p><strong>Q7.</strong> Points: (−2, 0), (0, 1), (2, 2), (4, 3) — gentle gradient ½ through (0, 1)</p>'
        '<p><strong>Q8.</strong> <strong>y = x and y = 3 − x tie</strong> (|m| = 1 each); y = ½x + 4 is the shallowest</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>y = mx + c — gradient m, y-intercept c</li>'
        '<li>Table method: pick easy x (including 0), substitute, plot, rule through</li>'
        '<li>Gradient: rise ÷ run between two grid-friendly points</li>'
        '<li>Special lines: y = 3 horizontal · x = −2 vertical · y = x diagonal (45°)</li>'
        '<li>Steepness = |m|; negative m slopes down left-to-right</li>'
        '</ul>'),
    context=CTX('<p>Straight-line graphs: 4–6 marks per paper — tables, plotting, reading. '
        'Plotting accuracy is marked (± half a square), so use a sharp pencil and ruler.</p>'
        '<p>Links to: gradients/intercepts (A10), real graphs (A14), coordinate geometry (G11).</p>'))

B["N3-order-of-operations.html"] = dict(
    marker="Q6: Calculate: 20 − 3 × 4 + 6 ÷ 2",
    worked=W_SEC("BIDMAS: Brackets, Indices, Division/Multiplication (left to right), Addition/Subtraction (left to right). Equal-priority operations run LEFT to RIGHT.",
        EX("Calculate: 12 ÷ 4 × 3",
            '<p>Left to right: 12 ÷ 4 = 3, then 3 × 3 = <strong>9</strong> — NOT 12 ÷ 12 = 1</p>',
            "B1 for 9. The ÷-then-× order trap is examined precisely here — same priority, so left first.") +
        EX("Insert brackets to make 3 + 4 × 2 = 14 true.",
            '<p>(3 + 4) × 2 = <strong>14</strong> ✓</p>',
            "B1. Bracket questions test whether you understand WHICH operation BIDMAS prioritises."))
    + '<p><strong>Exam wording to expect:</strong> "Work out the value of …" (BIDMAS silently assumed), "insert brackets".</p>',
    questions=["Q6: Calculate: 20 − 3 × 4 + 6 ÷ 2", "Q7: Calculate: (2 + 3)² − 4 × (6 ÷ 3)"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> × before +: 8 + 12 = <strong>20</strong></p>'
        '<p><strong>Q2.</strong> Brackets first: 9 ÷ 3 = <strong>3</strong></p>'
        '<p><strong>Q3.</strong> Powers first: 8 + 16 − 10 = <strong>14</strong></p>'
        '<p><strong>Q4.</strong> Left to right: 50 ÷ 5 = 10, × 2 = 20, + 3 = <strong>23</strong></p>'
        '<p><strong>Q5.</strong> Brackets: 5 × 16 = <strong>80</strong></p>'
        '<p><strong>Q6.</strong> 20 − 12 + 3 = <strong>11</strong> — the − 3×4 binds first, then ÷ before final +</p>'
        '<p><strong>Q7.</strong> 25 − 4 × 2 = 25 − 8 = <strong>17</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Order: Brackets → Indices → Divide/Multiply (left→right) → Add/Subtract (left→right)</li>'
        '<li>Same priority → work left to right (12 ÷ 4 × 3 = 9)</li>'
        '<li>A minus sign applies to the WHOLE product after it: 10 − 2 × 3 = 4</li>'
        '<li>Fraction bars act as brackets: (a + b)/c does the top first</li>'
        '<li>Check calculator usage: type expressions exactly, or use bracket keys</li>'
        '</ul>'),
    context=CTX('<p>BIDMAS: 1–3 marks on Paper 1, and silently inside every multi-step question. '
        'Left-to-right equal priority is the examined subtlety.</p>'
        '<p>Links to: four operations (N2), substitution (A2), negative numbers (N2).</p>'))

B["G13-plans-elevations.html"] = dict(
    marker="Q6: Draw the plan view of a cylinder lying on its curved side (describe it)",
    worked=W_SEC("Plans and elevations: plan = from above; front elevation = from the front; side elevation = from the side. Views are 2-D projections, so depth is lost.",
        EX("A solid has: plan = square, front elevation = square, side elevation = square. What could it be?",
            '<p>A <strong>cube</strong> (all three views square). A square-based pyramid viewed from directly '
            'above also gives a square plan — but its elevations would be triangles, so cube it is.</p>',
            "B1 for cube with reasoning. Matching ALL THREE views identifies the solid — one view is never enough.") +
        EX("A cylinder stands upright. Describe its three views.",
            '<p>Plan: <strong>circle</strong>. Front elevation: <strong>rectangle</strong>. Side elevation: <strong>rectangle</strong>.</p>',
            "B1 for all three. Upright vs lying-down cylinders swap which views are circles."))
    + '<p><strong>Exam wording to expect:</strong> "Draw the plan/front/side elevation", "circle the correct view", on square grids.</p>',
    questions=["Q6: Draw the plan view of a cylinder lying on its curved side (describe it)", "Q7: A solid's front and side elevations are triangles, plan is a square. Name it."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> The <strong>view from directly above</strong> (bird\u2019s-eye)</p>'
        '<p><strong>Q2.</strong> A <strong>5 × 3 rectangle</strong></p>'
        '<p><strong>Q3.</strong> A <strong>cylinder on its side</strong> — circular ends, rectangular body</p>'
        '<p><strong>Q4.</strong> A <strong>rectangle</strong> (the prism\u2019s side faces project as rectangles)</p>'
        '<p><strong>Q5.</strong> <strong>Triangular prism (lying down) or a pyramid</strong> — any solid with a triangular horizontal cross-section</p>'
        '<p><strong>Q6.</strong> Plan: <strong>rectangle</strong> (the curved surface from above); the circular ends appear only in the end elevation</p>'
        '<p><strong>Q7.</strong> A <strong>square-based pyramid</strong> (viewed from above: square; from the sides: triangles)</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Plan: view from ABOVE · Front elevation: from the FRONT · Side: from the SIDE</li>'
        '<li>Views are flat 2-D shapes — show edges/outline, no perspective</li>'
        '<li>Cuboid: three views are rectangles (possibly different sizes)</li>'
        '<li>Cylinder upright: plan circle, elevations rectangles</li>'
        '<li>Hidden edges are not drawn at GCSE — only visible outlines</li>'
        '</ul>'),
    context=CTX('<p>Plans and elevations: 2–4 marks on Paper 1/2, drawn on grids. Accuracy to the '
        'grid line matters; the identifying-from-views version is the AO2 layer.</p>'
        '<p>Links to: 3D shapes (G12), isometric drawing, area (G16).</p>'))

B["G12-3d-shapes.html"] = dict(
    marker="Q6: Verify Euler's formula for a square-based pyramid",
    worked=W_SEC("3-D shape properties: count faces (flat surfaces), edges, vertices (corners). Euler: F + V − E = 2 for polyhedra.",
        EX("Complete the table for a triangular prism: faces, edges, vertices.",
            '<p>Faces <strong>5</strong> (2 triangles + 3 rectangles), edges <strong>9</strong>, vertices <strong>6</strong></p>',
            "B1 each. Check with Euler: 5 + 6 − 9 = 2 ✓ — the formula double-checks your counting.") +
        EX("Which 3-D shapes have NO vertices?",
            '<p><strong>Sphere</strong> (no faces/edges/vertices) and <strong>cylinder</strong> (no vertices, though it has faces/edges of a curved kind)</p>',
            "B1 for sphere. Cylinders and cones are the boundary cases — cylinders have no vertices; cones have one apex (argued as a vertex)."))
    + '<p><strong>Exam wording to expect:</strong> "How many faces/edges/vertices…", "name the solid", "verify Euler\u2019s formula".</p>',
    questions=["Q6: Verify Euler's formula for a square-based pyramid", "Q7: Which shape has 2 circular faces and 1 curved surface?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> <strong>5 faces</strong> (2 triangles + 3 rectangles)</p>'
        '<p><strong>Q2.</strong> <strong>Sphere</strong> (or cylinder — no corners)</p>'
        '<p><strong>Q3.</strong> <strong>8 edges</strong> (4 base + 4 to the apex)</p>'
        '<p><strong>Q4.</strong> <strong>Cuboid</strong> (rectangular prism)</p>'
        '<p><strong>Q5.</strong> F = 4, V = 4, E = 6 → 4 + 4 − 6 = <strong>2 ✓</strong></p>'
        '<p><strong>Q6.</strong> F = 5, V = 5, E = 8 → 5 + 5 − 8 = <strong>2 ✓</strong></p>'
        '<p><strong>Q7.</strong> A <strong>cylinder</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Cube/cuboid: 6, 12, 8 · Triangular prism: 5, 9, 6 · Square pyramid: 5, 8, 5</li>'
        '<li>Tetrahedron: 4, 6, 4 · Octahedron: 8, 12, 6</li>'
        '<li>Euler\u2019s formula: F + V − E = 2</li>'
        '<li>Prisms: two identical polygon ends + rectangles · Pyramids: one polygon base + triangles to an apex</li>'
        '<li>Curved solids (sphere, cylinder, cone) sit outside Euler\u2019s rule</li>'
        '</ul>'),
    context=CTX('<p>3-D properties: 1–3 marks on Paper 1. Counting errors are common on hidden '
        'edges (pyramid base edges) — Euler\u2019s check catches them.</p>'
        '<p>Links to: plans/elevations (G13), volume (G16), nets.</p>'))

B["G5-congruence-criteria.html"] = dict(
    marker="Q6: Triangles PQR and XYZ: PQ = XY = 7 cm, QR = YZ = 9 cm, angle PQR = angle XYZ = 50°. Are they congruent? Which criterion?",
    worked=W_SEC("Congruence = identical shape AND size. Four criteria: SSS, SAS, ASA (or AAS), RHS. AAA and SSA are NOT criteria.",
        EX("Two triangles share: AB = DE = 6 cm, BC = EF = 8 cm, AC = DF = 10 cm. Congruent?",
            '<p><strong>Yes — SSS</strong> (all three pairs equal)</p>',
            "B1 with criterion named. Naming the criterion IS the marks — a bare 'yes' does not score.") +
        EX("Why do two triangles with angles 30°, 60°, 90° but sides 3-4-5 and 6-8-10 fail congruence?",
            '<p>All angles match (AAA) but the sizes differ — they are <strong>similar, not congruent</strong>.</p>',
            "B1 for the similarity distinction. AAA fixes shape but not scale — the classic distractor."))
    + '<p><strong>Exam wording to expect:</strong> "prove/explain whether the triangles are congruent", name the criterion in every proof.</p>',
    questions=["Q6: Triangles PQR and XYZ: PQ = XY = 7 cm, QR = YZ = 9 cm, angle PQR = angle XYZ = 50°. Are they congruent? Which criterion?", "Q7: Two right-angled triangles have hypotenuse 13 and one leg 5 (each). Congruent? Criterion?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> <strong>Side-Side-Side</strong></p>'
        '<p><strong>Q2.</strong> <strong>SAS</strong> — two sides and the angle BETWEEN them</p>'
        '<p><strong>Q3.</strong> AAA gives <strong>similar</strong> triangles (same shape, any size)</p>'
        '<p><strong>Q4.</strong> <strong>Hypotenuse</strong></p>'
        '<p><strong>Q5.</strong> <strong>Yes — RHS</strong> (right angle, hypotenuse, side)</p>'
        '<p><strong>Q6.</strong> <strong>Yes — SAS</strong>: two pairs of equal sides with the included angle equal</p>'
        '<p><strong>Q7.</strong> <strong>Yes — RHS</strong> (13, 5, and the right angle)</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>SSS: three pairs of sides · SAS: two sides + INCLUDED angle</li>'
        '<li>ASA/AAS: one side + two angles · RHS: right angle + hypotenuse + side</li>'
        '<li>NOT criteria: AAA (shape only) · SSA (ambiguous — the angle not included)</li>'
        '<li>Congruent ⇒ mirror-image flips are allowed (reflections still congruent)</li>'
        '<li>In proofs: quote the criterion, then conclude corresponding parts equal (CPCTC)</li>'
        '</ul>'),
    context=CTX('<p>Congruence: 2–4 marks on Paper 1. The criterion name is the marks — '
        'the included-angle condition is what separates SAS from the SSA trap.</p>'
        '<p>Links to: geometric proof (G6), similar shapes (G19), Pythagoras (G20).</p>'))

B["A25-nth-term.html"] = dict(
    marker="Q7: Find the nth term of 9, 13, 17, 21, … and use it to find the 40th term",
    worked=W_SEC("Linear nth term: coefficient = common difference; constant = zero-term adjustment. Quadratic: second difference ÷ 2 gives the n² coefficient.",
        EX("Find the nth term of 7, 10, 13, 16, …",
            '<p>Difference 3 → 3n; compare with 3n (3, 6, 9, 12): need +4 → <strong>3n + 4</strong></p>',
            "M1 for 3n, A1 for 3n + 4. The compare-with-3n method avoids sign slips on descending sequences.") +
        EX("Find the nth term of 11, 8, 5, 2, …",
            '<p>Difference −3 → −3n; compare with −3n (−3, −6, −9…): need +14 → <strong>−3n + 14</strong></p>',
            "M1 for −3n, A1 for −3n + 14. Descending sequences: negative coefficient, positive constant."))
    + '<p><strong>Exam wording to expect:</strong> "find an expression for the nth term", "use your nth term to find…", quadratic versions at Higher.</p>',
    questions=["Q7: Find the nth term of 9, 13, 17, 21, … and the 40th term", "Q8: Which term of 6n − 3 is the first above 100?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> Difference 4 → 4n + 2 (check: n=1 → 6? No: 4 + 2 = 6 ≠ 6? terms are 6,10,14 — '
        'given sequence starts 6: <strong>4n + 2 ✓</strong>)</p>'
        '<p><strong>Q2.</strong> Difference −4 → <strong>−4n + 54</strong></p>'
        '<p><strong>Q3.</strong> 7 × 100 − 3 = <strong>697</strong></p>'
        '<p><strong>Q4.</strong> 5n + 10 = 80 → n = 14 → <strong>yes, the 14th term</strong></p>'
        '<p><strong>Q5.</strong> Differences 3, 5, 7 → second difference 2 → <strong>n² + 1</strong></p>'
        '<p><strong>Q6.</strong> Differences 5, 7, 9 → second difference 2 → n² + 2n + 3?? check n=1: 6 ✓ (1+2+3=6) → <strong>n² + 2n + 3</strong></p>'
        '<p><strong>Q7.</strong> Difference 4 → <strong>4n + 5</strong>; 40th = <strong>165</strong></p>'
        '<p><strong>Q8.</strong> 6n − 3 > 100 → n > 17.2 → <strong>18th term</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Linear: an + b — a = common difference, b = term₀ (first term − a)</li>'
        '<li>Compare method: write an, line it under the sequence, the gap is b</li>'
        '<li>Quadratic: coefficient of n² = half the second difference; finish by matching</li>'
        '<li>"Is k a term?" — solve an + b = k; whole-number n required</li>'
        '<li>Check with n = 1 AND n = 2 before trusting the formula</li>'
        '</ul>'),
    context=CTX('<p>Nth term: 3–5 marks — finding it, using it, solving back. Quadratic nth terms '
        'are the Higher-boundary discriminator in this folder.</p>'
        '<p>Links to: generating sequences (A23), types (A24), solving equations (A17).</p>'))

B["R15-instantaneous-rate-change.html"] = dict(
    marker="Q6: A distance-time curve has a tangent at t = 4 s passing through (2, 6) and (7, 26). Find the instantaneous speed",
    worked=W_SEC("Instantaneous rate = gradient of the TANGENT at that point. Draw the tangent as long as the grid allows, then rise ÷ run on two clean grid points.",
        EX("A tangent to a distance-time graph at t = 3 s passes through (1, 10) and (5, 50). Find the speed at t = 3.",
            '<p>Gradient = (50 − 10)/(5 − 1) = 40/4 = <strong>10 m/s</strong></p>',
            "M1 for the gradient, A1 for 10. Use points ON THE TANGENT (not the curve) — any two of them give the same gradient.") +
        EX("On a cooling curve, the tangent at t = 2 min has gradient −8 °C/min. Interpret.",
            '<p>The liquid is cooling at <strong>8 degrees per minute</strong> at that moment — the '
            'instantaneous (not average) rate.</p>',
            "M1 for the magnitude with units, A1 for 'at that moment'. Negative gradient = decreasing temperature."))
    + '<p><strong>Exam wording to expect:</strong> "draw a tangent at t = … and find its gradient", "estimate the speed at …".</p>',
    questions=["Q6: A distance-time curve has a tangent at t = 4 s passing through (2, 6) and (7, 26). Find the instantaneous speed", "Q7: Why does the tangent method give a different answer from the chord between two distant points?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> (20 − 4)/(6 − 2) = 16/4 = <strong>4</strong></p>'
        '<p><strong>Q2.</strong> <strong>8 m/s</strong> — the tangent gradient IS the instantaneous speed</p>'
        '<p><strong>Q3.</strong> (9 − 1)/(2 − 0) = <strong>4</strong></p>'
        '<p><strong>Q4.</strong> y(3.9) = 15.21, y(4.1) = 16.81 → (16.81 − 15.21)/0.2 = <strong>8</strong></p>'
        '<p><strong>Q5.</strong> <strong>Deceleration of 2 m/s²</strong> at t = 3 s</p>'
        '<p><strong>Q6.</strong> (26 − 6)/(7 − 2) = 20/5 = <strong>4 m/s</strong></p>'
        '<p><strong>Q7.</strong> A chord measures the AVERAGE rate over the interval; the tangent '
        'measures the rate AT one instant — they differ whenever the rate is changing</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Instantaneous rate = tangent gradient at the point</li>'
        '<li>Average rate = chord gradient (rise ÷ run between two curve points)</li>'
        '<li>Draw tangents LONG — long tangents reduce reading error</li>'
        '<li>Small-interval trick: f(x + h) − f(x − h) over 2h approximates the tangent</li>'
        '<li>Units: distance-time tangent → speed at that instant</li>'
        '</ul>'),
    context=CTX('<p>Instantaneous rates: Higher-boundary content in this folder — 3–4 marks on '
        'Higher Papers 2/3. The tangent-drawing is marked for touching the curve at the point only.</p>'
        '<p>Links to: gradients/areas (A15), rates from graphs (R14), real-life graphs (A14).</p>'))

B["G9-circle-parts.html"] = dict(
    marker="Q6: A chord of length 16 cm sits in a circle of radius 10 cm. Find the distance from centre to chord",
    worked=W_SEC("Circle vocabulary: radius, diameter, chord, tangent, arc, sector, segment. The tangent-radius right angle and the chord-perpendicular-bisector property do the geometric work.",
        EX("A circle has radius 5 cm. A chord is 8 cm long. Find the distance from the centre to the chord.",
            '<p>Half-chord = 4. Pythagoras: d = √(5² − 4²) = √9 = <strong>3 cm</strong></p>',
            "M1 for the right-angled triangle (half-chord), A1 for 3. The perpendicular from the centre ALWAYS bisects the chord.") +
        EX("Name the part: the region between a chord and an arc.",
            '<p>A <strong>segment</strong> (vs a sector, bounded by two radii and an arc)</p>',
            "B1. Segment/sector confusion is the vocabulary trap — sector = 'pizza slice'."))
    + '<p><strong>Exam wording to expect:</strong> "name the part shown", "calculate the distance from the centre to the chord".</p>',
    questions=["Q6: A chord of length 16 cm sits in a circle of radius 10 cm. Find the distance from centre to chord", "Q7: Two tangents from an external point P touch the circle at A and B. If PA = 7 cm, find PB."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> 18 ÷ 2 = <strong>9 cm</strong></p>'
        '<p><strong>Q2.</strong> A <strong>tangent</strong></p>'
        '<p><strong>Q3.</strong> Sector: two radii + arc (<strong>pizza slice</strong>); segment: chord + arc</p>'
        '<p><strong>Q4.</strong> <strong>90°</strong> — tangent ⊥ radius at the contact point</p>'
        '<p><strong>Q5.</strong> Half-chord 12: d = √(13² − 12²) = √25 = <strong>5 cm</strong></p>'
        '<p><strong>Q6.</strong> Half-chord 8: √(100 − 64) = √36 = <strong>6 cm</strong></p>'
        '<p><strong>Q7.</strong> <strong>7 cm</strong> — tangents from an external point are equal</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Radius = diameter ÷ 2 · tangent touches at exactly one point</li>'
        '<li>Tangent ⊥ radius at the point of contact</li>'
        '<li>Perpendicular from centre bisects any chord (and bisects its arc)</li>'
        '<li>Chord problems: right triangle with hypotenuse r, legs = half-chord and distance</li>'
        '<li>Tangents from the same external point are equal in length</li>'
        '</ul>'),
    context=CTX('<p>Circle parts: 1–2 marks vocabulary + 3–4 marks chord calculations. '
        'The half-chord Pythagoras set-up is the examined geometry.</p>'
        '<p>Links to: Pythagoras (G20), circle theorems (G10), arcs/sectors (G18).</p>'))

B["G23-area-triangle-formula.html"] = dict(
    corrections=[("½ × 5 × 9 × sin 40° = 14.4 cm²", "½ × 5 × 9 × sin 40° = 14.5 cm²")],
    marker="Q6: Find the area of a triangle with sides 8 cm and 10 cm, included angle 50°",
    worked=W_SEC("When the included angle is known: Area = ½ab sin C. No height needed — the sine does the vertical work.",
        EX("Find the area of a triangle with sides 6 cm and 7 cm, included angle 90°.",
            '<p>½ × 6 × 7 × sin 90° = ½ × 42 × 1 = <strong>21 cm²</strong></p>',
            "M1 for the formula, A1 for 21. sin 90° = 1 recovers the ordinary ½bh — a good self-check.") +
        EX("A triangle has area 30 cm² with two sides 10 cm and 8 cm. Find the included angle.",
            '<p>30 = ½ × 10 × 8 × sin C = 40 sin C → sin C = 0.75 → C = <strong>48.6°</strong> (1 d.p.)</p>',
            "M1 for the rearrangement, A1 for 48.6. Reverse questions: divide by ½ab first, then inverse-sine."))
    + '<p><strong>Exam wording to expect:</strong> "included angle" signals this formula; Higher-tier topic in this folder.</p>',
    questions=["Q6: Find the area of a triangle with sides 8 cm and 10 cm, included angle 50°", "Q7: Two triangles have sides 6, 8 with included angles 30° and 150°. Compare their areas."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> ½ × 5 × 9 × sin 40° = 22.5 × 0.643 = <strong>14.5 cm²</strong> (3 s.f.)</p>'
        '<p><strong>Q2.</strong> ½ × 12 × 12 × sin 30° = 72 × 0.5 = <strong>36 cm²</strong></p>'
        '<p><strong>Q3.</strong> sin C = 40/60 = 2/3 → C = <strong>41.8°</strong> (1 d.p.)</p>'
        '<p><strong>Q4.</strong> ½ × 7 × 11 × sin 120° = 38.5 × 0.866 = <strong>33.3 cm²</strong></p>'
        '<p><strong>Q5.</strong> 50 = ½ × 15 × b × sin 45° → b = 100/(15 × 0.7071) = <strong>9.43 cm</strong></p>'
        '<p><strong>Q6.</strong> ½ × 8 × 10 × sin 50° = 40 × 0.766 = <strong>30.6 cm²</strong> (3 s.f.)</p>'
        '<p><strong>Q7.</strong> sin 30° = sin 150° = 0.5 → <strong>equal areas</strong> (supplementary angles share sine)</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Area = ½ab sin C — a and b must flank the INCLUDED angle C</li>'
        '<li>sin 90° = 1 recovers ½bh (right-angled case)</li>'
        '<li>Supplementary angles have equal sines → two possible triangles (ambiguous case)</li>'
        '<li>Reverse: sin C = 2 × Area ÷ (ab)</li>'
        '<li>Exact values pair with this: sin 30° = ½, sin 45° = √2/2, sin 60° = √3/2</li>'
        '</ul>'),
    context=CTX('<p>½ab sin C: Higher-tier content in this folder — 2–4 marks on Higher papers, '
        'usually paired with the cosine rule in multi-step triangle problems.</p>'
        '<p>Links to: sine/cosine rules (G22), exact trig values (G21), Pythagoras (G20).</p>'))

if __name__ == "__main__":
    run(B)
    run2(B)
