from .core import gaps, meanings, explicit, clauses, LESSONS, question
from .actions import ACTIONS
from .units021_050 import basic_contexts

advice_actions = ['mehr schlafen','regelmäßig üben','den Arzt anrufen','eine Pause machen','früher losfahren','den Vertrag lesen','die Rechnung prüfen','nachfragen','weniger arbeiten','einen Termin vereinbaren']
for action in advice_actions:
    LESSONS.setdefault(81, []).append(question(f'Ein Rat an einen Freund: Du ___ {action}. (sollen)', 'solltest',['musstest','solltestest','sollstet'],
        'Solltest is Konjunktiv II and presents a recommendation; it does not impose the force of musst.','Choose the tentative advice form.'))
    LESSONS[81].append(question(f'Ein vorsichtiger Vorschlag: Wir ___ {action}. (können)','könnten',['konnten','könntet','kann'],
        'Wir könnten offers a possible course of action as a tentative suggestion; konnten would refer to past ability.','Choose the tentative proposal form.'))

gaps(82, 'hätte|hättest|hätten|hättet|wäre|wärst|wären|wärt|könnte|könnten|würde|würden', """
Wenn ich mehr Zeit ___, würde ich üben. (haben)|hätte
Wenn du hier ___, könnten wir reden. (sein)|wärst
Wenn wir reich ___, würden wir reisen. (sein)|wären
Wenn ihr Urlaub ___, könntet ihr kommen. (haben)|hättet
Wenn er ein Auto ___, würde er fahren. (haben)|hätte
Wenn sie (Plural) Zeit ___, würden sie helfen. (haben)|hätten
Wenn ich gesund ___, könnte ich arbeiten. (sein)|wäre
Wenn du Geld ___, könntest du buchen. (haben)|hättest
Wenn ihr schon fertig ___, könnten wir gehen. (sein)|wärt
Wenn wir ein Haus ___, hätten wir Platz. (haben)|hätten
Mit mehr Zeit ___ ich jeden Tag lernen. (werden)|würde
Mit einem Auto ___ wir ans Meer fahren. (werden)|würden
Wenn ich das Wort wüsste, ___ ich antworten. (können)|könnte
Wenn wir frei hätten, ___ wir kommen. (können)|könnten
Wenn sie (Singular) hier ___, wäre es schöner. (sein)|wäre
Wenn wir früher da ___, hätten wir bessere Plätze. (sein)|wären
Wenn du ein Rad ___, könntest du mitfahren. (haben)|hättest
Wenn ich mehr Geld ___, würde ich sparen. (haben)|hätte
Wenn er mehr lernen würde, ___ er bessere Chancen. (haben)|hätte
Wenn wir näher wohnen würden, ___ wir öfter zu Besuch. (sein)|wären
""", "'{answer}' is the Konjunktiv II form agreeing with the subject; the condition and result describe an imagined situation rather than a stated fact.")

gaps(83, 'hätte|hättest|hätten|hättet|wäre|wärst|wären|wärt|würde|würdest|würden|würdet', """
Ich ___ gern mehr Zeit. (haben)|hätte
Du ___ gern schon zu Hause. (sein)|wärst
Wir ___ gern am Meer. (sein)|wären
Ihr ___ gern ein größeres Zimmer. (haben)|hättet
Sie (Singular) ___ gern einen Hund. (haben)|hätte
Ich ___ gern früher kommen. (werden)|würde
Du ___ gern mehr reisen. (werden)|würdest
Wir ___ gern länger bleiben. (werden)|würden
Ihr ___ gern weniger arbeiten. (werden)|würdet
Sie (Plural) ___ gern ein Haus. (haben)|hätten
Wenn ich doch frei ___! (sein)|wäre
Wenn du doch mehr Geduld ___! (haben)|hättest
Wenn wir doch schon fertig ___! (sein)|wären
Wenn ihr doch hier ___! (sein)|wärt
Wenn er doch mehr Glück ___! (haben)|hätte
___ ich doch zu Hause! (sein, Wunsch)|Wäre|Verb-first wäre plus doch expresses an unreal wish, not a request for information.
___ wir doch mehr Zeit! (haben, Wunsch)|Hätten|Hätten wir doch … is a verb-first wish clause with a plural subject.
Ich ___ gern ein ruhigeres Büro. (haben)|hätte
Wir ___ gern eine andere Wohnung. (haben)|hätten
Sie (Singular) ___ gern Ärztin. (sein)|wäre
""", "The Konjunktiv II form '{answer}', often with gern or doch, presents a desired situation rather than asserting that it is real.")

