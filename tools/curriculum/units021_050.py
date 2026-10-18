from .core import gaps, meanings, explicit, clauses, LESSONS, question

gaps(21, 'den|dem|der|das|die|einen|einem|einer', """
Wir gehen durch ___ Park. (der Park)|den
Sie kauft Blumen für ___ Nachbarin. (die Nachbarin)|die
Ohne ___ Führerschein darf er nicht fahren. (der Führerschein)|den
Der Ball fliegt gegen ___ Fenster. (das Fenster)|das
Wir laufen um ___ Gebäude. (das Gebäude)|das
Das Geschenk ist für ___ Kollegen. (ein Kollege)|einen
Sie fährt gegen ___ Baum. (der Baum)|den
Er kommt ohne ___ Tasche. (die Tasche)|die
Wir gehen durch ___ Tunnel. (der Tunnel)|den
Das ist für ___ Kind. (das Kind)|das
Die Sitzung dauert bis ___ nächsten Freitag. (der Freitag)|den
Sie kämpfen gegen ___ Lärm. (der Lärm)|den
Er geht ohne ___ Mantel hinaus. (ein Mantel)|einen
Wir sitzen um ___ Tisch. (der Tisch)|den
Die Reise führt durch ___ Schweiz. (die Schweiz)|die
Ich bezahle für ___ Kaffee. (der Kaffee)|den
Das Auto fährt gegen ___ Mauer. (eine Mauer)|eine|Gegen requires accusative; feminine eine remains eine.
Die Gruppe geht um ___ See. (der See)|den
Ohne ___ Genehmigung geht es nicht. (die Genehmigung)|die
Wir brauchen Zeit für ___ Gespräch. (das Gespräch)|das
""", "The preposition in this sentence requires accusative; '{answer}' matches the given noun's gender.")

gaps(22, 'dem|der|den|die|das|einem|einer|einen', """
Sie kommt aus ___ Büro. (das Büro)|dem
Wir fahren mit ___ Fähre. (die Fähre)|der
Er wohnt bei ___ Bruder. (der Bruder)|dem
Ich gehe zu ___ Apotheke. (die Apotheke)|der
Das Paket ist von ___ Verlag. (der Verlag)|dem
Seit ___ Ausbildung arbeitet sie hier. (die Ausbildung)|der
Außer ___ Lehrerin ist niemand da. (die Lehrerin)|der
Die Bank liegt gegenüber ___ Rathaus. (das Rathaus)|dem
Nach ___ Essen gehen wir spazieren. (das Essen)|dem
Wir sprechen mit ___ Gästen. (die Gäste)|den
Sie fährt zu ___ Eltern. (die Eltern)|den
Er kommt aus ___ kleinen Dorf. (ein Dorf)|einem
Bei ___ Prüfung war sie ruhig. (die Prüfung)|der
Das Hotel liegt ___ Bahnhof gegenüber. (der Bahnhof)|dem
Ich fahre mit ___ Freund. (ein Freund)|einem
Seit ___ Woche regnet es. (eine Woche)|einer
Von ___ Kollegen habe ich viel gelernt. (die Kollegen)|den
Nach ___ Konzert treffen wir uns. (das Konzert)|dem
Außer ___ Kind sind alle müde. (das Kind)|dem
Wir wohnen gegenüber ___ Schule. (die Schule)|der
""", "This preposition governs dative; '{answer}' is the matching determiner, including with gegenüber after its noun.")

gaps(23, 'seit|vor|in|bis', """
Ich wohne ___ drei Jahren hier und bleibe noch. (andauernd)|seit
Sie ist ___ zwei Tagen angekommen. (Vergangenheit)|vor
Wir fahren ___ einer Woche ab. (Zukunft)|in
Er arbeitet ___ Januar in dieser Firma. (noch immer)|seit
Der Kurs begann ___ einem Monat. (Vergangenheit)|vor
Die Prüfung findet ___ zwei Monaten statt. (Zukunft)|in
Ich warte ___ einer Stunde; sie ist noch nicht da.|seit
Wir haben uns ___ zehn Minuten getroffen. (Vergangenheit)|vor
Der Bus kommt ___ fünf Minuten. (Zukunft)|in
Sie lernt ___ ihrem Umzug täglich Deutsch. (noch immer)|seit
Die Rechnung wurde ___ drei Wochen bezahlt.|vor
Das Geschäft öffnet ___ einer halben Stunde. (Zukunft)|in
Er ist ___ Montag krank und liegt noch im Bett.|seit
___ zwei Jahren habe ich mein Abitur gemacht.|Vor|Vor marks a completed event two years ago; capitalize it at the sentence start.
Wir ziehen ___ einem Jahr um. (Zukunft)|in
Ich kenne sie ___ meiner Ausbildung. (bis heute)|seit
Sie hat ___ einer Stunde angerufen.|vor
Die Reparatur beginnt ___ drei Tagen. (Zukunft)|in
___ gestern funktioniert der Aufzug nicht. (weiterhin)|Seit|Seit introduces the starting point of an ongoing state; capitalize it here.
Der Aufenthalt endet ___ vier Wochen. (von heute aus)|in
""", {'seit': 'Seit marks an interval or starting point that continues into the present.', 'vor': 'Vor locates a completed event a stated distance before now.', 'in': 'In locates the event a stated distance after now.', 'bis': 'Bis marks an endpoint.'})

