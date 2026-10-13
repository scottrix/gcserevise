#!/usr/bin/env python3
"""Batch 2h: G22 (2 corrections), P4, P8, G20, G8, G15, P6, G10, S3, S1."""
from content_waves import W_SEC, EX, SOL_HEAD, KF, CTX, W2, run, run2

B = {}

B["G22-sine-cosine-rules.html"] = dict(
    corrections=[("cos R = (9² + 7² - 11²)/(2 × 9 × 7) = -7/126, R = 93.2°", "cos R = (81 + 49 - 121)/(2 × 9 × 7) = 9/126 = 0.0714, R = 85.9°"),
                 ("f² = 10² + 14² - 2 × 10 × 14 × cos 45° = 104.3, f = 10.2 cm", "f² = 100 + 196 - 280 × 0.7071 = 98.0, f = 9.90 cm")],
    marker="Q6: In triangle ABC: AB = 11 cm, BC = 13 cm, angle ABC = 74°. Find AC",
    worked=W_SEC("Sine rule (pairs of angle-side opposites) or cosine rule (two sides + included angle, or all three sides). Choosing is half the marks.",
        EX("Find side a in triangle ABC: angle A = 40°, angle B = 65°, b = 12 cm.",
            '<p>Angle C = 75°. Sine rule: a/sin 40° = 12/sin 65°</p>'
            '<p>a = 12 × sin 40°/sin 65° = 12 × 0.6428/0.9063 = <strong>8.51 cm</strong> (3 s.f.)</p>',
            "M1 for the sine rule set-up (find the third angle first), A1 for 8.51. Pair each side with the angle OPPOSITE it.") +
        EX("Triangle sides 8 cm and 11 cm with included angle 52°. Find the third side.",
            '<p>Cosine rule: c² = 8² + 11² − 2 × 8 × 11 × cos 52° = 64 + 121 − 108.1 = 76.9</p>'
            '<p>c = <strong>8.77 cm</strong> (3 s.f.)</p>',
            "M1 for the cosine rule, A1 for 8.77. Two sides + INCLUDED angle = cosine rule, always."))
    + '<p><strong>Exam wording to expect:</strong> non-right-angled triangles: "calculate the length of …", "calculate the size of angle …" (3 s.f.).</p>',
    questions=["Q6: In triangle ABC: AB = 11 cm, BC = 13 cm, angle ABC = 74°. Find AC", "Q7: In triangle PQR: PQ = 6 cm, PR = 9 cm, angle P = 40°. Find QR (3 s.f.)."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> a = 15 × sin 35°/sin 70° = 15 × 0.5736/0.9397 = <strong>9.15 cm</strong> (the page shows 9.08 — recompute: 15 × 0.5736 = 8.604; ÷ 0.9397 = 9.155 → <strong>9.15 cm</strong>, 3 s.f.)</p>'
        '<p><strong>Q2.</strong> cos R = (81 + 49 − 121)/126 = 9/126 = 0.0714 → R = <strong>85.9°</strong> (1 d.p.)</p>'
        '<p><strong>Q3.</strong> z² = 144 + 64 − 192 × cos 60° = 208 − 96 = 112 → z = <strong>10.6 cm</strong></p>'
        '<p><strong>Q4.</strong> f² = 100 + 196 − 280 × cos 45° = 296 − 197.99 = 98.0 → f = <strong>9.90 cm</strong> (3 s.f.)</p>'
        '<p><strong>Q5.</strong> sin B = 9 × sin 48°/7 = 0.9554 → B = <strong>72.7°</strong> or <strong>107.3°</strong> (ambiguous case — both valid)</p>'
        '<p><strong>Q6.</strong> Cosine rule: AC² = 11² + 13² − 2 × 11 × 13 × cos 74° = 121 + 169 − 286 × 0.2756 = 290 − 78.8 = 211.2 → AC = <strong>14.5 cm</strong> (3 s.f.)</p>'
        '<p><strong>Q7.</strong> QR² = 36 + 81 − 108 × cos 40° = 117 − 82.7 = 34.3 → QR = <strong>5.86 cm</strong> (3 s.f.)</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Sine rule: a/sin A = b/sin B = c/sin C — side with its OPPOSITE angle</li>'
        '<li>Cosine rule (side): c² = a² + b² − 2ab cos C</li>'
        '<li>Cosine rule (angle): cos C = (a² + b² − c²)/(2ab)</li>'
        '<li>Choose: two sides + included angle → cosine · angle-side opposite pairs → sine · three sides → cosine for an angle</li>'
        '<li>Answers to 3 s.f. unless told otherwise; ambiguous sine case gives two angles</li>'
        '</ul>'),
    context=CTX('<p>Non-right triangle trigonometry: Higher-boundary content in this folder — '
        '4–6 marks on Higher papers, often as multi-step journeys (angle then side, or both rules).</p>'
        '<p>Links to: ½ab sin C (G23), Pythagoras (G20), bearings (G15).</p>'))

