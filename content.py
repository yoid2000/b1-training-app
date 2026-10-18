"""Authored question bank. Each row: prompt | correct | 3 distractors | English explanation.

Stable question IDs connect attempts and review history. Do not reuse an existing ID
for a different question when expanding the curriculum.
"""

import random
import json
from pathlib import Path

UNIT_DETAILS = {
    1: ("Perfekt mit haben", "Use haben plus a past participle to describe completed actions. The participle goes at the end.", "Beschreibe abgeschlossene Handlungen mit haben und dem Partizip II. Das Partizip steht am Satzende."),
    2: ("Perfekt mit sein", "Use sein for many changes of place or state and for bleiben. Learn each verb with its auxiliary.", "Viele Verben der Orts- oder Zustandsveränderung und bleiben bilden das Perfekt mit sein. Lerne das Hilfsverb immer mit."),
    3: ("Starke und gemischte Partizipien", "Practise irregular past participles, including vowel changes and mixed forms such as gebracht and gedacht.", "Übe unregelmäßige Partizipien mit Vokalwechsel und gemischte Formen wie gebracht und gedacht."),
    4: ("Partizipien mit Präfixen", "Separable prefixes usually put ge- between prefix and stem. Inseparable prefixes such as be- and ver- do not add ge-.", "Bei trennbaren Präfixen steht ge- meist zwischen Präfix und Stamm. Untrennbare Präfixe wie be- und ver- erhalten kein ge-."),
    5: ("Partizipien auf -iert", "Verbs ending in -ieren form their participle with -iert and no ge-. Similar-looking verbs may follow other patterns.", "Verben auf -ieren bilden das Partizip mit -iert ohne ge-. Ähnlich aussehende Verben können anderen Mustern folgen."),
    6: ("Sein und haben früher", "Describe past situations with war and hatte. Match the ending to every person, including plural and formal Sie.", "Beschreibe frühere Situationen mit war und hatte. Achte auf die Endungen bei allen Personen und bei der Höflichkeitsform Sie."),
    7: ("Modalverben im Präteritum", "Use konnte, musste, durfte, sollte, wollte and mochte for past ability, necessity, permission and wishes.", "Verwende konnte, musste, durfte, sollte, wollte und mochte für Fähigkeiten, Pflichten, Erlaubnis und Wünsche in der Vergangenheit."),
    8: ("Kommen und sagen früher", "Tell a short past story with kam and sagte. Kommen is strong; sagen takes regular past-tense endings.", "Erzähle eine kurze Geschichte mit kam und sagte. Kommen ist stark; sagen hat regelmäßige Präteritumendungen."),
    9: ("Nomen im Dativ", "Use dem, der, dem and den in the dative. Plural nouns usually add -n unless they already end in -n or -s.", "Verwende dem, der, dem und den im Dativ. Pluralnomen erhalten meist -n, außer wenn sie schon auf -n oder -s enden."),
    10: ("Verben mit Dativ", "Learn verbs such as gefallen, fehlen, folgen, begegnen and zuhören with their dative objects.", "Lerne Verben wie gefallen, fehlen, folgen, begegnen und zuhören mit ihrem Dativobjekt."),
    11: ("Personalpronomen im Dativ", "Replace dative noun phrases with mir, dir, ihm, ihr, uns, euch, ihnen or formal Ihnen.", "Ersetze Dativgruppen durch mir, dir, ihm, ihr, uns, euch, ihnen oder die Höflichkeitsform Ihnen."),
    12: ("Dativ und Akkusativ", "With geben, schicken and similar verbs, the recipient takes dative and the thing takes accusative.", "Bei geben, schicken und ähnlichen Verben steht der Empfänger im Dativ und die Sache im Akkusativ."),
    13: ("Reihenfolge der Objekte", "In neutral word order, two nouns take dative before accusative, two unstressed pronouns accusative before dative. A pronoun usually precedes a noun.", "In neutraler Wortstellung steht bei zwei Nomen Dativ vor Akkusativ, bei zwei unbetonten Pronomen Akkusativ vor Dativ. Ein Pronomen steht meist vor einem Nomen."),
    14: ("Possessivartikel im Dativ", "Add -em, -er or -en to possessive determiners according to the gender and number of the possessed noun.", "Ergänze Possessivartikel mit -em, -er oder -en. Entscheidend sind Genus und Numerus des Nomens."),
    15: ("Reflexivverben im Akkusativ", "Use mich, dich, sich, uns and euch for reflexive actions without a separate accusative object.", "Verwende mich, dich, sich, uns und euch bei reflexiven Handlungen ohne zusätzliches Akkusativobjekt."),
    16: ("Reflexivpronomen im Dativ", "Use mir or dir when the reflexive action has another accusative object: Ich wasche mir die Hände.", "Verwende mir oder dir, wenn es ein weiteres Akkusativobjekt gibt: Ich wasche mir die Hände."),
    17: ("Einander und seine Verbindungen", "Express mutual actions with einander and compounds such as miteinander, füreinander and aufeinander.", "Drücke gegenseitige Handlungen mit einander und Verbindungen wie miteinander, füreinander und aufeinander aus."),
    18: ("Wechselpräpositionen und Fälle", "Use dative for a location and accusative for a destination with an, auf, hinter, in, neben, über, unter, vor and zwischen.", "Bei an, auf, hinter, in, neben, über, unter, vor und zwischen steht der Ort im Dativ und das Ziel im Akkusativ."),
    19: ("Position oder Bewegung", "Distinguish liegen/legen, stehen/stellen and sitzen/setzen. Hängen also changes its past form between position and placement.", "Unterscheide liegen/legen, stehen/stellen und sitzen/setzen. Auch hängen hat je nach Lage oder Handlung verschiedene Vergangenheitsformen."),
    20: ("Richtung: her und hin", "Her- points toward the speaker and hin- away. Practise directions inside, outside, up and down, plus common shortened forms.", "Her- zeigt zum Sprecher, hin- vom Sprecher weg. Übe Richtungen nach innen, außen, oben und unten sowie häufige Kurzformen."),
}

QUESTION_BANK = {}


def add(unit_id, rows, instruction="Complete the sentence."):
    questions = []
    for index, line in enumerate(rows.strip().splitlines(), 1):
        prompt, correct, a, b, c, explanation = [part.strip() for part in line.split("|")]
        options = [correct, a, b, c]
        assert len(set(options)) == 4, (unit_id, index)
        random.Random(f"{unit_id}-{index}").shuffle(options)
        questions.append({"id": f"u{unit_id:03d}-q{index:02d}", "unit_id": unit_id,
                          "prompt": prompt, "options": options, "correct_index": options.index(correct),
                          "explanation": explanation, "instruction": instruction})
    assert len(questions) == 20, (unit_id, len(questions))
    QUESTION_BANK[unit_id] = questions


add(1, """
Ich ___ den Vertrag geprüft. | habe | bin | ist | hat | Prüfen describes an action and forms the Perfekt with haben; ich takes habe.
Du ___ die Rechnung kontrolliert. | hast | bist | hat | seid | Kontrollieren takes haben, and the du form is hast.
Die Angestellte ___ den Kunden informiert. | hat | ist | haben | seid | The singular subject takes hat; informieren forms its Perfekt with haben.
Wir ___ die Wohnung geputzt. | haben | sind | hat | habt | Putzen takes haben; wir requires haben.
Ihr ___ an der Ampel gewartet. | habt | seid | hat | hast | Warten takes haben, even though it describes remaining in one place; ihr takes habt.
Die Nachbarn ___ die Musik gehört. | haben | sind | hat | habt | Hören takes haben; the plural subject requires haben.
Ich habe den Anzug ___. | gekauft | kaufen | gekaufen | kaufte | Kaufen is regular: ge- plus kauf- plus -t gives gekauft.
Wir haben lange ___. | gearbeitet | arbeiten | gearbeiten | arbeitete | Arbeiten adds -et in the participle because its stem ends in -t: gearbeitet.
Sie hat den Vertrag genau ___. | geprüft | prüfen | geprüfung | prüfte | The regular past participle of prüfen is geprüft.
Habt ihr die Tür ___? | geöffnet | öffnen | geöffnen | öffnete | Öffnen forms the past participle geöffnet with the ending -et.
Er hat seine Meinung ___. | geändert | ändern | geändern | änderte | Ändern forms the regular participle geändert.
Ich habe mich über den Lärm ___. | geärgert | ärgern | geärgern | ärgerte | The past participle of ärgern is geärgert, including in sich ärgern.
Was ___ du gestern gemacht? | hast | bist | hat | haben | A question still needs the conjugated auxiliary hast with du.
___ ihr den Betrag geprüft? | Habt | Seid | Hat | Haben | With ihr, prüfen uses habt at the start of a yes/no question.
Die Mitarbeiterin hat acht Stunden ___. | gearbeitet | arbeiten | gearbeitet hat | arbeitet | The auxiliary is already present; only the past participle gearbeitet belongs in the blank.
Wir haben auf den Bus ___. | gewartet | warten | gewarten | warteten | Warten is regular and needs -et after the stem ending in -t: gewartet.
Ich ___ den ganzen Abend telefoniert. | habe | bin | werde | war | Telefonieren forms the Perfekt with haben, so ich habe is required here.
Haben Sie die Unterlagen ___? | kopiert | kopieren | gekopiert | kopierte | Kopieren is an -ieren verb and forms its participle kopiert without ge-.
Gestern ___ wir im Büro diskutiert. | haben | sind | hat | habt | The Perfekt of diskutieren uses haben; wir takes haben even after an initial time expression.
Welche Perfektform ist richtig? | Ich habe den Vertrag geprüft. | Ich bin den Vertrag geprüft. | Ich habe den Vertrag prüfen. | Ich hat den Vertrag geprüft. | Prüfen takes haben; ich requires habe, and geprüft is the participle at the end.
""")

