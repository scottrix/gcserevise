#!/usr/bin/env python3
"""French grammar bank pages 1-2 (FR25 tenses, FR26 articles/adjectives).
Builds from the FR11 template: clone, swap slug/URLs, replace content sections."""
import re
import sys

TPL = 'topics/french/aqa/FR11-hobbies-and-interests.html'

def cut_share(h):
    m = re.search(r'<section class="section[^"]*">\s*<h2>Share this page</h2>', h)
    return h[m.start():] if m else h[-4000:]

def build(slug, title, desc, sections_html):
    h = open(TPL, encoding='utf-8').read()
    h = h.replace('FR11-hobbies-and-interests', slug)
    h = h.replace('<title>Hobbies and Interests - GCSE French</title>', f'<title>{title} - GCSE French</title>')
    h = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + desc + m.group(2), h, count=1)
    h = re.sub(r'(<meta name="keywords" content=")[^"]*(")',
               lambda m: m.group(1) + f'GCSE French, French grammar, {title.lower()}, GCSE revision, free revision notes, French' + m.group(2), h, count=1)
    h = h.replace('<meta property="og:title" content="Hobbies and Interests - GCSE French">',
                  f'<meta property="og:title" content="{title} - GCSE French">')
    h = re.sub(r'(<meta property="og:description" content=")[^"]*(")', lambda m: m.group(1) + desc + m.group(2), h, count=1)
    h = h.replace('<meta name="twitter:title" content="Hobbies and Interests">',
                  f'<meta name="twitter:title" content="{title}">')
    h = re.sub(r'(<meta name="twitter:description" content=")[^"]*(")', lambda m: m.group(1) + desc + m.group(2), h, count=1)
    # breadcrumb topic name
    h = h.replace('<a href="#">Hobbies</a>', '<a href="#">Grammar</a>')
    h = re.sub(r'(<span>Hobbies and Interests</span>)', f'<span>{title}</span>', h)
    # topic header id + name
    h = h.replace('>FR11<', '>' + slug.split('-')[0] + '<')
    h = h.replace('<span class="topic-name">Hobbies and Interests</span>',
                  f'<span class="topic-name">{title}</span>')
    h = re.sub(r'(<p class="topic-desc">)[^<]*(</p>)', lambda m: m.group(1) + desc + m.group(2), h, count=1)
    # replace content sections: first section .. before Share section
    m1 = re.search(r'<section class="section">', h)
    share = re.search(r'<section class="section[^"]*">\s*<h2>Share this page</h2>', h)
    h = h[:m1.start()] + sections_html + '\n\n' + h[share.start():]
    return h

SEC = lambda h2: f'<section class="section">\n<h2>{h2}</h2>\n'
END = '</section>'
TBL = lambda rows: '<table>' + ''.join(f'<tr>{"".join(f"<th>{c}</th>" if i==0 else f"<td>{c}</td>" for i,c in enumerate(r))}</tr>' for r in rows) + '</table>'
Q = lambda n, t: f'<div class="question">\n<p><strong>Q{n}:</strong> {t}</p>\n</div>'