B["P4-mutually-exclusive.html"] = dict(
    marker="Q6: A card is drawn from a standard deck. Are 'heart' and 'queen' mutually exclusive? Find P(heart or queen)",
    worked=W_SEC("Mutually exclusive events CANNOT both happen → P(A or B) = P(A) + P(B). If they CAN overlap, subtract the overlap: P(A) + P(B) − P(A and B).",
        EX("P(rain) = 0.3 and P(wind) = 0.6; they can occur together with P(both) = 0.15. Find P(rain or wind).",
            '<p>0.3 + 0.6 − 0.15 = <strong>0.75</strong></p>',
            "M1 for adding, M1 for subtracting the overlap, A1 for 0.75. Forgetting the subtraction double-counts the overlap.") +
        EX("A spinner: P(A) = 0.3, P(B) = 0.45. A and B are mutually exclusive. Find P(neither A nor B).",
            '<p>P(A or B) = 0.75 → P(neither) = 1 − 0.75 = <strong>0.25</strong></p>',
            "M1 for the sum, A1 for the complement. 'Neither' = 1 − P(either), building on the exclusive rule."))
    + '<p><strong>Exam wording to expect:</strong> "P(A or B)", "are these mutually exclusive?", Venn-diagram overlaps.</p>',
    questions=["Q6: A card is drawn from a standard deck. Are 'heart' and 'queen' mutually exclusive? Find P(heart or queen)", "Q7: P(A) = 0.5, P(B) = 0.4, P(A and B) = 0.2. Find P(A or B)."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> <strong>No</strong> — the 6 is even, so both can happen together</p>'
        '<p><strong>Q2.</strong> 5/10 + 2/10 = <strong>7/10</strong> (mutually exclusive — one colour each)</p>'
        '<p><strong>Q3.</strong> 0.4 + 0.35 = <strong>0.75</strong></p>'
        '<p><strong>Q4.</strong> 1 − 0.75 = <strong>0.25</strong></p>'
        '<p><strong>Q5.</strong> 40 + 35 − 15 = 60 → <strong>0 like neither</strong></p>'
        '<p><strong>Q6.</strong> <strong>Not exclusive</strong> (the queen of hearts). P = 13/52 + 4/52 − 1/52 = <strong>16/52 = 4/13</strong></p>'
        '<p><strong>Q7.</strong> 0.5 + 0.4 − 0.2 = <strong>0.7</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Mutually exclusive: cannot both happen → P(A or B) = P(A) + P(B)</li>'
        '<li>Overlapping: subtract the intersection P(A and B)</li>'
        '<li>Exhaustive: probabilities sum to 1 → P(neither) = 1 − P(A or B)</li>'
        '<li>Test: can both occur in ONE trial? If yes → overlap exists</li>'
        '<li>Venn diagrams: only the intersection region is counted twice</li>'
        '</ul>'),
    context=CTX('<p>Mutual exclusivity: 2–4 marks on Papers 1/2. The overlapping version '
        '(subtract the intersection) is the discriminator; Venn diagrams carry the reasoning.</p>'
        '<p>Links to: Venn diagrams (P6), probability scale (P3), trees (P8).</p>'))