gaps(24, 'für|bis|ab|seit|an', """
Ich miete das Zimmer ___ drei Monate. (geplante Dauer)|für
Die Praxis bleibt ___ Freitag geschlossen. (Endpunkt)|bis
___ Montag gilt der neue Fahrplan. (Start)|Ab|Ab marks the point when the new timetable starts; it is capitalized initially.
Von neun ___ zwölf ist das Büro offen.|bis
Vom ersten Juni ___ ist die Garage frei.|an
Sie ist ___ zwei Wochen im Urlaub. (geplante Dauer)|für
Wir warten ___ morgen. (Endpunkt)|bis
___ nächster Woche arbeite ich hier. (Beginn)|Ab|Ab identifies the beginning of the new working arrangement.
Von April ___ September ist das Bad geöffnet.|bis
Von diesem Tag ___ war alles anders.|an
Der Vertrag gilt ___ ein Jahr. (vereinbarte Dauer)|für
Die Anmeldung ist ___ zum 15. Mai möglich.|bis
___ sofort ist der Eintritt kostenlos. (Start)|Ab|Ab sofort means starting immediately, rather than an elapsed duration.
Vom nächsten Monat ___ zahle ich weniger.|an
Wir bleiben ___ eine Nacht. (geplant)|für
Sie arbeitet von Montag ___ Donnerstag.|bis
Der Kredit läuft ___ fünf Jahre. (vereinbart)|für
Die Frist läuft ___ Ende Oktober. (Ende)|bis
Von heute ___ komme ich pünktlich.|an
Der Ausweis wird ___ zehn Jahre ausgestellt. (Gültigkeitsdauer)|für
""", {'für':'Für marks the intended or agreed duration.', 'bis':'Bis identifies the endpoint; bis zu is used before a determiner such as zum.', 'ab':'Ab marks the starting boundary.', 'seit':'Seit would describe a period continuing from the past.', 'an':'The frame von/vom … an emphasizes the starting point.'})

gaps(25, 'des|der|dem|den|die|das', """
Während ___ Kurses bleibt das Handy aus. (der Kurs)|des
Während ___ Prüfung darf man nicht sprechen. (die Prüfung)|der
Während ___ Gesprächs mache ich Notizen. (das Gespräch)|des
Während ___ Ferien ist die Schule leer. (Plural)|der
Während ___ Vortrags hört er aufmerksam zu. (der Vortrag)|des
Während ___ Reise lesen wir viel. (die Reise)|der
Während ___ Essens klingelt das Telefon. (das Essen)|des
Während ___ Arbeiten ist der Weg gesperrt. (Plural)|der
Während ___ Aufenthalts besuchen wir das Museum. (der Aufenthalt)|des
Während ___ Ausbildung wohnt sie zu Hause. (die Ausbildung)|der
Während ___ Festes regnet es. (das Fest)|des
Während ___ Verhandlungen gibt es Kaffee. (Plural)|der
Während ___ Streiks fahren keine Busse. (der Streik)|des
Während ___ Beratung stellen wir Fragen. (die Beratung)|der
Während ___ Gewitters bleiben wir drinnen. (das Gewitter)|des
Während ___ Öffnungszeiten ist jemand erreichbar. (Plural)|der
Während ___ Besuchs sprechen wir Deutsch. (der Besuch)|des
Während ___ Pause gehe ich hinaus. (die Pause)|der
Während ___ Spiels bleibt er ruhig. (das Spiel)|des
Während ___ Sitzungen bleibt die Tür zu. (Plural)|der
""", {'des':'In formal written German, während takes genitive; masculine and neuter singular use des plus the noun ending -(e)s.', 'der':'Während takes genitive here; feminine singular and plural use der.', 'dem':'Dem is dative, not the formal genitive model used here.', 'den':'Den is not the required genitive article.', 'die':'Die is not a genitive article.', 'das':'Das is not a genitive article.'})

# Complete noun-phrase paradigms, with five lexical contexts in four cases.
adjectives = [
    ('Mitarbeiter','m','freundlich','Mitarbeiter','Mitarbeitern'),
    ('Wohnung','f','ruhig','Wohnungen','Wohnungen'),
    ('Gerät','n','modern','Geräte','Geräten'),
    ('Kollege','m','neu','Kollegen','Kollegen'),
    ('Angebot','n','günstig','Angebote','Angeboten'),
]
for unit in (26, 27):
    for noun, gender, stem, plural, datplural in adjectives:
        noun_acc = 'Kollegen' if noun == 'Kollege' else noun
        if unit == 26:
            forms = [
                (f"{'Der' if gender=='m' else 'Die' if gender=='f' else 'Das'} ___ {noun} ist hier.", 'e', 'Nominative singular after a definite article takes adjective -e.'),
                (f"Ich suche {'den' if gender=='m' else 'die' if gender=='f' else 'das'} ___ {noun_acc}.", 'en' if gender=='m' else 'e', 'After a definite article, masculine accusative takes -en; feminine and neuter accusative take -e.'),
                (f"Mit {'der' if gender=='f' else 'dem'} ___ {noun_acc} bin ich zufrieden.", 'en', 'Dative adjectives after a definite article take -en.'),
                (f"Mit den ___ {datplural} bin ich zufrieden.", 'en', 'Dative plural after den takes adjective -en and a dative plural noun.'),
            ]
        else:
            forms = [
                (f"{'Eine' if gender=='f' else 'Ein'} ___ {noun} ist hier.", {'m':'er','f':'e','n':'es'}[gender], 'After ein without an ending, the adjective marks gender; after eine it takes -e.'),
                (f"Ich suche {'einen' if gender=='m' else 'eine' if gender=='f' else 'ein'} ___ {noun_acc}.", {'m':'en','f':'e','n':'es'}[gender], 'Mixed adjective declension uses -en after einen, -e after eine, and -es after neuter ein.'),
                (f"Mit {'meiner' if gender=='f' else 'meinem'} ___ {noun_acc} bin ich zufrieden.", 'en', 'Dative adjectives after an ein-type determiner take -en.'),
                (f"Meine ___ {plural} sind hier.", 'en', 'Plural adjectives after a possessive determiner take -en.'),
            ]
        for prompt, ending, why in forms:
            correct = stem + ending
            wrong = [stem + e for e in ['e','en','er','es','em'] if e != ending][:3]
            LESSONS.setdefault(unit, []).append(question(prompt, correct, wrong, why, 'Complete the adjective.'))