past_verbs = [('finden','fand'),('nehmen','nahm'),('geben','gab'),('sehen','sah'),('lesen','las'),('schreiben','schrieb'),('sprechen','sprach'),('rufen','rief'),('fahren','fuhr'),('gehen','ging'),('bleiben','blieb'),('bringen','brachte'),('denken','dachte'),('kennen','kannte'),('nennen','nannte'),('wissen','wusste'),('bemerken','bemerkte'),('öffnen','öffnete'),('warten','wartete'),('arbeiten','arbeitete')]
for inf,past in past_verbs:
    LESSONS.setdefault(84, []).append(question(f'Erzählform für er: {inf} → er ___',past,[inf,inf+'te',past+'st'],
        f"The third-person singular Präteritum of '{inf}' is '{past}'; use this simple past form in the narrative frame.",'Choose the third-person singular Präteritum.'))

for action in ACTIONS[:10]:
    patient,plural,part,inf,present,past,obj,zu=action
    LESSONS.setdefault(85, []).append(question(f'Als ich ankam, ___ Anna {obj} schon {part}. (Vorvergangenheit)', 'hatte',['hat','hätte','wird'],
        f"'{part}' happened before the past arrival; hatte plus participle forms the Plusquamperfekt of this transitive verb.",'Choose the auxiliary for the earlier past event.'))

for subject,part in [('ich','gegangen'),('er','angekommen'),('sie','eingeschlafen'),('wir','umgezogen'),('die Gäste','abgereist'),('das Kind','aufgewacht'),('der Zug','abgefahren'),('wir','ausgestiegen'),('sie','geblieben'),('die Kinder','zurückgekommen')]:
    aux='waren' if subject in ('wir','die Gäste','die Kinder') else 'war'
    LESSONS.setdefault(85, []).append(question(f'Als der Anruf kam, ___ {subject} schon {part}. (Plusquamperfekt)',aux,
        ['hatte','sind' if aux=='waren' else 'ist','wären' if aux=='waren' else 'wäre'],
        f"This verb forms its perfect tenses with sein; '{aux} {part}' places the event before the past phone call.",'Choose the agreeing auxiliary for the earlier past event.'))

subjects=[('Ich','werde'),('Du','wirst'),('Er','wird'),('Wir','werden'),('Ihr','werdet')]
for subject,aux in subjects:
    for action in ['morgen anrufen','bald umziehen','die Rechnung bezahlen','den Kurs besuchen']:
        LESSONS.setdefault(86, []).append(question(f'{subject} ___ {action}. (Futur I)',aux,[v for v in ['werde','wirst','wird','werden','werdet'] if v!=aux][:3],
            f"Futur I uses the subject-matching form '{aux}' of werden plus a final infinitive; this is not passive werden plus participle.",'Complete the future-tense statement.'))