B["P8-tree-diagrams.html"] = dict(
    marker="Q6: A bag has 5 red and 3 blue balls. Two drawn WITHOUT replacement. P(one of each)?",
    worked=W_SEC("Tree diagrams: branches multiply ALONG the path, results ADD across paths. Without replacement, the second-stage fractions change.",
        EX("A coin is flipped and a die rolled. Tree or space: P(heads and an even number)?",
            '<p>P(H) × P(even) = ½ × ½ = <strong>1/4</strong></p>',
            "M1 for multiplying along the branch, A1 for 1/4. Independent events: the second probability ignores the first.") +
        EX("P(rain Sat) = 0.6, P(rain Sun) = 0.6, independent. Find P(rain on exactly one day).",
            '<p>RS + S̄Su: 0.6 × 0.4 + 0.4 × 0.6 = 0.24 + 0.24 = <strong>0.48</strong></p>',
            "M1 for the two paths, A1 for 0.48. 'Exactly one' = the two mixed paths — add them."))
    + '<p><strong>Exam wording to expect:</strong> "complete the tree diagram", "find the probability that …", with/without replacement pairs.</p>',
    questions=["Q6: A bag has 5 red and 3 blue balls. Two drawn WITHOUT replacement. P(one of each)?", "Q7: A test is 95% reliable: P(positive|has bug) = 0.95, P(negative|no bug) = 0.95. If 10% have the bug, find P(positive result)."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> 0.7 × 0.7 = <strong>0.49</strong></p>'
        '<p><strong>Q2.</strong> 6/10 × 6/10 = <strong>0.36</strong></p>'
        '<p><strong>Q3.</strong> 6/10 × 5/9 = 30/90 = <strong>1/3</strong></p>'
        '<p><strong>Q4.</strong> 0.05 × 0.8 + 0.95 × 0.2 = <strong>0.23</strong> (using the page\u2019s stated prior P(bug) = 0.05)</p>'
        '<p><strong>Q5.</strong> 1 − P(HHH) = 1 − 1/8 = <strong>7/8</strong></p>'
        '<p><strong>Q6.</strong> RB + BR = 5/8 × 3/7 + 3/8 × 5/7 = 15/56 + 15/56 = <strong>15/28</strong></p>'
        '<p><strong>Q7.</strong> 0.1 × 0.95 + 0.9 × 0.05 = 0.095 + 0.045 = <strong>0.14</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Along the path: MULTIPLY · Across paths: ADD</li>'
        '<li>Branch sums at each stage = 1 — the completion check</li>'
        '<li>Without replacement: denominators drop (5/8 then 4/7)</li>'
        '<li>"At least one" → 1 − P(none)</li>'
        '<li>"Exactly one" → add the two mixed paths</li>'
        '</ul>'),
    context=CTX('<p>Tree diagrams: 4–6 marks on Papers 1/2 — the biggest probability marks. '
        'Draw the full tree (both stages, both outcomes) even when only one path is needed.</p>'
        '<p>Links to: possibility spaces (P7), conditional probability (P9), mutual exclusivity (P4).</p>'))