P1 = (
    SEC('📋 Key Concepts: The Four Tenses You Need') +
    '<p>GCSE French writing and speaking rewards variety of TENSE above almost everything else. '
    'The 90-word and 150-word tasks explicitly reward referring to past, present and future events. '
    'Four tenses cover it: the <strong>present</strong>, the <strong>passé composé</strong> (completed past), '
    'the <strong>imparfait</strong> (description/habit in the past) and the <strong>future</strong> '
    '(futur proche and futur simple).</p>' +
    TBL([
        ['Tense','Use','Time marker clue','Example'],
        ['Present','What happens / habits / opinions','chaque jour, normalement, d’habitude','Je joue au foot chaque samedi.'],
        ['Passé composé','A completed past event','hier, la semaine dernière, soudain','J’ai joué au tennis hier.'],
        ['Imparfait','Description, feelings, repeated past','quand j’étais petit, avant, tous les étés','C’était génial et nous jouions dehors.'],
        ['Futur proche','Near future plan','ce soir, demain, la semaine prochaine','Je vais jouer au rugby demain.'],
        ['Futur simple','Simple future','quand j’aurai dix-huit ans (with si/future time)','J’aurai mon permis l’année prochaine.'],
    ]) + END +

    SEC('📝 The Present Tense') +
    '<p>Regular endings: <strong>-er</strong> verbs (je -e, tu -es, il/elle -e, nous -ons, vous -ez, ils/elles -ent); '
    '<strong>-ir</strong> verbs (je -is, tu -is, il -it, nous -issons, vous -issez, ils -issent); '
    '<strong>-re</strong> verbs (je -s, tu -s, il —, nous -ons, vous -ez, ils -ent).</p>' +
    '<p>The four irregulars that appear in almost every exam answer:</p>' +
    TBL([
        ['','être','avoir','aller','faire'],
        ['je','suis','ai','vais','fais'],
        ['tu','es','as','vas','fais'],
        ['il/elle','est','a','va','fait'],
        ['nous','sommes','avons','allons','faisons'],
        ['vous','êtes','avez','allez','faites'],
        ['ils/elles','sont','ont','vont','font'],
    ]) +
    '<p>Opinion verbs are present-tense currency: <strong>je pense que / à mon avis / je trouve que</strong> + opinion. '
    'Add a reason with <strong>parce que / car</strong> and a second clause for the two-part opinions examiners reward.</p>' + END +

    SEC('📝 The Passé Composé') +
    '<p>Formation: <strong>avoir</strong> (present) + past participle. Past participles: '
    '<strong>-er → -é</strong> (joué), <strong>-ir → -i</strong> (fini), most <strong>-re → -u</strong> (vendu). '
    'Key irregulars: être → <strong>été</strong>, avoir → <strong>eu</strong>, faire → <strong>fait</strong>, '
    'voir → <strong>vu</strong>, prendre → <strong>pris</strong>, mettre → <strong>mis</strong>, '
    'lire → <strong>lu</strong>, écrire → <strong>écrit</strong>, dire → <strong>dit</strong>.</p>' +
    '<p><strong>ÊTRE verbs</strong> (movement/change of state — the DR MRS VANDERTRAMP set: devenir, revenir, '
    'monter, rester, sortir, venir, aller, naître, descendre, entrer, rentrer, tomber, retourner, arriver, '
    'mourir, partir) form the passé composé with <strong>être</strong>, and the participle AGREES: '
    '<em>elle est allée</em>, <em>ils sont partis</em>. Reflexive verbs also take être and agree '
    '(<em>elle s’est levée</em>).</p>' +
    '<p>In the negative, wrap the AUXILIARY: <strong>je n’ai pas joué</strong> — never « je n’ai joué pas ».</p>' + END +

    SEC('📝 The Imparfait vs the Passé Composé') +
    '<p>Imparfait endings are the same for every verb: <strong>-ais, -ais, -ait, -ions, -iez, -aient</strong>. '
    'Take the <strong>nous</strong> present form, drop <strong>-ons</strong>, add the endings: '
    '<em>nous jouons → je jouais</em>. The only exception: <em>être → ét-</em> (j’étais).</p>' +
    '<p>Choose by MEANING, not by translating:</p>' +
    TBL([
        ['Situation','Tense','Example'],
        ['Ongoing background / weather / feelings','Imparfait','Il pleuvait et je m’ennuyais.'],
        ['Repeated past habit','Imparfait','Nous allions à la plage tous les étés.'],
        ['Single completed event','Passé composé','Nous sommes allés à la plage samedi.'],
        ['Interrupting event (during background)','PC interrupts imparfait','Je lisais quand le téléphone a sonné.'],
    ]) + END +

    SEC('📝 The Future: Futur Proche and Futur Simple') +
    '<p><strong>Futur proche</strong> = aller (present) + infinitive: <em>je vais réviser ce soir</em>. '
    'It is the safest future for speaking and short writing tasks.</p>' +
    '<p><strong>Futur simple</strong> = infinitive + <strong>-ai, -as, -a, -ons, -ez, -ont</strong> '
    '(-re verbs drop the e: je vendrai). Irregular stems worth memorising: '
    'être → <strong>ser-</strong>, avoir → <strong>aur-</strong>, aller → <strong>ir-</strong>, '
    'faire → <strong>fer-</strong>, pouvoir → <strong>pourr-</strong>, voir → <strong>verr-</strong>, '
    'venir → <strong>viendr-</strong>.</p>' +
    '<p>After <strong>quand</strong> and <strong>si</strong> in future-time sentences, French uses a FUTURE '
    'where English uses a present: <em>quand j’aurai dix-huit ans, je passerai le permis</em> — '
    'this single structure impresses examiners at every tier.</p>' + END +

    SEC('🧮 Worked Examples — Exam Style') +
    '<div class="example"><p><strong>Write a 90-word paragraph about a past weekend (2 past events, 1 opinion).</strong></p>'
    '<p>Model: « Le weekend dernier, je suis allé(e) au cinéma avec mes amis. Nous avons regardé un film '
    'd’action et nous avons mangé des tacos. C’était génial, mais c’était trop cher — dix-huit euros ! '
    'Quand je lisais le programme, j’ai vu qu’un nouveau film de science-fiction sortait la semaine suivante. »</p>'
    '<p><em>Marks: PC ×3 (all with correct auxiliaries), imparfait for the description (c’était), '
    'opinion + justification, one quasi-subordinate structure. Tense variety is the top-band descriptor.</em></p></div>'
    '<div class="example"><p><strong>Translate into French: “When I am older, I will travel to France and I will stay with a host family.”</strong></p>'
    '<p>« Quand je serai plus âgé(e), je voyagerai en France et je resterai dans une famille d’accueil. »</p>'
    '<p><em>Two futur simple stems (ser-, -erai) after quand — the structure the mark scheme singles out.</em></p></div>' + END +

    SEC('❓ Practice Questions') +
    '<div class="practice-questions">' +
    Q(1,'Give the passé composé of: je (finir) mes devoirs hier soir.') +
    Q(2,'Give the passé composé of: elle (aller) au cinéma.') +
    Q(3,'Imparfait or passé composé? « Quand j’___ petit, je ___ souvent au foot. » (être / jouer)') +
    Q(4,'Put into the futur simple: nous (être) contents.') +
    Q(5,'Translate: I am going to play tennis tomorrow.') +
    Q(6,'Translate: We were watching television when it started to rain.') +
    '</div>' + END +

    SEC('✅ Answers') +
    '<ol>'
    '<li>J’ai fini mes devoirs hier soir.</li>'
    '<li>Elle est allée au cinéma. (être verb + agreement)</li>'
    '<li>« Quand j’<strong>étais</strong> petit, je <strong>jouais</strong> souvent au foot. » — both imparfait: background + habit.</li>'
    '<li>Nous serons contents.</li>'
    '<li>Je vais jouer au tennis demain.</li>'
    '<li>Nous regardions la télévision quand il a commencé à pleuvoir.</li>'
    '</ol>' + END +

    SEC('📌 Key Facts to Memorise') +
    '<ul>'
    '<li>PC = avoir + PP; être verbs (movement/reflexives) + AGREED participle</li>'
    '<li>Imparfait: nous-form minus -ons + -ais/-ais/-ait/-ions/-iez/-aient (être → ét-)</li>'
    '<li>Futur simple stems: ser-, aur-, ir-, fer-, pourr-, verr-, viendr-</li>'
    '<li>Negative wraps the AUXILIARY: n’ai pas joué / ne vais pas jouer</li>'
    '<li>After quand/si (future meaning) → French uses the FUTURE</li>'
    '<li>Markers: hier/la semaine dernière → PC · d’habitude → present · quand j’étais petit → imparfait · demain → futur</li>'
    '</ul>' + END +

    SEC('🗺️ In the Exam') +
    '<p>The 90-word task and 150-word task both award marks for <strong>time frames</strong>: the highest bands '
    'require past AND future AND opinions, not just accurate present. Plan two sentences per required time frame '
    'BEFORE writing. In speaking (photo card and conversation), the same three-tense habit earns the communication '
    'marks: “J’ai fait… je fais… je vais faire…” answers almost any question about free time, holidays or school trips.</p>' + END +

    SEC('⚠️ Common Errors') +
    '<ul>'
    '<li><span class="wrong">Wrong: je ai joué</span> <span class="right">Correct: j’ai joué (elision before a vowel)</span></li>'
    '<li><span class="wrong">Wrong: elle a allé au cinéma</span> <span class="right">Correct: elle est allée (être verb + agreement)</span></li>'
    '<li><span class="wrong">Wrong: je n’ai joué pas</span> <span class="right">Correct: je n’ai pas joué</span></li>'
    '<li><span class="wrong">Wrong: quand j’ai dix-huit ans, je passerai…</span> <span class="right">Correct: quand j’aurai dix-huit ans… (future after quand)</span></li>'
    '<li><span class="wrong">Wrong: je vais aller à la piscine le week-end passé</span> <span class="right">Correct: je suis allé à la piscine le week-end dernier (past time = past tense)</span></li>'
    '</ul>' + END +

    SEC('🎯 Exam Tips') +
    '<ul>'
    '<li>Plan tense-by-tense before writing any 90/150-word answer: one past, one present, one future line</li>'
    '<li>Learn 4 irregular past participles per week — été, fait, pris, vu cover most answers</li>'
    '<li>Imparfait for « c’était » opinions about the past: c’était génial / c’était barbant</li>'
    '<li>Mix futur proche (safe) with ONE futur simple (impressive)</li>'
    '<li>Check agreement every time a être-verb or reflexive has a feminine/plural subject</li>'
    '</ul>' + END
)