gaps(87, 'als|wenn|wann|ob', """
___ ich gestern ankam, regnete es. (einmal)|Als|A single event in the past takes als, capitalized initially.
Immer ___ ich früher Urlaub hatte, fuhr ich ans Meer.|wenn
___ ich ein Kind war, wohnte ich in Bonn. (Lebensabschnitt)|Als|A single past life period takes als, even if it lasted years.
___ ich morgen komme, bringe ich Brot mit.|Wenn|A future occasion takes wenn, capitalized initially.
Jedes Mal, ___ es regnete, blieb er drinnen.|wenn
___ wir 2015 umzogen, war ich zehn. (einmal)|Als|One dated past occasion takes als.
___ ich Zeit habe, übe ich Deutsch. (regelmäßig)|Wenn|A repeated occasion takes wenn.
___ sie gestern anrief, war ich im Büro. (einmal)|Als|The one specific phone call yesterday takes als.
Immer ___ er in Köln war, besuchte er uns.|wenn
___ die Prüfung nächste Woche beginnt, bin ich bereit.|Wenn|A future temporal situation takes wenn.
___ wir Kinder waren, spielten wir draußen. (Lebensphase)|Als|A single past life period takes als.
Jedes Mal, ___ der Bus spät kam, warteten wir.|wenn
___ ich den Unfall sah, rief ich Hilfe. (einmal)|Als|One completed past event takes als.
___ du fertig bist, gehen wir. (heute später)|Wenn|A present/future occasion takes wenn.
Immer ___ sie Hilfe brauchte, rief sie an.|wenn
___ ich letztes Jahr krank war, half er mir. (einmal)|Als|The context specifies one past episode, so use als.
___ wir uns sehen, trinken wir Kaffee. (jedes Mal)|Wenn|A repeated occasion takes wenn.
___ der Zug gestern ausfiel, nahm ich ein Taxi.|Als|A specific past cancellation takes als.
___ es morgen regnet, bleiben wir hier.|Wenn|A realistic future condition takes wenn.
___ ich meinen ersten Job bekam, war ich froh.|Als|A unique past event takes als.
""",{'als':'Als marks a single past event or life period.', 'wenn':'Wenn marks repetition or a present/future occasion or condition.', 'wann':'Wann asks when, rather than connecting these events.', 'ob':'Ob introduces an indirect yes/no question.'})

clauses(88,'bevor',"""
Lies alles,|du|den Vertrag|unterschreibst|unterschreiben
Ruf an,|du|nach Berlin|losfährst|losfahren
Wir essen,|wir|zum Kurs|gehen|gehen
Mach das Licht aus,|du|das Büro|verlässt|verlassen
Frag nach,|du|die Rechnung|bezahlst|bezahlen
Ich lerne,|die Prüfung|morgen|beginnt|beginnen
Wir packen,|wir|in Urlaub|fahren|fahren
Sie duscht,|sie|zur Arbeit|geht|gehen
Prüfe die Adresse,|du|den Brief|verschickst|verschicken
Er spart Geld,|er|ein Auto|kauft|kaufen
Wir reservieren,|wir|ins Restaurant|gehen|gehen
Trink etwas,|du|weiter|arbeitest|arbeiten
Ich rufe dich an,|ich|den Termin|buche|buchen
Sie liest die Anleitung,|sie|das Gerät|benutzt|benutzen
Wir räumen auf,|die Gäste|zu Besuch|kommen|kommen
Ich frage die Ärztin,|ich|das Medikament|nehme|nehmen
Schließ die Tür,|du|ins Bett|gehst|gehen
Wir prüfen die Unterlagen,|wir|sie|abgeben|abgeben
Sie kauft Brot,|der Laden|heute|schließt|schließen
Ich mache eine Kopie,|ich|das Original|verschicke|verschicken
""")

for action in ACTIONS:
    patient,plural,part,inf,present,past,obj,zu=action
    correct=f'sie {obj} {part} hatte'
    LESSONS.setdefault(89, []).append(question(f'Nachdem ___, machte sie eine Pause. ({inf}; {obj})',correct,
        [f'sie hatte {obj} {part}',f'hatte sie {obj} {part}',f'sie {obj} hatte {part}'],
        f"The action '{obj} {part}' was completed before machte; nachdem takes verb-final order with the earlier event in Plusquamperfekt.",'Choose the ordered past-time clause.'))