B["G20-pythagoras-trigonometry.html"] = dict(
    marker="Q6: A 5 m ladder leans against a wall, foot 1.5 m from the base. How high up the wall does it reach?",
    worked=W_SEC("Right triangles: Pythagoras (two sides → third), trig ratios (angle + side → side, side + side → angle). SOH-CAH-TOA, label hypotenuse first.",
        EX("A right triangle has hypotenuse 26 cm and one side 10 cm. Find the other side.",
            '<p>x² = 26² − 10² = 676 − 100 = 576 → x = <strong>24 cm</strong></p>',
            "M1 for the subtraction (hypotenuse is ALWAYS the longest — subtract, never add), A1 for 24.") +
        EX("A ramp rises 1.2 m over a horizontal distance of 5 m. Find the angle it makes with the ground (1 d.p.).",
            '<p>tan θ = 1.2/5 = 0.24 → θ = tan⁻¹(0.24) = <strong>13.5°</strong></p>',
            "M1 for tan θ = opposite/adjacent, A1 for 13.5°. Opposite/adjacent pairs → tan; hypotenuse involved → sin or cos."))
    + '<p><strong>Exam wording to expect:</strong> "calculate the length of …", "calculate the size of angle …", 3-D versions at Higher.</p>',
    questions=["Q6: A 5 m ladder leans against a wall, foot 1.5 m from the base. How high up the wall does it reach?", "Q7: A ship sails 15 km on a bearing of 040°. How far north has it travelled (1 d.p.)?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> √(64 + 225) = √289 = <strong>17 cm</strong></p>'
        '<p><strong>Q2.</strong> √(400 − 256) = √144 = <strong>12 cm</strong></p>'
        '<p><strong>Q3.</strong> 12 × sin 35° = <strong>6.88 cm</strong></p>'
        '<p><strong>Q4.</strong> tan θ = 9/12 = 0.75 → θ = tan⁻¹(0.75) = <strong>36.9°</strong></p>'
        '<p><strong>Q5.</strong> √(4 + 36 + 81) = √121 = <strong>11 cm</strong></p>'
        '<p><strong>Q6.</strong> √(25 − 2.25) = √22.75 = <strong>4.77 m</strong> (2 d.p.)</p>'
        '<p><strong>Q7.</strong> North component = 15 × cos 40° = <strong>11.5 km</strong> (1 d.p.)</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>a² + b² = c² — c is the HYPOTENUSE (opposite the right angle)</li>'
        '<li>Missing hypotenuse → ADD squares; missing leg → SUBTRACT squares</li>'
        '<li>SOH CAH TOA: label O (opposite the angle), A (adjacent), H (hypotenuse) first</li>'
        '<li>Two sides → Pythagoras (right) or trig (angle present); angle+side → ratio of choice</li>'
        '<li>3-D: Pythagoras twice — base diagonal first, then space diagonal</li>'
        '</ul>'),
    context=CTX('<p>Pythagoras and trig: 6–10 marks per paper across both — the largest geometry '
        'investment. Bearings, ladders and 3-D boxes are the standard contexts.</p>'
        '<p>Links to: sine/cosine rules (G22), exact values (G21), coordinates (G11).</p>'))

B["G8-combined-transformations.html"] = dict(
    marker="Q6: Point (3, −2) is reflected in the y-axis, then translated by (−1, 4). Final position?",
    worked=W_SEC("Combined transformations apply IN ORDER (left to right as written). Invariant points (rotation centre, mirror-line points) are the quick wins.",
        EX("Reflect (5, 2) in the x-axis, then rotate 90° anticlockwise about the origin.",
            '<p>Reflection: (5, −2). Rotation 90° ACW: (x, y) → (−y, x) → <strong>(2, 5)</strong></p>',
            "M1 for each stage, A1 for (2, 5). Track the single point through both stages — no need to transform the whole shape.") +
        EX("Describe the single transformation equivalent to a reflection in x = 1 followed by a reflection in x = 5.",
            '<p>Two parallel mirror reflections = a <strong>translation by twice the distance between the lines</strong>: '
            '2 × 4 = 8 to the right → <strong>translation by the vector (8, 0)</strong></p>',
            "M1 for recognising the double-reflection property, A1 for the vector. Reflections in parallel lines compose to translations."))
    + '<p><strong>Exam wording to expect:</strong> "perform the combined transformation", "describe the single equivalent transformation".</p>',
    questions=["Q6: Point (3, −2) is reflected in the y-axis, then translated by (−1, 4). Final position?", "Q7: What single transformation equals a 90° rotation followed by a 270° rotation (same centre)?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> Two axis reflections → <strong>180° rotation about the origin</strong></p>'
        '<p><strong>Q2.</strong> The <strong>centre itself: (2, 3)</strong></p>'
        '<p><strong>Q3.</strong> Add the vectors: (3 + (−1), −2 + 5) = <strong>(2, 3)</strong></p>'
        '<p><strong>Q4.</strong> <strong>All points ON the x-axis</strong> (y = 0)</p>'
        '<p><strong>Q5.</strong> 120° + 240° = 360° → <strong>identity (no change)</strong></p>'
        '<p><strong>Q6.</strong> Reflect: (−3, −2); translate: <strong>(−4, 2)</strong></p>'
        '<p><strong>Q7.</strong> 90 + 270 = 360 → <strong>identity</strong> (same centre)</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Order matters: do transformations left to right (track ONE point if unsure)</li>'
        '<li>Two reflections in PARALLEL lines → translation (2 × gap)</li>'
        '<li>Two reflections in INTERSECTING lines → rotation (2 × angle about the intersection)</li>'
        '<li>Invariant points: rotation centre; all points on the mirror line; no invariant points under a non-zero translation</li>'
        '<li>Rotation angle sums ≥ 360° collapse to the remainder (or identity)</li>'
        '</ul>'),
    context=CTX('<p>Combined transformations: Higher-boundary in this folder — 3–5 marks. '
        'Tracking a labelled corner through each stage is the reliable method.</p>'
        '<p>Links to: transformations (G7), graph transformations (A13), coordinates (A8).</p>'))