gaps(28, 'frischer|frische|frisches|frischen|frischem', """
___ Kaffee steht bereit. (Nominativ)|Frischer|Without an article, masculine nominative takes -er; capitalize at the start.
Wir trinken ___ Kaffee. (Akkusativ)|frischen
Mit ___ Kaffee beginnt der Tag. (Dativ)|frischem
___ Milch ist im Kühlschrank. (Nominativ)|Frische|Without an article, feminine nominative takes -e; capitalize at the start.
Ich kaufe ___ Milch. (Akkusativ)|frische
Mit ___ Milch schmeckt es besser. (Dativ)|frischer
___ Brot liegt auf dem Tisch. (Nominativ)|Frisches|Without an article, neuter nominative takes -es; capitalize at the start.
Wir essen ___ Brot. (Akkusativ)|frisches
Mit ___ Brot ist die Suppe gut. (Dativ)|frischem
___ Blumen stehen am Fenster. (Plural)|Frische|Article-free nominative plural adjectives take -e; capitalize initially.
Ich kaufe ___ Blumen. (Akkusativ Plural)|frische
Mit ___ Blumen schmückt sie den Raum. (Dativ Plural)|frischen
Wir bieten ___ Gemüse an. (Akkusativ)|frisches
Sie kocht mit ___ Gemüse. (Dativ)|frischem
___ Käse riecht gut. (Nominativ)|Frischer|Masculine nominative without an article takes -er.
Wir kaufen ___ Käse. (Akkusativ)|frischen
Mit ___ Käse schmeckt die Pizza besser. (Dativ)|frischem
___ Äpfel sind angekommen. (Plural)|Frische|Without an article, nominative plural uses -e.
Die Lieferung enthält ___ Äpfel. (Akkusativ Plural)|frische
Der Saft besteht aus ___ Äpfeln. (Dativ Plural)|frischen
""", {'frischer':'Strong -er marks masculine nominative or feminine dative, as required by this phrase.', 'frische':'Strong -e marks feminine nominative/accusative or nominative/accusative plural.', 'frisches':'Strong -es marks neuter nominative or accusative without an article.', 'frischen':'Strong -en marks masculine accusative or dative plural here.', 'frischem':'Strong -em marks masculine or neuter dative without an article.'})

comparatives = [
 ('schnell','schneller'),('langsam','langsamer'),('klein','kleiner'),('groß','größer'),
 ('alt','älter'),('jung','jünger'),('warm','wärmer'),('kalt','kälter'),('kurz','kürzer'),
 ('lang','länger'),('hoch','höher'),('teuer','teurer'),('dunkel','dunkler'),('nah','näher'),
 ('gut','besser'),('viel','mehr'),('gern','lieber'),('billig','billiger'),('ruhig','ruhiger'),('einfach','einfacher')]
for stem, comparative in comparatives:
    prompt = f"Vergleich mit als: {stem} → ___"
    wrong = [stem, f'am {stem}sten', stem + 'est']
    LESSONS.setdefault(29, []).append(question(prompt, comparative, wrong,
        f"The comparative of '{stem}' is '{comparative}'; als introduces the unequal comparison.", 'Choose the comparative form.'))

gaps(30, 'schnellere|schnelleren|schnellerer|schnelleres|schnellsten|schnellste|schnellstes|schnellster', """
Der ___ Zug fährt schon ab. (Komparativ)|schnellere
Ich nehme den ___ Zug. (Komparativ)|schnelleren
Mit dem ___ Zug spare ich Zeit. (Komparativ)|schnelleren
Ein ___ Zug wäre besser. (Komparativ)|schnellerer
Wir suchen ein ___ Verkehrsmittel. (Komparativ)|schnelleres
Die ___ Verbindung ist teurer. (Komparativ)|schnellere
Ich wähle eine ___ Verbindung. (Komparativ)|schnellere
Wir fahren mit einer ___ Verbindung. (Komparativ)|schnelleren
Das ___ Auto steht dort. (Komparativ)|schnellere
Ich wünsche mir ___ Züge. (ohne Artikel; Komparativ)|schnellere
Der ___ Zug gewinnt den Vergleich. (Superlativ)|schnellste
Ich nehme den ___ Zug. (Superlativ)|schnellsten
Mit dem ___ Zug bin ich früher da. (Superlativ)|schnellsten
Die ___ Verbindung kostet mehr. (Superlativ)|schnellste
Das ___ Fahrzeug steht vorne. (Superlativ)|schnellste
Die ___ Züge halten hier nicht. (Superlativ)|schnellsten
Wir nehmen die ___ Verbindung. (Superlativ)|schnellste
Mit den ___ Zügen dauert es eine Stunde. (Superlativ)|schnellsten
Sein ___ Auto steht in der Garage. (Superlativ)|schnellstes
Ihr ___ Zug fährt um acht. (Superlativ; Nominativ Singular)|schnellster
""", "Use the requested comparative/superlative stem plus the adjective ending required by the determiner and case: '{answer}'.")

gaps(31, 'wie|als|dass|ob', """
Der Kurs ist genauso interessant ___ der vorige.|wie
Mein Zimmer ist größer ___ deins.|als
Sie fährt ebenso schnell ___ ihr Bruder.|wie
Dieser Weg ist nicht so lang ___ der andere.|wie
Heute ist es wärmer ___ gestern.|als
Die Miete ist so hoch ___ früher.|wie
Er arbeitet genauso sorgfältig ___ du.|wie
Ich trinke lieber Tee ___ Kaffee.|als
Der neue Bus ist ebenso bequem ___ der alte.|wie
Die Prüfung war leichter ___ erwartet.|als
Das Essen ist nicht so teuer ___ im Hotel.|wie
Wir haben genauso viel Zeit ___ ihr.|wie
Sie ist älter ___ ich.|als
Er spricht ebenso deutlich ___ die Lehrerin.|wie
Das Dach ist höher ___ das Nachbardach.|als
Die Wohnung ist so hell ___ unsere.|wie
Ich habe weniger Geld ___ du.|als
Die Fahrt dauert genauso lange ___ gestern.|wie
Das Angebot ist günstiger ___ das andere.|als
Die Aufgaben sind nicht so schwierig ___ gedacht.|wie
""", {'wie':'Equality with so, genauso or ebenso uses wie, including negated equality.', 'als':'A comparative such as größer, mehr or lieber takes als.', 'dass':'Dass introduces a content clause, not this comparison.', 'ob':'Ob introduces an indirect yes/no question, not this comparison.'})

