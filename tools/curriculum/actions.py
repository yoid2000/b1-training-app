"""Explicit principal parts and complements shared by tense/voice exercises."""
# Patient, plural?, participle, infinitive, finite present, finite past, object, zu-infinitive.
TEXT = """
Der Antrag|0|geprüft|prüfen|prüft|prüfte|den Antrag|zu prüfen
Die Rechnung|0|bezahlt|bezahlen|bezahlt|bezahlte|die Rechnung|zu bezahlen
Das Gerät|0|repariert|reparieren|repariert|reparierte|das Gerät|zu reparieren
Die Briefe|1|verschickt|verschicken|verschickt|verschickte|die Briefe|zu verschicken
Der Vertrag|0|unterschrieben|unterschreiben|unterschreibt|unterschrieb|den Vertrag|zu unterschreiben
Die Tür|0|geöffnet|öffnen|öffnet|öffnete|die Tür|zu öffnen
Das Fenster|0|geschlossen|schließen|schließt|schloss|das Fenster|zu schließen
Die Unterlagen|1|kopiert|kopieren|kopiert|kopierte|die Unterlagen|zu kopieren
Der Termin|0|verschoben|verschieben|verschiebt|verschob|den Termin|zu verschieben
Die Wohnung|0|geputzt|putzen|putzt|putzte|die Wohnung|zu putzen
Das Formular|0|ausgefüllt|ausfüllen|füllt|füllte|das Formular|auszufüllen
Die Gäste|1|begrüßt|begrüßen|begrüßt|begrüßte|die Gäste|zu begrüßen
Der Wagen|0|verkauft|verkaufen|verkauft|verkaufte|den Wagen|zu verkaufen
Die Straße|0|gesperrt|sperren|sperrt|sperrte|die Straße|zu sperren
Das Paket|0|geöffnet|öffnen|öffnet|öffnete|das Paket|zu öffnen
Die Fragen|1|beantwortet|beantworten|beantwortet|beantwortete|die Fragen|zu beantworten
Der Bericht|0|geschrieben|schreiben|schreibt|schrieb|den Bericht|zu schreiben
Die Suppe|0|gekocht|kochen|kocht|kochte|die Suppe|zu kochen
Das Zimmer|0|aufgeräumt|aufräumen|räumt|räumte|das Zimmer|aufzuräumen
Die Bücher|1|bestellt|bestellen|bestellt|bestellte|die Bücher|zu bestellen
"""
ACTIONS = [tuple(line.split('|')) for line in TEXT.strip().splitlines()]

def active_middle(action):
    patient, plural, part, infinitive, present, past, obj, zu = action
    particle = {'ausfüllen':'aus','aufräumen':'auf'}.get(infinitive,'')
    return obj + (' '+particle if particle else '')