B["G15-measuring-bearings.html"] = dict(
    marker="Q6: A plane flies 200 km on a bearing of 130°. How far east has it travelled (3 s.f.)?",
    worked=W_SEC("Bearings: clockwise from north, three figures. Distance questions combine bearings with trigonometry — draw the north line at BOTH points.",
        EX("A walker walks 4 km north, then 3 km east. Find the bearing of the finish from the start (1 d.p.).",
            '<p>Triangle: north 4, east 3 → angle from north = tan⁻¹(3/4) = 36.9°</p>'
            '<p>Bearing = <strong>036.9°</strong> (three figures)</p>',
            "M1 for the tangent, A1 for the angle, B1 for three-figure form. The north-point line at the START is the reference."))
    + '<p><strong>Exam wording to expect:</strong> "measure/write the bearing of B from A", "find how far … has travelled north/east".</p>',
    questions=["Q6: A plane flies 200 km on a bearing of 130°. How far east has it travelled (3 s.f.)?", "Q7: The bearing of B from A is 310°. Find the bearing of A from B."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> <strong>000°</strong> (north is the zero direction)</p>'
        '<p><strong>Q2.</strong> <strong>270°</strong></p>'
        '<p><strong>Q3.</strong> 120 + 180 = <strong>300°</strong></p>'
        '<p><strong>Q4.</strong> 315° is 45° west of north → <strong>north-west (NW)</strong></p>'
        '<p><strong>Q5.</strong> 070 + 180 = <strong>250°</strong></p>'
        '<p><strong>Q6.</strong> East = 200 × sin 50° (130° is 50° past east of south... precisely: component east of north = 200 sin 130° = 200 sin 50°) = <strong>153 km</strong> (3 s.f.)</p>'
        '<p><strong>Q7.</strong> 310 − 180 = <strong>130°</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Bearings: measured CLOCKWISE from NORTH, always THREE digits (047°, not 47°)</li>'
        '<li>Back bearing: ±180° (add if < 180, subtract if ≥ 180)</li>'
        '<li>Compass: N 000°, NE 045°, E 090°, SE 135°, S 180°, SW 225°, W 270°, NW 315°</li>'
        '<li>North-line at BOTH points for two-way bearing problems</li>'
        '<li>Components: north = d cos θ, east = d sin θ (θ from north)</li>'
        '</ul>'),
    context=CTX('<p>Bearings: 2–5 marks on Papers 2/3 (protractor + ruler for measuring, calculator '
        'for trig versions). The three-figure convention is itself examined.</p>'
        '<p>Links to: Pythagoras/trig (G20), scale drawings (R2), sine/cosine rules (G22).</p>'))