add(2, """
Wir ___ rechtzeitig umgestiegen. | sind | haben | seid | hat | Umsteigen expresses a change from one vehicle to another and takes sein; wir takes sind.
Ich ___ zur Apotheke gegangen. | bin | habe | ist | hat | Gehen describes a change of place and forms its Perfekt with sein.
Du ___ spät angekommen. | bist | hast | sind | hat | Ankommen takes sein; the du form is bist.
Der Aufzug ___ nach oben gefahren. | ist | hat | haben | sind | Intransitive fahren describing movement to another place uses sein.
Die Kinder ___ schnell eingeschlafen. | sind | haben | ist | seid | Einschlafen is a change of state, so it uses sein with a plural subject.
Ihr ___ lange in Berlin geblieben. | seid | habt | sind | ist | Bleiben is an important sein verb even though it does not describe movement.
Sie (Singular) ___ früh aufgewacht. | ist | hat | sind | haben | Aufwachen expresses a change from sleep to wakefulness and takes sein.
Wir ___ die Koffer ausgepackt. | haben | sind | seid | ist | Auspacken is an action with an object and takes haben, unlike movement verbs here.
Ich ___ im Zug gelesen. | habe | bin | ist | sind | Lesen takes haben; being in a moving train does not change the verb's auxiliary.
Der Zug ___ um neun abgefahren. | ist | hat | sind | haben | Abfahren describes departure and takes sein; der Zug is singular.
___ du schon zurückgekommen? | Bist | Hast | Sind | Hat | Zurückkommen takes sein; a question with du starts with Bist.
Wir ___ gestern zu Hause geblieben. | sind | haben | ist | seid | Bleiben forms the Perfekt with sein; wir takes sind.
Die Suppe ___ kalt geworden. | ist | hat | sind | haben | Werden describes a change of state and uses sein; the participle here is geworden.
Ich ___ mich nach der Reise ausgeruht. | habe | bin | ist | sind | Sich ausruhen forms the Perfekt with haben, even after a journey.
Ihr ___ an der nächsten Haltestelle ausgestiegen. | seid | habt | sind | hat | Aussteigen takes sein and ihr requires seid.
Meine Schwester ___ nach Köln umgezogen. | ist | hat | haben | seid | Umziehen meaning to move home takes sein; changing clothes would use haben.
Das Glas ___ vom Tisch gefallen. | ist | hat | sind | haben | Fallen expresses a change of position and takes sein.
Wir ___ auf den Anschluss gewartet. | haben | sind | ist | seid | Warten takes haben; the travel context does not make it a sein verb.
Die Gäste ___ sehr spät gekommen. | sind | haben | ist | seid | Kommen takes sein, and die Gäste is plural.
Welche Perfektform ist richtig? | Sie ist Ärztin geworden. | Sie hat Ärztin geworden. | Sie ist Ärztin gewordet. | Sie haben Ärztin geworden. | Becoming a doctor is a change of state: werden uses ist geworden with a singular subject.
""")

add(3, """
Sie hat den Termin ___. | vergessen | gevergessen | vergesst | vergisst | Vergessen is strong and has the participle vergessen; its inseparable prefix prevents extra ge-.
Ich habe an dich ___. | gedacht | gedenkt | gedanken | denken | Denken is a mixed verb: its participle is gedacht, with a changed stem and -t.
Er hat die Batterie ___. | gebracht | gebringt | gebringen | bringen | Bringen is mixed and forms the participle gebracht.
Wir haben die Ausstellung ___. | gesehen | geseht | gesieht | sehen | Sehen is strong; the past participle is gesehen.
Du hast den Brief ___. | geschrieben | geschreibt | geschriebt | schreiben | Schreiben changes its vowel and forms the strong participle geschrieben.
Ich habe das Buch ___. | gelesen | gelest | geliest | lesen | The strong participle of lesen is gelesen.
Sie hat den Schlüssel ___. | gefunden | gefindet | gefinden | finden | Finden changes its stem vowel in the participle gefunden.
Wir haben den Kuchen selbst ___. | gebacken | gebackteten | gebäckt | backen | The standard past participle of backen is gebacken.
Er hat mir Bescheid ___. | gegeben | gegebt | gegibt | geben | Geben is strong and forms the participle gegeben.
Ich habe den alten Mantel ___. | behalten | gebehalten | behaltet | behaltenen | Behalten has the strong participle behalten and adds no ge- after be-.
Sie hat den Preis ___. | genannt | genennt | genennen | nennen | Nennen is mixed: the changed stem nann- takes -t in genannt.
Wir haben uns schon lange ___. | gekannt | gekennt | gekennen | kennen | Kennen is mixed and has the participle gekannt.
Ihr habt zu viel Benzin ___. | gebraucht | gebrauchen | gegebraucht | brauchte | Brauchen forms the regular participle gebraucht; not every past participle is strong.
Ich habe den Berg auf dem Foto ___. | erkannt | geerkannt | erkennet | erkennen | Erkennen has the mixed participle erkannt and no added ge- after er-.
Du hast das Fenster ___. | geschlossen | geschließt | geschließen | schließen | Schließen forms the strong participle geschlossen.
Sie hat einen neuen Anzug ___. | getragen | getragt | geträgt | tragen | Tragen has the strong participle getragen with the ending -en.
Wir haben die Fähre ___. | genommen | genehmt | genimmt | nehmen | Nehmen changes its stem and forms the participle genommen.
Er hat das Wasser ___. | getrunken | getrinkt | getrinken | trinken | Trinken changes i to u in the participle getrunken.
Ich habe eine gute Beratung ___. | bekommen | gebekommen | bekommt | bekommte | Bekommen is strong and its be- prefix prevents an added ge-.
Die Kinder haben im Garten ___. | gesessen | gesitzt | gesitzen | sitzen | Sitzen has the strong participle gesessen; the stem changes from sitz- to sess-.
""")

