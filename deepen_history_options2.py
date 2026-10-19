#!/usr/bin/env python3
"""Second deepening layer: case-study focus + extended answer plan per option topic."""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from expand_topics import insert_before_section

CS = lambda t, b: (f'<section class="section">\n<h2>🔬 Case Study Focus — {t}</h2>\n{b}\n</section>')
PLAN = lambda q, body: (f'<section class="section">\n<h2>✍️ Extended Answer Plan — {q}</h2>\n{body}\n</section>')

D = {}

D["N41-establishing-control-castles-and-harrying"] = [
    CS("William of Warenne and Castle Acre", (
        '<p>Castle Acre (Norfolk) shows the complete Anglo-Norman pattern: Warenne, one of the richest '
        'tenants-in-chief, built castle, Cluniac priory (from Lewes, 1089) and planned town TOGETHER — '
        'military power, spiritual legitimacy and commerce in one complex. The castle\u2019s earthworks '
        '(massive motte, twin baileys) survive; the priory ruins show the wealth of the new elite. '
        'Use it for any "how did the Normans control East Anglia" question: control was land + church + '
        'market acting together, not castles alone.</p>')),
    PLAN('"The main reason for peasant submission was fear of Norman violence." How far do you agree? (16 + 4)', (
        '<p><strong>FOR:</strong> the harrying (1069–70) was recent memory; murdrum and forest law criminalised '
        'normal life; castles garrisoned by mounted knights could reach any village in a day.</p>'
        '<p><strong>AGAINST:</strong> peasants submitted to LANDLORDS daily, not to knights; the Church taught '
        'obedience as duty; harvest rhythms bound people harder than any garrison; the Danelaw\u2019s sokemen '
        'bargained rents instead of fighting.</p>'
        '<p><strong>Judgement:</strong> fear worked at the elite level (no leaders to follow); at village level, '
        'custom and faith delivered obedience more cheaply than violence. Conclude: violence cowed the mighty, '
        'structure absorbed the many.</p>')),
]

D["N42-feudalism-government-and-law"] = [
    CS("The 1086 Salisbury Oath in Context", (
        '<p>Anglo-Saxon England had no direct oath of ALL landholders to the king — homage flowed to immediate '
        'lords only. William\u2019s Salisbury summons (1 August 1086) gathered bishops, abbots and every tenant '
        'holding "of the king" and took their oath personally. The Old English Chronicle calls it a council where '
        '"they all submitted to him and became his men". Why it mattered: it prevented the Frankish pattern of '
        'castellans building private power; it made rebellion against a lord treason against the king. '
        'It was possible BECAUSE Domesday had just priced every holding — information made oath-taking '
        'enforceable. Link: oath → Domesday → forest law as one system of recorded, personal royal power.</p>')),
    PLAN('"Norman government strengthened Anglo-Saxon institutions rather than replacing them." How far do you '
         'agree? (16 + 4)', (
        '<p><strong>STRENGTHENED:</strong> shire/hundred courts continued under new sheriffs; the geld and '
        'writs became MORE efficient; coinage better controlled; the Church kept parish structure.</p>'
        '<p><strong>REPLACED:</strong> earldoms broken up; English aristocracy removed (5% land); murdrum/forest '
        'introduced; trial by combat added; writs standardised under Lanfranc\u2019s chancery habits.</p>'
        '<p><strong>Judgement:</strong> the INSTITUTIONS were strengthened precisely because their personnel '
        'and purposes were revolutionised — continuity of form masked a rupture of function. Finish with the '
        'phrase: "William conquered England with England\u2019s own machinery".</p>')),
]

