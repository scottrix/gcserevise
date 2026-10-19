#!/usr/bin/env python3
"""History option: Norman England (N40-47) — boards aqa/edexcel/ocr."""
from build_medicine_a import build, H, END, TBL, Q

S1 = (
    H('📋 Key Concepts: Claim, Conquest and Control (1064–87)', (
        '<p><strong>The succession crisis:</strong> Edward the Confessor died childless (January 1066) with '
        'four claimants: <strong>William of Normandy</strong> (alleged 1051 promise + Godwinson oath of 1064), '
        '<strong>Harold Godwinson</strong> (chosen by the Witan, crowned immediately), <strong>Edgar '
        'Aetheling</strong> (blood claim, aged ~14), <strong>Harald Hardrada</strong> (Tostig\u2019s alliance '
        'plus a deal with the Pope helped William gain support).</p>' +
        TBL([
            ['Battle','Date','Opponent','Outcome'],
            ['Gate Fulford','20 Sep 1066','Tostig + Hardrada','Harold\u2019s earls Edwin & Morcar defeated'],
            ['Stamford Bridge','25 Sep 1066','Hardrada & Tostig','Both killed; Viking threat ended'],
            ['Hastings','14 Oct 1066','William','Harold killed (arrow/blade to the eye per Bayeux Tapestry); William crowned Christmas Day 1066'],
        ]) +
        '<p><strong>Establishing control 1066–87:</strong> motte-and-bailey castles (3,000+, built in days), '
        'the <strong>Harrying of the North (1069–70)</strong> after the 1069 rising (Yorkshire devastated — '
        'Domesday records it "waste"), <strong> Submission of the earls (1075)</strong>, and replacing the '
        'Anglo-Saxon aristocracy: by 1086 only two surviving major landholders were English.</p>') + END) +

    H('📝 Feudalism, Landholding and Domesday', (
        '<p><strong>Feudalism</strong>: the king owned all land; tenants-in-chief (barons/bishops, ~170) held '
        'it for knight service; <strong>knight\u2019s fees</strong> (~4,000–5,000 knights owed ~40 days\u2019 '
        'military service); peasants at the bottom. <strong>Sanctuary and salvage:</strong> introducing '
        '<strong>forests</strong> (royal hunting, harsh forest law) and the <strong>murdrum fine</strong> '
        '(a hundred paid 46 marks if a dead Norman was found with no killer produced — protecting the '
        'conquerors).</p>' +
        '<p><strong>Domesday Book (1086):</strong> the great survey — who owned what, what it was worth '
        'under Edward and now; purposes: taxation, dispute settlement, control. "No Briton ever described '
        'England so thoroughly" — it legalised the conquest\u2019s land grab by RECORDING it.</p>') + END) +

    H('📝 Life Under the Normans: Villages, Towns, Church', (
        '<p><strong>Village life:</strong> most were <strong>villeins</strong> (tied to the lord\u2019s land, '
        'working ~2–3 days/week on demesne land); life revolved around the manor, harvest cycles and the '
        'village priest. <strong>Towns:</strong> growth of trade; <strong>Norman castles replaced Anglo-Saxon '
        'burhs</strong>; Jews invited over as moneylenders (Christians could not legally lend at interest).</p>' +
        '<p><strong>Church:</strong> William replaced English bishops/abbots with Normans (by 1087 only '
        'Wulfstan of Worcester survived among senior figures); <strong>Lanfranc</strong> as Archbishop of '
        'Canterbury (1070) rebuilt discipline, raised cathedral schools, extended the hierarchy; monasticism '
        'flourished; <strong>Norman Romanesque architecture</strong> — massive cathedrals (Durham begun 1093) '
        'and castles as statements of power.</p>' +
        '<p><strong>William Rufus (1087–1100) and Henry I (1100–35):</strong> succession struggles, Odo\u2019s '
        'rebellion (1088), Malcolm III\u2019s raids, Robert Curthose\u2019s Normandy rivalry — Henry won '
        'Normandy at <strong>Tinchebray (1106)</strong>; the Ango-Norman realm stabilised; Henry\u2019s '
        '<strong>Coronation Charter (1100)</strong> promised to end Rufus\u2019s abuses.</p>') + END) +

    H('🧮 Worked Examples — Exam Style', (
        '<div class="example"><p><strong>"The Harrying of the North was the main reason Norman control '
        'succeeded." How far do you agree? (AQA 16 + 4)</strong></p>'
        '<p>YES: the 1069–70 harrying destroyed the North\u2019s ability to resist (Domesday shows "waste"; '
        'chroniclers record famine, even cannibalism reports); no northern rising after 1070. NO: castles '
        'garrisoned across the country were the daily instrument of control; land confiscation removed '
        'resistance leadership; Stamford Bridge had already destroyed the alternative dynasty. JUDGEMENT: '
        'the harrying finished the north specifically; castles + landholding held everything — argue '
        '"harrying was the bluntest, castles the constant, instrument".</p></div>'
        '<div class="example"><p><strong>Describe two features of the feudal system (4).</strong></p>'
        '<p>« All land was held from the king in exchange for military service — about 170 tenants-in-chief '
        'subinfeudated to ~4,000–5,000 knights. Second, obligations ran downward too: lords owed protection '
        'and land, vassals loyalty and service, binding society in a pyramid. »</p></div>') + END) +

    H('❓ Practice Questions', (
        '<div class="practice-questions">' +
        Q(1,'Describe two features of the Battle of Hastings.') +
        Q(2,'Give two reasons William built motte-and-bailey castles so rapidly.') +
        Q(3,'Describe two features of the Harrying of the North.') +
        Q(4,'What was the murdrum fine, and what does it reveal?') +
        Q(5,'Explain why William commissioned the Domesday survey (two reasons, 4 marks).') +
        Q(6,'"Castles were the most important way the Normans established control." How far do you agree? '
           '(16 + 4 marks)') +
        '</div>') + END) +

    H('✅ Answers', (
        '<ol>'
        '<li>Harold fought exhausted after Stamford Bridge and a forced march south; the shield wall held '
        'until the Norman feigned-flight retreats drew out and killed Harold (and his brothers Gyrth and '
        'Leofwine).</li>'
        '<li><strong>Speed</strong> — earth-and-timber construction in days with forced labour; '
        '<strong>dominance</strong> — a small garrison could hold a district and overawe rebellion.</li>'
        '<li><strong>1069–70 devastation</strong> of Yorkshire/Durham (crops, livestock, villages burned — '
        'Domesday records 60%+ "waste" in some wapentakes); famine the following winter; northern resistance '
        'to the conquest effectively ended.</li>'
        '<li>A fine on a hundred when a Norman was found dead without his killer produced — shows Normans '
        'FEARED for their safety and legalised collective responsibility to protect them.</li>'
        '<li><strong>Taxation</strong> — know exactly what could be levied; <strong>legal control</strong> — '
        'settle land-disputes between Normans and fix ownership permanently.</li>'
        '<li>Plan: castles (daily military dominance), landholding (a new loyal elite), harrying '
        '(devastating the north), the Church (legitimacy + Lanfranc). Judgement: castles WERE the most '
        'visible instrument, but land-transference made control permanent — weigh temporary vs permanent '
        'mechanisms.</li>'
        '</ol>') + END) +

    H('📌 Key Facts to Memorise', (
        '<ul>'
        '<li>1064 oath · Gate Fulford 20/9 · Stamford Bridge 25/9 · Hastings 14/10 · crowned 25/12/1066</li>'
        '<li>Harrying 1069–70 · Submission of the Earls 1075 · Revolt of the Earls 1075</li>'
        '<li>Feudal pyramid: king → ~170 tenants-in-chief → ~4,000–5,000 knights → peasants</li>'
        '<li>Domesday Book 1086 (taxation + disputes) · Lanfranc Archbishop 1070 · murdrum fine 46 marks</li>'
        '<li>Rufus 1087–1100; Henry I 1100–35; Tinchebray 1106</li>'
        '</ul>') + END) +

    H('🗺️ In the Exam', (
        '<p>This option is <strong>British-depth + historic environment</strong> (AQA: castle-focused). '
        'For the historic-environment question, know ONE castle in detail — e.g. <strong>Warkworth or '
        'Pleshey or Pevensey</strong>: building phases, defensive features (motte height, bailey functions, '
        'tower keeps), how design responded to the threat level. For interpretation questions the Bayeux '
        'Tapestry and Domesday entries are the default sources — practise "how useful" with purpose '
        '(propaganda/tax record) and missing context.</p>') + END) +

    H('⚠️ Common Errors', (
        '<ul>'
        '<li><span class="wrong">Wrong: "Harold died from an arrow to the eye — proven fact"</span> '
        '<span class="right">Correct: the Bayeux Tapestry shows a figure with an arrow; other accounts say '
        'Harold was cut down by knights — say "sources disagree"</span></li>'
        '<li><span class="wrong">Wrong: "the Harrying was in 1066"</span> '
        '<span class="right">Correct: 1069–70, three years into the reign, after the northern rising</span></li>'
        '<li><span class="wrong">Wrong: "Domesday recorded people"</span> '
        '<span class="right">Correct: land, resources and VALUES — a tax audit, not a census of persons</span></li>'
        '</ul>') + END) +

    H('🎯 Exam Tips', (
        '<ul>'
        '<li>Control narrative = castles + landholding + harrying + Church + law — deploy as factor '
        'paragraphs in that order</li>'
        '<li>Hastings tactics: shield wall vs cavalry/archers; the feigned retreat ×2 — tactical detail '
        'earns the description marks</li>'
        '<li>For 16-markers, always name the factor in the topic sentence, evidence second, judgement '
        'weighed against a rival factor</li>'
        '</ul>') + END)
)

PAGES = [
    ("N40-claim-and-conquest-1064-1066",
     "Norman Claim and Conquest, 1064–66",
     "The succession crisis after Edward the Confessor, four claimants, the battles of Fulford, Stamford Bridge and Hastings, and William's coronation — with Hastings tactics and the Bayeux Tapestry debate.",
     S1),
]

if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else 'topics/history/aqa'
    for slug, title, desc, body in PAGES:
        html = build(slug, title, desc, body)
        open(f'{out}/{slug}.html', 'w', encoding='utf-8').write(html)
        print('wrote', f'{out}/{slug}.html', len(html), 'bytes')