add(4, """
Er hat die Rechnung ___. | bezahlt | gebezahlt | bezahlte | bezahlen | Be- is inseparable, so bezahlen forms bezahlt without ge-.
Ich habe den Betrag ___. | eingetragen | geeintragen | eintragen | eintragt | Eintragen is separable: ge- goes between ein- and the strong participle stem.
Wir haben das Licht ___. | ausgemacht | geausmacht | ausmacht | ausmachen | Ausmachen is separable, so the participle is aus-ge-macht.
Sie hat die Tür ___. | zugemacht | gezumacht | zumacht | zumachen | Zu- separates from machen; the participle puts ge- in the middle.
Du hast die Bewerbung ___. | abgeschickt | geabschickt | abschickt | abschicken | Abschicken is separable and forms ab-ge-schickt.
Ich habe den Bildschirm ___. | eingeschaltet | geeinschaltet | einschaltet | einschalten | Einschalten is separable: ein-ge-schaltet.
Wir haben den Zug ___. | verpasst | geverpasst | verpasste | verpassen | Ver- is inseparable, so verpassen has no ge- in its participle.
Sie hat die Frage ___. | beantwortet | gebeantwortet | beantwort | beantworten | Beantworten has an inseparable be- prefix and takes the ending -et.
Er hat mir alles ___. | erklärt | geerklärt | erkläret | erklären | Er- is inseparable, so erklären forms erklärt without ge-.
Ich habe den Besuch ___. | vorbereitet | gevorbereitet | vorgebereitet | vorbereiten | Vorbereiten is separable, but the base bereiten already has inseparable be-, so no ge- is added.
Wir haben den Raum ___. | aufgeräumt | geaufräumt | aufräumt | aufräumen | Aufräumen is separable and places ge- between auf- and räumt.
Sie hat das Blatt ___. | zerrissen | gezerrissen | zergerissen | zerreißen | Zer- is inseparable; the strong participle of zerreißen is zerrissen.
Du hast die Einladung ___. | erhalten | geerhalten | ergehalten | erhaltet | Erhalten has an inseparable er- prefix and the strong participle erhalten.
Ich habe die Nachricht ___. | empfangen | geempfangen | empfängt | empfangt | Emp- is inseparable, so the participle is empfangen without ge-.
Wir haben die Bluse ___. | anprobiert | angeprobiert | geanprobiert | anprobieren | Anprobieren is separable but its -ieren base forms probiert without ge-.
Sie hat den Vertrag ___. | abgeschlossen | geabschlossen | abschließt | abschließen | Abschließen is separable and strong: ab-ge-schlossen.
Er hat die Tasche ___. | ausgepackt | geauspackt | auspackt | auspacken | Auspacken is separable and forms aus-ge-packt.
Ich habe die Geschichte ___. | erzählt | geerzählt | ergezählt | erzählen | Er- is inseparable and erzählen forms erzählt without ge-.
Wir haben das Wort ___. | missverstanden | gemissverstanden | missgeverstanden | missverstehen | Missverstehen has inseparable prefixes and uses missverstanden without ge-.
Sie hat sich über den Besuch ___. | beschwert | gebeschwert | beschweren | beschwerte | Beschweren has inseparable be- and forms beschwert, also in the reflexive construction.
""")

add(5, """
Wir haben die Heizung ___. | repariert | gerepariert | reparieren | reparierte | Reparieren ends in -ieren, so its participle is repariert without ge-.
Ich habe einen Tisch ___. | reserviert | gereserviert | reservieren | reservierte | Reservieren forms reserviert with -iert and no ge-.
Sie hat den Brief ___. | kopiert | gekopiert | kopieren | kopierte | Kopieren follows the -ieren pattern: kopiert.
Wir haben im Büro ___. | diskutiert | gediskutiert | diskutieren | diskutierte | Diskutieren forms diskutiert without ge-, even in a longer sentence.
Er hat Informatik ___. | studiert | gestudiert | studieren | studierte | Studieren ends in -ieren and forms studiert.
Ich habe die E-Mail-Adresse ___. | notiert | genotiert | notieren | notierte | Notieren forms the past participle notiert, without ge-.
Du hast den Drucker ___. | installiert | geinstalliert | installieren | installierte | Installieren uses -iert in its participle: installiert.
Ihr habt die Fahrt ___. | organisiert | georganisiert | organisieren | organisierte | Organisieren has the participle organisiert with no ge-.
Die Polizei hat den Verkehr ___. | kontrolliert | gekontrolliert | kontrollieren | kontrollierte | Kontrollieren is an -ieren verb and forms kontrolliert.
Ich habe dir zum Geburtstag ___. | gratuliert | gegratuliert | gratulieren | gratulierte | Gratulieren forms gratuliert; the dative recipient does not affect the participle.
Wir haben die Grammatik ___. | wiederholt | gewiederholt | wiederholen | wiederholte | Wiederholen meaning repeat is inseparable and forms wiederholt, another reason for having no ge-.
Sie hat die Kinder ___. | fotografiert | gefotografiert | fotografieren | fotografierte | Fotografieren ends in -ieren and forms fotografiert.
Er hat auf die Frage ___. | reagiert | gereagiert | reagieren | reagierte | Reagieren forms reagiert without ge-.
Ich habe die Rechnung ___. | korrigiert | gekorrigiert | korrigieren | korrigierte | Korrigieren forms korrigiert with the ending -iert.
Wir haben den Kuchen ___. | probiert | geprobiert | probieren | probierte | Probieren follows the -ieren rule and forms probiert.
Du hast die Nachricht ___. | ignoriert | geignoriert | ignorieren | ignorierte | Ignorieren forms ignoriert without adding ge-.
Ihr habt die Batterie ___. | kontrolliert | gekontrolliert | kontrollieren | kontrollierte | The participle kontrolliert stays the same for every subject.
Der Unfall ist gestern ___. | passiert | gepassiert | passieren | passierte | Passieren ends in -ieren and forms passiert without ge-; in this meaning it uses sein.
Die Kinder haben im Winter ___. | gefroren | friert | gefriert | frieren | Frieren is a strong verb, not an -ieren-pattern verb; its participle is gefroren.
Wir haben das Fest ___. | gefeiert | feiert | feieren | feierte | Feiern ends in -ern rather than the suffix -ieren, so it forms gefeiert with ge-.
""")

add(6, """
Früher ___ ich oft auf dem Dach. | war | waren | wart | warst | The ich form of sein in the Präteritum is war.
Gestern ___ du sehr müde. | warst | war | wart | waren | Sein takes -st with du in the past: du warst.
Die Diskussion ___ interessant. | war | waren | warst | wart | A singular third-person subject uses war.
Damals ___ wir direkte Nachbarn. | waren | war | wart | warst | The wir form of sein in the Präteritum is waren.
Letzte Woche ___ ihr dagegen. | wart | waren | war | warst | The ihr form is wart, without an extra -e-.
Die Kinder ___ schon dabei. | waren | war | wart | warst | A plural third-person subject takes waren.
Frau Roth, ___ Sie gestern im Büro? | waren | war | wart | warst | Formal Sie uses the plural verb form waren.
Ich ___ damals mehr Zeit. | hatte | hatten | hattest | hattet | The ich form of haben in the Präteritum is hatte.
Du ___ einen alten Wagen. | hattest | hatte | hatten | hattet | Haben takes -st with du: hattest.
Er ___ eine klare Meinung. | hatte | hatten | hattest | hattet | The third-person singular past form of haben is hatte.
Wir ___ eine lange Diskussion. | hatten | hatte | hattet | hattest | Wir takes hatten in the Präteritum.
Ihr ___ früher mehr Platz. | hattet | hatte | hatten | hattest | Ihr requires hattet, with the ending -et on hatt-.
Die Nachbarn ___ ein dickes Buch. | hatten | hatte | hattest | hattet | The plural subject die Nachbarn takes hatten.
Herr Klein, ___ Sie genug Diesel? | hatten | hatte | hattet | hattest | Formal Sie takes hatten, like the third-person plural.
___ du gestern dabei? | Warst | Wart | War | Waren | A yes/no question with du uses Warst at the beginning.
___ ihr damals einen Garten? | Hattet | Hatten | Hatte | Hattest | The ihr form remains hattet when it begins a question.
Meine Schwester und ich ___ krank. | waren | war | wart | warst | Meine Schwester und ich corresponds to wir, so the verb is waren.
Du und Paul ___ wenig Zeit. | hattet | hatten | hatte | hattest | Du und Paul corresponds to ihr, which takes hattet.
Es ___ damals sehr dunkel. | war | waren | warst | wart | Es is third-person singular and takes war.
___ wir früher mehr Geduld? | Hatten | Hattet | Hatte | Hattest | A question with wir uses hatten, the first-person plural past form.
""")

