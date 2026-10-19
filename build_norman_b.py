#!/usr/bin/env python3
"""Norman England — remaining topics N41-N47."""
from build_medicine_a import build, H, END, TBL, Q

S = {}

S["N41-establishing-control-castles-and-harrying"] = (
    H('📋 Key Concepts: How the Normans Took and Kept England', (
        '<p><strong>1066–69 rebellions:</strong> Exeter (1068), Harold\u2019s sons\u2019 raid (1068), the '
        '<strong>northern rising (1069)</strong> — Edgar Aetheling + Northumbrians + Danish fleet — answered '
        'by the <strong>Harrying of the North (1069–70)</strong>. The <strong>Revolt of the Earls (1075)</strong> '
        'was the last major internal rising (Waltheof executed 1076).</p>' +
        TBL([
            ['Method','Detail','Effect'],
            ['Motte-and-bailey castles','3,000+; earth-timber, built in days','Constant military dominance'],
            ['Land confiscation','~5% of land English by 1086','Resistance leadership removed'],
            ['Harrying of the North','1069–70: York to Durham wasted','Famine; no northern rising after 1070'],
            ['Law changes','Murdrum fine; forest law; coinage control','Norman safety; economic grip'],
            ['The Church','Lanfranc; Norman bishops','Legitimacy and discipline'],
        ]) +
        '<p><strong>Submission of the Earls (1068)</strong> at York: Edwin, Morcar, Waltheof, Gospatric — '
        'temporary peace, later broken.</p>') + END) +

    H('🧮 Worked Examples — Exam Style', (
        '<div class="example"><p><strong>"Land confiscation was more important than castles in establishing '
        'Norman control." How far do you agree? (16 + 4)</strong></p>'
        '<p>Castles: immediate, military, visible. Land: permanent, economic, generational — the new elite '
        'had everything to lose. Judgement: castles controlled the FIRST decade; landholding secured the '
        'NEXT century — "castles the bluntest instrument, landholding the deepest".</p></div>'
        '<div class="example"><p><strong>Describe two features of the Harrying of the North (4).</strong></p>'
        '<p>« Crops, herds and tools were destroyed between York and Durham — Domesday records villages as '
        '"waste" twenty years later. Refugees died of famine that winter; Orderic Vitalis claims 100,000+ '
        'deaths and calls William a "great tormentor". »</p></div>') + END) +

    H('❓ Practice Questions', (
        '<div class="practice-questions">' +
        Q(1,'Describe two features of the revolts of 1068–69.') +
        Q(2,'Give two reasons motte-and-bailey castles suited the conquest.') +
        Q(3,'Describe two features of the Revolt of the Earls (1075).') +
        Q(4,'Explain why Norman control survived after 1070 (two reasons, 4 marks).') +
        Q(5,'"The harrying was William\u2019s greatest mistake." How far do you agree? (16 + 4 marks)') +
        '</div>') + END) +

    H('✅ Answers', (
        '<ol>'
        '<li><strong>Exeter 1068</strong> (Gytha — 18-day siege); <strong>1069 northern rising</strong> '
        '(Edgar + Danes — Durham garrison murdered).</li>'
        '<li><strong>Speed</strong> (earth-timber in days); <strong>garrison economy</strong> (small force '
        'overawes a district).</li>'
        '<li><strong>Three earls</strong> (Ralph de Gael, Roger de Breteuil, Waltheof) plotted during '
        'William\u2019s absence; crushed by loyal bishops; Waltheof executed 1076 — last English earl.</li>'
        '<li><strong>Castle network</strong> garrisoned with loyal knights; <strong>elite replacement</strong> '
        '— no leaders left; (Danish fleet bought off 1070).</li>'
        '<li>Plan — YES: northern resistance permanently broken. NO: economy crippled (less tax); reputation '
        'damaged; castles/landholding did the holding. Verdict: harrying punished, castles governed.</li>'
        '</ol>') + END) +

    H('📌 Key Facts to Memorise', (
        '<ul>'
        '<li>Exeter 1068 · northern rising 1069 · Harrying 1069–70 · Earls 1075 · Waltheof executed 1076</li>'
        '<li>Land 5% English by 1086 · 3,000+ motte-and-baileys · 500+ stone by 1100</li>'
        '<li>Murdrum 46 marks · forest law · Domesday "waste" entries</li>'
        '</ul>') + END) +

    H('🗺️ In the Exam', (
        '<p>Match each control method to its DATE: 1066 shock → 1067 consolidation → 1068–69 risings → '
        '1069–70 harrying → 1070s institutional grip. Precise sequencing earns marks over lists.</p>') + END) +

    H('⚠️ Common Errors', (
        '<ul>'
        '<li><span class="wrong">Wrong: "stone castles from 1066"</span> '
        '<span class="right">Correct: earth-timber first; stone keeps from the 1070s–90s</span></li>'
        '<li><span class="wrong">Wrong: "Waltheof was Norman"</span> '
        '<span class="right">Correct: last ENGLISH earl, executed 1076</span></li>'
        '</ul>') + END) +

    H('🎯 Exam Tips', (
        '<ul>'
        '<li>Order control factors by DURATION: harrying (event) → castles (years) → landholding '
        '(generations)</li>'
        '<li>Quote Domesday "waste" as documentary evidence of the harrying</li>'
        '</ul>') + END)
)