# Everyday clause contexts, explicitly inflected; no machine translation or inflection guesses.
basic_contexts = """
Ich bleibe zu Hause,|ich|krank|bin|sein
Wir nehmen den Bus,|das Auto|kaputt|ist|sein
Sie lernt viel,|sie|morgen eine Prüfung|hat|haben
Er ruft an,|er|eine Auskunft|braucht|brauchen
Ich gehe früh ins Bett,|ich|sehr müde|bin|sein
Wir warten,|der Zug|noch nicht da|ist|sein
Sie nimmt eine Jacke mit,|es|draußen kalt|ist|sein
Er spart Geld,|er|ein Fahrrad kaufen|möchte|möchten
Ich esse etwas,|ich|Hunger|habe|haben
Wir fahren nicht,|es|stark|regnet|regnen
Sie fragt nach,|sie|die Erklärung nicht|versteht|verstehen
Er nimmt Urlaub,|er|sich erholen|will|wollen
Ich bin froh,|du|rechtzeitig gekommen|bist|sein
Wir sind spät dran,|wir|lange gearbeitet|haben|haben
Sie bleibt im Büro,|sie|den Bericht schreiben|muss|müssen
Er sucht ein Zimmer,|er|nach Köln gezogen|ist|sein
Ich nehme das Rad,|der Weg|kurz|ist|sein
Wir kaufen Brot,|wir|keines mehr|haben|haben
Sie macht eine Pause,|ihr|der Kopf|wehtut|wehtun
Er geht zum Arzt,|er|sich verletzt|hat|haben
"""
clauses(32, 'weil', basic_contexts)
clauses(33, 'wenn', """
Wir gehen spazieren,|das Wetter|morgen schön|ist|sein
Ich helfe dir,|du|meine Hilfe|brauchst|brauchen
Wir kommen mit,|wir|Zeit|haben|haben
Du bestehst die Prüfung,|du|regelmäßig|lernst|lernen
Ich kaufe das Rad,|es|nicht zu teuer|ist|sein
Wir rufen an,|der Zug|Verspätung|hat|haben
Du kannst bleiben,|du|noch arbeiten|möchtest|möchten
Ich öffne das Fenster,|es|dir zu warm|ist|sein
Wir nehmen ein Taxi,|der Bus|nicht mehr|fährt|fahren
Sie hilft uns,|wir|sie|fragen|fragen
Ich schicke die Datei,|der Computer|wieder|funktioniert|funktionieren
Wir buchen die Reise,|wir|genug Geld|haben|haben
Ich komme früher,|du|mich|abholst|abholen
Er nimmt teil,|er|die Gebühr bezahlt|hat|haben
Wir fahren los,|alle|eingestiegen|sind|sein
Du darfst gehen,|du|fertig|bist|sein
Ich reserviere einen Tisch,|ihr|mitkommen|wollt|wollen
Wir machen die Arbeit,|sie|dringend|ist|sein
Ich unterschreibe,|ich|alles verstanden|habe|haben
Du bekommst Bescheid,|sich|der Termin|ändert|ändern
""")

gaps(34, 'wenn|wann|als|ob', """
Immer ___ ich Spätschicht habe, nehme ich den Bus.|wenn
___ beginnt morgen der Kurs? (direkte Frage)|Wann|Wann asks for a time; it does not introduce a repeated occasion.
Jedes Mal, ___ es regnet, bleiben wir drinnen.|wenn
___ ich morgen Zeit habe, besuche ich dich.|Wenn|A present/future occasion uses wenn, capitalized initially.
Ich weiß nicht, ___ der Zug abfährt. (Uhrzeit)|wann
Immer ___ wir Urlaub haben, fahren wir ans Meer.|wenn
Sag mir, ___ du Geburtstag hast. (Datum)|wann
___ die Kinder krank sind, arbeitet sie zu Hause. (regelmäßig)|Wenn|Repeated situations take wenn; initial capitalization is required.
Jeden Abend, ___ er nach Hause kommt, kocht er.|wenn
___ hast du heute Feierabend? (Frage)|Wann|Wann asks at what time an event occurs.
Immer ___ sie in Berlin ist, besucht sie uns.|wenn
Ich möchte wissen, ___ die Prüfung stattfindet. (Termin)|wann
___ wir uns sehen, sprechen wir Deutsch. (jedes Mal)|Wenn|Wenn introduces a repeated temporal occasion.
Sag bitte, ___ die Ferien anfangen. (Datum)|wann
Jedes Mal, ___ ich anrufe, ist besetzt.|wenn
___ kommt der nächste Bus? (Frage)|Wann|Use wann to ask for a particular time.
Immer ___ die Sonne scheint, öffnet er das Fenster.|wenn
___ du später kommst, bin ich zu Hause. (zukünftig)|Wenn|A future temporal occasion uses wenn.
Ich weiß, ___ der Laden öffnet. (Uhrzeit)|wann
Jeden Sonntag, ___ wir frühstücken, hören wir Radio.|wenn
""", {'wenn':'Wenn introduces a repeated occasion or a present/future temporal situation.', 'wann':'Wann asks for the time of an event, directly or indirectly.', 'als':'Als would introduce a single past occasion, not the repeated situation here.', 'ob':'Ob asks whether something happens, not when.'})

