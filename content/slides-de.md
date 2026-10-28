# Folien (Deutsch)

Format pro Folie: **Slide** = was auf der Folie steht. **Animation** = nur wo es im Plan steht. **Notes** = was Tina sagt.
Ziel: etwa 30 Minuten. Wenn die Probe zu lang ist, zuerst die Folien 7, 8 und 16 kürzen.

---

## 1. Titel (0.5 min)

**Slide**
- Qualität für fitnessfirst.de
- Die teuren Fehler zuerst finden, und zwar früh.

**Notes**
Vielen Dank für die Einladung. Meine Präsentation hat eine einzige Idee. Ich möchte die Fehler finden, die am meisten Geld und Vertrauen kosten. Und ich möchte sie so früh wie möglich finden, solange sie noch billig zu beheben sind. Alles, was ich heute zeige, führt zu dieser Idee zurück.

---

## 2. Mein Ausgangspunkt (1.5 min)

**Slide**
So habe ich mich vorbereitet:
- Die Website als Besucherin erkundet, um die Abläufe zu verstehen
- Geprüft, ob sie sich für Nutzer langsam anfühlt oder ungewöhnlich langsam ist (PageSpeed Insights, mobil)
- Geprüft, ob die Seite sich anpasst und für Handys geeignet ist
- Barrierefreiheit angeschaut (nur automatische Werte, kein vollständiger Test)
- Nichts abgeschickt, kein Login, keine Tests auf Ihrer Live-Seite

Das habe ich angenommen:
- Sie haben Testumgebungen neben der Produktion
- Zahlungsanbieter sind Dritte, darum kann man sie nicht auf der Produktion testen
- Die meisten Nutzer haben ein Handy, keinen Laptop

**Notes**
Bevor ich anfange, möchte ich offen sagen, was ich gemacht und was ich angenommen habe. Zuerst habe ich Ihre Website wie eine normale Besucherin angeschaut, um die Abläufe zu verstehen. Ich habe kein Formular abgeschickt und mich nicht eingeloggt, weil es Ihr Live-System ist. Dann habe ich mich gefragt: Fühlt sich die Seite für Nutzer langsam an, oder ist sie ungewöhnlich langsam? Ich habe das mit dem PageSpeed-Werkzeug von Google auf dem Handy gemessen. Ich habe auch geschaut, ob die Seite sich anpasst und für Handys geeignet ist. Und ich habe die Barrierefreiheit angeschaut, denn die Regeln für barrierefreie Online-Angebote werden wichtiger. Dabei habe ich nur die automatischen Werte benutzt. Das ist kein vollständiger Test. Außerdem habe ich drei Annahmen gemacht. Erstens: Sie haben Testumgebungen neben der Produktion. Zweitens: Zahlungsanbieter sind Dritte, darum können wir Zahlungen nicht auf dem Live-System testen. Drittens: Die meisten Ihrer Nutzer haben ein Handy und keinen Laptop. Wenn eine Annahme falsch ist, sagen Sie es mir bitte. Ich passe mich gerne an.

---

## 3. So erkunde ich (2 min)

**Slide**
Exploratives Testen: kurze Runden mit einem klaren Ziel.

Beispiel für ein Ziel: "Den Checkout erkunden und oft die Meinung ändern, um falsche Summen zu finden."

Das schreibe ich jedes Mal auf:
- Ziel und Aufbau (Gerät, Browser, Version der Seite)
- Was ich abgedeckt habe
- Fehler, mit Schritten und Screenshots
- Offene Fragen
- Was ich NICHT getestet habe

Gespeichert beim Ticket, damit das Team es sieht.

**Notes**
Ich beginne immer mit exploratorem Testen. Das heißt: Ich folge keinem festen Skript. Ich erkunde mit einem klaren Ziel und einer Zeitgrenze, meistens 60 bis 90 Minuten. Für Ihre Website waren meine Ziele einfach. Erstens: die Abläufe verstehen. Zweitens: sehen, ob sich die Seite für Nutzer langsam anfühlt. Drittens: sehen, ob sie auf dem Handy gut funktioniert. Ein Ziel für den Checkout könnte sein: Ich erkunde ihn und ändere oft meine Meinung, um falsche Summen zu finden. Ich gehe zurück, ich wechsle den Club, ich wechsle den Tarif, ich lade die Seite neu. Beim Testen mache ich Notizen. Ich schreibe immer auf: das Ziel, das Gerät und den Browser und welche Version der Seite ich gesehen habe. Dann, was ich abgedeckt habe, die Fehler mit genauen Schritten und Screenshots, meine offenen Fragen und auch, was ich nicht getestet habe. Dieser letzte Punkt ist wichtig. Er zeigt dem Team, wo die Lücken sind, statt sie zu verstecken. Die Notizen werden beim Ticket gespeichert, damit jeder sie später lesen kann.

---

## 4. Was ich gelernt habe: die wichtigsten Bereiche (2 min)

**Slide**
Risiko = wie schlimm, wenn es kaputtgeht x wie wahrscheinlich, dass es kaputtgeht