S["N42-feudalism-government-and-law"] = (
    H('📋 Key Concepts: The Feudal System and Norman Government', (
        '<p><strong>Feudalism</strong>: land-for-service — <strong>~170 tenants-in-chief</strong> held from '
        'the king; subinfeudation to <strong>~4,000–5,000 knights</strong> (40 days\u2019 service); homage + '
        'oath of fealty bound each level. William KEPT English machinery: shires, sheriffs, hundred courts, '
        'writs, coinage — and ADDED: murdrum fine (46 marks), forest law, trial by combat, Domesday. His 1067 '
        'pledge to keep English law bought pragmatic legitimacy.</p>') + END) +

    H('🧮 Worked Examples — Exam Style', (
        '<div class="example"><p><strong>"William kept English government and only filled it with Normans." '
        'How far do you agree? (16 + 4)</strong></p>'
        '<p>KEEP: shires, hundreds, sheriffs, writs, coinage, the 1067 law pledge. CHANGE: feudal landholding, '
        'murdrum, forest law, trial by combat, Lanfranc\u2019s Church, Domesday. Verdict: English skeleton, '
        'Norman muscle — "continuity of machinery, rupture of personnel and land".</p></div>'
        '<div class="example"><p><strong>Describe two features of royal writs (4).</strong></p>'
        '<p>« Short sealed letters in the king\u2019s name ordering officials — cheap, quick, permanent '
        'evidence. Under Lanfranc\u2019s influence they became the standard instrument of shire '
        'government. »</p></div>') + END) +

    H('❓ Practice Questions', (
        '<div class="practice-questions">' +
        Q(1,'Describe two features of homage and fealty.') +
        Q(2,'What was subinfeudation?') +
        Q(3,'Give two purposes of the Domesday survey.') +
        Q(4,'Explain why William kept English law (two reasons, 4 marks).') +
        Q(5,'"Norman government was revolutionary rather than evolutionary." How far do you agree? (16 + 4)') +
        '</div>') + END) +

    H('✅ Answers', (
        '<ol>'
        '<li><strong>Homage</strong>: kneeling, hands between the lord\u2019s — becoming "his man"; '
        '<strong>fealty</strong>: loyalty oath on relics — breach = forfeiture.</li>'
        '<li>Sub-letting part of a fief to a knight in exchange for service — multiplying mounted force.</li>'
        '<li><strong>Taxation</strong> (geld on true values); <strong>settling ownership disputes</strong> '
        'after 20 years of confiscation.</li>'
        '<li><strong>Legitimacy</strong> (ruling as Edward\u2019s heir); <strong>practicality</strong> (the '
        'systems worked — switching costs high).</li>'
        '<li>Plan: machinery English; personnel/land Norman; NEW instruments (Domesday, murdrum, forest). '
        'Verdict: evolutionary machinery, revolutionary ownership.</li>'
        '</ol>') + END) +

    H('📌 Key Facts to Memorise', (
        '<ul>'
        '<li>~170 tenants-in-chief · ~4,000–5,000 knights · 40 days\u2019 service</li>'
        '<li>Writs · murdrum 46 marks · forest law · trial by combat introduced</li>'
        '<li>Domesday 1086 (taxes + disputes) · 1067 pledge to keep English law</li>'
        '</ul>') + END) +

    H('🗺️ In the Exam', (
        '<p>Build answers as "kept X, changed Y, added Z" — the third element separates grades.</p>') + END) +

    H('⚠️ Common Errors', (
        '<ul>'
        '<li><span class="wrong">Wrong: "feudalism was invented by the Normans"</span> '
        '<span class="right">Correct: evolved from Frankish practice — William APPLIED it fully</span></li>'
        '<li><span class="wrong">Wrong: "all peasants became slaves"</span> '
        '<span class="right">Correct: most were villeins (unfree but not owned); slavery declined</span></li>'
        '</ul>') + END) +

    H('🎯 Exam Tips', (
        '<ul>'
        '<li>Learn the pyramid numbers — quantitative detail is instantly credible</li>'
        '<li>"Continuity of machinery, rupture of personnel" is a portable judgement phrase</li>'
        '</ul>') + END)
)