simultaneous = """
Ich lese,|sie|in der Küche|kocht|kochen
Wir reden,|die Kinder|im Garten|spielen|spielen
Sie hört Musik,|sie|die Wohnung|putzt|putzen
Er macht Notizen,|die Lehrerin|die Regel|erklärt|erklären
Ich halte die Leiter,|du|die Lampe|befestigst|befestigen
Wir warten draußen,|die Mitarbeiterin|den Raum|reinigt|reinigen
Sie deckt den Tisch,|er|das Essen|macht|machen
Er telefoniert,|ich|die Unterlagen|ordne|ordnen
Ich trinke Tee,|es|draußen|regnet|regnen
Wir frühstücken,|das Radio|leise|läuft|laufen
Sie liest vor,|das Kind|im Bett|liegt|liegen
Er schreibt,|seine Kollegin|am Computer|arbeitet|arbeiten
Ich sehe fern,|die Waschmaschine|im Keller|läuft|laufen
Wir planen die Reise,|wir|auf den Zug|warten|warten
Sie lernt Wörter,|sie|im Bus|sitzt|sitzen
Er hört zu,|du|von der Reise|erzählst|erzählen
Ich halte die Tür,|du|die Kiste|trägst|tragen
Wir machen Fotos,|die Sonne|über dem See|untergeht|untergehen
Sie singt,|sie|das Essen|vorbereitet|vorbereiten
Er sucht den Schlüssel,|wir|die Taschen|packen|packen
"""
clauses(90,'während',simultaneous)

clauses(91,'seitdem',"""
Ich fahre mit dem Rad,|ich|hier|arbeite|arbeiten
Sie lernt Deutsch,|sie|in Berlin|wohnt|wohnen
Wir haben mehr Platz,|wir|umgezogen|sind|sein
Er kocht öfter,|er|eine neue Küche|hat|haben
Ich bin ruhiger,|ich|regelmäßig Sport|mache|machen
Wir sparen Geld,|wir|kein Auto mehr|haben|haben
Sie schläft besser,|sie|weniger Kaffee|trinkt|trinken
Er kennt viele Leute,|er|im Verein|ist|sein
Ich verstehe mehr,|ich|jeden Tag|übe|üben
Wir sind zufrieden,|die Heizung|wieder|funktioniert|funktionieren
Sie arbeitet zu Hause,|sie|den neuen Job|hat|haben
Er geht früher ins Bett,|er|um sechs aufstehen|muss|müssen
Ich kenne den Weg,|ich|ihn einmal gegangen|bin|sein
Wir treffen uns öfter,|wir|Nachbarn|sind|sein
Sie benutzt die Treppe,|der Aufzug|kaputt|ist|sein
Er liest viel,|er|mehr Zeit|hat|haben
Ich esse gesünder,|ich|selbst|koche|kochen
Wir hören nichts mehr,|das Fenster|geschlossen|ist|sein
Sie ist glücklicher,|sie|die Ausbildung begonnen|hat|haben
Er trägt eine Brille,|er|schlechter|sieht|sehen
""")