add(7, """
Gestern ___ ich wegen des Streiks warten. (müssen) | musste | müsste | musst | müssen | The factual past form is musste; müsste is Konjunktiv II, not the simple past.
Als Kind ___ du schon gut schwimmen. (können) | konntest | könntest | konnte | konnten | Können forms its Präteritum without an umlaut, and du takes -st.
Wir ___ gestern nicht hinausgehen. (dürfen) | durften | dürften | durfte | dürft | The past plural form of dürfen is durften, without an umlaut.
Ihr ___ den Bericht fertig machen. (sollen) | solltet | sollten | sollte | sollst | Ihr requires solltet; the other verb remains an infinitive.
Er ___ ein paar Dosen kaufen. (wollen) | wollte | wolltet | wollten | will | The third-person singular Präteritum of wollen is wollte.
Früher ___ ich diese Musik. (mögen) | mochte | möchte | mochten | mag | Mochte is the factual past of mögen; möchte expresses a present wish.
Die Kinder ___ drinnen bleiben. (müssen) | mussten | müsste | musste | müsst | The plural subject takes mussten in the past.
___ ihr die Einführung verstehen? (können, Vergangenheit) | Konntet | Könntet | Konnte | Konnten | Ihr takes konntet in the Präteritum; könntet is hypothetical.
Ich ___ früher kein eigenes Zimmer haben. (dürfen) | durfte | dürfe | dürft | durften | The ich form of dürfen in the Präteritum is durfte.
Du ___ dringend anrufen. (sollen, Vergangenheit) | solltest | sollte | solltet | sollen | Du takes solltest; the required phone call is expressed by the final infinitive.
Wir ___ ein eigenes Haus kaufen. (wollen, Vergangenheit) | wollten | wollte | wolltet | wolltest | Wir takes wollten in the Präteritum.
Ihr ___ als Kinder keinen Spinat. (mögen) | mochtet | mochte | mochten | möchtet | The factual past with ihr is mochtet; möchtet expresses a wish.
Sie (Singular) ___ gestern nicht kommen. (können) | konnte | könnte | konnten | konntet | A factual inability yesterday uses konnte with a singular subject.
___ du gestern lange arbeiten? (müssen) | Musstest | Müsstest | Musste | Musstet | The du form of müssen in the past is musstest, with no umlaut.
Die Teilnehmer ___ Fragen stellen. (dürfen, Vergangenheit) | durften | durfte | dürften | dürft | Die Teilnehmer is plural, so the past form is durften.
Wir mussten gestern lange ___. | warten | gewartet | wartet | warteten | A modal verb takes a bare infinitive at the end: mussten warten.
Er konnte die Antwort nicht ___. | finden | gefunden | findet | fand | Konnte combines with the infinitive finden, not a participle.
Sie wollte uns ihre Idee ___. | erklären | erklärt | erklärte | geerklärt | Wollte is conjugated; erklären stays in the infinitive.
Frau Weber, ___ Sie damals Auto fahren? (können) | konnten | konnte | konntet | könntet | Formal Sie requires konnten in the factual past.
Du und ich ___ früh aufstehen. (müssen, Vergangenheit) | mussten | musste | musstet | müsste | Du und ich is wir, so the past form is mussten.
""")

add(8, """
Gestern ___ ich spät nach Hause. (kommen) | kam | kamst | kamen | kommt | The ich form of kommen in the Präteritum is kam.
Du ___ endlich zur Besprechung. (kommen, Vergangenheit) | kamst | kam | kamt | kamen | The strong past stem kam- takes -st with du.
Der Enkel ___ aus dem Erdgeschoss. (kommen, Vergangenheit) | kam | kamen | kommt | kamst | A singular third-person subject takes kam.
Wir ___ direkt zum Empfang. (kommen, Vergangenheit) | kamen | kam | kamt | kommt | The wir form of kommen in the Präteritum is kamen.
Ihr ___ mit dem elektrischen Zug. (kommen, Vergangenheit) | kamt | kamen | kam | kamst | The ihr form is kamt, without an extra -e-.
Die Gäste ___ erst um neun. (kommen, Vergangenheit) | kamen | kam | kamt | kommt | Die Gäste is plural and takes kamen.
___ Sie gestern zu Fuß, Frau Klein? (kommen) | Kamen | Kamt | Kam | Kamst | Formal Sie takes kamen, including at the start of a question.
Ich ___ sofort Bescheid. (sagen, Vergangenheit) | sagte | sagten | sagtest | sagtet | Sagen is regular in the Präteritum: ich sagte.
Du ___ nichts über den Empfang. (sagen, Vergangenheit) | sagtest | sagte | sagtet | sagten | Du adds -st to sagte: sagtest.
Sie (Singular) ___ ihren Namen. (sagen, Vergangenheit) | sagte | sagten | sagtest | sagtet | Third-person singular uses sagte.
Wir ___ allen Einwohnern Bescheid. (sagen, Vergangenheit) | sagten | sagte | sagtet | sagtest | Wir takes sagten in the Präteritum.
Ihr ___ die Wahrheit. (sagen, Vergangenheit) | sagtet | sagten | sagte | sagtest | The ihr form of sagen in the past is sagtet.
Die Kinder ___ kein Wort. (sagen, Vergangenheit) | sagten | sagte | sagtet | sagtest | The plural subject takes sagten.
Was ___ Sie damals, Herr Meier? (sagen) | sagten | sagte | sagtet | sagtest | Formal Sie uses sagten.
Als er ankam, ___ er sofort Hallo. (sagen) | sagte | sagen | gesagt | sagtet | In a past narrative, the singular subject er takes sagte.
___ du gestern pünktlich? (kommen) | Kamst | Kamt | Kam | Kamen | A past question with du starts with kamst.
___ ihr der Nachbarin Bescheid? (sagen, Vergangenheit) | Sagtet | Sagten | Sagtest | Sagte | Ihr takes sagtet, also in question position.
Meine Schwester und ich ___ zusammen. (kommen, Vergangenheit) | kamen | kam | kamt | kamst | Meine Schwester und ich is wir, so use kamen.
Paul und du ___ nichts dazu. (sagen, Vergangenheit) | sagtet | sagten | sagte | sagtest | Paul und du corresponds to ihr and takes sagtet.
Welche Erzählung steht im Präteritum? | Sie kam später und sagte Bescheid. | Sie ist später gekommen und hat Bescheid gesagt. | Sie kommt später und sagt Bescheid. | Sie wird später kommen und Bescheid sagen. | Kam and sagte are simple past forms; the other options are perfect, present or future.
""")

add(9, """
Wir fahren mit ___ Fähre. (die Fähre) | der | dem | den | die | Mit requires dative; the feminine article die becomes der.
Der Fahrplan hängt neben ___ Eingang. (der Eingang; Ort) | dem | den | der | das | A fixed location after neben takes dative; masculine der becomes dem.
Ich spreche mit ___ Kindern. | den | die | dem | der | The dative plural article is den; Kindern already includes the dative -n.
Die Erlaubnis liegt bei ___ Chef. (der Chef) | dem | den | die | das | Bei requires dative; masculine der becomes dem.
Sie arbeitet in ___ Fabrik. (die Fabrik) | der | die | dem | den | A fixed workplace after in takes dative; feminine die becomes der.
Wir sitzen vor ___ Fenster. (das Fenster) | dem | das | den | der | A location after vor takes dative; neuter das becomes dem.
Ich fahre mit den ___. (der Bus; Plural) | Bussen | Busse | Bus | Busses | The plural Busse gains -n in the dative: mit den Bussen.
Er spricht mit den ___. (der Mitarbeiter; Plural) | Mitarbeitern | Mitarbeiter | Mitarbeiters | Mitarbeiteren | Plural Mitarbeiter gains the dative ending -n.
Sie fährt mit den ___. (das Auto; Plural) | Autos | Auton | Autosen | Auto | Plurals already ending in -s do not add a dative -n.
Wir helfen den ___. (die Frau; Plural) | Frauen | Fraun | Frauens | Frau | Frauen already ends in -n, so no additional dative ending is added.
Die Unterlagen sind in ___ Büro. (das Büro; Ort) | dem | den | der | die | In describes a location here, so the neuter dative article is dem.
Ich fahre zu ___ Ausstellung. (die Ausstellung) | der | dem | den | die | Zu always requires dative, so die Ausstellung becomes der Ausstellung.
Sie wohnt bei ___ Eltern. (Plural) | den | die | dem | der | Bei takes dative; plural Eltern takes den and already ends in -n.
Mit ___ Ermäßigung ist die Fahrt günstiger. (eine Ermäßigung) | einer | eine | einem | einen | The feminine dative form of eine is einer.
Er fährt mit ___ Fahrrad. (ein Fahrrad) | einem | einen | einer | ein | Fahrrad is neuter; ein becomes einem in the dative.
Wir sprechen mit ___ Freund. (ein Freund) | einem | einen | einer | eines | Freund is masculine and takes einem after mit.
Der Export hilft den ___. (das Unternehmen; Plural) | Unternehmen | Unternehmenn | Unternehmens | Unternehme | Unternehmen already ends in -n in the plural, so dative does not add another ending.
Sie erzählt von ___ Erfahrung. (eine Erfahrung) | einer | einen | einem | eine | Von requires dative; the feminine phrase is von einer Erfahrung.
Ich warte gegenüber ___ Apotheke. (die Apotheke) | der | die | den | dem | Gegenüber requires dative, so the feminine article is der.
Wir gehen mit den ___ zum Bahnhof. (der Freund; Plural) | Freunden | Freunde | Freund | Freunds | Freunde gains -n in the dative plural: den Freunden.
""")