S["N43-domesday-economy-and-towns"] = (
    H('📋 Key Concepts: Domesday Book and the Norman Economy', (
        '<p><strong>Domesday (1086):</strong> commissioners + shire juries reported land, livestock, mills, '
        'ploughs and values (1066 vs 1086). <strong>Great Domesday</strong> (condensed) + <strong>Little '
        'Domesday</strong> (East Anglia, fuller). Final judgements — hence "Domesday". <strong>Economy:</strong> '
        'agrarian manors; ~100 boroughs by 1086; castle-borough pairs; <strong>Jewish communities from Rouen '
        '(c1070)</strong> providing credit; wool exports; forest law reserving royal hunting land.</p>') + END) +

    H('🧮 Worked Examples — Exam Style', (
        '<div class="example"><p><strong>"Domesday Book was mainly a tool of oppression." How far do you '
        'agree? (16 + 4)</strong></p>'
        '<p>OPPRESS: fixed the confiscations; "waste" entries record the harrying; the Anglo-Saxon Chronicle '
        'says men "shuddered" at the inquest. BUT: settled disputes, standardised taxation, unique economic '
        'record. Verdict: oppressive in origin, administrative in use.</p></div>'
        '<div class="example"><p><strong>Describe two features of town life (4).</strong></p>'
        '<p>« Towns clustered around castles — defence and trade together (Chester, Newcastle). Jewish '
        'moneylenders financed abbeys and castles, since Christians could not lend at interest. »</p></div>') + END) +

    H('❓ Practice Questions', (
        '<div class="practice-questions">' +
        Q(1,'What are Great and Little Domesday?') +
        Q(2,'Describe two features of the Norman economy.') +
        Q(3,'Why were Jewish communities invited to England?') +
        Q(4,'Explain why Domesday was called "Domesday" (two reasons, 4 marks).') +
        Q(5,'"Domesday strengthened royal power more than any castle." How far do you agree? (16 + 4)') +
        '</div>') + END) +

    H('✅ Answers', (
        '<ol>'
        '<li><strong>Great</strong>: condensed, most shires; <strong>Little</strong>: fuller East Anglian '
        'returns (project unfinished at William\u2019s death).</li>'
        '<li><strong>Manorial farming</strong> (demesne + villein labour); <strong>growing boroughs</strong> '
        'with markets, mints and Jewish finance.</li>'
        '<li><strong>Usury</strong> — Christians could not lend at interest; Jews could, and the crown '
        'taxed/seized their profits.</li>'
        '<li>Judgements <strong>final without appeal</strong>; covering <strong>every shire and '
        'holding</strong> — total, like Doomsday records.</li>'
        '<li>Plan: castles = military; Domesday = fiscal/legal control (it priced the kingdom). Argue '
        'information was the deeper power.</li>'
        '</ol>') + END) +

    H('📌 Key Facts to Memorise', (
        '<ul>'
        '<li>1086 · Great vs Little · juries reporting 1066-vs-1086 values</li>'
        '<li>~100 boroughs · castle-borough pairing · Jews from Rouen c1070</li>'
        '<li>Forest law = whole districts under royal hunting restrictions</li>'
        '</ul>') + END) +

    H('🗺️ In the Exam', (
        '<p>Quote Domesday\u2019s dual values (1066 vs 1086) to "measure" the conquest and its "waste" '
        'entries to evidence the harrying — documentary evidence beats adjectives.</p>') + END) +

    H('⚠️ Common Errors', (
        '<ul>'
        '<li><span class="wrong">Wrong: "Domesday recorded every person"</span> '
        '<span class="right">Correct: land, livestock, mills, VALUES — a tax audit</span></li>'
        '<li><span class="wrong">Wrong: "forest law covered only woodland"</span> '
        '<span class="right">Correct: whole districts — "forest" = land under forest law</span></li>'
        '</ul>') + END) +

    H('🎯 Exam Tips', (
        '<ul>'
        '<li>Use Domesday numbers (5% English land, waste %) in control essays</li>'
        '<li>Link Jewish finance to cathedral building — connects economy and Church topics</li>'
        '</ul>') + END)
)