D["N43-domesday-economy-and-towns"] = [
    CS("York in Domesday", (
        '<p>York shows the conquest\u2019s full arc in one city: two castles (Clifford\u2019s Tower motte built '
        '1068, rebuilt 1069 after the massacre of its garrison), the harrying\u2019s "waste" entries (529 empty '
        'houses in one entry), Jewish settlement from the 1170s (the 1190 Clifford\u2019s Tower massacre came '
        'later), and the Minster rebuilt in Norman stone. Domesday lists York\u2019s seven shires, mills and '
        'churches with 1066-vs-1086 values — the survey\u2019s evidence in miniature. Exam use: York answers '
        '"change over time" questions with named, datable evidence.</p>')),
    PLAN('"The Domesday survey shows the Normans ruled by information as much as by force." How far do you '
         'agree? (16 + 4)', (
        '<p><strong>INFORMATION:</strong> juries, standardised valuations, ownership records — the first European '
        'state database; tax justice and dispute settlement followed from records.</p>'
        '<p><strong>FORCE:</strong> the survey was itself an imposition (the Chronicle\u2019s "shame" quote); '
        'its data enabled harsher geld; "waste" entries normalised devastation as bookkeeping.</p>'
        '<p><strong>Judgement:</strong> force made the survey possible; information made conquest PERMANENT. '
        'The strongest answers note that a castle was only as useful as the tax roll that paid its garrison.</p>')),
]

D["N44-village-life-and-peasants"] = [
    CS("The Slave Trade's Quiet End", (
        '<p>Domesday records ~28,000 slaves (10% of the population) — Bristol\u2019s trade shipping English '
        'slaves to Ireland was notorious (Wulfstan\u2019s sermons against it). Within a generation the class '
        'vanishes from records: the Church\u2019s pressure (a slave could be ordained — awkward for masters), '
        'economic logic (villeins with land ties worked harder than owned labour), and the Norman elite\u2019s '
        'preference for customary dues over ownership. Exam use: the ONE clear social IMPROVEMENT in the '
        'period — deploy it as the counter-weight in "Norman rule was purely oppressive" essays.</p>')),
    PLAN('"For ordinary people the Norman Conquest changed less than historians claim." How far do you agree? '
         '(16 + 4)', (
        '<p><strong>LESS:</strong> same fields, same saints, same manor courts; lords were distant; three-field '
        'farming spread on its own logic; English survived as the spoken tongue.</p>'
        '<p><strong>MORE:</strong> the lord\u2019s language and law changed overnight; forest law criminalised '
        'hunting; dues rose (merchet, heriot); castles took land and labour; 1086\u2019s slaves were freed while '
        '1086\u2019s villeins were fixed tighter.</p>'
        '<p><strong>Judgement:</strong> measure "change" by the FREQUENCY of contact: peasants met stewards, '
        'not kings — so daily life changed least; but the FEW points of contact (court, dues, church) were all '
        'in Norman hands. Verdict: the conquest re-wired the top; the village felt the rewiring only at the '
        'junctions.</p>')),
]

D["N45-town-life-trade-and-jews"] = [
    CS("The Jew's House, Lincoln", (
        '<p>One of the earliest surviving stone town houses in England (c1170–80), built by a Jewish financier '
        'on the Steep Hill below the castle and cathedral — Norman Jews lived in stone beside the institutions '
        'their credit built. Aaron of Lincoln\u2019s estate (died 1186) was so large the crown created a special '
        'department (the Aaron\u2019s Exchequer) to collect it. Exam use: the house is physical evidence of the '
        'protection-exploitation duality — permanent stone, precarious people. Pair with the archa (royal debt '
        'chest) and the 1290 expulsion to show the arc.</p>')),
    PLAN('"Norman towns were built for Norman purposes." How far do you agree? (16 + 4)', (
        '<p><strong>FOR:</strong> castles sited over mints and crossings; French borough quarters; markets '
        'licensed by the king; Jews invited for royal finance.</p>'
        '<p><strong>AGAINST:</strong> English merchants kept their churches and customs; boroughs grew from '
        'Anglo-Saxon burhs (Norwich, York pre-date the Normans); guild self-government grew English civic '
        'identity.</p>'
        '<p><strong>Judgement:</strong> Norman PURPOSE, English PRACTICE — the plans were Norman; the life '
        'inside them became English again within two generations. Note the growth statistics: ~100 boroughs '
        'by 1086, many more chartered by 1200.</p>')),
]