add(10, """
Das Fest gefällt ___ Nachbarin. | der | die | den | das | Gefallen takes a dative experiencer; die Nachbarin becomes der Nachbarin.
Der Feuerwehrmann folgt ___ Wagen. | dem | den | der | das | Folgen requires dative, so der Wagen becomes dem Wagen.
Ich begegne ___ Lehrerin im Park. | der | die | dem | den | Begegnen takes dative; a feminine singular noun uses der.
Die Kinder hören ___ Großvater zu. | dem | den | der | das | Zuhören takes a dative listener's object: dem Großvater.
Die Ferien fehlen ___ Kindern. | den | die | dem | der | The people missing something are dative with fehlen: den Kindern.
Die Jacke passt ___ Mann. | dem | den | der | das | Passen takes the person in the dative: dem Mann.
Das Fernsehgerät gehört ___ Frau. | der | die | dem | den | Gehören takes a dative owner; feminine die changes to der.
Die Antwort fällt ___ Teilnehmer ein. | dem | den | der | das | With einfallen, the person who thinks of something is dative: dem Teilnehmer.
Das Essen schmeckt ___ Gästen. | den | die | dem | der | Schmecken takes a dative experiencer; the plural article is den.
Der Urlaub tut ___ Kollegin gut. | der | die | dem | den | Guttun takes dative; the person benefiting is der Kollegin.
Ich vertraue ___ Arzt. | dem | den | der | das | Vertrauen requires dative, so der Arzt becomes dem Arzt.
Wir gratulieren ___ Schwester. | der | die | dem | den | Gratulieren takes dative, giving der Schwester.
Die Kinder widersprechen ___ Lehrer. | dem | den | der | das | Widersprechen takes a dative object: dem Lehrer.
Die Einführung hilft ___ Teilnehmern. | den | die | dem | der | Helfen takes dative; the plural phrase is den Teilnehmern.
Der Rock steht ___ Frau gut. | der | die | dem | den | Stehen meaning to suit someone takes a dative person: der Frau.
Die Blumen gefallen ___ Eltern. | den | die | dem | der | Gefallen takes dative; Eltern is plural, so use den.
Ich antworte ___ Nachbarn. (Singular: der Nachbar) | dem | den | die | das | Antworten takes dative; the singular masculine phrase is dem Nachbarn.
Das Feuerzeug gehört ___ Kollegen. (Plural) | den | die | dem | der | Gehören takes dative; a plural owner takes den Kollegen.
Der Hund folgt ___ Frau bis zur Tür. | der | die | dem | den | Folgen takes dative regardless of the later destination phrase.
Welche Ergänzung passt zu zuhören? | dem Kind | das Kind | den Kind | der Kind | Zuhören requires dative; das Kind becomes dem Kind.
""")

add(11, """
Ich antworte dem Friseur. Ich antworte ___. | ihm | ihn | er | ihr | Dem Friseur is masculine dative and is replaced by ihm.
Das gehört der Nachbarin. Das gehört ___. | ihr | sie | ihn | ihm | A feminine singular dative noun phrase is replaced by ihr.
Der Lehrer hilft den Kindern. Er hilft ___. | ihnen | sie | ihr | ihn | Den Kindern is dative plural, so its pronoun is ihnen.
Kannst du ___ helfen? (ich) | mir | mich | ich | mein | Helfen requires dative; the dative of ich is mir.
Ich höre ___ zu. (du) | dir | dich | du | dein | Zuhören takes dative, so du becomes dir.
Die Lehrerin erklärt ___ die Regel. (wir) | uns | wir | unser | euch | The dative form of wir is uns; the rule is the separate accusative object.
Ich schicke ___ ein Foto. (ihr, Plural) | euch | ihr | euer | ihnen | The dative form of the informal plural ihr is euch.
Frau Roth, ich danke ___. | Ihnen | ihnen | Sie | ihr | Formal Sie has the capitalized dative pronoun Ihnen.
Wie geht es ___, Herr Klein? | Ihnen | Sie | ihnen | euch | Addressing Herr Klein formally requires the capitalized dative Ihnen.
Wir sprechen mit dem Kollegen. Wir sprechen mit ___. | ihm | ihn | er | ihr | Mit requires dative; a male colleague is replaced by ihm.
Ich fahre mit meiner Schwester. Ich fahre mit ___. | ihr | sie | ihm | ihren | Mit takes dative, and a feminine singular person is replaced by ihr.
Das Geschenk ist von den Eltern. Es ist von ___. | ihnen | sie | ihr | Ihnen | Referring to parents in the third person uses lowercase ihnen after von.
Kommst du zu ___? (wir) | uns | wir | unser | euch | Zu takes dative; wir becomes uns.
Der Hund folgt ___. (du) | dir | dich | du | deiner | Folgen takes dative, so the correct pronoun is dir.
Die Jacke passt ___. (ich) | mir | mich | mein | ich | Passen takes a dative person; ich becomes mir.
Fehlt ___ etwas? (ihr, Plural) | euch | ihr | euer | uns | The people lacking something are dative with fehlen; ihr becomes euch.
Der Termin passt ___. (sie, Plural) | ihnen | ihr | sie | Ihnen | Third-person plural sie becomes lowercase ihnen in the dative.
Ich gratuliere ___. (er) | ihm | ihn | er | ihr | Gratulieren takes dative; er becomes ihm.
Die Kollegin begegnet ___. (ich) | mir | mich | ich | mein | Begegnen requires dative, giving mir.
Das ist unsere Lehrerin. Wir hören ___ zu. | ihr | sie | ihm | ihnen | A singular female teacher is replaced by the dative pronoun ihr.
""")

add(12, """
Sie erklärt ___ Kunden den Unterschied. (der Kunde) | dem | den | der | das | The recipient of an explanation is dative: dem Kunden; the difference is accusative.
Ich gebe dem Mann ___ Schlüssel. (der Schlüssel) | den | dem | der | des | The transferred thing is accusative; der Schlüssel becomes den Schlüssel.
Wir schicken ___ Schwester ein Paket. (die Schwester) | der | die | den | dem | The recipient takes dative, so use der Schwester.
Er zeigt dem Kind ___ Garten. (der Garten) | den | dem | der | des | The thing shown is accusative: den Garten.
Sie schenkt ___ Freund eine Geldbörse. (ein Freund) | einem | einen | einer | eines | The friend receives the gift and takes the dative einem Freund.
Ich bringe der Kollegin ___ Gabel. (eine Gabel) | eine | einer | einem | einen | The item brought is accusative; feminine eine stays eine.
Wir leihen ___ Nachbarn das Auto. (die Nachbarn; Plural) | den | die | dem | der | The borrowers are dative plural: den Nachbarn.
Er gibt dem Kind ___ Ball. (ein Ball) | einen | einem | einer | ein | Ball is masculine; the transferred object takes accusative einen.
Ich erkläre ___ Frau die Garantie. (die Frau) | der | die | dem | den | The person receiving an explanation takes dative: der Frau.
Die Mitarbeiterin nennt dem Kunden ___ Preis. (der Preis) | den | dem | der | des | The price named is the accusative object: den Preis.
Sie bietet ___ Gästen einen Kaffee an. (die Gäste) | den | die | dem | der | The people receiving an offer are dative plural: den Gästen.
Ich empfehle dem Freund ___ Film. (ein Film) | einen | einem | einer | eines | The recommended thing is accusative, so masculine ein becomes einen.
Wir erzählen ___ Kindern eine Geschichte. (die Kinder) | den | die | dem | der | The listeners are dative plural: den Kindern.
Er verspricht der Frau ___ Besuch. (ein Besuch) | einen | einem | einer | eines | The promised visit is the accusative object: einen Besuch.
Ich reiche ___ Kollegin das Formular. (die Kollegin) | der | die | dem | den | The recipient is dative; feminine die becomes der.
Sie verkauft dem Mann ___ Wagen. (der Wagen) | den | dem | der | des | The thing sold takes accusative: den Wagen.
Wir schicken dem Fundbüro ___ Brief. (ein Brief) | einen | einem | einer | eines | The letter is the accusative thing sent; the office is the dative recipient.
Er bringt ___ Kind die Tasche. (das Kind) | dem | das | den | der | The child is the recipient and takes neuter dative dem.
Ich wünsche der Nachbarin ___ schönen Abend. | einen | einem | einer | eines | The thing wished is accusative; masculine Abend takes einen.
Wer bekommt etwas? In: Sie gibt dem Mann den Schlüssel. | dem Mann | den Schlüssel | Sie | gibt | Dem Mann is the dative recipient; den Schlüssel is the accusative object being given.
""")