1. Mitgliedschaft abschließen
2. Cookie-Einwilligung und Tracking
3. Pausieren, kündigen, widerrufen
4. Probetraining buchen
5. Aktionen und Angebote
6. Clubsuche
7. Mitglieder-Login
8. Kursplan
9. Magazin, Karriere

**Animation**
[rank] Die 9 Bereiche erscheinen nacheinander in zufälliger Reihenfolge und gleiten dann in die richtige Reihenfolge. Die ersten 4 werden türkis.

**Notes**
Nach dem Erkunden wusste ich, welche Bereiche am wichtigsten sind. Ich habe sie mit einer Frage geordnet: Wie schlimm ist es, wenn das kaputtgeht, und wie wahrscheinlich ist es? Ich habe auf Geld, rechtliche Probleme und die Zahl der betroffenen Nutzer geschaut. Und auf komplizierte Regeln, fremde Systeme und häufige Änderungen. Der Abschluss der Mitgliedschaft ist klar die Nummer eins. Dort werden Verträge verkauft, und die Preise hängen von vielen Regeln ab. Die Cookie-Einwilligung ist Nummer zwei, weil sie ein rechtliches Thema ist und etwa fünfzehn Tracking-Dienste auf Ihren Seiten laden. Pausieren und Kündigen sind auch rechtliche Abläufe. Das Probetraining bringt neue Mitglieder. Das Magazin steht ganz unten. Ein Fehler dort ist sichtbar, aber billig. Diese Reihenfolge entscheidet, wo ich meine Zeit einsetze. Ich schaue mir die zwei Abläufe genau an, die Mitglieder bringen: den Checkout und die Probetraining-Buchung.

---

## 5. Mein Plan für jedes Risiko (2.5 min)

**Slide**
| Bereich | Hauptrisiko | Mein Plan |
|---|---|---|
| Mitgliedschaft abschließen | Falscher Preis, oder ein Vertrag kommt nie an | Tests für die Preisregeln, End-to-End-Tests, alle 15 Minuten eine Prüfung in der Produktion |
| Cookie-Einwilligung und Tracking | Marketing-Tracker laden nach "Ablehnen" | Automatische Prüfung nach "Alle ablehnen", Abstimmung mit dem Datenschutzbeauftragten |
| Pausieren, kündigen, widerrufen | Ein rechtlicher Ablauf funktioniert nicht mehr | End-to-End-Test bei jedem Release, Texte von Hand prüfen |
| Probetraining buchen | Termin gibt es nicht, Buchung erreicht den Club nie | Eine End-to-End-Buchung pro Handytyp, prüfen, dass sie ankommt |
| Aktionen und Angebote | Ein altes Angebot erscheint noch nach dem Ende | Tests für die Daten, anschauen, was der Cache zeigt |

Die anderen Bereiche: leichtere Prüfungen, meistens von Hand.

**Notes**
Für jeden Bereich mache ich einen Plan für sein Hauptrisiko. Ich plane nach Risiko, nicht nach Seite. Beim Abschluss der Mitgliedschaft ist das Hauptrisiko ein falscher Preis oder ein Vertrag, der nie ankommt. Darum teste ich die Preisregeln mit vielen kleinen Tests, und ich baue End-to-End-Tests, die den ganzen Ablauf durchklicken. Nach dem Release prüft ein kleiner Roboter alle 15 Minuten die ersten Schritte. Bei der Cookie-Einwilligung ist das Risiko, dass Marketing-Tracker noch laden, nachdem ein Besucher Nein gesagt hat. Darum klickt eine automatische Prüfung auf "Ablehnen" und schaut, welche Dienste laden. Kündigen und Pausieren sind rechtliche Abläufe. Sie bekommen bei jedem Release einen End-to-End-Test, und ich lese die Texte von Hand. Bei der Probetraining-Buchung sind die Risiken ein Termin, den es nicht gibt, und eine Buchung, die den Club nie erreicht. Darum teste ich eine Buchung pro Handytyp und prüfe, dass sie ankommt. Bei Angeboten ist das Risiko ein altes Angebot, das nach dem Ende noch erscheint. Darum teste ich die Daten und schaue, was der Cache zeigt. Die anderen Bereiche bekommen leichtere Prüfungen, meistens von Hand.

---

## 6. Ablauf 1: Mitgliedschaft abschließen, die Risiken (2.5 min)

**Slide**
5 Schritte: Club > Tarif > Extras > Ihre Daten > Zahlung

Was schiefgehen kann:
- Falscher Preis: Club, Tarif, Aktion, Alter, Land
- Die Zusammenfassung passt nicht zur Auswahl
- Kunde bleibt hängen und geht
- Vertrag oder Zahlung erreicht Ihre Systeme nicht
- Rechtlicher Text fehlt oder ist falsch

Am teuersten: ein falscher Preis oder ein Vertrag, der nie angelegt wurde.