D["N46-church-monasticism-and-lanfranc"] = [
    CS("Durham: Castle, Cathedral and the North", (
        '<p>Durham\u2019s peninsula — river on three sides — holds castle (1072) and cathedral (1093) side by '
        'side: the message needs no words. The cathedral pioneered rib-vaulting and massive geometric pillars '
        '(Europe\u2019s first Gothic experiment) — Norman engineering at its peak. Its bishops were '
        '<strong>prince-bishops</strong> (palatinate powers: their own sheriffs, courts and coinage) ruling a '
        'troubled frontier. Exam use: Durham answers military, spiritual AND administrative questions — '
        'one site, three functions, all datable.</p>')),
    PLAN('"The Norman Church served the conqueror more than God." How far do you agree? (16 + 4)', (
        '<p><strong>CONQUEROR:</strong> English bishops replaced; cathedral-castle siting; Stigand\u2019s '
        'deposition as conquest-legitimacy; William\u2019s appointments control.</p>'
        '<p><strong>GOD:</strong> genuine Gregorian reform (celibacy, simony); monastic learning and the '
        'Constitutions; tithe-funded charity; Anselm\u2019s willingness to exile himself for principle.</p>'
        '<p><strong>Judgement:</strong> separate the INSTRUMENT (the Church as government partner) from the '
        'FAITH (real reform ideals). Conclude: Lanfranc served two masters and believed he was serving one — '
        'the ambiguity is the answer.</p>')),
]

D["N47-norman-architecture-historic-environment-castles"] = [
    CS("Rochester Castle (1127): The Keep as Textbook", (
        '<p>Rochester\u2019s great tower (1127, built for the Archbishop by Gundulf\u2019s successor William '
        'de Corbeil) is the best-documented study keep: 113ft high, walls 12ft thick at the base, cross-wall '
        'dividing it (each half independently defensible), well shaft in the forebuilding\u2019s depth, chapel '
        'on the second floor, entrance via a forebuilding with a chapel above the gate passage. It survived '
        'the 1215 siege (mined south-east tower propped with timber props) — later rebuilt HALF round. '
        'Every feature answers the exam question "what does this feature show?" — defence (cross-wall, '
        'first-floor entry), status (chapel, Caen-quality stonework), date (round-arched Romanesque '
        'windows).</p>')),
    PLAN('"Norman castles were as much symbols as fortresses." How far do you agree? (16 + 4)', (
        '<p><strong>FORTRESS:</strong> siting, sight-lines, garrisons, wells; motte-and-bailey\u2019s speed '
        'was a military choice; Rochester\u2019s cross-wall and thick base are pure defence.</p>'
        '<p><strong>SYMBOL:</strong> height over necessity (White Tower); cathedral-castle pairing; the keep '
        'visible for miles = "we are here forever"; coins and seals show castles as royal iconography.</p>'
        '<p><strong>Judgement:</strong> function and symbolism were the same decision — a castle that could '
        'not be seen deterred nobody. Conclude: Norman architecture "spoke" power; the exam answer shows the '
        'feature does both jobs at once.</p>')),
]

D["A40-plains-indians-way-of-life"] = [
    CS("The Sun Dance and the Sacred Circle", (
        '<p>The annual Sun Dance (summer, when bands gathered): a circular lodge around a sacred cottonwood '
        'pole; dancers faced the sun for days without food or water; some pierced their chest muscles with '
        'skewers (Sun Dance piercing) as sacrifice for visions — personal suffering for the people\u2019s '
        'renewal. Everything about the ritual encoded the worldview: the circle, Wakan Tanka\u2019s presence '
        'in all things, the primacy of the collective over the individual. The US government banned the '
        'Sun Dance (and -piercing) in the 1880s as part of assimilation — banning a CEREMONY was an attempt '
        'to kill a worldview. Exam use: the ban is the perfect evidence that Washington understood the '
        'culture\u2019s strength lay in its beliefs, not just its warriors.</p>')),
    PLAN('"Plains Indian life was shaped by the buffalo more than by religion." How far do you agree? '
         '(16 + 4)', (
        '<p><strong>BUFFALO:</strong> every material need (food, tipi, clothing, tools, fuel); the hunt '
        'structured the calendar, the band and the warfare.</p>'
        '<p><strong>RELIGION:</strong> the buffalo WAS sacred (Wakan Tanka\u2019s gift); the Sun Dance, circles, '
        'visions and counting coup shaped law, honour and identity — immaterial but organising.</p>'
        '<p><strong>Judgement:</strong> the buffalo shaped HOW they lived; religion explained WHY — and the '
        'White assault on both (hide hunting + Sun Dance ban) proves the two were inseparable. Conclude: '
        'separating them is the settlers\u2019 mistake; the strongest answers refuse it.</p>')),
]