clauses(35, 'dass', """
Ich glaube,|der Kurs|morgen|beginnt|beginnen
Sie sagt,|sie|heute keine Zeit|hat|haben
Wir wissen,|der Bus|später|kommt|kommen
Er hofft,|die Prüfung|nicht zu schwer|ist|sein
Ich finde,|du|sehr gut|sprichst|sprechen
Sie merkt,|ihr|der Schlüssel|fehlt|fehlen
Wir denken,|die Wohnung|zu teuer|ist|sein
Er erklärt,|er|noch warten|muss|müssen
Ich höre,|ihr|nach Hamburg gezogen|seid|sein
Sie glaubt,|wir|die Rechnung bezahlt|haben|haben
Wir hoffen,|das Wetter|besser|wird|werden
Er sagt,|er|morgen mitkommen|kann|können
Ich weiß,|du|viel gearbeitet|hast|haben
Sie findet,|die Aufgabe|leicht|ist|sein
Wir merken,|die Kinder|müde|sind|sein
Er behauptet,|er|nichts gesehen|hat|haben
Ich hoffe,|die Reparatur|nicht lange|dauert|dauern
Sie erzählt,|sie|einen neuen Beruf|lernt|lernen
Wir wissen,|der Vertrag|noch|gilt|gelten
Er verspricht,|er|pünktlich|kommt|kommen
""")

clauses(36, 'ob', """
Ich frage,|noch|Plätze frei|sind|sein
Sie weiß nicht,|der Zug|pünktlich|kommt|kommen
Wir prüfen,|die Rechnung|richtig|ist|sein
Er möchte wissen,|du|Zeit|hast|haben
Ich bin unsicher,|das Geschäft|heute|öffnet|öffnen
Sie fragt nach,|wir|schon bezahlt|haben|haben
Wir wissen nicht,|er|mitkommen|kann|können
Er prüft,|die Tür|geschlossen|ist|sein
Ich frage mich,|sie|den Brief erhalten|hat|haben
Sie möchte wissen,|das Hotel|noch Zimmer|hat|haben
Wir fragen,|ihr|morgen|arbeitet|arbeiten
Er weiß nicht,|die Kinder|schon schlafen|wollen|wollen
Ich prüfe,|der Drucker|wieder|funktioniert|funktionieren
Sie fragt,|du|den Weg|kennst|kennen
Wir möchten wissen,|der Kurs|ausfallen|muss|müssen
Er fragt nach,|die Anmeldung|angekommen|ist|sein
Ich weiß nicht,|wir|hier parken|dürfen|dürfen
Sie prüft,|das Angebot|noch|gilt|gelten
Wir fragen uns,|es|morgen|regnet|regnen
Er möchte wissen,|sie|ihm helfen|kann|können
""")

gaps(37, 'wann|wo|warum|wie|wer|was|wohin|woher', """
Ich weiß nicht, ___ der Kurs beginnt. (Uhrzeit)|wann
Kannst du sagen, ___ die Apotheke ist? (Ort)|wo
Er fragt, ___ der Zug ausfällt. (Grund)|warum
Sie erklärt, ___ das Gerät funktioniert. (Art und Weise)|wie
Wir wissen nicht, ___ angerufen hat. (Person)|wer
Ich frage, ___ du bestellen möchtest. (Sache)|was
Er möchte wissen, ___ du fährst. (Ziel)|wohin
Sag mir, ___ dieses Paket kommt. (Herkunft)|woher
Ich frage, ___ die Prüfung stattfindet. (Datum)|wann
Sie weiß, ___ der Schlüssel liegt. (Ort)|wo
""", "The requested information determines the W-word '{answer}'; in an indirect question the finite verb stays at the end.")

for connector,context in [
 ('wann','Ich weiß nicht,|der Kurs|morgen|beginnt|beginnen'),
 ('wo','Sie fragt,|die Apotheke|genau|liegt|liegen'),
 ('warum','Wir verstehen nicht,|der Zug|heute|ausfällt|ausfallen'),
 ('wie','Er erklärt,|das Gerät|genau|funktioniert|funktionieren'),
 ('wer','Ich möchte wissen,|uns|heute|hilft|helfen'),
 ('was','Sie fragt,|du|morgen kaufen|möchtest|möchten'),
 ('wohin','Wir wissen nicht,|er|heute|fährt|fahren'),
 ('woher','Er fragt,|der Lärm|eigentlich|kommt|kommen'),
 ('wann','Sag mir,|die Prüfung|morgen|endet|enden'),
 ('wie','Ich frage,|man|die Datei speichern|kann|können'),
]:
    clauses(37,connector,context)

for adverb in ['deshalb','deswegen','daher','darum']:
    for cause, subject, verb, rest in [
        ('Der Zug fällt aus.', 'wir', 'nehmen', 'den Bus'),
        ('Es regnet.', 'ich', 'bleibe', 'zu Hause'),
        ('Die Miete ist hoch.', 'sie', 'sucht', 'eine andere Wohnung'),
        ('Er ist krank.', 'er', 'geht', 'zum Arzt'),
        ('Wir haben wenig Zeit.', 'wir', 'fahren', 'sofort los')]:
        correct = f'{verb} {subject} {rest}'
        LESSONS.setdefault(38, []).append(question(f'{cause} {adverb.capitalize()} ___.', correct,
            [f'{subject} {verb} {rest}',f'{subject} {rest} {verb}',f'{verb} {rest} {subject}'],
            f"{adverb.capitalize()} occupies the first position in a main clause, so '{verb}' must follow immediately.", 'Choose the neutral main-clause order.'))