**Notes**
Warum ist dieser Ablauf so wichtig? Hier verdienen Sie Geld. Und die Regeln sind kompliziert. Ein Vertrag über 24 Monate mit 12 freien Wochen. Ein Trainingspaket, das 39 oder 49 Euro kostet, je nach Club. Eine Startgebühr, die manchmal entfällt. Ein Studentenrabatt bis 25 Jahre. Und Österreich hat auf derselben Website eigene Regeln. Jede Regel ist ein Ort, an dem ein Preis falsch sein kann. Die schlimmsten Fehler sind ein falscher Preis, weil das ein rechtliches Problem und ein Vertrauensproblem ist, und ein Vertrag, den der Kunde unterschrieben hat, der aber Ihr System nie erreicht. Dann verlieren Sie den Kunden und wissen es nicht einmal. Ein weiteres Risiko: Der Checkout benutzt den Club in der Webadresse. Wenn jemand mittendrin den Club wechselt, muss sich die Zusammenfassung richtig ändern.

---

## 7. Ablauf 2: Probetraining buchen (1.5 min)

**Slide**
3 Schritte: Club > Datum und Uhrzeit > Ihre Daten

Was schiefgehen kann:
- Der gebuchte Termin existiert im Club nicht
- Die Buchung erreicht den Club nie
- Datumsfehler: heute, Wochenende, Monatswechsel, Feiertage
- Langsame Reaktion: 361 ms pro Tippen bei echten Nutzern (gut: 200 ms)

Automatisieren: Regeln für Termine, Buchung kommt im Club an, eine End-to-End-Buchung pro Handytyp.

**Notes**
Der zweite Ablauf ist das Probetraining. Die Risiken sind anders. Hier zahlt niemand, aber Sie verlieren ein zukünftiges Mitglied, wenn es nicht klappt. Das größte Risiko ist eine Buchung, die den Club nie erreicht. Die Person kommt ins Studio, und niemand erwartet sie. Das ist ein schlechter erster Eindruck. Auch Datumsfehler sind riskant: heute, das Wochenende, der Monatswechsel, Feiertage. Und eine Überraschung aus dem Test zur Seitengeschwindigkeit: Echte Nutzer warten hier 361 Millisekunden auf eine Reaktion, wenn sie etwas antippen. Die Grenze von Google für "gut" ist 200. Darauf komme ich zurück.

---

## 8. Geräte, Nutzer, fremde Systeme (1.5 min)

**Slide**
Geräte: zuerst der Desktop-Browser, dann die mobile Browser-Ansicht. Echte Handys: iPhone Safari, Android Chrome.
Bildschirmbreiten: 360, 390, 768, 1280 Pixel.

Nutzer: neue Besucher, Studenten, Menschen, die das Studio wechseln, Besucher aus Österreich, Menschen mit Tastatur oder Screenreader, langsames mobiles Internet, Menschen, die Cookies ablehnen.

Fremde Systeme, die ich gesehen habe:
- Usercentrics (Cookie-Einwilligung)
- VWO (A/B-Tests: nicht alle sehen dieselbe Seite)
- Google Tag Manager und etwa 15 Werbedienste
- Wahrscheinlich Baqend und Cloudflare (Tempo und Cache)
- Mir unbekannt: Zahlung, Buchung, Mitgliedersystem

**Notes**
Welche Geräte? Ich nehme an, dass die meisten Ihrer Besucher ein Handy benutzen. Das prüfe ich in Ihren Analysedaten. Ich baue die End-to-End-Tests zuerst im Desktop-Browser, weil man dort am schnellsten bauen und reparieren kann. Dann lasse ich dieselben Tests in der mobilen Browser-Ansicht laufen, auf einem Bildschirm in Handygröße. Vor großen Releases prüfe ich auch auf echten Handys. Ich denke auch in Nutzergruppen, nicht nur in Geräten. Ein Student sieht einen anderen Preis. Jemand aus Österreich sieht andere Regeln. Wer Cookies ablehnt, muss trotzdem kaufen können. Und Menschen mit Tastatur oder Screenreader müssen auch durch den Checkout kommen. Ich habe außerdem geschaut, welche fremden Dienste Ihre Seiten laden. Zwei sind für das Testen wichtig. Erstens VWO, ein Werkzeug für A/B-Tests. Das heißt: Verschiedene Besucher können verschiedene Versionen einer Seite sehen. Darum muss jeder Fehlerbericht sagen, welche Version angezeigt wurde. Zweitens die Cache-Dienste. Sie machen die Seite schnell, aber sie können auch ein altes Angebot zeigen, nachdem es beendet ist.

---

## 9. Checkout-Tests: was jeder erwartet (3 min)

**Slide**
Testpyramide: unten viele kleine, schnelle Tests, oben wenige langsame.

- **Explorativ (von Hand):** neue Aktionen, ungewöhnliche Kombinationen (Student, anderer Club), Österreich. Erwartet: kein falscher Preis oder Text.
- **End-to-End (wenige):** Club und Tarif wählen, bis zur Zahlung, auf iPhone und Android. Club mittendrin wechseln. Erwartet: jeder Schritt öffnet sich, Preis ändert sich.
- **Optik und Barrierefreiheit:** Erwartet: sieht richtig aus, Tastatur erreicht jeden Schritt, Fehler werden vorgelesen.
- **API und Integration:** Tarife, Preise, Vertrag, Zahlung im Testmodus. Erwartet: richtige Daten, Vertrag kommt an.
- **Unit (viele):** jede Preisregel und jedes Aktionsdatum. Erwartet: gleiche Eingabe, genau gleicher Preis.