D["A41-homesteaders-and-the-railroads"] = [
    CS("The Exodusters in Kansas (1879)", (
        '<p>In 1879 thousands of black sharecroppers left Mississippi, Louisiana and Tennessee for Kansas — '
        "Benjamin \u2018Pap\u2019 Singleton\u2019s Exodus — fleeing Reconstruction\u2019s collapse, Jim Crow "
        'violence and the 1878 yellow-fever epidemics. ~15,000–20,000 arrived; some founded all-black towns '
        '(Nicodemus, 1877). The St Louis mayor tried to block the steamboats; Kansas\u2019s governor, John St '
        'John, welcomed them. Exam use: the Exodusters prove the Homestead Act\u2019s promise cut across race, '
        'BUT their harder credit and harsher town reception show the West\u2019s limits — pair with the fact '
        'that the Plains\u2019 160-acre units assumed eastern rainfall.</p>')),
    PLAN('"Federal policy was the most important reason the Plains were settled." How far do you agree? '
         '(16 + 4)', (
        '<p><strong>FEDERAL:</strong> Homestead Act 1862; Pacific Railway Act (land grants); army protection; '
        'treaty-breaking that cleared Native title.</p>'
        '<p><strong>OTHER:</strong> Manifest Destiny ideology (the motive), railroad companies\u2019 advertising '
        'and credit (the mechanism), European immigration and Exodusters (the people), barbed wire/windmills '
        '(the survival kit).</p>'
        '<p><strong>Judgement:</strong> federal policy WROTE the rules; railroads and technology played the '
        'game. Conclude: policy without railroads settles nothing; railroads without policy settle nothing '
        'legally — argue the partnership and give the last word to the mechanism (trains move people).</p>')),
]

D["A42-cattle-industry-and-open-range"] = [
    CS("Dodge City: Law, Order and the Myth Machine", (
        '<p>Dodge City (1872–85) was the Queen of the Cow Towns: 5,000 people at peak, the Santa Fe Railroad, '
        '15 saloons and 19 licensed brothels in its heyday. Marshals Bat Masterson and Wyatt Earp enforced an '
        'ordinance DISARMING visitors north of the railroad tracks — the famous OK-Corral-style violence was '
        'rare: Dodge recorded ~15 killings in 15 years, mostly in the south-side brothel district. The myth '
        '(dime novels, later Hollywood) outgrew the reality; exam use: Dodge answers "law and order" questions '
        'with the paradox that the frontier\u2019s wildest town was tamed by ORDINANCES, not gunfights — and '
        'the cattle trade funded the civilisation that ended it.</p>')),
    PLAN('"The open range ended because of natural causes, not human ones." How far do you agree? (16 + 4)', (
        '<p><strong>NATURAL:</strong> the Big Die-Up (1886–87) killed up to 90% of some herds; the 1886 drought '
        'starved overstocked ranges.</p>'
        '<p><strong>HUMAN:</strong> overstocking itself (2m head); barbed wire (1874) cut trails; homesteaders '
        'ploughed the range; railroads reached Texas making drives pointless; Johnson County War (1892) = '
        'ranchers\u2019 last stand against homesteaders.</p>'
        '<p><strong>Judgement:</strong> the winter was the TRIGGER, but human overstocking (greed) made herds '
        'fragile and fences made the range unnatural. Conclude: nature rang the bell on a system humans had '
        'already broken.</p>')),
]