add(13, """
Ich gebe ___. (der Mann + das Buch) | dem Mann das Buch | das Buch dem Mann | der Mann das Buch | dem Mann dem Buch | In neutral order, a full dative noun phrase precedes a full accusative noun phrase.
Sie schickt ___. (die Frau + der Brief) | der Frau den Brief | den Brief der Frau | die Frau den Brief | der Frau dem Brief | With two full noun objects, neutral order places dative der Frau before accusative den Brief.
Wir zeigen ___. (das Kind + der Garten) | dem Kind den Garten | den Garten dem Kind | das Kind den Garten | dem Kind dem Garten | Neutral noun-object order is recipient in dative, then thing in accusative.
Ich gebe ___. (es + ihm) | es ihm | ihm es | er ihm | es ihn | Two unstressed personal pronouns normally put accusative es before dative ihm.
Sie schickt ___. (ihn + ihr) | ihn ihr | ihr ihn | er ihr | ihn sie | With two unstressed pronouns, accusative ihn precedes dative ihr.
Wir erklären ___. (es + ihnen) | es ihnen | ihnen es | es sie | er ihnen | The accusative pronoun es comes before the dative pronoun ihnen in neutral order.
Ich gebe ___. (ihm + das Buch) | ihm das Buch | das Buch ihm | ihn das Buch | ihm dem Buch | A personal pronoun normally comes before a full noun object; the recipient is ihm.
Sie schickt ___. (ihn + die Frau) | ihn der Frau | der Frau ihn | ihm die Frau | ihn die Frau | A pronoun precedes a full noun object, so accusative ihn comes before dative der Frau.
Wir zeigen ___. (es + das Kind) | es dem Kind | dem Kind es | es das Kind | ihm das Kind | The accusative pronoun es normally precedes the dative noun phrase dem Kind.
Er leiht ___. (die Nachbarin + der Wagen) | der Nachbarin den Wagen | den Wagen der Nachbarin | die Nachbarin den Wagen | der Nachbarin dem Wagen | Two noun objects usually put the dative recipient before the accusative thing.
Ich bringe ___. (sie + dir; die Tasche) | sie dir | dir sie | ihr dich | sie dich | Die Tasche becomes accusative sie, which precedes dative dir with two pronouns.
Sie schenkt ___. (es + uns) | es uns | uns es | er uns | es wir | Two unstressed pronouns use accusative-before-dative order: es uns.
Wir geben ___. (sie + euch; die Schlüssel) | sie euch | euch sie | ihnen ihr | sie ihr | The plural keys become accusative sie and come before dative euch.
Er erklärt ___. (mir + die Regel) | mir die Regel | die Regel mir | mich die Regel | mir der Regel | A dative pronoun normally precedes the full accusative noun phrase.
Ich erzähle ___. (die Kinder + die Geschichte) | den Kindern die Geschichte | die Geschichte den Kindern | die Kinder die Geschichte | den Kindern der Geschichte | In neutral order, the dative noun phrase den Kindern precedes the accusative story.
Sie verkauft ___. (ihn + der Kunde; der Wagen) | ihn dem Kunden | dem Kunden ihn | ihm den Kunden | ihn den Kunden | Accusative ihn, referring to the car, comes before the full dative recipient.
Wir empfehlen ___. (ihn + Ihnen; der Film) | ihn Ihnen | Ihnen ihn | er Ihnen | ihn Sie | With two unstressed pronouns, accusative ihn comes before formal dative Ihnen.
Ich reiche ___. (dir + das Formular) | dir das Formular | das Formular dir | dich das Formular | dir dem Formular | The dative pronoun dir normally precedes the full accusative noun phrase.
Sie bringt ___. (sie + ihm; die Gabel) | sie ihm | ihm sie | ihr ihn | sie ihn | Accusative sie, referring to the fork, precedes the dative pronoun ihm.
Er zeigt ___. (die Gäste + die Wohnung) | den Gästen die Wohnung | die Wohnung den Gästen | die Gäste die Wohnung | den Gästen der Wohnung | For two full noun phrases, the neutral pattern is dative den Gästen then accusative die Wohnung.
""", "Choose the usual neutral order. Personal pronouns are unstressed.")

add(14, """
Ich fahre mit ___ Wagen. (mein) | meinem | meinen | meiner | mein | Wagen is masculine; a dative possessive takes -em: meinem.
Du sprichst mit ___ Schwester. (dein) | deiner | deinem | deinen | deine | Schwester is feminine, so the dative form is deiner.
Er hilft ___ Kind. (sein) | seinem | seinen | seiner | sein | Kind is neuter and takes the dative possessive seinem.
Sie wohnt bei ___ Eltern. (ihr = her) | ihren | ihrem | ihrer | ihre | Eltern is plural, so the dative possessive is ihren.
Wir fahren mit ___ Auto. (unser) | unserem | unseren | unserer | unsere | Auto is neuter; unser takes -em in the dative: unserem.
Ihr sprecht mit ___ Lehrer. (euer) | eurem | euren | eurer | euer | Euer usually drops its second e before an ending: eurem Lehrer.
Die Kinder spielen mit ___ Freunden. (ihr = their) | ihren | ihrem | ihrer | ihre | Freunde is plural; the dative phrase is ihren Freunden.
Frau Meier, ich spreche mit ___ Mann. (Ihr) | Ihrem | Ihren | Ihrer | Ihr | Formal Ihr stays capitalized and takes masculine dative -em.
Ich bin bei ___ Mutter. (mein) | meiner | meinem | meinen | meine | Mutter is feminine; bei requires dative meiner.
Du hilfst ___ Bruder. (dein) | deinem | deinen | deiner | dein | Bruder is masculine; helfen requires dative deinem.
Er erzählt von ___ Ausbildung. (sein) | seiner | seinem | seinen | seine | Ausbildung is feminine and von takes dative: seiner.
Sie fährt zu ___ Kindern. (ihr = her) | ihren | ihrem | ihrer | ihre | Zu takes dative, and the plural possessive is ihren.
Wir warten vor ___ Haus. (unser; Ort) | unserem | unseren | unserer | unser | A location after vor uses dative; neuter Haus takes unserem.
Ihr arbeitet in ___ Garage. (euer) | eurer | eurem | euren | eure | Garage is feminine, so the dative possessive is eurer.
Ich gehe mit ___ Freunden. (mein) | meinen | meinem | meiner | meine | Plural dative needs meinen and the noun form Freunden.
Die Katze schläft auf ___ Handtuch. (dein; Ort) | deinem | deinen | deiner | dein | Handtuch is neuter; a location after auf takes dative deinem.
Er steht an ___ Haltestelle. (sein; Ort) | seiner | seinem | seinen | seine | Haltestelle is feminine and a location uses dative seiner.
Wir sprechen mit ___ Nachbarn. (unser; Plural) | unseren | unserem | unserer | unsere | The plural dative form of unser is unseren.
Ihr spielt mit ___ Hund. (euer) | eurem | euren | eurer | eure | Hund is masculine; after mit the possessive is eurem.
Herr Braun, wir danken ___ Kollegin. (Ihr) | Ihrer | Ihrem | Ihren | Ihre | Kollegin is feminine, so the formal dative possessive is Ihrer.
""")

add(15, """
Ich beeile ___, weil der Bus kommt. | mich | mir | dich | sich | Sich beeilen requires an accusative reflexive pronoun; ich takes mich.
Du erinnerst ___ an den Termin. | dich | dir | mich | sich | Sich erinnern uses accusative; du takes dich.
Er beschwert ___ über die Heizung. | sich | ihn | ihm | mich | Third-person reflexive verbs use sich, referring back to er.
Wir bereiten ___ auf die Prüfung vor. | uns | euch | sich | unser | The reflexive pronoun matching wir is uns.
Ihr interessiert ___ für Kunst. | euch | uns | sich | euer | Sich interessieren requires the pronoun euch with ihr.
Die Kinder freuen ___ auf die Ferien. | sich | sie | ihnen | euch | Third-person plural subjects use the reflexive pronoun sich.
Ich ärgere ___ über den Lärm. | mich | mir | sich | dich | Sich ärgern has an accusative reflexive object: mich.
Du ruhst ___ nach der Arbeit aus. | dich | dir | sich | mich | Sich ausruhen takes accusative; du takes dich.
Sie (Singular) zieht ___ schnell an. | sich | ihr | sie | mich | Without a separate clothing object, sich anziehen uses accusative sich.
Wir treffen ___ um acht. | uns | euch | sich | unser | The matching reflexive or reciprocal pronoun with wir is uns.
Ihr setzt ___ auf die Bank. | euch | uns | sich | euer | Sich setzen takes accusative; with ihr the pronoun is euch.
Ich fühle ___ heute besser. | mich | mir | sich | dich | Sich fühlen uses accusative mich with ich.
Du meldest ___ für den Kurs an. | dich | dir | sich | mich | Sich anmelden requires an accusative reflexive pronoun matching du: dich.
Er entschuldigt ___ bei der Kollegin. | sich | ihm | ihn | mir | Sich entschuldigen uses sich for a third-person subject.
Wir unterhalten ___ über das Konzert. | uns | euch | sich | unser | Sich unterhalten takes uns when the subject is wir.
Ihr entscheidet ___ für den früheren Zug. | euch | uns | sich | euer | Sich entscheiden uses euch with ihr.
Die Gäste verabschieden ___. | sich | sie | ihnen | uns | Sich verabschieden uses sich with a third-person plural subject.
Frau Klein, freuen Sie ___ auf die Reise? | sich | Ihnen | Sie | euch | Formal Sie uses the reflexive pronoun sich, which is not capitalized.
Ich wasche ___ vor dem Essen. (ganze Person) | mich | mir | sich | dich | With no separate accusative object, washing oneself takes accusative mich.
Du musst ___ auf die Prüfung vorbereiten. | dich | dir | sich | mich | The reflexive pronoun still refers to du when the verb is an infinitive after musst.
""")