gaps(39, 'auf|über|für|an|um|bei|mit|von', """
Ich interessiere mich ___ den Kurs.|für
Sie freut sich ___ den Urlaub nächste Woche. (Vorfreude)|auf
Wir freuen uns ___ das Geschenk, das schon hier liegt.|über
Er erinnert sich ___ die Reise.|an
Ich kümmere mich ___ die Kinder.|um
Sie beschwert sich ___ den Lärm. (Thema)|über
Wir bedanken uns ___ die Hilfe. (Grund)|für
Er entschuldigt sich ___ der Kollegin. (Person)|bei
Ich bereite mich ___ die Prüfung vor.|auf
Sie bewirbt sich ___ eine Stelle.|um
Wir unterhalten uns ___ den Film. (Thema)|über
Er beschäftigt sich ___ Grammatik.|mit
Ich verabschiede mich ___ meinen Gästen.|von
Sie gewöhnt sich ___ den neuen Alltag.|an
Wir ärgern uns ___ die Verspätung.|über
Er erkundigt sich ___ der Mitarbeiterin. (Ansprechperson)|bei
Ich treffe mich ___ einem Freund.|mit
Sie entscheidet sich ___ das günstigere Angebot.|für
Wir verlassen uns ___ deine Zusage.|auf
Er bemüht sich ___ eine Lösung.|um
""", "This reflexive verb is learned with the fixed preposition '{answer}'; retain the whole verb-preposition frame.")

gaps(40, 'jemand|jemanden|jemandem|niemand|niemanden|niemandem|etwas|nichts', """
___ hat geklingelt; ich habe eine Person gesehen.|Jemand|Jemand refers to an unspecified person as subject; it is capitalized initially.
Ich sehe ___ im Flur. (eine unbekannte Person; mit Kasusendung)|jemanden
Sie hilft ___. (einer unbekannten Person; mit Kasusendung)|jemandem
Hier ist ___; das Zimmer ist leer.|niemand
Ich kenne hier ___. (keine Person; mit Kasusendung)|niemanden
Er vertraut ___. (keiner Person; mit Kasusendung)|niemandem
Hat ___ meinen Schlüssel gesehen? (eine Person)|jemand
Wir suchen ___. (eine Person; mit Kasusendung)|jemanden
Ich spreche mit ___. (einer Person; mit Kasusendung)|jemandem
___ war zu Hause; alle waren weg.|Niemand|Niemand is the subject meaning no person; capitalize it initially.
Die Polizei hat ___ gefunden. (keine Person; mit Kasusendung)|niemanden
Sie hat ___ davon erzählt. (keiner Person; mit Kasusendung)|niemandem
Ich möchte ___ trinken. (eine Sache)|etwas
In der leeren Schachtel ist ___. (keine Sache)|nichts
___ wartet vor der Tür. (eine Person)|Jemand|Jemand is the nominative subject, capitalized at the start.
Wir brauchen ___ für die Arbeit. (eine Person; mit Kasusendung)|jemanden
Der Mantel gehört ___. (einer unbekannten Person; mit Kasusendung)|jemandem
___ muss mehr bezahlen; alles ist kostenlos.|Niemand|Niemand is a subject referring to no person.
Ich habe ___ angerufen. (keine Person; mit Kasusendung)|niemanden
Ich bin mit ___ verabredet. (keiner Person; mit Kasusendung)|niemandem
""", {'jemand':'Jemand is nominative and refers to a person.', 'jemanden':'The explicitly inflected accusative form is jemanden; the verb requires an object in accusative.', 'jemandem':'The explicitly inflected dative form is jemandem.', 'niemand':'Niemand is the nominative subject meaning no one.', 'niemanden':'The explicitly inflected accusative negative person pronoun is niemanden.', 'niemandem':'The explicitly inflected dative negative person pronoun is niemandem.', 'etwas':'Etwas refers to an unspecified thing, rather than a person.', 'nichts':'Nichts means no thing, unlike niemand for no person.'})

gaps(41, 'welcher|welche|welches|welchen|welchem', """
Hier sind zwei Mäntel. ___ gefällt dir? (der Mantel; Frage)|Welcher|A masculine nominative pronoun is welcher; capitalize the question's first word.
Du brauchst Stifte? Ich habe ___. (unbestimmte Menge)|welche
Von den Kleidern: ___ nimmst du? (das Kleid; Akkusativ)|Welches|A neuter accusative question pronoun is welches, capitalized initially.
Es gibt mehrere Busse. Mit ___ fahren wir? (Singular)|welchem
Von den Taschen: ___ gehört dir? (die Tasche)|Welche|The feminine nominative question form is welche.
Ich brauche Klebstoff. Hast du ___? (unbestimmte Menge; der Klebstoff)|welchen
Wir brauchen Milch. Hast du ___? (unbestimmte Menge)|welche
Es gibt mehrere Geräte. ___ funktioniert? (das Gerät; Singular)|Welches|Neuter nominative uses welches.
Die Schuhe sind schön. ___ kaufst du? (Plural)|Welche|Plural accusative uses welche.
Ich brauche einen Stift. Mit ___ schreibst du? (Singular)|welchem
Wir suchen Bücher. Hier liegen ___. (einige)|welche
Hier sind zwei Frauen. Mit ___ hast du gesprochen? (Singular)|welcher
Es gibt mehrere Züge. ___ fährt zuerst? (der Zug)|Welcher|A masculine nominative standalone pronoun is welcher.
Ich suche frisches Brot. Hast du ___? (unbestimmte Menge)|welches
Diese Äpfel sind reif. Ich nehme ___. (einige)|welche
Hier stehen zwei Wagen. ___ leihst du mir? (der Wagen)|Welchen|Masculine accusative takes welchen.
Das sind die Farben. Mit ___ malst du? (Plural)|welchen
Es gibt zwei Schulen. ___ besuchst du? (die Schule)|Welche|Feminine accusative uses welche.
Ich habe Papier. Brauchst du ___? (unbestimmte Menge)|welches
Die Schlüssel liegen dort. ___ ist deiner? (der Schlüssel)|Welcher|The pronoun replaces a masculine nominative noun, so it is welcher.
""", "The standalone form '{answer}' agrees with the omitted noun in gender/number and takes the case required in its own clause.")