Dazu in der Produktion: alle 15 Minuten öffnet ein Roboter die Schritte 1 bis 3. Erwartet: alles lädt, sonst wird das Team informiert.

Reihenfolge beim Bauen: Priorität 1 zuerst im Desktop-Browser, dann mobile Ansicht, dann Priorität 2.

**Animation**
[pyramid] 

**Notes**
Das würde ich beim Abschluss der Mitgliedschaft automatisieren, und das erwartet jeder Test. Stellen Sie sich eine Pyramide vor. Unten sind viele kleine und schnelle Tests. Das sind Unit-Tests, also Tests für ein kleines Stück Code. Jede Preisregel bekommt einen eigenen Test, auch das Enddatum einer Aktion. Denn Angebote, die nach Datum ein- und ausgeschaltet werden, sind eine klassische Fehlerquelle. Erwartet: Dieselbe Eingabe ergibt immer genau denselben Preis. In der Mitte sind API- und Integrationstests. Sie prüfen, dass die Systeme richtig miteinander sprechen. Bekommen wir für diesen Club die richtigen Tarife und Preise? Kommt der Vertrag im Mitgliedersystem an? Bei fremden Systemen wie der Zahlung benutze ich deren Testmodus. Erwartet: Die richtigen Daten kommen zurück, und der Vertrag kommt an. Dann kommen die Prüfungen von Optik und Barrierefreiheit. Erwartet: Es sieht richtig aus, die Tastatur erreicht jeden Schritt, und Fehler werden vorgelesen. Oben sind nur wenige End-to-End-Tests. End-to-End heißt: Ein Roboter klickt wie ein Kunde durch den echten Ablauf. Ich würde den Hauptweg auf einem iPhone und einem Android-Handy testen, und den Fall, dass jemand den Club wechselt. Erwartet: Jeder Schritt öffnet sich, und Zusammenfassung und Preis ändern sich. Darüber kommt das Ausprobieren von Hand, für Dinge, die neu sind oder menschliches Urteil brauchen. Nach dem Release prüft ein kleiner Roboter alle 15 Minuten die ersten Schritte. So merken wir ein Problem, bevor Kunden anrufen. Die End-to-End-Tests baue ich nach Priorität, aus der Reihenfolge von vorhin. Priorität eins sind der Abschluss der Mitgliedschaft, die Probetraining-Buchung, Pausieren und Kündigen und die Prüfung der Cookie-Einwilligung. Die baue ich zuerst im Desktop-Browser, weil man dort am schnellsten bauen und reparieren kann. Dann lasse ich dieselben Tests in der mobilen Ansicht laufen, auf einem Bildschirm in Handygröße. Danach kommt Priorität zwei: Aktionen und Angebote, Clubsuche und Login. Der Rest bekommt leichtere Prüfungen, meistens von Hand.

---

## 10. Was ich automatisiere und was nicht (1.5 min)

**Slide**
Automatisieren, wenn:
- der Test oft läuft, wichtig ist und das erwartete Ergebnis klar ist
- er stabil ist und wenig Pflege braucht
- Beispiel: Preisregeln (Unit-Tests)

Von Hand lassen, wenn:
- es neu ist oder sich noch ändert
- menschliches Urteil nötig ist: Aussehen, Wortwahl, Screenreader
- Beispiele: eine neue Aktionsseite, der Screenreader im Checkout

Was ich nicht testen würde:
- Fremde Dienste selbst: Zahlungsanbieter, Cookie-Werkzeug, Werbedienste. Ich teste nur unsere Seite.
- Lasttests und Sicherheitsangriffe auf die Live-Seite
- Bereiche mit niedrigem Risiko nicht in der Tiefe, zum Beispiel das Magazin: ein kurzer Blick reicht

**Notes**
Wie entscheide ich, was ich automatisiere? Ich stelle drei Fragen. Läuft dieser Test oft? Ist er wichtig? Und wissen wir genau, was das richtige Ergebnis ist? Wenn ja, automatisiere ich ihn. Wenn eine Funktion neu ist und sich noch ändert, teste ich sie zuerst von Hand. Sonst verbringen wir mehr Zeit damit, Tests zu reparieren, als Fehler zu finden. Ein unzuverlässiger Test, der manchmal besteht und manchmal ohne echten Grund durchfällt, kostet mehr als die Prüfung von Hand, die er ersetzt hat. Manches braucht immer einen Menschen. Wie sieht eine Seite aus? Ist der Text klar? Ergibt der Screenreader Sinn? Das bleibt von Hand. Ich sage auch klar, was ich nicht testen würde. Erstens die fremden Dienste selbst. Wir können den Zahlungsanbieter oder das Cookie-Werkzeug nicht testen. Das machen deren eigene Teams. Ich teste unsere Seite: dass sie die richtigen Daten sendet, dass sie eine klare Meldung zeigt, wenn der Dienst ausfällt, und dass nichts kaputtgeht, wenn der Dienst langsam oder nicht erreichbar ist. Bei Zahlungen nehme ich einen Testmodus auf einer Testumgebung an, nie das Live-System. Zweitens mache ich keine Lasttests oder Sicherheitsangriffe auf die Live-Seite. Sie ist die Produktion, darum braucht das eine Testumgebung und vorher eine Absprache. Drittens bekommen Bereiche mit niedrigem Risiko, wie das Magazin, nur einen kurzen Blick. Ein Fehler dort ist sichtbar, aber billig. Zu sagen, was ich auslasse, gehört zum Plan. Dann wissen alle, wo die Lücken sind.