B["P6-systematic-listing.html"] = dict(
    marker="Q6: A 4-digit PIN cannot start with 0. How many possible PINs?",
    worked=W_SEC("Counting with sets: product rule for stages; Venn diagrams for overlapping groups (add only, subtract the intersection); set notation n(A ∪ B) = n(A) + n(B) − n(A ∩ B).",
        EX("In a class of 30: 18 study Spanish, 15 study French, 6 study both. How many study neither?",
            '<p>Spanish or French: 18 + 15 − 6 = 27 → neither: 30 − 27 = <strong>3</strong></p>',
            "M1 for the union formula, A1 for 3. Draw the Venn: 12 + 6 + 9 in the three regions, 3 outside.") +
        EX("How many ways can 3 different prizes be awarded to 10 people (one each)?",
            '<p>10 × 9 × 8 = <strong>720 ways</strong></p>',
            "M1 for the product, A1 for 720. Prizes are distinct → order matters → descending product."))
    + '<p><strong>Exam wording to expect:</strong> "how many possible …", Venn diagram shading/completion, set notation.</p>',
    questions=["Q6: A 4-digit PIN cannot start with 0. How many possible PINs?", "Q7: Universal set 1–20. A = multiples of 3, B = even numbers. Find n(A ∩ B) and n(A ∪ B)."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> 3 × 4 = <strong>12</strong></p>'
        '<p><strong>Q2.</strong> <strong>AA, AB, BA, BB</strong> — 4 outcomes</p>'
        '<p><strong>Q3.</strong> Only cats 14, only dogs 10, both 8 → neither = 40 − 32 = <strong>8</strong></p>'
        '<p><strong>Q4.</strong> In B but not A — <strong>B minus the overlap</strong> (right crescent)</p>'
        '<p><strong>Q5.</strong> 10⁴ = <strong>10,000</strong></p>'
        '<p><strong>Q6.</strong> 9 × 10 × 10 × 10 = <strong>9000</strong></p>'
        '<p><strong>Q7.</strong> A ∩ B = multiples of 6 ≤ 20: {6, 12, 18} → <strong>3</strong>; '
        'n(A) = 6, n(B) = 10 → union = 6 + 10 − 3 = <strong>13</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Product rule: multiply choices per stage (independent stages)</li>'
        '<li>n(A ∪ B) = n(A) + n(B) − n(A ∩ B) — subtract the overlap once</li>'
        '<li>Venn regions: only ∩ counted twice — fill the INTERSECTION first, then subtract outwards</li>'
        '<li>Set notation: ∪ or · ∩ and · A′ not-A</li>'
        '<li>Restricted digits (no leading zero): multiply the reduced first-stage choice</li>'
        '</ul>'),
    context=CTX('<p>Counting with sets: 3–5 marks on Papers 1/2 — PINs, menus, Venn completions. '
        'The Venn-fill order (centre first) prevents every arithmetic slip.</p>'
        '<p>Links to: listing (N5), mutual exclusivity (P4), probability from sets (P3).</p>'))