add(16, """
Ich wasche ___ die Hände. | mir | mich | sich | dich | Die Hände is the accusative object, so the reflexive pronoun is dative mir.
Du putzt ___ die Zähne. | dir | dich | mir | sich | Die Zähne is already accusative; du therefore takes the dative reflexive dir.
Er zieht ___ das Hemd an. | sich | ihn | ihm | mich | The reflexive recipient is dative, but the third-person reflexive form remains sich.
Wir kaufen ___ einen Kalender. | uns | euch | sich | unser | The calendar is accusative; the dative reflexive form matching wir is uns.
Ihr holt ___ etwas zu trinken. | euch | uns | sich | euer | The dative reflexive pronoun for ihr is euch; etwas is the object obtained.
Die Kinder wünschen ___ ein Haustier. | sich | ihnen | sie | euch | With an accusative thing wished for, the reflexive pronoun is dative sich.
Ich kann ___ die neue Wohnung gut vorstellen. | mir | mich | dir | sich | Sich etwas vorstellen meaning imagine has a dative reflexive pronoun and an accusative object.
Du hast ___ den Arm verletzt. | dir | dich | mir | sich | Den Arm is the accusative object, so the reflexive pronoun is dative dir.
Ich ziehe ___ die Jacke aus. | mir | mich | dir | sich | The jacket is the separate accusative object; ich takes dative mir.
Du kämmst ___ die Haare. | dir | dich | mir | sich | Die Haare is accusative, leaving the reflexive pronoun in dative: dir.
Ich merke ___ den Termin. | mir | mich | dir | sich | Sich etwas merken uses a dative reflexive pronoun; the date is accusative.
Du siehst ___ den Film an. | dir | dich | mir | sich | In sich etwas ansehen, the film is accusative and the reflexive pronoun is dative dir.
Ich bestelle ___ einen Kaffee. | mir | mich | dir | sich | Einen Kaffee is accusative; the beneficiary matching ich is dative mir.
Du nimmst ___ eine Pause. | dir | dich | mir | sich | Eine Pause is accusative, so the reflexive pronoun is dative dir.
Ich habe ___ eine Idee notiert. | mir | mich | dir | sich | Eine Idee is the accusative object, so ich uses the dative reflexive mir.
Du musst ___ den Namen merken. | dir | dich | mir | sich | Sich etwas merken takes dative dir with du and an accusative name.
Ich wasche ___. (ganze Person; kein weiteres Objekt) | mich | mir | dir | sich | Without a separate accusative object, sich waschen uses accusative mich.
Du ziehst ___ an. (kein Kleidungsstück genannt) | dich | dir | mir | sich | Without a separate clothing object, sich anziehen takes accusative dich.
Ich stelle ___ der neuen Kollegin vor. (meine Person) | mich | mir | dir | sich | Introducing oneself uses accusative mich; imagining something uses the different frame mir etwas vorstellen.
Du stellst ___ deinen Urlaub am Meer vor. (in Gedanken) | dir | dich | mir | sich | Imagining a holiday uses dative dir because deinen Urlaub is the accusative object.
""")

add(17, """
Wir helfen ___ bei den Hausaufgaben. (gegenseitig) | einander | miteinander | füreinander | aufeinander | Helfen takes a dative object; einander expresses helping each other directly.
Die Kollegen sprechen ___. (mit + einander) | miteinander | füreinander | voneinander | gegeneinander | Sprechen mit combines mit and einander as miteinander.
Die Nachbarn achten ___. (auf + einander) | aufeinander | miteinander | voneinander | durcheinander | Auf jemanden achten uses auf; the reciprocal compound is aufeinander.
Wir sorgen ___. (für + einander) | füreinander | voneinander | miteinander | gegeneinander | Für jemanden sorgen becomes füreinander sorgen for mutual care.
Die Teams spielen ___. (gegen + einander) | gegeneinander | miteinander | füreinander | voneinander | Gegen einander combines as gegeneinander for opposing teams.
Die beiden lernen ___. (von + einander) | voneinander | zueinander | füreinander | gegeneinander | Learning from each other uses von, giving voneinander.
Die Freunde warten ___. (auf + einander) | aufeinander | miteinander | füreinander | voneinander | Warten auf becomes aufeinander warten when each waits for the other.
Die Familien wohnen ___. (neben + einander) | nebeneinander | gegeneinander | füreinander | voneinander | Neben einander becomes nebeneinander, meaning next to each other.
Die Gäste sitzen ___. (gegenüber + einander) | einander gegenüber | einander gegen | einander mit | einander für | Gegenüber can follow its complement: einander gegenüber means facing each other.
Wir erzählen ___ von unserem Tag. | einander | miteinander | voneinander | gegeneinander | Erzählen takes a dative recipient; einander means telling each other.
Die Schwestern erinnern sich ___. (an + einander) | aneinander | voneinander | miteinander | füreinander | Sich an jemanden erinnern uses an; the reciprocal form is aneinander.
Die Kinder rennen ___. (hinter + einander) | hintereinander | füreinander | voneinander | gegeneinander | Hintereinander means one behind another, combining hinter and einander.
Die Bücher liegen ___. (auf + einander) | aufeinander | miteinander | füreinander | voneinander | Aufeinander describes things placed one on top of another.
Wir sind ___ da. (für + einander) | füreinander | gegeneinander | voneinander | durcheinander | Füreinander da sein means being there for each other or supporting each other.
Die beiden reden ___. (über + einander) | übereinander | miteinander | füreinander | gegeneinander | Über jemanden reden becomes übereinander reden; miteinander would mean speaking with each other.
Wir haben lange nichts ___ gehört. (von + einander) | voneinander | füreinander | gegeneinander | aufeinander | Von jemandem hören becomes voneinander hören for news of each other.
Die Freunde gehen ___. (zu + einander) | zueinander | voneinander | füreinander | durcheinander | Zu einander combines as zueinander for movement toward each other.
Wir unterscheiden uns ___. (von + einander) | voneinander | miteinander | füreinander | aufeinander | Sich von jemandem unterscheiden takes von, giving voneinander.
Welche Aussage ist eindeutig gegenseitig? | Sie helfen einander. | Jeder wäscht sich selbst. | Sie arbeitet allein. | Er hilft nur sich selbst. | Einander explicitly describes a mutual action; sich selbst refers to oneself.
Die Nachbarn streiten ___. (mit + einander) | miteinander | füreinander | voneinander | zueinander | Mit jemandem streiten becomes miteinander streiten when the neighbors argue with each other.
""")