---

## 11. Der Qualitätsprozess, den ich fördern würde (2.5 min)

**Slide**
Sechs Phasen, eine Frage: Was kann schiefgehen, und wie verhindern wir es?
Fehler kosten weniger, wenn wir sie früh finden.
1. Anforderungen: verstehen, warum
2. Risiko: gemeinsam entscheiden, was am wichtigsten ist
3. Entwicklung: früh erkunden und zu zweit arbeiten
4. Automatisierung: das Richtige automatisieren
5. Release: "fertig" ist ein Kriterium, kein Gefühl
6. Nach dem Release: aus dem lernen, was durchgerutscht ist

**Animation**
[cycle] Die sechs Phasen stehen im Kreis. Eine Phase nach der anderen leuchtet auf.

**Notes**
Jetzt zum Qualitätsprozess, den ich fördern würde, damit Fehler billiger werden. Die Idee ist einfach. Je früher wir einen Fehler finden, desto billiger ist er. Ein Fehler, der in einem Gespräch auffällt, kostet Minuten. Ein Fehler, der in der Produktion auffällt, kostet Geld und Vertrauen. Darum stelle ich in jeder Phase dieselbe Frage: Was kann schiefgehen, und wie verhindern wir es, nicht nur wie fangen wir es? Bei den Anforderungen frage ich, warum wir etwas bauen und für wen. In der Risikophase entscheiden wir als Team, was am wichtigsten ist. In der Entwicklung teste ich früh und arbeite mit den Entwicklern zu zweit. Dann automatisiere ich, was sich lohnt. Beim Release hat "fertig" klare Kriterien. Und nach dem Release schaue ich, was wir übersehen haben, denn das ist die ehrlichste Rückmeldung, die wir bekommen. Dann beginnt der Kreis von vorne.

---

## 12. Qualität ist die Aufgabe des Teams (2 min)

**Slide**
- **Produkt:** klare Ziele und Akzeptanzkriterien. Entscheidet gemeinsam mit dem Team über Risiken.
- **Entwickler:** Unit- und API-Tests für ihren Code. Reparieren, was die Pipeline stoppt.
- **Fachabteilungen:** prüfen, dass es für das Geschäft richtig ist (Abnahme).
- **QA:** Torwächter beim Release und Hilfe für alle:
  - hilft, Akzeptanzkriterien zu schreiben
  - arbeitet mit Entwicklern zu zweit
  - hält die Testfälle aktuell
  - schult das Team im Testen

**Notes**
Ich glaube, dass Qualität die Aufgabe des ganzen Teams ist, nicht nur von QA. Wenn nur QA verantwortlich ist, wird Qualität zu einer Kontrolle am Ende. Dann werden Fehler spät gefunden, wenn sie teuer sind. Darum hat jeder einen Teil. Produktverantwortliche schreiben klare Ziele und Akzeptanzkriterien. Akzeptanzkriterien sind die Bedingungen, die sagen, wann eine Funktion fertig ist. Entwickler schreiben Unit- und API-Tests für ihren eigenen Code. Die Fachabteilungen prüfen, ob das Ergebnis für das Geschäft richtig ist. Und meine Rolle hat zwei Seiten. Auf der einen Seite bin ich der Torwächter. Beim Release sage ich klar, was getestet ist, was nicht, und wie hoch das Risiko ist. Auf der anderen Seite bin ich eine Hilfe. Das Team kann zu mir kommen. Ich helfe, Akzeptanzkriterien zu schreiben, ich arbeite mit Entwicklern zu zweit, ich pflege die Testfälle, damit sie nützlich bleiben, und ich helfe dem Team, besser zu testen. Oft machen wir das in einem kurzen Treffen, das Three Amigos heißt: Produkt, Entwicklung und QA schauen gemeinsam eine Aufgabe an, bevor jemand anfängt zu bauen.

---

## 13. Von der Idee zur Live-Website (2 min)

**Slide**
Feature > Merge Request > Dev > Stage > Produktion > Nach dem Release