gaps(42, 'hätte|hätten|wäre|wären|könnte|könnten|könntest|hättest', """
Ich ___ gern einen Termin. (haben, höflich)|hätte
___ Sie bitte das Fenster öffnen? (können, höflich)|Könnten|Formal Sie takes könnten; initial capitalization is required.
Es ___ nett, wenn Sie kurz warteten. (sein)|wäre
Wir ___ gern zwei Einzelzimmer. (haben)|hätten
___ du mir bitte helfen? (können)|Könntest|The polite du form is könntest.
Ich ___ Ihnen morgen Bescheid geben. (können)|könnte
___ Sie mit einem späteren Termin zufrieden? (sein)|Wären|Formal Sie uses wären in this tentative question.
___ du kurz Zeit für mich? (haben, höflich)|Hättest|Hättest is the tentative du form of haben.
Wir ___ Ihnen einen anderen Tag anbieten. (können)|könnten
Ein ruhiges Zimmer ___ mir lieber. (sein)|wäre
Ich ___ noch eine Frage. (haben, höflich)|hätte
___ Sie etwas Geduld? (haben, höflich)|Hätten|Formal Sie takes hätten for a polite request.
Das ___ eine gute Lösung. (sein, vorsichtig)|wäre
___ du die Rechnung prüfen? (können, höflich)|Könntest|Könntest is Konjunktiv II for a polite informal request.
Wir ___ gern einen Tisch am Fenster. (haben)|hätten
Ich ___ morgen vorbeikommen. (können, vorsichtig)|könnte
___ Sie so freundlich, mich anzurufen? (sein)|Wären|Wären Sie so freundlich is a polite formal request frame.
___ du lieber einen anderen Termin? (haben)|Hättest|The tentative du form is hättest.
___ Sie bitte etwas langsamer sprechen? (können)|Könnten|Könnten Sie expresses polite possibility as a request.
Ich ___ Ihnen sehr dankbar. (sein)|wäre
""", "The requested Konjunktiv II form '{answer}' makes the preference or request tentative and agrees with the subject.")

fraction_labels = {
 'half':('One of two equal parts', 'Hälfte or ein Halb denotes one half, 1/2, rather than a rank.'),
 'third':('One of three equal parts', 'Ein Drittel is 1/3 of the whole.'),
 'quarter':('One of four equal parts', 'Ein Viertel is 1/4 of a quantity; no clock time is meant here.'),
 'threequarters':('Three of four equal parts', 'Drei Viertel denotes 3/4 of the stated whole.'),
 'rank':('A position in a sequence', 'An ordinal such as dritte identifies rank, not a fraction.'),
}
meanings(43, """
Die Hälfte des Kuchens ist übrig.|half
Ein Drittel der Gruppe fehlt.|third
Ein Viertel des Preises ist bezahlt.|quarter
Drei Viertel der Plätze sind besetzt.|threequarters
Das ist der dritte Vorschlag.|rank
Wir teilen die Hälfte des Brotes.|half
Ein Drittel der Strecke ist geschafft.|third
Ein Viertel der Einwohner wohnt hier.|quarter
Drei Viertel des Tages sind vorbei.|threequarters
Sie wohnt im vierten Stock.|rank
Die Hälfte der Miete zahlt er.|half
Ein Drittel des Gartens gehört ihr.|third
Ein Viertel der Menge reicht.|quarter
Drei Viertel der Antworten sind richtig.|threequarters
Er ist der zweite Bewerber.|rank
Ein halbes Kilo Äpfel reicht.|half
Ein Drittel des Geldes bleibt übrig.|third
Ein Viertel Liter Milch fehlt.|quarter
Drei Viertel des Weges liegen hinter uns.|threequarters
Der erste Abschnitt ist kurz.|rank
""", fraction_labels, 'Which quantity or sequence relation is expressed?')

gaps(44, 'montags|dienstags|mittwochs|donnerstags|freitags|samstags|sonntags|morgens|abends|täglich|werktags', """
Jeden Montag lerne ich. Ich lerne ___.|montags
Jeden Dienstag arbeite ich. Ich arbeite ___.|dienstags
Jeden Mittwoch laufe ich. Ich laufe ___.|mittwochs
Jeden Donnerstag koche ich. Ich koche ___.|donnerstags
Jeden Freitag telefoniere ich. Ich telefoniere ___.|freitags
Jeden Samstag kaufe ich ein. Ich kaufe ___ ein.|samstags
Jeden Sonntag schlafe ich lange. Ich schlafe ___ lange.|sonntags
Jeden Morgen trinke ich Tee. Ich trinke ___ Tee.|morgens
Jeden Abend lese ich. Ich lese ___.|abends
Jeden Tag übe ich. Ich übe ___.|täglich
An Werktagen ist geöffnet. Es ist ___ geöffnet.|werktags
Der Kurs ist jeden Montag. Der Kurs ist ___.|montags
Wir treffen uns jeden Dienstag. Wir treffen uns ___.|dienstags
Sie kommt jeden Mittwoch. Sie kommt ___.|mittwochs
Er arbeitet jeden Donnerstag. Er arbeitet ___.|donnerstags
Wir fahren jeden Freitag. Wir fahren ___.|freitags
Der Markt ist jeden Samstag. Der Markt ist ___.|samstags
Das Museum ist jeden Sonntag offen. Es ist ___ offen.|sonntags
Sie läuft jeden Morgen. Sie läuft ___.|morgens
Wir üben jeden Tag. Wir üben ___.|täglich
""", "The recurring-time adverb '{answer}' expresses the repeated schedule stated in the first sentence and is written lowercase inside the sentence.")

counts = [(1,'einmal'),(2,'zweimal'),(3,'dreimal'),(4,'viermal'),(5,'fünfmal'),(6,'sechsmal'),(7,'siebenmal'),(8,'achtmal'),(9,'neunmal'),(10,'zehnmal')]
for n, word in counts:
    alternatives = [w for m,w in counts if m != n][:3]
    for prompt in [f'Ich habe genau {n} {"Versuch" if n==1 else "Versuche"} gemacht. Ich habe es ___ versucht.', f'Sie übt {n} Mal pro Woche. Sie übt ___ pro Woche.']:
        LESSONS.setdefault(45, []).append(question(prompt, word, alternatives,
            f"{word.capitalize()} counts {n} occurrence(s); pro Woche makes the second pattern a weekly frequency.", 'Choose the matching repetition count.'))