S["N44-village-life-and-peasants"] = (
    H('📋 Key Concepts: Village Life Under the Normans', (
        '<p><strong>Peasant hierarchy:</strong> <strong>villeins</strong> (tied to the manor, ~2–3 days\u2019 '
        'week-work), <strong>cottars/bordars</strong> (small plots, more labour), <strong>slaves</strong> '
        '(~10% in Domesday, gone by c1120), <strong>freemen/sokemen</strong> (Danelaw). Dues: <strong>merchet</strong> '
        '(marriage), <strong>heriot</strong> (best beast on death), mill fees; manor courts + frankpledge '
        'policing. Daily life changed slowly: same fields, seasons and saints\u2019 days; new lords, stone '
        'churches, forest law.</p>') + END) +

    H('🧮 Worked Examples — Exam Style', (
        '<div class="example"><p><strong>"Village life changed little for ordinary people after 1066." How '
        'far do you agree? (16 + 4)</strong></p>'
        '<p>CHANGE: new lords, French elite, heavier dues, forest law, stone churches. CONTINUITY: fields, '
        'faith, courts, dialect. Verdict: political revolution, social evolution — with forest law the '
        'harshest daily change.</p></div>'
        '<div class="example"><p><strong>Describe two features of villein obligations (4).</strong></p>'
        '<p>« Week-work: two or three days on the lord\u2019s demesne every week. Boon-work at harvest plus '
        'dues such as merchet for a daughter\u2019s marriage. »</p></div>') + END) +

    H('❓ Practice Questions', (
        '<div class="practice-questions">' +
        Q(1,'Describe two differences between villeins and freemen.') +
        Q(2,'What was merchet?') +
        Q(3,'Give two signs slavery declined after 1066.') +
        Q(4,'Explain why villeins rarely left their manor (two reasons, 4 marks).') +
        Q(5,'"Norman rule mattered little to peasants." How far do you agree? (16 + 4 marks)') +
        '</div>') + END) +

    H('✅ Answers', (
        '<ol>'
        '<li>Villeins <strong>tied</strong> to the manor owing labour; freemen/sokemen held freely, could '
        'sell or leave.</li>'
        '<li>A fine for a <strong>daughter\u2019s marriage</strong> outside the manor.</li>'
        '<li>Domesday counts <strong>~10% slaves</strong> but records stop by the 1120s; the Church '
        'discouraged chattel slavery.</li>'
        '<li><strong>Legal</strong> (villeinage bound to the manor court); <strong>economic</strong> (no wage '
        'market; land held through the lord).</li>'
        '<li>Plan: lords, dues, forest law changed the edges; fields, faith and custom continued. Verdict: '
        'political upheaval, social continuity.</li>'
        '</ol>') + END) +

    H('📌 Key Facts to Memorise', (
        '<ul>'
        '<li>Villein / cottar / slave / sokemen — by freedom (slaves declining)</li>'
        '<li>Week-work 2–3 days · boon-work · merchet · heriot · mill fees</li>'
        '<li>Manor court + frankpledge = village policing</li>'
        '</ul>') + END) +

    H('🗺️ In the Exam', (
        '<p>See the conquest from BELOW: Domesday categories + the continuity argument — most candidates '
        'write only about barons.</p>') + END) +

    H('⚠️ Common Errors', (
        '<ul>'
        '<li><span class="wrong">Wrong: "all Anglo-Saxons were slaves"</span> '
        '<span class="right">Correct: slavery DECLINED; most were villeins (unfree, not owned)</span></li>'
        '<li><span class="wrong">Wrong: "peasants spoke French"</span> '
        '<span class="right">Correct: English survived as the peasants\u2019 tongue</span></li>'
        '</ul>') + END) +

    H('🎯 Exam Tips', (
        '<ul>'
        '<li>One specific due (merchet/heriot) as evidence — specifics score</li>'
        '<li>"Elite revolution, social evolution" — portable judgement</li>'
        '</ul>') + END)
)