- **Feature:** Akzeptanzkriterien und Risiken vereinbart
- **Merge Request:** Code-Review, Unit-Tests, Code-Prüfungen
- **Dev:** API- und Integrationstests, Smoke-Test
- **Stage:** End-to-End-Regression, Optik, Barrierefreiheit, Seitengeschwindigkeit, Prüfung der Einwilligung, Abnahme durch das Geschäft
- **Produktion:** Smoke-Test direkt nach dem Deploy
- **Nach dem Release:** Überwachung und Seitengeschwindigkeit bei echten Nutzern. Rollback bereit.

Testdaten: keine echten Kundendaten auf Stage. Kopierte Daten werden anonymisiert.

**Animation**
[pipe] Eine Feature-Karte wandert von links nach rechts. An jedem Kontrollpunkt wird ein Licht grün. Im zweiten Durchlauf wird das Licht bei Stage rot, und die Karte bleibt stehen.

**Notes**
Hier ist der Weg von einem Feature bis zur Live-Website. Bei Acquia nehme ich drei Umgebungen an: Entwicklung, Staging und Produktion. Bei jedem Schritt gibt es eine Prüfung. Wenn ein Entwickler einen Merge Request öffnet, also die Bitte, seine Änderung in den Hauptcode zu übernehmen, gibt es ein Code-Review und die schnellen Tests. Auf der Entwicklungsumgebung laufen die API- und Integrationstests und ein Smoke-Test. Ein Smoke-Test ist eine kurze Prüfung, ob die wichtigsten Dinge noch funktionieren. Wie bei einer Maschine: Man schaltet sie ein und schaut, ob Rauch aufsteigt. Auf Staging läuft die volle Regression. Regressionstests prüfen, dass alte Funktionen nach einer Änderung noch funktionieren. Dort prüfen wir auch Optik, Barrierefreiheit, Seitengeschwindigkeit und Einwilligung. Die Fachabteilungen machen ihre Abnahme ebenfalls auf Staging. Nach dem Deploy auf die Produktion läuft der Smoke-Test noch einmal. Dann übernimmt die Überwachung. Wenn etwas schiefgeht, gehen wir zur letzten guten Version zurück. Ein wichtiger Punkt bei den Testdaten: Drupal-Seiten kopieren oft die Datenbank der Produktion auf Staging. Diese Kopie darf keine echten Kundendaten enthalten. Sie muss anonymisiert sein.

---

## 14. Wann stoppen wir ein Release? (2 min)

**Slide**
**Stoppt das Release:**
- Falscher Preis, Checkout oder Buchung kaputt
- Kündigen oder Pausieren kaputt
- "Ablehnen" bei den Cookies funktioniert nicht
- Sicherheitsproblem, oder jemand sieht die Daten einer anderen Person
- Hauptablauf mit der Tastatur nicht benutzbar

**Darf mit Bedingungen live gehen:**
- Kleiner Fehler mit einfacher Umgehung, Ticket und Termin für die Reparatur
- Problem auf einer Seite mit wenig Besuchern
- Neue Funktion mit einem Feature-Flag ausgeschaltet

**Unzuverlässige Tests:** noch einmal laufen lassen. Wenn er besteht, kommt er in Quarantäne, mit Besitzer und Frist. Nie einfach ignoriert.


**Notes**
Wann stoppen wir ein Release? Manche Dinge stoppen es immer: ein falscher Preis, ein kaputter Checkout oder eine kaputte Buchung, eine kaputte Kündigen-Schaltfläche, ein Cookie-Banner, bei dem "Ablehnen" nicht funktioniert, jedes Sicherheitsproblem oder ein Hauptablauf, den man mit der Tastatur nicht beenden kann. Andere Fehler dürfen live gehen, wenn wir Bedingungen vereinbaren. Zum Beispiel ein kleiner Fehler mit einer einfachen Umgehung, wenn es ein Ticket und einen Termin für die Reparatur gibt. Was ist mit unzuverlässigen Tests? Ich lasse einen durchgefallenen Test noch einmal laufen. Wenn er beim zweiten Mal besteht, ist er wahrscheinlich unzuverlässig. Dann kommt er in Quarantäne. Das heißt: Er stoppt die Pipeline nicht mehr, aber er hat einen Besitzer und eine Frist für die Reparatur. Er wird nie einfach ignoriert. Sehr lange Tests laufen nachts, nicht bei jeder Änderung. Wenn ein Release dringend ist, gebe ich eine klare Empfehlung, zum Beispiel ob wir live gehen oder warten sollen. Aber die Entscheidung trifft das Team, mit offenen Augen.

---

## 15. Mehr als "es funktioniert" (2.5 min)

**Slide**
| Bereich | Automatisch | Von Hand | Grenze (Gate) |
|---|---|---|---|
| Barrierefreiheit | Barrierefreiheits-Scan bei jedem Merge Request | Tastatur und Screenreader in den Hauptabläufen bei jedem Release, Experten-Prüfung einmal im Jahr | Keine kritischen Probleme im Checkout und bei der Buchung |
| Datenschutz und Einwilligung | Nach "Alle ablehnen" laden nur erlaubte Dienste | Texte im Banner mit dem Datenschutzbeauftragten prüfen | Jeder Marketing-Tracker nach dem Ablehnen stoppt das Release |
| Seitengeschwindigkeit | Lighthouse in der Pipeline, Messung der Buchungsschritte | Jede Woche die Daten echter Nutzer ansehen | Echte Nutzer: LCP 2,5 s, INP 200 ms, CLS 0,1. Pipeline: keine Seite langsamer als heute |