D["A43-conflict-reservations-and-wounded-knee"] = [
    CS("Wounded Knee, 29 December 1890", (
        '<p>The 7th Cavalry (Custer\u2019s old regiment) escorted ~350 Lakota — mostly Big Foot\u2019s '
        'Miniconjou, many sick with pneumonia, fleeing after Sitting Bull\u2019s killing — to Wounded Knee '
        'Creek. The army positioned four Hotchkiss rapid-fire guns on the ridge; a scuffle over a rifle '
        '(Black Coyote, deaf, refusing to surrender it) triggered the massacre: ~250–300 Lakota men, women '
        'and children killed in minutes; 25 soldiers died (mostly friendly fire). Bodies frozen in a mass '
        'grave dug by the escort. Congress awarded 20 Medals of Honor. Exam use: Wounded Knee answers '
        '"the end of the Plains wars" with the full policy arc — Ghost Dance panic + Sitting Bull\u2019s '
        'death + army fear = the massacre that ended armed resistance with the murder of the unarmed.</p>')),
    PLAN('"The Dawes Act 1887 was the most destructive measure in Plains Indian history." How far do you '
         'agree? (16 + 4)', (
        '<p><strong>DAWES:</strong> allotment (160 acres/family) legally dissolved tribal land-holding; '
        '"surplus" sold — two-thirds of reservation land lost by 1934; it attacked the COMMUNAL idea that '
        'was the culture\u2019s core.</p>'
        '<p><strong>OTHERS:</strong> buffalo destruction (starvation); Sand Creek/Wounded Knee (terror); '
        'boarding schools (children); the 1876 Black Hills seizure (sacred land).</p>'
        '<p><strong>Judgement:</strong> the Dawes Act was the QUIETEST and most complete destruction — it '
        'did not kill people but dissolved the legal and spiritual basis of their society. Conclude: bullets '
        'killed warriors; paper killed nations.</p>')),
]

D["R40-tsarist-russia-and-the-1905-revolution"] = [
    CS("Stolypin's Necktie and the Wager on the Strong", (
        '<p>Pyotr Stolypin (PM 1906–11) ran repression and reform as one policy: field courts-martial hanged '
        '~3,800 in 18 months ("Stolypin\u2019s necktie" — the noose); meanwhile his agrarian reform let '
        'peasants leave the mir, consolidate strips into single farms (khutors) and buy land through the '
        'Peasant Bank — the "wager on the strong": create a loyal kulak class. By 1914 ~2m households had '
        'left the mir (10–15%); the rest stayed. He was shot at Kiev opera house (September 1911, in front '
        'of Nicholas II — by a double agent, Bogrov). Exam use: Stolypin answers "could the Tsar have survived?" '
        '— his reforms MIGHT have modernised autocracy, but the war interrupted and the Terror discredited '
        'the man delivering them.</p>')),
    PLAN('"The 1905 Revolution changed nothing." How far do you agree? (16 + 4)', (
        '<p><strong>CHANGED NOTHING:</strong> the Fundamental Laws restored autocracy; Stolypin\u2019s coup '
        '(1907) reversed the franchise; repression increased.</p>'
        '<p><strong>CHANGED MUCH:</strong> the Duma existed (a forum never before allowed); trade unions and '
        'a free press briefly legal; Stolypin\u2019s land reform began; the Tsar\u2019s sacred image never '
        'recovered; the parties and Soviets of 1905 were the machinery of 1917.</p>'
        '<p><strong>Judgement:</strong> constitutionally nothing, politically everything — 1905 taught both '
        'sides the lessons they used in 1917. Conclude: 1905 was the dress rehearsal whose script 1917 '
        'improved.</p>')),
]