S["N45-town-life-trade-and-jews"] = (
    H('📋 Key Concepts: Towns, Trade and the Jewish Communities', (
        '<p><strong>Towns:</strong> castle-borough pairs; chartered markets; separate "French boroughs" '
        '(Nottingham); ~100 boroughs by 1086. <strong>Trade:</strong> wool to Flanders, salt (Droitwich), '
        'lead/tin. <strong>Jewish communities</strong> (from Rouen, c1070): moneylending under royal '
        'protection — and royal exploitation (Rufus notoriously seized assets).</p>') + END) +

    H('🧮 Worked Examples — Exam Style', (
        '<div class="example"><p><strong>"Towns were the biggest economic change of Norman England." How '
        'far do you agree? (16 + 4)</strong></p>'
        '<p>YES: castle-borough growth, charters, Jewish finance, wool exports — commercialisation begins. '
        'NO: ~90% agrarian; manors fed everything; towns were islands. Verdict: towns the FASTEST change, '
        'agriculture the BIGGEST.</p></div>'
        '<div class="example"><p><strong>Describe two features of Jewish communities (4).</strong></p>'
        '<p>« Invited from Rouen c1070 to provide credit — financing abbeys and castles. Under the king\u2019s '
        'direct protection, which also meant he could tax and seize from them at will. »</p></div>') + END) +

    H('❓ Practice Questions', (
        '<div class="practice-questions">' +
        Q(1,'Describe two features of castle-borough towns.') +
        Q(2,'Why could Jewish moneylenders charge interest?') +
        Q(3,'Give two examples of Norman town planning.') +
        Q(4,'Explain why kings protected Jewish communities (two reasons, 4 marks).') +
        Q(5,'"Norman rule stimulated English towns." How far do you agree? (16 + 4 marks)') +
        '</div>') + END) +

    H('✅ Answers', (
        '<ol>'
        '<li>Castles <strong>overlooking markets</strong>; <strong>separate French boroughs</strong> beside '
        'English settlements.</li>'
        '<li><strong>Church law banned usury</strong> for Christians; Jewish lenders filled the credit gap.</li>'
        '<li><strong>Grid layouts</strong> in new boroughs; <strong>castle over market/mint</strong>; chartered '
        'markets.</li>'
        '<li><strong>Finance</strong> (cathedrals, castles, campaigns); <strong>revenue</strong> (a royal '
        'reserve to tax or seize).</li>'
        '<li>Plan: castle-boroughs, charters, credit, wool = stimulus; agrarian continuity + northern '
        'devastation = limits. Weigh south-east growth against northern destruction.</li>'
        '</ol>') + END) +

    H('📌 Key Facts to Memorise', (
        '<ul>'
        '<li>~100 boroughs by 1086 · castle-borough pairs · French boroughs (Nottingham)</li>'
        '<li>Jews from Rouen c1070 · protection = exploitation · wool exports to Flanders</li>'
        '</ul>') + END) +

    H('🗺️ In the Exam', (
        '<p>The castle-borough pairing is your signature example of PRACTICAL Norman power (defence + '
        'revenue in one).</p>') + END) +

    H('⚠️ Common Errors', (
        '<ul>'
        '<li><span class="wrong">Wrong: "Jews were expelled under the Normans"</span> '
        '<span class="right">Correct: expulsion came in 1290 — Norman England protected (and exploited) '
        'them</span></li>'
        '<li><span class="wrong">Wrong: "towns declined after 1066"</span> '
        '<span class="right">Correct: boroughs and market charters GREW — around castles</span></li>'
        '</ul>') + END) +

    H('🎯 Exam Tips', (
        '<ul>'
        '<li>Nottingham\u2019s "French borough" = your named example</li>'
        '<li>Link Jewish finance to cathedral building — connects trade and Church</li>'
        '</ul>') + END)
)