Heute, echte Nutzer, mobil: alle 3 Seiten laden schnell, alle 3 reagieren zu langsam.
Mitgliedschaft INP 227 ms, Probetraining 361 ms.

**Notes**
Neben "es funktioniert" habe ich drei Bereiche gewählt. Erstens die Barrierefreiheit. Sie veröffentlichen eine Erklärung zur Barrierefreiheit, also ist sie Ihnen wichtig. Ein automatischer Scan findet nur einen Teil der Probleme. Den Rest muss ein Mensch prüfen: Kann ich den Checkout nur mit der Tastatur beenden? Liest ein Screenreader die Fehlermeldungen vor? Mein Gate ist einfach: kein kritisches Problem im Checkout und bei der Buchung. Zweitens Datenschutz und Cookie-Einwilligung. Mit etwa fünfzehn Werbediensten auf der Seite ist das ein echtes Risiko. Ich würde eine einfache Prüfung automatisieren: Ein Roboter klickt auf "Alle ablehnen", und dann schauen wir, welche Dienste trotzdem laden. Wenn ein Marketing-Tracker nach dem Ablehnen lädt, stoppt das Release. Die rechtlichen Regeln selbst würde ich mit Ihrem Datenschutzbeauftragten klären. Drittens die Seitengeschwindigkeit. Google gibt klare Grenzen für echte Nutzer vor. Ich habe Ihre Seiten gemessen. Sie laden für echte Nutzer schnell, das ist toll. Aber alle drei reagieren zu langsam, wenn jemand etwas antippt. Auf der Probetraining-Seite sind es 361 Millisekunden, und die Grenze ist 200. Ein interessantes Detail: Der Labortest sagt, die Probetraining-Seite sei Ihre schnellste Seite. Das liegt daran, dass der Labortest die Seite nur lädt und nie den Kalender anklickt. Darum würde ich auch die Buchungsschritte selbst messen. In der Pipeline wäre meine erste Regel: Keine Seite wird langsamer als heute. Später können wir die Grenzen strenger machen.

---

## 16. Wo KI hilft und wo nicht (2.5 min)

**Slide**
KI hilft bei:
1. **Anforderungen:** findet Lücken und fehlende Sonderfälle in Akzeptanzkriterien
2. **Exploratives Testen:** Agenten erkunden mit einem Ziel und müssen für jedes Ergebnis einen Beweis zeigen
3. **Fehlgeschlagene Tests:** gruppiert Fehler, schlägt "echter Fehler" oder "unzuverlässig" vor

Immer bei Menschen:
- Endgültige Priorität von Fehlern
- Freigabe oder Stopp des Releases
- Rechtliche Entscheidungen, Barrierefreiheit und Datenschutz

Regeln: keine echten Kundendaten in KI-Werkzeugen. Jedes Ergebnis braucht einen Beweis. Die KI muss auflisten, was sie nicht getestet hat.

**Animation**
[loop] Ein Kreislauf. loop: KI schlägt vor > Eine Person prüft > Das Team entscheidet. Die Person in der Mitte bleibt die ganze Zeit sichtbar.

**Notes**
Wo passt KI hin? Ich benutze sie an drei Stellen. Erstens bei den Anforderungen. In meinem letzten Job habe ich KI-Agenten gebaut, die Akzeptanzkriterien lesen und nach Lücken und fehlenden Sonderfällen suchen. Ein Mensch entscheidet dann, welche Lücken echt sind. Zweitens beim exploratorischen Testen. Ich habe eine Gruppe von KI-Testagenten entworfen, die eine Website mit einem klaren Ziel erkunden. Ich muss hier ehrlich sein: Dieses System ist entworfen und mit Beispieldaten getestet, aber ich habe es noch nicht auf einer Live-Website laufen lassen. Wichtig sind die Regeln. Jedes Ergebnis braucht einen Beweis, zum Beispiel Screenshots. Der Agent muss aufschreiben, was er nicht getestet hat. Und Text auf einer Webseite gilt als Daten, nie als Anweisung, damit eine Seite den Agenten nicht austricksen kann. Drittens bei fehlgeschlagenen Tests. Die KI kann Fehler gruppieren und vorschlagen, ob es ein echter Fehler oder ein unzuverlässiger Test ist. Aber manche Dinge bleiben immer bei Menschen: die endgültige Priorität eines Fehlers, die Entscheidung, ob ein Release live geht, und alles Rechtliche. Und keine echten Kundendaten kommen in KI-Werkzeuge. Die KI macht Vorschläge. Das Team entscheidet.

---

# Zusatzfolien

## B1. Details zur Seitengeschwindigkeit

| Seite (mobil) | Echte Nutzer: LCP | Echte Nutzer: INP | Echte Nutzer: CLS | Laborwert |
|---|---|---|---|---|
| Startseite | 2 s | 208 ms | 0,03 | 43 |
| Mitgliedschaft | 1,1 s | 227 ms | 0,04 | 36 |
| Probetraining | 1,3 s | 361 ms | 0,05 | 69 |