P2 = (
    SEC('📋 Key Concepts: Articles and Agreement') +
    '<p>French nouns carry GENDER (masculine/feminine) and NUMBER (singular/plural), and every article and '
    'adjective must agree with them. Master four article sets and the agreement rules, and accuracy across '
    'all four skills improves immediately.</p>' +
    TBL([
        ['','Masculine','Feminine','Plural','Before vowel (m/f)'],
        ['the (definite)','le','la','les','l’'],
        ['a/an (indefinite)','un','une','des','un/une'],
        ['some (partitive)','du','de la','des','de l’'],
        ['my / your / his-her','mon','ma','mes','mon (mon ami(e))'],
    ]) +
    '<p>Contractions are compulsory: <strong>à + le → au</strong> (au cinéma), <strong>à + les → aux</strong> '
    '(aux États-Unis), <strong>de + le → du</strong> (du pain), <strong>de + les → des</strong>.</p>' +
    '<p>After a NEGATION, du/de la/des becomes <strong>de</strong>: <em>je mange du pain</em> → '
    '<em>je ne mange pas de pain</em>. (But definite articles survive: <em>j’aime le sport → je n’aime pas le sport.</em>)</p>' + END +

    SEC('📝 Adjective Agreement') +
    '<p>Regular feminine: +<strong>e</strong> (grand → grande); regular plural: +<strong>s</strong> '
    '(grands, grandes). Four common patterns:</p>' +
    TBL([
        ['Masculine','Feminine','Plural (m/f)','Meaning'],
        ['sportif','sportive','sportifs / sportives','sporty'],
        ['généreux','généreuse','généreux / généreuses','generous'],
        ['actif','active','actifs / actives','active'],
        ['beau (bel)','belle','beaux / belles','beautiful'],
        ['vieux (vieil)','vieille','vieux / vieilles','old'],
        ['nouveau (nouvel)','nouvelle','nouveaux / nouvelles','new'],
    ]) +
    '<p><strong>Position:</strong> most adjectives FOLLOW the noun (un film intéressant). A small set go BEFORE '
    'the noun — beauty, age, good/bad, size (<strong>BAGS</strong>: beau, joli, vieux, nouveau, bon, mauvais, '
    'grand, petit, gros).</p>' + END +

    SEC('📝 Comparatives and Superlatives') +
    '<p><strong>plus / moins / aussi … que</strong> for comparisons: <em>le foot est plus populaire que le tennis</em>. '
    'Superlative: <strong>le/la/les plus</strong> (+ adjective): <em>c’est le plus important</em>. '
    'Two irregulars: <strong>bon → meilleur (le meilleur)</strong> but <strong>bien → mieux (le mieux)</strong> — '
    'meilleur qualifies nouns, mieux qualifies verbs: <em>ce livre est meilleur</em> vs <em>je joue mieux</em>.</p>' + END +

    SEC('🧮 Worked Examples — Exam Style') +
    '<div class="example"><p><strong>Translate: “My old school is bigger than my new school but the canteen is worse.”</strong></p>'
    '<p>« Mon vieux collège est plus grand que mon nouveau collège mais la cantine est pire. »</p>'
    '<p><em>Old/new BEFORE the noun (BAGS), plus…que comparison, irregular superlative pire. '
    'Adjective position errors are among the most common accuracy-mark losses.</em></p></div>'
    '<div class="example"><p><strong>Correct the errors: « Je n’aime pas le du fromage et je porte des vieux vêtements. »</strong></p>'
    '<p>« Je n’aime pas <strong>le</strong> fromage (definite article survives negation when expressing a liking) — '
    'but with du: « je ne mange pas <strong>de</strong> fromage ». And « je porte de <strong>vieux</strong> '
    'vêtements » — vieux already ends in -s? No: des + vieux → « de vieux vêtements »? Standard: '
    '« je porte de vieux vêtements » (des → de before adjective + noun).</p>'
    '<p><em>Two rules tested: negation with partitives, and des → de before a plural adjective + noun '
    '(une règle que les correcteurs adorent tester).</em></p></div>' + END +

    SEC('❓ Practice Questions') +
    '<div class="practice-questions">' +
    Q(1,'Give the correct article: « Je mange ___ pommes chaque jour. » (some)') +
    Q(2,'Negative: « Il boit ___ ___ limonade. » (doesn’t drink any)') +
    Q(3,'Agree the adjective: « Mes sœurs sont très (sportif) ___ . »') +
    Q(4,'Contract: « Je vais ___ (à + les) États-Unis en été. »') +
    Q(5,'Comparative: « Le rugby est ___ (dangerous) ___ le foot. »') +
    Q(6,'Superlative (good): « C’est ___ restaurant de la ville. »') +
    '</div>' + END +

    SEC('✅ Answers') +
    '<ol>'
    '<li>des pommes</li>'
    '<li>Il ne boit pas de limonade.</li>'
    '<li>sportives (feminine plural)</li>'
    '<li>aux États-Unis</li>'
    '<li>plus dangereux que le foot</li>'
    '<li>le meilleur restaurant</li>'
    '</ol>' + END +

    SEC('📌 Key Facts to Memorise') +
    '<ul>'
    '<li>à + le = au · à + les = aux · de + le = du · de + les = des · à/de + la = no change</li>'
    '<li>Negation: du/de la/des → de (but le/la/les stay)</li>'
    '<li>des → de before a plural adjective + noun (de vieux livres)</li>'
    '<li>BAGS adjectives go BEFORE the noun; everything else after</li>'
    '<li>bon → meilleur (nouns) · bien → mieux (verbs) · mauvais → pire</li>'
    '<li>mon/ton/son become mon/ton/son before feminine nouns starting with a vowel (mon amie)</li>'
    '</ul>' + END +

    SEC('🗺️ In the Exam') +
    '<p>Accuracy of agreement decides the <strong>communication marks</strong> in the 90/150-word tasks: '
    'a wrong gender article can obscure meaning (« une problème »). Quick self-check routine before moving on: '
    '(1) every noun — did I pick le/la correctly? (2) every describing word — does it end the way the noun '
    'demands? (3) any à/de next to le/les — contracted? In speaking, agreement errors cost less than tense '
    'errors — prioritise verbs first, then agreement.</p>' + END +

    SEC('⚠️ Common Errors') +
    '<ul>'
    '<li><span class="wrong">Wrong: je n’aime pas des légumes</span> <span class="right">Correct: je n’aime pas les légumes (liking + definite article)</span></li>'
    '<li><span class="wrong">Wrong: une problème intéressante</span> <span class="right">Correct: un problème intéressant (problème is masculine)</span></li>'
    '<li><span class="wrong">Wrong: les sals sportives? — les filles sportives ✓ / il est plus mieux</span> <span class="right">Correct: il est meilleur (nouns take meilleur, not mieux)</span></li>'
    '<li><span class="wrong">Wrong: mon petite sœur</span> <span class="right">Correct: ma petite sœur (agreement with the NOUN, not the owner)</span></li>'
    '</ul>' + END +

    SEC('🎯 Exam Tips') +
    '<ul>'
    '<li>Learn nouns WITH their article (le vélo, la voiture) — gender is then free</li>'
    '<li>Keep a personal top-5 agreement errors list and check it in the last 2 minutes of writing tasks</li>'
    '<li>Use plus…que at least once per writing task — it is a complex-structure mark at Higher</li>'
    '<li>For photo-card descriptions: colour adjectives (vert(e), brun(e)) give free agreement practice</li>'
    '</ul>' + END
)

if __name__ == "__main__":
    PAGES = [
        ("FR25-tenses-present-perfect-imperfect-and-future",
         "French Tenses: Present, Perfect, Imperfect and Future",
         "Master the four core GCSE French tenses: present, passé composé, imparfait, futur proche and futur simple — formation, time markers, and 90/150-word exam technique.",
         P1),
        ("FR26-articles-adjectives-and-agreement",
         "French Articles, Adjectives and Agreement",
         "Definite, indefinite and partitive articles, contractions (au, du, aux), adjective agreement and position, comparatives and superlatives — with exam technique.",
         P2),
    ]
    out = sys.argv[1] if len(sys.argv) > 1 else 'topics/french/aqa'
    for slug, title, desc, body in PAGES:
        html = build(slug, title, desc, body)
        open(f'{out}/{slug}.html', 'w', encoding='utf-8').write(html)
        print('wrote', f'{out}/{slug}.html', len(html), 'bytes')