endpoints = """
Ich warte hier,|du|zurück|kommst|kommen
Wir bleiben,|der Regen|auf|hört|hören
Sie liest,|der Bus|endlich|kommt|kommen
Er arbeitet,|der Bericht|fertig|ist|sein
Ich spare,|ich|genug Geld|habe|haben
Wir üben,|alle|die Regel|verstehen|verstehen
Sie wartet,|das Geschäft|wieder|öffnet|öffnen
Er bleibt im Bett,|er|wieder gesund|ist|sein
Ich halte die Tür,|alle|drinnen|sind|sein
Wir bleiben hier,|die Gefahr|vorbei|ist|sein
Sie lernt,|sie|alle Wörter|kennt|kennen
Er sucht,|er|den Schlüssel|findet|finden
Ich warte,|die Rechnung|angekommen|ist|sein
Wir reden,|wir|eine Lösung|haben|haben
Sie bleibt,|die Kinder|eingeschlafen|sind|sein
Er arbeitet,|seine Kollegin|zurück|kommt|kommen
Ich warte,|du|die Datei gespeichert|hast|haben
Wir bleiben draußen,|der Raum|frei|ist|sein
Sie zählt,|alle|anwesend|sind|sein
Er bleibt dort,|die Reparatur|beendet|ist|sein
"""
# Correct nonseparable full final verbs; the middle field excludes detachable particles.
endpoints=endpoints.replace('der Regen|auf|hört|hören','der Regen|endlich|aufhört|aufhören').replace('du|zurück|kommst|kommen','du|wieder|zurückkommst|zurückkommen').replace('seine Kollegin|zurück|kommt|kommen','seine Kollegin|wieder|zurückkommt|zurückkommen')
clauses(92,'bis',endpoints)
clauses(93,'sobald',endpoints.replace('Ich spare,','Ich buche die Reise,').replace('Sie lernt,','Sie macht die Prüfung,').replace('Er sucht,','Er ruft mich an,').replace('Er arbeitet,|der Bericht','Er macht eine Pause,|der Bericht').replace('Wir üben,','Wir beginnen die Aufgabe,').replace('Ich warte hier,','Ich rufe dich an,').replace('Ich warte,','Ich melde mich,').replace('Wir bleiben,','Wir gehen hinaus,').replace('Wir bleiben hier,','Wir fahren los,').replace('Wir bleiben draußen,','Wir gehen hinein,').replace('Er bleibt im Bett,','Er geht wieder arbeiten,').replace('Sie wartet,','Sie kauft ein,').replace('Er bleibt dort,','Er fährt heim,').replace('Sie bleibt,','Sie geht ins Bett,').replace('Sie zählt,','Sie beginnt mit dem Unterricht,').replace('Wir reden,','Wir setzen den Plan um,').replace('Ich halte die Tür,','Ich schließe die Tür,').replace('Sie liest,','Sie steigt ein,').replace('Er arbeitet,|seine Kollegin','Er geht in die Pause,|seine Kollegin'))

clauses(94,'solange',"""
Wir bleiben drinnen,|es|draußen|regnet|regnen
Ich helfe dir,|du|meine Hilfe|brauchst|brauchen
Wir benutzen ein anderes Gerät,|die Reparatur|noch|dauert|dauern
Sie darf bleiben,|sie|ruhig|ist|sein
Er arbeitet zu Hause,|sein Büro|geschlossen|ist|sein
Ich warte hier,|du|im Laden|bist|sein
Wir bleiben Freunde,|wir|einander|vertrauen|vertrauen
Sie fährt Rad,|das Wetter|gut|ist|sein
Er wohnt bei uns,|er|ein Zimmer|sucht|suchen
Ich lerne weiter,|ich|Zeit|habe|haben
Wir helfen mit,|wir|hier|sind|sein
Sie bleibt im Bett,|sie|Fieber|hat|haben
Er hört zu,|du|etwas|erklärst|erklären
Ich halte die Leiter,|du|oben|arbeitest|arbeiten
Wir bleiben leise,|das Kind|noch|schläft|schlafen
Sie trägt die Brille,|sie|am Computer|arbeitet|arbeiten
Er spart Geld,|er|einen Job|hat|haben
Ich bin zufrieden,|alles|gut|funktioniert|funktionieren
Wir haben Platz,|die Gäste|noch nicht da|sind|sein
Sie bleibt erreichbar,|das Projekt|noch|läuft|laufen
""")
clauses(95,'da',basic_contexts)

contrast = """
Ich gehe spazieren,|es|draußen|regnet|regnen
Wir fahren los,|wir|müde|sind|sein
Sie kommt zum Kurs,|sie|wenig Zeit|hat|haben
Er kauft das Rad,|es|teuer|ist|sein
Ich verstehe ihn,|er|sehr schnell|spricht|sprechen
Wir sind pünktlich,|der Zug|Verspätung|hat|haben
Sie hilft uns,|sie|selbst viel arbeiten|muss|müssen
Er lächelt freundlich,|er|traurig|ist|sein
Ich esse noch etwas,|ich|schon gegessen|habe|haben
Wir bleiben draußen,|es|kalt|ist|sein
Sie besteht die Prüfung,|sie|nervös|ist|sein
Er findet den Weg,|er|die Stadt nicht|kennt|kennen
Ich nehme das Auto,|der Weg|kurz|ist|sein
Wir gehen ins Kino,|wir|den Film schon gesehen|haben|haben
Sie arbeitet weiter,|sie|eine Pause machen|könnte|können
Er kommt zu Fuß,|er|ein Auto|hat|haben
Ich kaufe das Buch,|ich|wenig Geld|habe|haben
Wir verstehen alles,|die Erklärung|kurz|ist|sein
Sie ist freundlich,|sie|einen schlechten Tag|hat|haben
Er trinkt Kaffee,|er|schlafen|möchte|möchten
"""
clauses(96,'obwohl',contrast)