D["R41-1917-february-october-and-dual-power"] = [
    CS("Order No. 1 and the Collapse of Authority", (
        '<p>The Petrograd Soviet\u2019s Order No. 1 (1 March 1917) — issued without the Provisional '
        'Government\u2019s knowledge — ordered soldiers to obey the Soviet, elect committees, keep weapons, '
        'and salute only off-duty. It was the death warrant of army discipline: desertion rose (2m by winter), '
        'officers shot by their men, the June offensive collapsed. Exam use: Order No. 1 proves dual '
        'power was UNWORKABLE from day one — two sovereignties, one army. It also explains the Bolsheviks\u2019 '
        'October ease: by autumn the government commanded almost nothing and the Soviets everything.</p>')),
    PLAN('"The Bolsheviks seized power in October because the Provisional Government had destroyed itself." '
         'How far do you agree? (16 + 4)', (
        '<p><strong>PG SELF-DESTRUCTION:</strong> war continuation (April crisis), land delay (peasant '
        'seizures), elections postponed, Kornilov panic, food collapse; by October the PG commanded nothing.</p>'
        '<p><strong>BOLSHEVIK ACTION:</strong> Lenin\u2019s April Theses re-armed the party; Trotsky\u2019s MRC '
        'organised the seizure; slogans answered each PG failure directly; the party grew (24,000 Feb → '
        '240,000 Oct).</p>'
        '<p><strong>Judgement:</strong> the PG dug the grave; the Bolsheviks jumped in with a programme. '
        'Conclude: opportunity + organisation = revolution — neither alone suffices; weight your verdict '
        'toward the PG\u2019s suicide but credit the seizure\u2019s professionalism.</p>')),
]

D["R42-civil-war-war-communism-and-nep"] = [
    CS("The Kronstadt Rebellion (March 1921)", (
        '<p>The sailors of Kronstadt — the fortress island guarding Petrograd, heroes of 1917 ("the reddest '
        'of the red") — rose against War Communism: for re-elected soviets, free speech for socialists, '
        'release of political prisoners, an end to requisitioning. Tukhachevsky stormed the ice fortress '
        'with 60,000 troops across frozen Gulf ice (7–18 March); ~10,000 casualties; survivors shot or sent '
        'to the first gulags. Lenin called it "the flash that lit up reality better than anything else" — '
        'the NEP was announced days later at the same Party Congress. Exam use: Kronstadt proves War '
        'Communism had broken the regime\u2019s own base — the most persuasive single piece of evidence for '
        'any "War Communism failed" essay.</p>')),
    PLAN('"The NEP betrayed the Revolution." How far do you agree? (16 + 4)', (
        '<p><strong>BETRAYAL:</strong> private trade and NEPmen restored capitalism; kulaks grew rich; '
        'socialist ideals abandoned; Bukharin\u2019s "enrich yourselves" scandalised purists.</p>'
        '<p><strong>SAVED IT:</strong> production recovered to 1913 levels by 1926; famine ended; the party '
        'survived (Kronstadt proved the alternative was collapse); Lenin called it a "retreat to take two '
        'steps back for one forward".</p>'
        '<p><strong>Judgement:</strong> the NEP saved the revolution\u2019s STATE while betraying its '
        'ECONOMY — and the party never forgave it (Stalin ended it in 1929). Conclude: betrayal of theory, '
        'loyalty to survival — argue the party chose survival, proving what it really valued.</p>')),
]

D["R43-stalin-collectivisation-plans-and-terror"] = [
    CS("Magnitogorsk: Building Socialism on the Steppe", (
        '<p>The magnet mountain: a purpose-built steel city rising from 1929 — 25,000 arrivals a month, '
        'barracks and mud, foreign engineers (Ford built the car plant), Stakhanovite heroics, totalitarian '
        'planning. By 1934 Magnitka produced more steel than all Tsarist Russia. Living conditions: queues, '
        'lice, criminal chaos — then proper blocks for the elite. John Scott\u2019s memoir (Behind the Urals) '
        'records the heroism AND the horror. Exam use: Magnitogorsk answers "did the plans succeed?" with '
        'industrial triumph + human cost in one place — the two-sided verdict in a single city.</p>')),
    PLAN('"Stalin\u2019s economic policies transformed the USSR by 1939." How far do you agree? (16 + 4)', (
        '<p><strong>TRANSFORMED:</strong> second-largest industrial power; steel/oil/electricity tripled; '
        'the Dnieper dam and new industrial cities; no unemployment (the West\u2019s Depression contrast); '
        'tractor/tank capacity that beat Hitler.</p>'
        '<p><strong>AT WHAT COST:</strong> collectivisation\u2019s famine (5–7m); consumption collapsed; '
        'labour camps (Belomor Canal, ~25,000 deaths); falsified statistics; consumer goods catastrophic.</p>'
        '<p><strong>Judgement:</strong> define "transformed" — the economy changed beyond recognition; the '
        'PEOPLE paid the entire bill. Conclude: transformation and terror were the same policy — the plans '
        'were built on the famine and the camps.</p>')),
]