S["N46-church-monasticism-and-lanfranc"] = (
    H('📋 Key Concepts: The Norman Church', (
        '<p><strong>Personnel:</strong> by 1087 only <strong>Wulfstan of Worcester</strong> among English '
        'bishops; <strong>Stigand</strong> deposed 1070; <strong>Lanfranc</strong> (Archbishop 1070–89) — '
        'councils (1070, 1075), sees moved to towns, celibacy enforced, cathedral schools. <strong>Buildings:</strong> '
        'Romanesque cathedrals beside castles (Durham 1093). <strong>Monasticism:</strong> Cluniac Lewes '
        '(1077), monks as bishops. <strong>Rome:</strong> William controlled appointments — no homage to the '
        'pope demanded. <strong>Anselm vs Rufus</strong> — the First Quarrel (exile 1097).</p>') + END) +

    H('🧮 Worked Examples — Exam Style', (
        '<div class="example"><p><strong>"The Norman Church was reformed more for political than religious '
        'reasons." How far do you agree? (16 + 4)</strong></p>'
        '<p>POLITICAL: bishops replaced (control); cathedral-castle pairing; William\u2019s appointments; '
        'reform removed Stigand (old-regime symbol). RELIGIOUS: genuine Gregorian ideals (celibacy, simony), '
        'monastic learning, Lanfranc\u2019s scholarship. Verdict: religious methods, political outcomes.</p></div>'
        '<div class="example"><p><strong>Describe two features of Lanfranc\u2019s reforms (4).</strong></p>'
        '<p>« Councils of 1070 and 1075 enforced celibacy and moved bishops\u2019 sees to towns. He replaced '
        'irregular appointments and built cathedral schools training Norman administrators. »</p></div>') + END) +

    H('❓ Practice Questions', (
        '<div class="practice-questions">' +
        Q(1,'Who was the only English bishop to survive, and where?') +
        Q(2,'Describe two features of Norman Romanesque architecture.') +
        Q(3,'What did the 1075 Council rule about sees?') +
        Q(4,'Explain why William replaced English bishops (two reasons, 4 marks).') +
        Q(5,'"Lanfranc did more to secure the conquest than any baron." How far do you agree? (16 + 4)') +
        '</div>') + END) +

    H('✅ Answers', (
        '<ol>'
        '<li><strong>Wulfstan of Worcester</strong> — the exception, and a model of holiness the Normans '
        'used to validate their rule.</li>'
        '<li><strong>Massive round-arched (Romanesque) naves/towers</strong> in stone; <strong>cathedrals '
        'sited in castle towns</strong> (Durham beside the castle).</li>'
        '<li><strong>Sees moved from villages to towns</strong> — administration where power lay.</li>'
        '<li><strong>Loyalty</strong> (English prelates backed risings in 1069); <strong>legitimacy</strong> '
        '(reforming the "corrupt" Church justified the conquest to Rome).</li>'
        '<li>Plan: the Church taxed, taught, recorded and preached obedience — every baronial skill with '
        'better paperwork.</li>'
        '</ol>') + END) +

    H('📌 Key Facts to Memorise', (
        '<ul>'
        '<li>Stigand deposed 1070 · Lanfranc 1070–89 · Anselm 1093 · Wulfstan survives</li>'
        '<li>Councils 1070/1075 · sees to towns · celibacy · Durham begun 1093</li>'
        '<li>William\u2019s control of appointments — no homage to the pope</li>'
        '</ul>') + END) +

    H('🗺️ In the Exam', (
        '<p>Church questions link to CONTROL (legitimacy), ADMINISTRATION (literacy) and ARCHITECTURE '
        '(power in stone) — Durham\u2019s castle-cathedral pairing is the ready example.</p>') + END) +

    H('⚠️ Common Errors', (
        '<ul>'
        '<li><span class="wrong">Wrong: "Lanfranc was a puppet"</span> '
        '<span class="right">Correct: a genuine Gregorian reformer serving both pope and king</span></li>'
        '<li><span class="wrong">Wrong: "Anselm served Rufus loyally"</span> '
        '<span class="right">Correct: quarrelled and exiled himself (1097–1100)</span></li>'
        '</ul>') + END) +

    H('🎯 Exam Tips', (
        '<ul>'
        '<li>Durham = castle + cathedral in one town — military and spiritual dominance together</li>'
        '<li>Stigand\u2019s deposition = the symbolic start of reform</li>'
        '</ul>') + END)
)