factors = [(1,'einfach'),(2,'zweifach'),(3,'dreifach'),(4,'vierfach'),(5,'fünffach'),(6,'sechsfach'),(7,'siebenfach'),(8,'achtfach'),(9,'neunfach'),(10,'zehnfach')]
for n, word in factors:
    alternatives = [w for m,w in factors if m != n][:3]
    for base in [2,5]:
        LESSONS.setdefault(46, []).append(question(f'Früher waren es {base} Liter, jetzt {base*n} Liter. Die Menge ist ___ so groß. (Faktor {n})',word, alternatives,
            f"{base*n} divided by {base} is {n}; '{word}' denotes this multiplicative factor, not how often an event happens.", 'Choose the multiplicative form.'))

enumeration = ['erstens','zweitens','drittens','viertens','fünftens','sechstens','siebtens','achtens','neuntens','zehntens']
for i, word in enumerate(enumeration,1):
    for noun in ['Grund','Schritt']:
        LESSONS.setdefault(47, []).append(question(f'Als Aufzählungsadverb für {noun} Nummer {i}: ___',word,
            [w for w in enumeration if w != word][:3],
            f"'{word}' introduces item {i} in a list; it is an adverb and receives no adjective ending.", 'Choose the enumeration adverb.'))

ordinals = [(3,'dritt'),(4,'viert'),(5,'fünft'),(6,'sechst'),(7,'siebt'),(8,'acht'),(9,'neunt'),(10,'zehnt'),(20,'zwanzigst'),(21,'einundzwanzigst')]
for n, stem in ordinals:
    for prompt, ending, why in [
        (f'Der ___ Vorschlag ist gut. (Nummer {n})','e','After der in nominative singular, the ordinal takes -e.'),
        (f'Mit dem ___ Vorschlag bin ich zufrieden. (Nummer {n})','en','After dem in dative, the ordinal takes -en.')]:
        LESSONS.setdefault(48, []).append(question(prompt, stem+ending,[stem+e for e in ['e','en','er','es','em'] if e!=ending][:3],why,'Complete the ordinal adjective.'))

gaps(49, 'des|der|dem|den|die|das', """
Das ist das Dach ___ Hauses.|des
Die Tasche ___ Frau ist rot.|der
Die Namen ___ Kinder stehen hier. (Plural)|der
Die Tür ___ Büros ist zu.|des
Der Titel ___ Buches ist lang.|des
Das Ende ___ Reise war schön.|der
Die Arbeit ___ Kollegen ist fertig. (Plural)|der
Die Öffnungszeiten ___ Geschäfts haben sich geändert.|des
Der Anfang ___ Films ist spannend.|des
Die Nummer ___ Wohnung fehlt.|der
Die Farbe ___ Autos gefällt mir.|des
Die Stimme ___ Lehrerin ist leise.|der
Die Rechte ___ Arbeitnehmer sind wichtig. (Plural)|der
Der Preis ___ Fahrrads ist hoch.|des
Die Dauer ___ Ausbildung beträgt drei Jahre.|der
Der Garten ___ Nachbarn ist groß. (ein Nachbar)|des
Die Meinung ___ Eltern ist klar.|der
Die Adresse ___ Hotels steht hier.|des
Der Inhalt ___ Tasche ist nass.|der
Die Ergebnisse ___ Prüfungen kommen morgen. (Plural)|der
""", {'des':'Masculine/neuter genitive singular uses des; regular masculine/neuter nouns add -(e)s, while weak nouns such as Nachbar take -n.', 'der':'Feminine singular and plural genitive use der; the following noun does not add a new genitive -s.', 'dem':'Dem marks dative, not possession in this genitive noun phrase.', 'den':'Den is not the genitive article required here.', 'die':'Die is not the required genitive article.', 'das':'Das is not the required genitive article.'})

gaps(50, 'des|der|dem|den|die|das|einer|einem|einen', """
Innerhalb ___ Woche bekommen Sie Bescheid. (eine Woche)|einer
Außerhalb ___ Stadt ist es ruhiger. (die Stadt)|der
Statt ___ Originals schicken wir eine Kopie. (das Original)|des
Anstatt ___ Autos nehmen wir das Rad. (das Auto)|des
Innerhalb ___ Gebäudes gilt Rauchverbot. (das Gebäude)|des
Außerhalb ___ Öffnungszeiten ist geschlossen. (Plural)|der
Statt ___ Rechnung bekam ich eine Mahnung. (die Rechnung)|der
Innerhalb ___ Monats muss es fertig sein. (der Monat)|des
Außerhalb ___ Geländes darf man parken. (das Gelände)|des
Anstatt ___ Lehrerin kommt der Leiter. (die Lehrerin)|der
Innerhalb ___ Grenzen gilt das Gesetz. (Plural)|der
Außerhalb ___ Arbeitszeit bin ich nicht erreichbar. (die Arbeitszeit)|der
Statt ___ Briefes schreibe ich eine E-Mail. (der Brief)|des
Innerhalb ___ Frist zahlen wir. (die Frist)|der
Außerhalb ___ Dorfes liegt ein See. (das Dorf)|des
Anstatt ___ Vertrags bekam sie ein Angebot. (der Vertrag)|des
Innerhalb ___ Jahres änderte sich alles. (das Jahr)|des
Außerhalb ___ Schule wartet die Gruppe. (die Schule)|der
Statt ___ Geschenke sammeln wir Geld. (Plural)|der
Innerhalb ___ Stunde ist er da. (eine Stunde)|einer
""", "The formal written model uses genitive after this preposition; '{answer}' matches the noun's gender and number.")