Grenzen für "gut" (75 % der Besuche): LCP 2,5 s, INP 200 ms, CLS 0,1. Quelle: PageSpeed Insights, 27. Oktober 2026. Die Laborwerte stammen aus Einzelmessungen und schwanken.

**Notes**
LCP heißt: Wie lange dauert es, bis der Hauptinhalt sichtbar ist. INP heißt: Wie schnell reagiert die Seite auf ein Antippen. CLS heißt: Wie stark springt die Seite beim Laden. Der Labortest der Startseite zeigte fast 29 Sekunden bis zum Hauptinhalt auf einem langsamen Handy, während echte Nutzer ihn nach 2 Sekunden sehen. Ich kenne den genauen Grund nicht. Es könnte der Cache für wiederkehrende Besucher sein oder einfach das langsame Testnetz. Ich würde das mit Ihrem Team genauer anschauen.

## B2. Testdaten und Umgebungen

- Stage: anonymisierte Kopie der Produktion, oder erzeugte Testdaten
- Feste Testkonten und Testclubs, regelmäßig zurückgesetzt
- Zahlungsanbieter im Testmodus, nie echte Zahlungen
- Fremde Systeme, die wir nicht steuern können: in API-Tests simuliert (Mock), echt nur in wenigen End-to-End-Tests auf Stage
- Test-E-Mails nur an reservierte Testdomains

**Notes**
Bei den Testdaten gilt eine einfache Regel: keine echten Kundendaten außerhalb der Produktion. Wenn ein System schwer zu steuern ist, zum Beispiel ein Zahlungsanbieter, simuliere ich es in den meisten Tests. Das nennt man Mocking. Nur wenige End-to-End-Tests benutzen den echten Testmodus des Anbieters.

## B3. Meine KI-Testagenten (entworfen, noch nicht auf einer Live-Seite benutzt)

- 4 Agenten: Explorer, Komponente, Ablauf, API
- Regeln: nur erlaubte Testseiten, keine echten Käufe, Geheimnisse versteckt, Beweis für jedes Ergebnis
- Ergebnisse: bestanden, durchgefallen mit Priorität, oder "verdächtig" mit Begründung
- Mehrere Läufe werden zusammengeführt, weil KI-Ergebnisse von Lauf zu Lauf schwanken
- Ein P1-Fehler kann die Pipeline stoppen. Den Rest entscheiden Menschen.

**Notes**
Das ist das System, das ich erwähnt habe. Ich möchte klar sagen: Es ist gebaut und mit Beispieldaten getestet, aber noch nicht auf einer echten Website. Worauf ich stolz bin, sind die Regeln, denn sie beantworten Ihre Fragen zur Kontrolle: Beweise, Ehrlichkeit über Lücken, und Menschen, die die endgültigen Entscheidungen treffen.

## B4. Meine ersten Wochen

- Woche 1 bis 2: das Produkt, das Team und den Release-Prozess kennenlernen. Die Fehlerhistorie lesen.
- Woche 3 bis 4: Risikokarte mit dem Team, erste schnelle Erfolge (Prüfung der Einwilligung, Smoke-Tests)
- Monat 2 bis 3: Regressionstests für Checkout und Buchung, Quality Gates in der Pipeline

**Notes**
Wenn ich anfange, würde ich nicht am ersten Tag alles ändern. Zuerst lerne ich, wie Sie arbeiten und woher die Fehler in der Vergangenheit kamen. Dann vereinbaren wir gemeinsam eine Risikokarte. Die ersten schnellen Erfolge wären die Prüfung der Einwilligung und die Smoke-Tests, weil sie klein sind und viel schützen.

## B5. Eine normale Woche

**Slide**
- **Planung:** Three Amigos bei neuen Aufgaben, Risiken vereinbart
- **Jeden Tag:** zu zweit arbeiten, Merge Requests prüfen, kurze Fragen
- **Während des Sprints:** explorative Runden bei neuen Funktionen
- **Vor dem Release:** Regression auf Stage, Abnahme mit dem Geschäft
- **Release-Tag:** Smoke-Test, Überwachung
- **Nach dem Release:** schauen, was durchgerutscht ist, und einen Test dafür ergänzen

**Notes**
Damit man sieht, dass das im echten Alltag funktioniert, hier eine normale Woche. Bei der Planung schauen wir neue Aufgaben gemeinsam an und vereinbaren die Risiken. Jeden Tag arbeite ich mit Entwicklern zu zweit und schaue Merge Requests an. Während des Sprints mache ich explorative Runden bei den neuen Funktionen. Vor dem Release läuft die Regression auf Staging, und das Geschäft macht die Abnahme. Am Release-Tag gibt es einen Smoke-Test und Überwachung. Und nach dem Release schaue ich, was durchgerutscht ist. Für jeden Fehler, der die Produktion erreicht hat, ergänzen wir einen Test, damit er nicht wiederkommt.