S["N47-norman-architecture-historic-environment-castles"] = (
    H('📋 Key Concepts: Castles as Historic Environment', (
        '<p>Prepare ONE castle across three lenses: <strong>function</strong> (motte ~5–10m, bailey = '
        'garrison/stores/court, well for sieges), <strong>phases</strong> (1066 timber → 1070s–90s stone '
        'keeps → 12th-century gatehouses/shell keeps — each phase a threat level), <strong>evidence</strong> '
        '(earthworks, keep footprints, mason marks, chapels). <strong>White Tower c1078</strong> (Gundulf, '
        '27m+, Caen stone) = the biggest; <strong>Pevensey 1066</strong> = the landing fort; <strong>Durham</strong> '
        '= castle+cathedral pairing.</p>') + END) +

    H('🧮 Worked Examples — Exam Style', (
        '<div class="example"><p><strong>Historic-environment: "Explain how features of the castle show '
        'defensive and symbolic purposes." (AQA style)</strong></p>'
        '<p>Method: feature (motte height) → function (archery range, flood defence) → symbol (seen for '
        'miles = lordship) → phase/date link (stone keep after the 1088 rising). Site numbers are '
        'everything.</p></div>'
        '<div class="example"><p><strong>"Norman castles were built for defence, not display." How far do '
        'you agree? (16 + 4)</strong></p>'
        '<p>DEFENCE: siting, storage, garrisons. DISPLAY: the White Tower\u2019s scale beyond need; '
        'cathedral-castle pairing; the message to subjects. Verdict: early castles defend; later stone '
        'ones advertise — the function shifted as the conquest stabilised.</p></div>') + END) +

    H('❓ Practice Questions', (
        '<div class="practice-questions">' +
        Q(1,'Describe two defensive features of a motte-and-bailey castle.') +
        Q(2,'What was the White Tower, and when was it built?') +
        Q(3,'Give two features showing a castle\u2019s administrative role.') +
        Q(4,'Explain why castles changed from timber to stone (two reasons, 4 marks).') +
        Q(5,'"Every feature of a Norman castle was military." How far do you agree? (16 + 4 marks)') +
        '</div>') + END) +

    H('✅ Answers', (
        '<ol>'
        '<li><strong>The motte</strong> (raised mound with palisaded tower — range + flood defence); '
        '<strong>the bailey</strong> (walled yard: garrison, stables, stores, workshops).</li>'
        '<li>The <strong>Great Tower (White Tower)</strong>, London — begun c1078 by Gundulf; largest keep '
        'in England, Caen stone shipped over.</li>'
        '<li><strong>Mints and courts</strong> in the bailey; <strong>markets at the gate</strong> — tolls '
        'and administration through the lord.</li>'
        '<li><strong>Fire risk</strong> (timber burns); <strong>status/permanence</strong> — stone says '
        '"here forever".</li>'
        '<li>Plan: motte/bailey = military; chapels, halls, market gates = lordship. Weigh by phase: 1060s '
        'defensive, 1090s symbolic.</li>'
        '</ol>') + END) +

    H('📌 Key Facts to Memorise', (
        '<ul>'
        '<li>Motte 5–10m · bailey functions · palisade → shell keep</li>'
        '<li>White Tower c1078 (Gundulf) · Durham 1072/1093 · Pevensey 1066</li>'
        '<li>Phases: timber → stone keeps → gatehouses (12th century)</li>'
        '</ul>') + END) +

    H('🗺️ In the Exam', (
        '<p>The historic-environment question is PURE site recall — no sources given. Feature → function → '
        'symbol → phase/date. Practise one castle until the numbers are automatic.</p>') + END) +

    H('⚠️ Common Errors', (
        '<ul>'
        '<li><span class="wrong">Wrong: "stone castles immediately after Hastings"</span> '
        '<span class="right">Correct: timber first — speed was the weapon</span></li>'
        '<li><span class="wrong">Wrong: "keeps were only for the lord\u2019s family"</span> '
        '<span class="right">Correct: garrisons, stores, courts, even minting in/below keeps</span></li>'
        '</ul>') + END) +

    H('🎯 Exam Tips', (
        '<ul>'
        '<li>Memorise ONE castle\u2019s numbers — site detail is the whole mark scheme</li>'
        '<li>Say every feature twice: "functionally X, symbolically Y"</li>'
        '</ul>') + END)
)