B["G10-circle-theorems.html"] = dict(
    marker="Q6: A and B are points on a circle centre O. Angle OAB = 28°. Find angle AOB",
    worked=W_SEC("Eight theorems; the two isosceles facts (radii) unlock most questions. Name each theorem as you use it.",
        EX("Points A, B, C on a circle. Angle ABC = 55°. Find the angle at the centre AOC (subtended by the same arc).",
            '<p>Angle at centre = 2 × angle at circumference = <strong>110°</strong></p>',
            "M1 for the theorem, A1 for 110°. 'Subtended by the same arc' is the condition — check the angle arms touch the same two points.") +
        EX("A cyclic quadrilateral has angles x and (x + 40)° opposite each other. Find both.",
            '<p>x + x + 40 = 180 → x = 70 → <strong>70° and 110°</strong></p>',
            "M1 for the supplementary rule, A1 for both. Opposite angles in cyclic quadrilaterals ALWAYS sum to 180°."))
    + '<p><strong>Exam wording to expect:</strong> "find the angle …, giving reasons" — the reason names the theorem; Higher-tier topic in this folder.</p>',
    questions=["Q6: A and B are points on a circle centre O. Angle OAB = 28°. Find angle AOB", "Q7: T is a tangent at P; angle between T and chord PQ is 54°. Find the angle in the alternate segment."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> 2 × 42 = <strong>84°</strong> (angle at centre theorem)</p>'
        '<p><strong>Q2.</strong> 180 − 85 = <strong>95°</strong> (cyclic quadrilateral)</p>'
        '<p><strong>Q3.</strong> <strong>90°</strong> — angle in a semicircle is always a right angle</p>'
        '<p><strong>Q4.</strong> Tangents from an external point are equal → <strong>15 cm</strong></p>'
        '<p><strong>Q5.</strong> Alternate segment: <strong>62°</strong></p>'
        '<p><strong>Q6.</strong> Triangle OAB is isosceles (OA = OB radii) → angle OBA = 28° → '
        'angle AOB = 180 − 56 = <strong>124°</strong></p>'
        '<p><strong>Q7.</strong> <strong>54°</strong> — alternate segment theorem</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Centre = 2 × circumference (same arc) · semicircle angle = 90°</li>'
        '<li>Same segment: angles equal · cyclic quad: opposite angles sum to 180°</li>'
        '<li>Tangent ⊥ radius · tangents from a point equal · alternate segment theorem</li>'
        '<li>Isosceles triangles formed by two radii — the base-angle workhorse</li>'
        '<li>Every answer needs its theorem NAMED as the reason</li>'
        '</ul>'),
    context=CTX('<p>Circle theorems: Higher-tier content in this folder — 4–6 marks on Higher '
        'Paper 1/2. The reason lines carry as many marks as the numbers.</p>'
        '<p>Links to: circle parts (G9), angle rules (G3), geometric proof (G6).</p>'))

B["S3-grouped-data.html"] = dict(
    marker="Q6: A histogram bar spans 30–50 (width 20) with frequency 36. Find its frequency density",
    worked=W_SEC("Grouped data: frequency density = frequency ÷ class width (histograms); cumulative frequency counts 'up to' values for medians/quartiles.",
        EX("A class runs 10 ≤ w < 20 with frequency 24. Find the frequency density and plot height.",
            '<p>Density = 24 ÷ 10 = <strong>2.4</strong> — the bar\u2019s HEIGHT (not the frequency)</p>',
            "M1 for ÷ width, A1 for 2.4. Histograms plot DENSITY, never frequency — unequal widths make that the whole point.") +
        EX("Cumulative frequencies at 30, 40, 50 are 12, 45, 78 (total 90). Estimate the median.",
            '<p>Median position = 90 ÷ 2 = 45 → the median sits where CF = 45 → <strong>40</strong></p>',
            "M1 for n/2, A1 for 40. Read ACROSS from the CF axis to the curve, then DOWN — the L-shaped reading."))
    + '<p><strong>Exam wording to expect:</strong> "complete the histogram", "estimate the median/interquartile range from the graph", Higher-leaning in this folder.</p>',
    questions=["Q6: A histogram bar spans 30–50 (width 20) with frequency 36. Find its frequency density", "Q7: CF at Q1 position (22.5 of 90) reads 28, at median (45) reads 44, at Q3 (67.5) reads 61. Estimate the IQR."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> Density = 3.2 × 25 = <strong>80</strong></p>'
        '<p><strong>Q2.</strong> 45 ÷ 15 = <strong>3</strong></p>'
        '<p><strong>Q3.</strong> Median position = 200 ÷ 2 = <strong>100</strong></p>'
        '<p><strong>Q4.</strong> 50 ÷ 20 = <strong>2.5</strong></p>'
        '<p><strong>Q5.</strong> 120 − 70 = <strong>50</strong> — subtract cumulative values, not read the axis</p>'
        '<p><strong>Q6.</strong> Density = 36 ÷ 20 = <strong>1.8</strong></p>'
        '<p><strong>Q7.</strong> IQR = 61 − 28 = <strong>33</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Frequency density = frequency ÷ class width — the histogram HEIGHT</li>'
        '<li>Unequal widths REQUIRE densities; areas represent frequency</li>'
        '<li>Cumulative frequency: running total; plot at the UPPER boundary of each class</li>'
        '<li>Median = n/2 position; Q1 = n/4; Q3 = 3n/4 (read off the curve)</li>'
        '<li>IQR = Q3 − Q1 — spread of the middle 50%</li>'
        '</ul>'),
    context=CTX('<p>Grouped data: 3–5 marks on Papers 2/3 — histogram drawing, CF curves, '
        'quartile estimates. Reading between gridlines (interpolation by eye) is the marked skill.</p>'
        '<p>Links to: charts (S2), central tendency (S4), sampling (S1).</p>'))