for line in contrast.strip().splitlines():
    main,subject,middle,finite,inf = [x.strip() for x in line.split('|')]
    main=main.rstrip(',')
    # Main clauses are explicitly simple S-V-X sequences.
    subj,verb,rest=main.split(' ',2)
    cause=f'{subject[0].upper()+subject[1:]} {finite} {middle}.'
    correct=f'{verb} {subj.lower()} {rest}'
    LESSONS.setdefault(97, []).append(question(cause+' Trotzdem ___.',correct,
        [f'{subj.lower()} {verb} {rest}',f'{subj.lower()} {rest} {verb}',f'{verb} {rest} {subj.lower()}'],
        f"Trotzdem links an unexpected result and occupies position one, so the finite verb '{verb}' follows immediately.",'Choose the neutral main-clause word order.'))

clauses(98,'damit',"""
Ich schicke dir die Adresse,|du|uns|findest|finden
Wir sprechen leise,|das Kind|weiter schlafen|kann|können
Sie erklärt die Regel,|alle|sie|verstehen|verstehen
Er öffnet die Tür,|wir|hineingehen|können|können
Ich schreibe alles auf,|ich|nichts|vergesse|vergessen
Wir sparen,|die Kinder|studieren|können|können
Sie ruft an,|er|Bescheid|weiß|wissen
Er macht das Licht an,|wir|besser|sehen|sehen
Ich gebe dir den Schlüssel,|du|die Tür öffnen|kannst|können
Wir reservieren,|wir|einen Platz|haben|haben
Sie kocht Suppe,|die Gäste|etwas essen|können|können
Er spricht langsam,|ich|ihn|verstehe|verstehen
Ich helfe dir,|du|früher fertig|bist|sein
Wir schließen das Fenster,|es|leiser|wird|werden
Sie leiht mir das Rad,|ich|pünktlich|ankomme|ankommen
Er schickt die Datei,|sie|weiterarbeiten|kann|können
Ich lerne viel,|ich|die Prüfung|bestehe|bestehen
Wir bauen eine Rampe,|alle|hineinkommen|können|können
Sie legt Geld zurück,|sie|die Reise bezahlen|kann|können
Er trägt die Kiste,|ich|die Tür öffnen|kann|können
""")

for action in ACTIONS:
    patient,plural,part,inf,present,past,obj,zu=action
    correct=f'{obj} {zu}'
    LESSONS.setdefault(99, []).append(question(f'Ich nehme mir Zeit, um ___. ({inf}; {obj})',correct,
        [f'{obj} {inf}',f'{obj} {inf} zu',f'ich {obj} {zu}'],
        f"Um … zu names my purpose; the logical subject is shared with ich. The infinitive form here is '{zu}'.",'Complete the shared-subject purpose clause.'))

clauses(100,'falls',"""
Wir informieren Sie,|der Termin|morgen|ausfällt|ausfallen
Ich rufe an,|ich|später|komme|kommen
Wir bleiben hier,|es|stark|regnet|regnen
Sie hilft dir,|du|Fragen|hast|haben
Er nimmt ein Taxi,|der Bus|nicht mehr|fährt|fahren
Ich bringe Brot mit,|der Laden|schon geschlossen|ist|sein
Wir sagen Bescheid,|sich|etwas|ändert|ändern
Sie bleibt zu Hause,|sie|krank|wird|werden
Er fährt mit,|er|Zeit|hat|haben
Ich nehme eine Jacke,|es|kalt|ist|sein
Wir buchen später,|die Preise|zu hoch|sind|sein
Sie fragt nach,|sie|etwas nicht|versteht|verstehen
Er kommt früher,|du|Hilfe|brauchst|brauchen
Ich bleibe erreichbar,|es|Probleme|gibt|geben
Wir öffnen den Saal,|mehr Gäste|kommen|wollen|wollen
Sie ruft den Arzt,|das Fieber|höher|wird|werden
Er nimmt das Rad,|das Auto|kaputt|ist|sein
Ich mache eine Kopie,|du|eine|brauchst|brauchen
Wir bestellen mehr,|das Essen|nicht|reicht|reichen
Sie schreibt uns,|sie|den Termin nicht wahrnehmen|kann|können
""")