D["C40-origins-of-the-cold-war-1945-49"] = [
    CS("Czechoslovakia, February 1948: The Last Democracy Falls", (
        '<p>Czechoslovakia was the one Eastern European democracy with genuine multiparty politics and a '
        'pro-Western public. Gottwald\u2019s communists (38% vote, 1946) took power by SALAMI TACTICS then '
        'finished it: armed workers\u2019 militias, police purges, the non-communist ministers\u2019 '
        'resignations trapped by their own tactics, and armed action on 25 February. Jan Masaryk\u2019s '
        'window death (10 March) marked the end. Truman pushed the Marshall Plan through Congress in WEEKS; '
        'the West\u2019s lesson: containment needed alliances (NATO, April 1949). Exam use: Czechoslovakia is '
        'the coup that converted US public opinion — the Cold War\u2019s point of no return for many '
        'Americans.</p>')),
    PLAN('"Stalin was more to blame than Truman for the Cold War." How far do you agree? (16 + 4)', (
        '<p><strong>STALIN:</strong> broke the Yalta promise (Polish elections); salami tactics; rigged '
        'Czechoslovakia; the blockade as first military move; Cominform discipline.</p>'
        '<p><strong>TRUMAN:</strong> the atomic monopoly as diplomacy; doctrine of permanent confrontation; '
        'Marshall Aid as economic containment that Stalin could not accept; NATO\u2019s alliance.</p>'
        '<p><strong>STRUCTURALISTS:</strong> two superpowers, one ideological planet — conflict was baked in; '
        'personalities only timed it.</p>'
        '<p><strong>Judgement:</strong> Stalin\u2019s actions were the provocations; Truman\u2019s responses '
        'were escalations in kind. Conclude: "more to blame" is the wrong question — but the FIRST '
        'unprovoked move (Czechoslovakia, the blockade) weighs on Stalin\u2019s side.</p>')),
]

D["C41-hungary-1956-and-the-berlin-wall-1961"] = [
    CS("Peter Fechter and the Wall's Arithmetic", (
        '<p>17 August 1962: 18-year-old Peter Fechter, shot in the pelvis trying to cross near Checkpoint '
        'Charlie, bled to death over an hour in the death strip while guards on both sides refused to help '
        '(East: orders; West: shots kept rescuers back). The photo went round the world; "Ihr Mörder!" '
        '(your murderers) chants met the Western garrison. At least 140 killed at the Wall over 28 years. '
        'Exam use: Fechter humanises the Wall\u2019s arithmetic — 3m emigrants before 1961, ~140 deaths after '
        '— the Wall SOLVED the GDR\u2019s demographic crisis by killing individuals; that trade-off is the '
        'essay\u2019s heart.</p>')),
    PLAN('"Khrushchev handled both the Hungarian uprising and the Berlin Wall badly." How far do you agree? '
         '(16 + 4)', (
        '<p><strong>HUNGARY — badly:</strong> the invasion handed the West a propaganda gift for a generation; '
        'Nagy\u2019s execution martyred a communist; world communism fractured (Western communist parties '
        'left).</p>'
        '<p><strong>BERLIN — well (short term):</strong> the ultimatum failed but the Wall solved the '
        'emigration crisis overnight WITHOUT war; the GDR stabilised for 28 years.</p>'
        '<p><strong>Judgement:</strong> judge by objectives: Hungary = objective (keep the empire) achieved '
        'at huge reputational cost; Berlin = objective (stop the drain) achieved at small cost. Conclude: '
        'badly on paper, effectively in practice — the dilemma between propaganda and power is the essay.</p>')),
]