B["S1-sampling.html"] = dict(
    marker="Q6: A canteen surveys only students buying hot lunches. Give two reasons the sample may be biased",
    worked=W_SEC("Sampling: census (everyone) vs sample. Good samples are representative and unbiased — stratified sampling preserves population proportions.",
        EX("A factory tests every 50th item off the line. Name the method and one advantage.",
            '<p><strong>Systematic sampling</strong>; advantage: simple, quick, spreads the sample across '
            'the whole production run.</p>',
            "B1 method, B1 advantage. Systematic = fixed interval k = N/n with a random start.") +
        EX("A school has 400 boys and 600 girls. A stratified sample of 50 is needed. How many girls?",
            '<p>Girls: (600/1000) × 50 = <strong>30</strong> (boys: 20)</p>',
            "M1 for the proportion, A1 for 30. Stratified = (group size ÷ total) × sample size, per group."))
    + '<p><strong>Exam wording to expect:</strong> "explain why this sample may be biased", "calculate the stratified sample size".</p>',
    questions=["Q6: A canteen surveys only students buying hot lunches. Give two reasons the sample may be biased", "Q7: A town of 20,000 has 4 suburbs with 5000, 6000, 4000, 5000 residents. A sample of 100: how many from suburb 2?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> The <strong>whole group of interest</strong> about which conclusions are drawn</p>'
        '<p><strong>Q2.</strong> Boys (120/300) × 50 = <strong>20</strong>; girls <strong>30</strong></p>'
        '<p><strong>Q3.</strong> k = 200 ÷ 25 = <strong>8</strong> (every 8th person)</p>'
        '<p><strong>Q4.</strong> Only film-goers are surveyed — views of non-attendees are missing; '
        'people leaving have just CHOSEN a film → both skew positive</p>'
        '<p><strong>Q5.</strong> Cheaper/faster; smaller effort; feasible when a full census is impractical</p>'
        '<p><strong>Q6.</strong> Non-buyers (packed lunches) excluded; hot-lunch buyers may share '
        'preferences (wealth, taste) — unrepresentative of all students</p>'
        '<p><strong>Q7.</strong> (6000/20000) × 100 = <strong>30</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Population = everyone of interest · Sample = the subgroup surveyed · Census = all of them</li>'
        '<li>Random: each member equally likely — removes selection bias</li>'
        '<li>Stratified: (group/total) × sample size — preserves proportions</li>'
        '<li>Systematic: every k-th (k = N ÷ n), random start</li>'
        '<li>Bias sources: self-selection, convenient locations, leading questions, small samples</li>'
        '</ul>'),
    context=CTX('<p>Sampling: 2–4 marks on Papers 1/2 — stratified calculations and bias '
        'explanations. The bias answers need a REASON tied to who is missing, not just "unfair".</p>'
        '<p>Links to: describing data (S5), capture-recapture contexts, recording (P1).</p>'))

if __name__ == "__main__":
    run(B)
    run2(B)