add(18, """
Die Kamera liegt auf ___ Tisch. (der Tisch) | dem | den | der | das | Liegen gives a location, so auf takes dative dem Tisch.
Ich lege die Kamera auf ___ Tisch. (der Tisch) | den | dem | der | das | Placing the camera onto a destination uses accusative den Tisch.
Die Katze schläft unter ___ Brücke. (die Brücke) | der | die | dem | den | The cat's location after unter takes dative der Brücke.
Die Katze läuft unter ___ Brücke und bleibt dort. (die Brücke) | die | der | dem | den | The bridge is the destination of the movement, so use accusative die Brücke.
Die Kanne steht neben ___ Fenster. (das Fenster) | dem | das | den | der | A position next to the window uses dative dem Fenster.
Ich stelle die Kanne neben ___ Fenster. (das Fenster) | das | dem | den | der | A new destination after neben takes accusative das Fenster.
Die Kette hängt an ___ Wand. (die Wand) | der | die | dem | den | Hanging in a fixed position uses dative der Wand.
Ich hänge die Kette an ___ Wand. (die Wand) | die | der | dem | den | Placing the chain onto the wall uses accusative die Wand.
Der Kassettenrekorder steht hinter ___ Sofa. (das Sofa) | dem | das | den | der | A location behind the sofa requires dative dem Sofa.
Ich stelle den Rekorder hinter ___ Sofa. (das Sofa) | das | dem | den | der | Moving the recorder to a destination uses accusative das Sofa.
Die Lampe hängt über ___ Tisch. (der Tisch) | dem | den | der | das | The lamp's position above the table takes dative dem Tisch.
Wir hängen die Lampe über ___ Tisch. (der Tisch) | den | dem | der | das | Hanging the lamp into a new position uses accusative den Tisch.
Der Hund sitzt vor ___ Tür. (die Tür) | der | die | dem | den | Sitting in a place uses dative der Tür.
Der Hund setzt sich vor ___ Tür. (die Tür) | die | der | dem | den | Sitting down in a new position gives a destination and accusative die Tür.
Die Schlüssel liegen zwischen ___ Büchern. (die Bücher) | den | die | dem | der | A location between plural objects uses dative den Büchern.
Ich lege die Schlüssel zwischen ___ Bücher. | die | den | dem | der | The destination after zwischen takes accusative plural die Bücher.
Wir gehen im Park spazieren. Welcher Fall folgt auf in? | Dativ | Akkusativ | Nominativ | Genitiv | Movement within a place still describes where the activity happens, so im Park is dative.
Wir gehen in den Park. Welcher Fall folgt auf in? | Akkusativ | Dativ | Nominativ | Genitiv | The park is the destination, so in takes accusative den Park.
Die Kinder spielen in ___ Garten. (der Garten) | dem | den | der | das | Playing occurs within the garden; this is a location, so use dative dem Garten.
Die Kinder laufen in ___ Garten hinein. (der Garten) | den | dem | der | das | Hinein makes the garden the destination, so use accusative den Garten.
""")

add(19, """
Die Flasche ___ auf dem Tisch. (aufrecht; Position) | steht | stellt | legt | setzt | An upright object's existing position is described by stehen, not stellen.
Ich ___ die Flasche auf den Tisch. (aufrecht) | stelle | stehe | liege | sitze | Placing an upright object uses stellen with an accusative destination.
Das Buch ___ auf dem Sofa. (flach; Position) | liegt | legt | stellt | setzt | A flat object's position uses liegen.
Ich ___ das Buch auf das Sofa. (flach) | lege | liege | stehe | sitze | Placing a flat object uses legen, with the destination in accusative.
Das Kind ___ auf dem Stuhl. (Position) | sitzt | setzt | stellt | legt | Sitting in a position uses sitzen.
Die Mutter ___ das Kind auf den Stuhl. | setzt | sitzt | steht | liegt | Placing someone in a seated position uses setzen.
Das Kleid ___ im Schrank. (Position) | hängt | stellt | legt | setzt | An existing suspended position is described by hängen.
Ich ___ das Kleid in den Schrank. (am Bügel) | hänge | liege | stehe | sitze | Transitive hängen means placing something in a hanging position.
Der Kinderwagen ___ vor der Kirche. (Position) | steht | stellt | setzt | legt | A parked upright object uses stehen for its position.
Wir ___ den Kinderwagen vor die Kirche. | stellen | stehen | liegen | sitzen | Moving the stroller into position uses stellen.
Die Unterlagen haben auf dem Tisch ___. | gelegen | gelegt | gestellt | gesetzt | A past flat position uses the strong participle gelegen from liegen.
Ich habe die Unterlagen auf den Tisch ___. | gelegt | gelegen | gestanden | gesessen | Placing an object uses legen, whose regular participle is gelegt.
Die Vase hat im Flur ___. | gestanden | gestellt | gesetzt | gelegt | A past upright position uses gestanden from stehen.
Er hat die Vase in den Flur ___. | gestellt | gestanden | gesessen | gelegen | Placing an upright vase uses stellen and its participle gestellt.
Das Kind hat auf der Bank ___. | gesessen | gesetzt | gestellt | gelegt | A past seated position uses gesessen from sitzen.
Sie hat das Kind auf die Bank ___. | gesetzt | gesessen | gestanden | gelegen | Seating someone uses setzen, whose participle is gesetzt.
Das Bild hat an der Wand ___. (Position) | gehangen | gehängt | gestellt | gesetzt | Intransitive hängen describing a position has the strong participle gehangen.
Wir haben das Bild an die Wand ___. (Handlung) | gehängt | gehangen | gestanden | gesessen | Transitive hängen describing placement has the weak participle gehängt.
Der Kollege ___ sich neben mich. (nimmt Platz) | setzt | sitzt | steht | liegt | Taking a seat is a change of position and uses sich setzen.
Der Kollege ___ neben mir. (ist schon da) | sitzt | setzt | stellt | legt | An existing seated position uses sitzen and a dative location.
""")

add(20, """
Ich bin im Büro, du stehst draußen. Komm bitte ___ zu mir! (nach innen) | herein | hinein | hinaus | hinauf | Her- points toward the speaker; movement inside toward the speaker is herein.
Ich bleibe draußen. Geh bitte ___ in das Büro! (von mir weg) | hinein | herein | heraus | herauf | Hin- points away from the speaker; movement into a room away from the speaker is hinein.
Ich stehe draußen. Komm aus dem Haus ___ zu mir! | heraus | hinaus | hinein | hinauf | Coming out toward the speaker is heraus.
Ich bleibe im Haus. Geh bitte ___ auf die Straße! | hinaus | heraus | herein | herauf | Going out away from the speaker is hinaus.
Ich bin oben. Komm die Treppe ___ zu mir! | herauf | hinauf | hinunter | hinaus | Upward movement toward the speaker is herauf.
Ich bleibe unten. Geh die Treppe ___ ins Büro! | hinauf | herauf | herunter | hinaus | Upward movement away from the speaker is hinauf.
Ich stehe unten. Komm die Treppe ___ zu mir! | herunter | hinunter | hinauf | herein | Downward movement toward the speaker is herunter.
Ich bleibe oben. Geh die Treppe ___ in den Keller! | hinunter | herunter | herauf | hinein | Downward movement away from the speaker is hinunter.
Ich stehe am anderen Ufer. Komm über die Brücke ___ zu mir! | herüber | hinüber | hinaus | hinunter | Movement across toward the speaker is herüber.
Ich bleibe hier. Geh über die Brücke ___ zum anderen Ufer! | hinüber | herüber | herein | herunter | Movement across away from the speaker is hinüber.
Ich rufe aus meinem Zimmer: Komm ___! (zu mir an diesen Ort) | hierher | dorthin | hinaus | hinunter | Hierher means to here, toward the speaker's present location.
Ich zeige auf das Lager dort: Geh ___! | dorthin | hierher | herein | herauf | Dorthin points to a destination over there, away from the speaker.
Was bedeutet Komm rein! in der Alltagssprache? | Komm herein! | Geh hinauf! | Geh hinaus! | Komm herunter! | Rein is a common shortened form for inward direction; with Komm it invites someone in.
Was bedeutet Geh raus! in der Alltagssprache? | Geh hinaus! | Komm herein! | Geh hinauf! | Komm herauf! | Raus is a common shortened form for outward direction; Geh raus means go out.
Was bedeutet Komm runter! hier? | Komm herunter! | Komm herein! | Geh hinauf! | Komm herüber! | Runter is the everyday shortened form for downward movement.
Was bedeutet Geh rauf! hier? | Geh hinauf! | Geh hinaus! | Komm herunter! | Komm herein! | Rauf is the everyday shortened form for upward movement.
Ich bin in der Küche. Bring die Lampe ___ zu mir! (von draußen nach innen) | herein | hinein | hinaus | hinunter | Bringing something inside toward the speaker takes herein.
Ich bleibe in der Küche. Trag die Kiste ___ in den Garten! | hinaus | heraus | herein | herauf | Taking the box outside away from the speaker takes hinaus.
Ich bin im Erdgeschoss. Bring den Kalender aus dem ersten Stock ___ zu mir! | herunter | hinunter | hinauf | hinein | Bringing something down toward the speaker takes herunter.
Ich bleibe unten. Trag die Lampe in den ersten Stock ___! | hinauf | herauf | herunter | heraus | Carrying something up away from the speaker takes hinauf.
""")

# Additional units are bundled as concrete questions, not generated at runtime.
# Keep the original 400 questions above unchanged for saved-attempt compatibility.
for _unit in json.loads((Path(__file__).resolve().parent / "data" / "questions_021_170.json").read_text(encoding="utf-8")):
    _id = _unit["id"]
    if _id in QUESTION_BANK:
        raise ValueError(f"Duplicate curriculum unit: {_id}")
    UNIT_DETAILS[_id] = (_unit["title"], _unit["goal_en"], _unit["goal_de"])
    QUESTION_BANK[_id] = _unit["questions"]