D["C42-cuban-missile-crisis-1962"] = [
    CS("Black Saturday, 27 October 1962", (
        '<p>The most dangerous day in human history, three times over: (1) Major Rudolf Anderson\u2019s U-2 '
        'shot down over Cuba (killed — against Khrushchev\u2019s standing order); (2) the B-59 Soviet '
        'submarine, depth-charged by US destroyers and out of contact, needed the two arming keys for a nuclear '
        'torpedo — Vasili Arkhipov (flotilla commander) refused consent; (3) a U-2 strayed over Siberia, '
        'fighters scrambled with nuclear air-to-air missiles. Kennedy: "there is always some sonofabitch who '
        'doesn\u2019t get the word". The same day, Kennedy answered Khrushchev\u2019s FIRST letter, ignored '
        'the second, and sent RFK to Dobrynin with the Jupiter trade. Exam use: Black Saturday converts '
        '"the crisis was dangerous" into evidence — three separate near-launches in one day.</p>')),
    PLAN('"Mutually Assured Destruction made the world safer." How far do you agree? (16 + 4)', (
        '<p><strong>SAFER:</strong> after Cuba, both sides built communication (hotline), agreements (test '
        'ban, non-proliferation) and restraint (quarantine not strike); no direct superpower war 1945–91.</p>'
        '<p><strong>MORE DANGEROUS:</strong> the arms race multiplied warheads (US 1967: 31,000); near-misses '
        '(1962; Able Archer 1983; Petrov 1983); proxies fought the hot wars (Korea, Vietnam, Afghanistan).</p>'
        '<p><strong>Judgement:</strong> MAD prevented superpower war while privatising violence to the Third '
        'World and gambling the species on command systems. Conclude: safer for Moscow and Washington, not '
        'necessarily for the planet — the exam\u2019s strongest two-sided verdict.</p>')),
]

D["C43-vietnam-detente-and-the-collapse"] = [
    CS("The Tet Offensive (January 1968): Defeat as Victory", (
        '<p>Militarily: the NVA/VC lost ~40,000 men, held no town, the uprising never came — a crushing '
        'military defeat. Politically: the offensive reached the US embassy grounds on live television; '
        'Johnson\u2019s credibility broke (Cronkite: "mired in stalemate"); LBJ declined re-election (31 '
        'March); Westmoreland requested 206,000 more troops and was refused. Exam use: Tet is the perfect '
        'evidence for "wars are won on television" — the perception gap between battlefield and broadcast '
        'decided the outcome; pair with the Pentagon Papers (1971) for credibility collapse.</p>')),
    PLAN('"The Cold War ended because the Soviet economy could not compete." How far do you agree? (16 + 4)', (
        '<p><strong>ECONOMY:</strong> 1960s–80s growth fell from 5% to stagnation; consumer shortages; '
        'the arms burden (~25% of GDP vs US ~6%); oil-price collapse (1986); SDI\u2019s technological threat '
        'to an economy that could not answer it.</p>'
        '<p><strong>GORBACHEV\u2019S CHOICES:</strong> glasnost legitimised criticism; perestroika destabilised '
        'planning; the unilateral cuts and the refusal to crush 1989 — decisions, not inevitabilities; '
        'Reagan\u2019s pressure only set the price.</p>'
        '<p><strong>Judgement:</strong> the economy made the USSR fragile; Gorbachev\u2019s choices made it '
        'fall apart peacefully. Conclude: structure loaded the gun; Gorbachev pulled the trigger on his own '
        'empire — the strongest answers refuse a single-cause verdict.</p>')),
]

if __name__ == "__main__":
    only = None
    if len(sys.argv) > 2:
        only = set(sys.argv[2].split(','))
    n = 0
    for f in glob.glob('topics/history/*/*.html'):
        base = os.path.basename(f)[:-5]
        if base not in D or (only and base not in only):
            continue
        h = open(f, encoding='utf-8').read()
        for sec_html in D[base]:
            m = re.search(r'<h2>([^<]+)</h2>', sec_html)
            t = m.group(1).split('—')[0].strip()
            if t in h:
                continue
            for anchor in ('🎯 Exam Tips', '⚠️ Common Errors', '🗺️ In the Exam'):
                h2, ok = insert_before_section(h, anchor, sec_html)
                if ok:
                    open(f, 'w', encoding='utf-8').write(h2)
                    n += 1
                    break
    print(f'sections injected: {n}')