gaps(101,'sondern|aber|weil|oder',"""
Ich brauche keinen Vertrag, ___ eine Kopie. (Korrektur)|sondern
Sie wohnt nicht in Bonn, ___ in Köln.|sondern
Er kommt nicht heute, ___ morgen.|sondern
Wir fahren nicht mit dem Auto, ___ mit dem Zug.|sondern
Das ist kein Fehler, ___ eine neue Regel.|sondern
Die Wohnung ist klein, ___ schön. (bloßer Gegensatz)|aber
Er ist müde, ___ er hilft trotzdem. (Gegensatz)|aber
Sie trinkt keinen Kaffee, ___ Tee.|sondern
Wir bleiben nicht hier, ___ gehen nach Hause.|sondern
Das Buch ist nicht teuer, ___ günstig.|sondern
Ich komme gern, ___ ich habe wenig Zeit. (Gegensatz)|aber
Er hat nicht angerufen, ___ eine Nachricht geschickt.|sondern
Sie ist nicht Ärztin, ___ Lehrerin.|sondern
Das war nicht gestern, ___ vorgestern.|sondern
Der Weg ist lang, ___ sicher. (Gegensatz)|aber
Wir suchen keine Garage, ___ ein Zimmer.|sondern
Er möchte nicht gehen, ___ bleiben.|sondern
Sie hilft nicht nur mir, ___ auch dir. (Ergänzung)|sondern
Das Gerät ist alt, ___ es funktioniert. (Gegensatz)|aber
Ich habe nicht zwei, ___ drei Tickets.|sondern
""",{'sondern':'Sondern corrects or replaces a preceding negated element; in nicht nur … sondern auch it adds a further element.', 'aber':'Aber introduces a contrast without replacing a negated element.', 'weil':'Weil would introduce a reason with final verb order.', 'oder':'Oder presents an alternative rather than the specified correction.'})

pair_items=[('Tee','Kaffee'),('Deutsch','Englisch'),('Brot','Käse'),('Bus','Bahn'),('Kino','Theater'),('Anna','Paul'),('Lesen','Schreiben'),('Zeit','Geld'),('Montag','Dienstag'),('Bonn','Köln')]
for unit in range(102,107):
    for a,b in pair_items:
        if unit==102:
            prompt=f'Als Alternativen: entweder {a} ___ {b}'; correct='oder'; wrong=['und','noch','als auch']; why='Entweder … oder presents alternative choices; it does not assert both.'
        elif unit==103:
            prompt=f'Beides trifft zu: sowohl {a} ___ {b}'; correct='als auch'; wrong=['oder','noch','aber']; why='Sowohl … als auch includes both coordinated items on equal terms.'
        elif unit==104:
            prompt=f'Zusätzlich betont: nicht nur {a}, ___ {b}'; correct='sondern auch'; wrong=['oder nur','weder noch','aber nicht']; why='Nicht nur … sondern auch adds a second included item with emphasis.'
        elif unit==105:
            prompt=f'Beides verneint: weder {a} ___ {b}'; correct='noch'; wrong=['oder','als auch','sondern']; why='Weder … noch negates both alternatives; no extra nicht is needed.'
        else:
            prompt=f'Einräumung und Gegensatz: zwar {a}, ___ nicht {b}'; correct='aber'; wrong=['noch','als auch','weil']; why='Zwar … aber concedes the first point and contrasts it with the second.'
        LESSONS.setdefault(unit, []).append(question(prompt,correct,wrong,why,'Complete the paired conjunction.'))
    # Recognition complements the ten form items with ten complete, authored contexts.