PAGES = [
    ("N41-establishing-control-castles-and-harrying",
     "Establishing Control: Castles and the Harrying",
     "The rebellions of 1068–70, the Harrying of the North, motte-and-bailey castles, land confiscation and the Revolt of the Earls — how the Normans took and kept England.",
     S["N41-establishing-control-castles-and-harrying"]),
    ("N42-feudalism-government-and-law",
     "Feudalism, Government and Law",
     "The feudal pyramid, homage and fealty, sheriffs and writs, murdrum and forest law — Norman government built on English machinery with new instruments of control.",
     S["N42-feudalism-government-and-law"]),
    ("N43-domesday-economy-and-towns",
     "Domesday, Economy and Towns",
     "The Domesday survey of 1086, the manorial economy, castle-borough towns, Jewish communities and forest law — the Norman economy in numbers.",
     S["N43-domesday-economy-and-towns"]),
    ("N44-village-life-and-peasants",
     "Village Life and the Peasants",
     "Villeins, cottars and sokemen; week-work and boon-work; merchet, heriot and the manor court — Norman rule as ordinary people lived it.",
     S["N44-village-life-and-peasants"]),
    ("N45-town-life-trade-and-jews",
     "Town Life, Trade and the Jewish Communities",
     "Castle-borough towns, French boroughs, wool exports, chartered markets and the Jewish moneylenders invited by William — protection and exploitation under the crown.",
     S["N45-town-life-trade-and-jews"]),
    ("N46-church-monasticism-and-lanfranc",
     "The Church, Monasticism and Lanfranc",
     "Lanfranc's councils, Norman bishops, Romanesque cathedrals beside castles, monastic learning and William's control of appointments — reform with political purpose.",
     S["N46-church-monasticism-and-lanfranc"]),
    ("N47-norman-architecture-historic-environment-castles",
     "Norman Architecture and the Castle Historic Environment",
     "Motte-and-bailey to great towers: defensive and symbolic features, building phases 1066–1135, and exam technique for the historic-environment site question.",
     S["N47-norman-architecture-historic-environment-castles"]),
]

if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else 'topics/history/aqa'
    for slug, title, desc, body in PAGES:
        html = build(slug, title, desc, body)
        open(f'{out}/{slug}.html', 'w', encoding='utf-8').write(html)
        print('wrote', f'{out}/{slug}.html', len(html), 'bytes')