contexts = {
102: ('alternative', """
Wir trinken entweder Tee oder Kaffee.
Entweder du kommst heute oder ich besuche dich morgen.
Wir fahren entweder mit dem Bus oder mit der Bahn.
Sie wählt entweder Montag oder Dienstag.
Entweder wir sparen oder wir verschieben die Reise.
Er kann entweder anrufen oder eine Nachricht schreiben.
Entweder Anna oder Paul übernimmt die Aufgabe.
Wir treffen uns entweder hier oder im Büro.
Entweder du fragst nach oder du wartest auf eine Antwort.
Sie nimmt entweder den roten oder den blauen Mantel.
"""),
103: ('both', """
Sie spricht sowohl Deutsch als auch Englisch.
Sowohl Anna als auch Paul lernen hier.
Der Kurs verbessert sowohl das Lesen als auch das Schreiben.
Wir brauchen sowohl Zeit als auch Geld.
Sowohl der Bus als auch die Bahn fahren zum Bahnhof.
Sie hilft sowohl ihrer Mutter als auch ihrem Vater.
Das Angebot gilt sowohl heute als auch morgen.
Er arbeitet sowohl im Büro als auch zu Hause.
Wir besuchen sowohl Bonn als auch Köln.
Sowohl die Wohnung als auch die Garage sind frei.
"""),
104: ('emphasis', """
Er hat nicht nur Zeit, sondern auch Geld.
Sie liest nicht nur Bücher, sondern auch Zeitungen.
Wir helfen nicht nur heute, sondern auch morgen.
Nicht nur Anna, sondern auch Paul nimmt teil.
Der Kurs ist nicht nur günstig, sondern auch interessant.
Sie spricht nicht nur Deutsch, sondern auch Englisch.
Wir brauchen nicht nur einen Plan, sondern auch Geduld.
Er arbeitet nicht nur schnell, sondern auch sorgfältig.
Sie hat nicht nur angerufen, sondern auch geschrieben.
Das Zimmer ist nicht nur hell, sondern auch ruhig.
"""),
105: ('neither', """
Wir haben weder angerufen noch geschrieben.
Er trinkt weder Milch noch Saft.
Sie hat weder Zeit noch Geld.
Der Kurs findet weder heute noch morgen statt.
Wir fahren weder nach Bonn noch nach Köln.
Sie kennt weder Anna noch Paul.
Das Gerät ist weder alt noch kaputt.
Er kann weder schwimmen noch Rad fahren.
Wir brauchen weder einen Wagen noch ein Taxi.
Sie hat weder gefragt noch geantwortet.
"""),
106: ('concession', """
Der Weg ist zwar lang, aber sicher.
Das Zimmer ist zwar klein, aber hell.
Sie ist zwar müde, aber sie hilft uns.
Der Kurs ist zwar teuer, aber sehr gut.
Wir haben zwar wenig Zeit, aber einen guten Plan.
Er spricht zwar langsam, aber deutlich.
Die Wohnung ist zwar alt, aber günstig.
Sie kennt zwar den Weg, aber nicht die Hausnummer.
Das Gerät ist zwar beschädigt, aber noch brauchbar.
Die Reise dauert zwar lange, aber sie lohnt sich.
"""),
}
pair_labels={
 'alternative':('One alternative or the other','Entweder … oder presents alternatives, not a statement that both apply.'),
 'both':('Both items, equally included','Sowohl … als auch includes both coordinated elements.'),
 'emphasis':('Both items, with an emphatic addition','Nicht nur … sondern auch emphasizes the addition of the second element.'),
 'neither':('Neither item applies','Weder … noch negates both coordinated elements.'),
 'concession':('A conceded point followed by a contrast','Zwar … aber accepts a first point before emphasizing a contrasting one.'),
}
for unit in range(102,107):
    key,text=contexts[unit]
    meanings(unit,'\n'.join(f'{s.strip()}|{key}' for s in text.strip().splitlines()),pair_labels,'What relationship do the paired conjunctions express?')
