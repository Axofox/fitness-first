# Folien (Deutsch, sehr einfach)

Gleiche Folien wie in slides-de.md, aber mit noch einfacheren Wörtern und kürzeren Sätzen.
Ziel: etwa 30 Minuten. Wenn die Probe zu lang ist, zuerst die Folien 7, 8 und 16 kürzen.

---

## 1. Titel (0.5 min)

**Slide**
- Qualität für fitnessfirst.de
- Die teuren Fehler zuerst finden. Und zwar früh.

**Notes**
Danke für die Einladung. Meine Präsentation hat eine Idee. Ich suche zuerst die Fehler, die viel Geld und Vertrauen kosten. Und ich suche sie früh. Dann sind sie noch billig zu beheben. Alles, was ich heute zeige, hat mit dieser Idee zu tun.

---

## 2. Mein Start (1.5 min)

**Slide**
Das habe ich gemacht:
- Die Website wie eine Besucherin angeschaut, um die Abläufe zu verstehen
- Geprüft: Ist sie für Nutzer langsam? Oder ist sie ungewöhnlich langsam? (PageSpeed Insights, mobil)
- Geprüft: Passt sich die Seite an? Geht sie gut auf dem Handy?
- Barrierefreiheit angeschaut (nur automatische Werte, keine volle Prüfung)
- Nichts abgeschickt, kein Login, keine Tests auf Ihrer Live-Seite

Das nehme ich an:
- Sie haben Test-Umgebungen neben der echten Seite
- Zahlungsanbieter gehören anderen Firmen. Auf der echten Seite kann man sie nicht testen.
- Die meisten Nutzer haben ein Handy, keinen Laptop

**Notes**
Zuerst sage ich offen, was ich gemacht habe und was ich annehme. Ich habe Ihre Website angeschaut wie eine normale Besucherin. So habe ich die Abläufe verstanden. Ich habe kein Formular abgeschickt. Ich habe mich nicht eingeloggt. Es ist Ihre echte Seite, die Kunden benutzen. Dann habe ich mich gefragt: Ist die Seite langsam für Nutzer? Oder ist sie ungewöhnlich langsam? Ich habe das mit dem Werkzeug PageSpeed von Google gemessen, auf dem Handy. Ich habe auch geschaut, ob die Seite sich gut an das Handy anpasst. Und ich habe die Barrierefreiheit angeschaut. Barrierefrei heißt: Alle Menschen können die Seite benutzen. Dabei habe ich nur automatische Werte benutzt. Das ist keine volle Prüfung. Ich habe drei Annahmen gemacht. Erstens: Sie haben Test-Umgebungen. Zweitens: Zahlungsanbieter gehören anderen Firmen. Darum teste ich Zahlungen nicht auf der echten Seite. Drittens: Die meisten Nutzer haben ein Handy. Wenn eine Annahme falsch ist, sagen Sie es bitte. Dann passe ich mich an.

---

## 3. So probiere ich aus (2 min)

**Slide**
Ausprobieren mit einem Ziel, in kurzen Runden. Man sagt dazu: exploratives Testen.

Beispiel für ein Ziel: "Ich probiere den Checkout aus und ändere oft meine Meinung. So finde ich falsche Summen."

Das schreibe ich immer auf:
- Ziel und Aufbau (Gerät, Browser, Version der Seite)
- Was ich angeschaut habe
- Fehler, mit Schritten und Screenshots
- Offene Fragen
- Was ich NICHT getestet habe

Gespeichert beim Ticket. So sieht es das ganze Team.

**Notes**
Ich fange immer mit dem Ausprobieren an. Das Fachwort dafür ist exploratives Testen. Ich habe keinen festen Plan mit Schritten. Ich habe ein Ziel und eine Zeit. Meistens sind es 60 bis 90 Minuten. Bei Ihrer Website hatte ich drei einfache Ziele. Erstens: die Abläufe verstehen. Zweitens: sehen, ob die Seite langsam ist. Drittens: sehen, ob sie auf dem Handy gut geht. Ein Ziel für den Checkout wäre: Ich ändere oft meine Meinung, um falsche Summen zu finden. Ich gehe zurück. Ich wechsle den Club. Ich wechsle den Tarif. Ich lade die Seite neu. Dabei schreibe ich auf. Ich schreibe das Ziel auf, das Gerät und den Browser. Dann, was ich angeschaut habe. Dann die Fehler, mit genauen Schritten und Screenshots. Dann meine offenen Fragen. Und auch, was ich nicht getestet habe. Das ist wichtig. So sieht das Team, wo noch Lücken sind. Wir verstecken sie nicht. Die Notizen liegen beim Ticket. Jeder kann sie später lesen.

---

## 4. Das habe ich gelernt: Diese Bereiche sind wichtig (2 min)

**Slide**
Risiko = wie schlimm, wenn es kaputt geht x wie wahrscheinlich, dass es kaputt geht

1. Mitgliedschaft abschließen
2. Cookie-Auswahl und Tracking
3. Pausieren, kündigen, widerrufen
4. Probetraining buchen
5. Aktionen und Angebote
6. Clubsuche
7. Mitglieder-Login
8. Kursplan
9. Magazin, Karriere

**Animation**
[rank] Die 9 Bereiche erscheinen nacheinander in zufälliger Reihenfolge. Dann gleiten sie in die richtige Reihenfolge. Die ersten 4 werden türkis.

**Notes**
Nach dem Ausprobieren wusste ich, welche Bereiche am wichtigsten sind. Ich habe sie mit einer Frage geordnet. Wie schlimm ist es, wenn das kaputt geht? Und wie wahrscheinlich ist es? Ich habe auf Geld geschaut und auf rechtliche Probleme. Und darauf, wie viele Nutzer betroffen sind. Dazu auf schwierige Regeln, fremde Systeme und häufige Änderungen. Die Nummer eins ist klar: Mitgliedschaft abschließen. Hier verkaufen Sie Verträge. Und der Preis hängt von vielen Regeln ab. Nummer zwei ist die Cookie-Auswahl. Das ist ein rechtliches Thema. Und etwa fünfzehn Werbedienste laden auf Ihren Seiten. Pausieren und Kündigen sind auch rechtlich wichtig. Das Probetraining bringt neue Mitglieder. Das Magazin steht ganz unten. Ein Fehler dort sieht man, aber er ist billig. Diese Reihenfolge sagt mir, wo ich meine Zeit einsetze. Ich schaue mir zwei Abläufe genau an. Das sind die Abläufe, die Mitglieder bringen: der Checkout und die Buchung vom Probetraining.

---

## 5. Mein Plan für jedes Risiko (2.5 min)

**Slide**
| Bereich | Größtes Risiko | Mein Plan |
|---|---|---|
| Mitgliedschaft abschließen | Falscher Preis, oder der Vertrag kommt nie an | Tests für die Preisregeln, Tests für den ganzen Ablauf, alle 15 Minuten ein Smoke-Test auf der echten Seite |
| Cookie-Auswahl und Tracking | Werbe-Dienste laden nach "Ablehnen" | Automatischer Check nach "Alle ablehnen", mit dem Datenschutz-Beauftragten besprechen |
| Pausieren, kündigen, widerrufen | Ein rechtlicher Ablauf geht nicht mehr | Test des ganzen Ablaufs bei jedem Release, Texte von Hand lesen |
| Probetraining buchen | Den Termin gibt es nicht, oder die Buchung kommt im Club nicht an | Eine Buchung pro Handy-Typ testen, prüfen, ob sie ankommt |
| Aktionen und Angebote | Ein altes Angebot ist nach dem Ende noch da | Datum testen, schauen, was der Zwischenspeicher zeigt |

Die anderen Bereiche: leichtere Checks, meistens von Hand.

**Notes**
Für jeden Bereich mache ich einen Plan für das größte Risiko. Ich plane nach Risiko, nicht nach Seite. Bei der Mitgliedschaft ist das größte Risiko ein falscher Preis. Oder ein Vertrag, der nie ankommt. Darum teste ich die Preisregeln mit vielen kleinen Tests. Dazu baue ich Tests, die den ganzen Ablauf durchklicken. Nach dem Release läuft alle 15 Minuten ein kleines Skript als Smoke-Test. Ein Smoke-Test ist ein kurzer Check, ob das Wichtigste noch geht. Bei den Cookies ist das Risiko: Werbe-Dienste laden weiter, obwohl der Besucher Nein gesagt hat. Darum klickt ein automatischer Check auf "Ablehnen". Dann schaut er, welche Dienste laden. Kündigen und Pausieren sind rechtlich wichtig. Sie bekommen bei jedem Release einen Test. Und ich lese die Texte selbst. Bei der Buchung vom Probetraining gibt es zwei Risiken. Den Termin gibt es nicht. Oder die Buchung kommt im Club nicht an. Darum teste ich eine Buchung pro Handy-Typ. Und ich prüfe, ob sie ankommt. Bei den Angeboten ist das Risiko ein altes Angebot, das noch da ist. Darum teste ich die Daten. Und ich schaue, was der Zwischenspeicher zeigt. Die anderen Bereiche bekommen leichtere Checks, meistens von Hand.

---

## 6. Ablauf 1: Mitgliedschaft abschließen, die Risiken (2.5 min)

**Slide**
5 Schritte: Club > Tarif > Extras > Ihre Daten > Zahlung

Was schiefgehen kann:
- Falscher Preis: Club, Tarif, Aktion, Alter, Land
- Die Zusammenfassung passt nicht zur Auswahl
- Der Kunde kommt nicht weiter und geht
- Vertrag oder Zahlung kommt bei Ihnen nicht an
- Ein rechtlicher Text fehlt oder ist falsch

Am teuersten: ein falscher Preis oder ein Vertrag, der nie entstanden ist.

**Notes**
Warum ist dieser Ablauf so wichtig? Hier verdienen Sie Geld. Und die Regeln sind schwierig. Ein Vertrag über 24 Monate mit 12 freien Wochen. Ein Trainingspaket für 39 oder 49 Euro, je nach Club. Eine Startgebühr, die manchmal wegfällt. Ein Rabatt für Studenten bis 25 Jahre. Und Österreich hat eigene Regeln auf derselben Website. Bei jeder Regel kann ein Preis falsch sein. Am schlimmsten sind zwei Fehler. Erstens ein falscher Preis. Das ist ein rechtliches Problem, und Kunden verlieren Vertrauen. Zweitens ein Vertrag, den der Kunde unterschrieben hat, der aber nie bei Ihnen ankommt. Dann verlieren Sie den Kunden und wissen es nicht. Noch ein Risiko: Der Checkout speichert den Club in der Webadresse. Wenn jemand mittendrin den Club wechselt, muss die Zusammenfassung sich richtig ändern.

---

## 7. Ablauf 2: Probetraining buchen (1.5 min)

**Slide**
3 Schritte: Club > Datum und Uhrzeit > Ihre Daten

Was schiefgehen kann:
- Den gebuchten Termin gibt es im Club nicht
- Die Buchung kommt im Club nicht an
- Fehler beim Datum: heute, Wochenende, Monatswechsel, Feiertage
- Langsame Reaktion: 361 ms bei jedem Tippen (echte Nutzer). Gut wäre: 200 ms.

Automatisieren: die Regeln für Termine, ob die Buchung im Club ankommt, eine Buchung pro Handy-Typ.

**Notes**
Der zweite Ablauf ist das Probetraining. Hier sind die Risiken anders. Niemand zahlt. Aber Sie verlieren ein neues Mitglied, wenn es nicht klappt. Das größte Risiko: Die Buchung kommt im Club nicht an. Die Person kommt ins Studio, und niemand erwartet sie. Das ist ein schlechter erster Eindruck. Auch das Datum ist riskant. Heute, das Wochenende, der Monatswechsel, Feiertage. Und eine Überraschung aus dem Tempo-Test: Echte Nutzer warten hier 361 Millisekunden, wenn sie etwas antippen. Google sagt: Gut ist 200 oder weniger. Darauf komme ich später zurück.

---

## 8. Geräte, Nutzer, fremde Systeme (1.5 min)

**Slide**
Geräte: zuerst der Browser am Computer, dann die Handy-Ansicht im Browser. Echte Handys: iPhone Safari, Android Chrome.
Bildschirmbreiten: 360, 390, 768, 1280 Pixel.

Nutzer: neue Besucher, Studenten, Menschen, die das Studio wechseln, Besucher aus Österreich, Menschen mit Tastatur oder Screenreader, langsames Handy-Internet, Menschen, die Cookies ablehnen.

Fremde Systeme, die ich gesehen habe:
- Usercentrics (Cookie-Auswahl)
- VWO (A/B-Tests: nicht alle sehen dieselbe Seite)
- Google Tag Manager und etwa 15 Werbedienste
- Wahrscheinlich Baqend und Cloudflare (Tempo und Zwischenspeicher)
- Mir nicht bekannt: Zahlung, Buchung, Mitglieder-System

**Notes**
Welche Geräte? Ich nehme an: Die meisten Besucher benutzen ein Handy. Das prüfe ich in Ihren Zahlen. Ich baue die Tests zuerst für den Browser am Computer. Dort kann man am schnellsten bauen und reparieren. Dann lasse ich dieselben Tests in der Handy-Ansicht laufen. Das ist ein kleiner Bildschirm im Browser. Vor großen Releases prüfe ich auch auf echten Handys. Ich denke auch in Gruppen von Nutzern. Ein Student sieht einen anderen Preis. Jemand aus Österreich sieht andere Regeln. Wer Cookies ablehnt, muss trotzdem kaufen können. Und wer mit Tastatur oder Screenreader arbeitet, muss durch den Checkout kommen. Ich habe auch geschaut, welche fremden Dienste Ihre Seiten laden. Zwei sind wichtig für das Testen. Erstens VWO. Das ist ein Werkzeug für A/B-Tests. Verschiedene Besucher sehen verschiedene Versionen der Seite. Darum muss jeder Fehlerbericht sagen: Welche Version habe ich gesehen? Zweitens der Zwischenspeicher. Er macht die Seite schnell. Aber er kann auch ein altes Angebot zeigen, obwohl es schon vorbei ist.

---

## 9. Checkout-Tests: Was jeder erwartet (3 min)

**Slide**
Test-Pyramide: unten viele kleine, schnelle Tests. Oben wenige, langsame.

- **Von Hand ausprobieren:** neue Aktionen, ungewöhnliche Kombinationen (Student, anderer Club), Österreich. Erwartet: kein falscher Preis oder Text.
- **Ganzer Ablauf (wenige):** Club und Tarif wählen, bis zur Zahlung, auf iPhone und Android. Club mittendrin wechseln. Erwartet: Jeder Schritt öffnet sich. Der Preis ändert sich.
- **Aussehen und Barrierefreiheit:** Erwartet: Es sieht richtig aus. Die Tastatur kommt zu jedem Schritt. Fehler werden vorgelesen.
- **Schnittstellen:** Tarife, Preise, Vertrag, Zahlung im Test-Modus. Erwartet: Die Daten stimmen. Der Vertrag kommt an.
- **Kleine Tests (viele):** jede Preisregel und jedes Datum einer Aktion. Erwartet: Gleiche Eingabe gibt genau den gleichen Preis.

Dazu auf der echten Seite: alle 15 Minuten öffnet ein Smoke-Test-Skript die Schritte 1 bis 3. Erwartet: Alles lädt. Sonst bekommt das Team Bescheid.

Reihenfolge beim Bauen: wichtigste Abläufe zuerst im Browser am Computer, dann Handy-Ansicht, dann die zweite Gruppe.

**Animation**
[pyramid] 

**Notes**
Das würde ich bei der Mitgliedschaft automatisieren. Und das erwartet jeder Test. Stellen Sie sich eine Pyramide vor. Unten sind viele kleine, schnelle Tests. Jede Preisregel hat einen eigenen Test. Auch das Ende einer Aktion. Angebote, die nach Datum an und aus gehen, sind eine typische Fehlerquelle. Erwartet: Gleiche Eingabe gibt immer genau den gleichen Preis. In der Mitte sind die Tests für die Schnittstellen. Das sind die Stellen, an denen Systeme miteinander sprechen. Bekommen wir für diesen Club die richtigen Tarife und Preise? Kommt der Vertrag im Mitglieder-System an? Bei fremden Systemen wie der Zahlung nutze ich den Test-Modus der Firma. Erwartet: Die richtigen Daten kommen zurück. Und der Vertrag kommt an. Dann prüfe ich Aussehen und Barrierefreiheit. Erwartet: Es sieht richtig aus. Die Tastatur kommt zu jedem Schritt. Fehler werden vorgelesen. Oben sind nur wenige Tests für den ganzen Ablauf. Man sagt dazu End-to-End. Ein Skript klickt durch den echten Ablauf, wie ein Kunde. Ich teste den Hauptweg auf einem iPhone und auf einem Android-Handy. Und den Fall, dass jemand den Club wechselt. Erwartet: Jeder Schritt öffnet sich. Zusammenfassung und Preis ändern sich. Ganz oben probiere ich von Hand aus. Das ist für Dinge, die neu sind oder bei denen ein Mensch urteilen muss. Nach dem Release prüft das Smoke-Test-Skript alle 15 Minuten die ersten Schritte. So sehen wir ein Problem, bevor Kunden anrufen. Ich baue die Tests nach Wichtigkeit, mit der Reihenfolge von vorhin. Zuerst die wichtigsten Abläufe: Mitgliedschaft, Buchung vom Probetraining, Pausieren und Kündigen und der Cookie-Check. Die baue ich zuerst im Browser am Computer. Dort kann man am schnellsten bauen und reparieren. Dann lasse ich dieselben Tests in der Handy-Ansicht laufen. Danach kommt die zweite Gruppe: Aktionen und Angebote, Clubsuche und Login. Der Rest bekommt leichtere Checks, meistens von Hand.

---

## 10. Was ich automatisiere und was nicht (1.5 min)

**Slide**
Automatisieren, wenn:
- der Test oft läuft, wichtig ist und das richtige Ergebnis klar ist
- er stabil ist und wenig Arbeit macht
- Beispiel: Preisregeln

Von Hand machen, wenn:
- etwas neu ist oder sich noch ändert
- ein Mensch urteilen muss: Aussehen, Wörter, Screenreader
- Beispiele: eine neue Aktionsseite, der Screenreader im Checkout

Das würde ich nicht testen:
- Die fremden Dienste selbst: Zahlungsanbieter, Cookie-Werkzeug, Werbedienste. Ich teste nur unsere Seite.
- Last-Tests und Angriffe auf die echte Seite
- Bereiche mit kleinem Risiko nicht genau, zum Beispiel das Magazin: ein kurzer Blick reicht

**Notes**
Wie entscheide ich, was ich automatisiere? Ich stelle drei Fragen. Läuft der Test oft? Ist er wichtig? Und wissen wir genau, was richtig ist? Wenn ja, automatisiere ich ihn. Wenn eine Funktion neu ist und sich noch ändert, teste ich zuerst von Hand. Sonst reparieren wir mehr Tests, als wir Fehler finden. Ein Test, der mal klappt und mal nicht, ohne echten Grund, kostet mehr als der Check von Hand. Manches braucht immer einen Menschen. Wie sieht die Seite aus? Sind die Wörter klar? Ergibt der Screenreader Sinn? Das bleibt von Hand. Ich sage auch klar, was ich nicht teste. Erstens die fremden Dienste selbst. Den Zahlungsanbieter oder das Cookie-Werkzeug testen deren eigene Teams. Ich teste unsere Seite. Sendet sie die richtigen Daten? Zeigt sie eine klare Meldung, wenn der Dienst ausfällt? Geht nichts kaputt, wenn der Dienst langsam ist? Für Zahlungen nehme ich einen Test-Modus auf einer Test-Umgebung an. Nie die echte Seite. Zweitens mache ich keine Last-Tests und keine Angriffe auf die echte Seite. Das braucht eine Test-Umgebung und vorher eine Absprache. Drittens schaue ich Bereiche mit kleinem Risiko nur kurz an, zum Beispiel das Magazin. Ein Fehler dort ist sichtbar, aber billig. Ich sage, was ich auslasse. Dann wissen alle, wo die Lücken sind.

---

## 11. Der Qualitäts-Prozess, den ich vorschlagen würde (2.5 min)

**Slide**
Sechs Phasen, eine Frage: Was kann schiefgehen? Und wie verhindern wir es?
Fehler kosten weniger, wenn wir sie früh finden.
1. Anforderungen: verstehen, warum
2. Risiko: zusammen entscheiden, was wichtig ist
3. Entwicklung: früh ausprobieren und zu zweit arbeiten
4. Automatisierung: das Richtige automatisieren
5. Release: "fertig" hat klare Regeln
6. Nach dem Release: lernen, was durchgerutscht ist

**Animation**
[cycle] Die sechs Phasen stehen im Kreis. Eine Phase nach der anderen leuchtet auf.

**Notes**
Jetzt zum Prozess für Qualität. Er soll Fehler billiger machen. Die Idee ist einfach. Je früher wir einen Fehler finden, desto billiger ist er. Ein Fehler, den wir im Gespräch finden, kostet Minuten. Ein Fehler auf der echten Seite kostet Geld und Vertrauen. Darum stelle ich in jeder Phase dieselbe Frage. Was kann schiefgehen? Und wie verhindern wir es? Nicht nur: Wie finden wir es? Bei den Anforderungen frage ich: Warum bauen wir das? Und für wen? In der Risiko-Phase entscheiden wir zusammen, was am wichtigsten ist. In der Entwicklung teste ich früh. Ich arbeite mit den Entwicklern zu zweit. Dann automatisiere ich, was sich lohnt. Beim Release hat "fertig" klare Regeln. Es ist kein Gefühl. Und nach dem Release schaue ich, was wir übersehen haben. Das ist die ehrlichste Rückmeldung. Dann beginnt der Kreis von vorn.

---

## 12. Qualität ist Aufgabe des ganzen Teams (2 min)

**Slide**
- **Produkt:** klare Ziele und Regeln, wann etwas fertig ist. Entscheidet mit dem Team über Risiken.
- **Entwickler:** kleine Tests und Tests für Schnittstellen für ihren Code. Reparieren, was die automatische Strecke stoppt.
- **Fachabteilungen:** prüfen, ob es für das Geschäft passt (Abnahme).
- **QA:** der letzte Check vor dem Release, und Hilfe für alle:
  - hilft, die Regeln für "fertig" zu schreiben
  - arbeitet mit Entwicklern zu zweit
  - hält die Testfälle aktuell
  - zeigt dem Team, wie man gut testet

**Notes**
Ich glaube: Qualität ist die Aufgabe des ganzen Teams. Nicht nur von QA. Wenn nur QA verantwortlich ist, ist Qualität nur ein Check am Ende. Dann finden wir Fehler spät. Und dann sind sie teuer. Darum hat jeder einen Teil. Das Produkt-Team schreibt klare Ziele. Und klare Regeln, wann eine Funktion fertig ist. Dafür gibt es das Wort Akzeptanzkriterien. Die Entwickler schreiben Tests für ihren eigenen Code. Die Fachabteilungen prüfen, ob das Ergebnis für das Geschäft richtig ist. Meine Rolle hat zwei Seiten. Auf der einen Seite mache ich den letzten Check vor dem Release. Ich sage klar: Das ist getestet. Das nicht. Das ist das Risiko. Auf der anderen Seite helfe ich. Das Team kann zu mir kommen. Ich helfe bei den Regeln für "fertig". Ich arbeite mit Entwicklern zu zweit. Ich halte die Testfälle aktuell, damit sie nützlich bleiben. Und ich helfe dem Team, besser zu testen. Oft machen wir das in einem kurzen Treffen. Es heißt Three Amigos. Produkt, Entwicklung und QA schauen zusammen eine Aufgabe an. Das passiert, bevor jemand anfängt zu bauen.

---

## 13. Von der Idee zur Live-Website (2 min)

**Slide**
Feature > Merge Request > Dev > Stage > Echte Seite > Nach dem Release

- **Feature:** Regeln für "fertig" und Risiken sind abgesprochen
- **Merge Request:** Code wird von einem Kollegen gelesen, kleine Tests, automatische Code-Checks
- **Dev:** Tests für Schnittstellen, ein kurzer Check, ob das Wichtigste geht (Smoke-Test)
- **Stage:** alle Tests für den ganzen Ablauf, Aussehen, Barrierefreiheit, Tempo, Cookie-Check, Abnahme durch das Geschäft
- **Echte Seite:** Smoke-Test direkt nach dem Start
- **Nach dem Release:** beobachten und Tempo bei echten Nutzern messen. Zurück zur alten Version ist vorbereitet.

Testdaten: keine echten Kundendaten auf Stage. Kopierte Daten werden unkenntlich gemacht.

**Animation**
[pipe] Eine Feature-Karte wandert von links nach rechts. An jedem Kontrollpunkt wird ein Licht grün. Im zweiten Durchlauf wird das Licht bei Stage rot, und die Karte bleibt stehen.

**Notes**
Hier sehen Sie den Weg von einer neuen Funktion bis zur echten Website. Bei Acquia nehme ich drei Umgebungen an: Dev, Stage und die echte Seite. Bei jedem Schritt gibt es einen Check. Zuerst öffnet ein Entwickler einen Merge Request. Das ist die Bitte, seine Änderung in den Hauptcode zu übernehmen. Dann liest ein Kollege den Code. Und die schnellen Tests laufen. Auf Dev laufen die Tests für die Schnittstellen. Dazu ein Smoke-Test. Das ist ein kurzer Check, ob das Wichtigste noch geht. Wie bei einer Maschine: Man schaltet sie an und schaut, ob Rauch kommt. Auf Stage laufen alle Tests, die prüfen, ob alte Funktionen noch gehen. Dort prüfen wir auch Aussehen, Barrierefreiheit, Tempo und die Cookie-Auswahl. Die Fachabteilungen machen ihre Abnahme auch auf Stage. Nach dem Start auf der echten Seite läuft der Smoke-Test noch einmal. Dann beobachten wir die Seite. Wenn etwas schiefgeht, gehen wir zur letzten guten Version zurück. Noch ein wichtiger Punkt bei den Testdaten: Bei Drupal-Seiten kopiert man oft die echte Datenbank auf Stage. Diese Kopie darf keine echten Kundendaten haben. Man muss sie unkenntlich machen.

---

## 14. Wann stoppen wir ein Release? (2 min)

**Slide**
**Das stoppt das Release:**
- Falscher Preis, Checkout oder Buchung kaputt
- Kündigen oder Pausieren kaputt
- "Ablehnen" bei den Cookies geht nicht
- Sicherheitsproblem, oder jemand sieht die Daten einer anderen Person
- Hauptablauf geht mit der Tastatur nicht

**Das darf mit Bedingungen live gehen:**
- Kleiner Fehler mit einfachem Ausweg, Ticket und Termin zum Reparieren
- Problem auf einer Seite mit wenig Besuchern
- Neue Funktion ist ausgeschaltet (Feature-Flag)

**Tests, die mal klappen und mal nicht:** noch einmal laufen lassen. Wenn der Test klappt, wird er zur Seite gelegt. Er hat einen Besitzer und eine Frist. Er wird nie einfach ignoriert.


**Notes**
Wann stoppen wir ein Release? Manche Dinge stoppen es immer. Ein falscher Preis. Ein kaputter Checkout oder eine kaputte Buchung. Eine kaputte Kündigen-Schaltfläche. Ein Cookie-Banner, bei dem "Ablehnen" nicht geht. Jedes Sicherheitsproblem. Oder ein Hauptablauf, den man mit der Tastatur nicht schafft. Andere Fehler dürfen live gehen, wenn wir Bedingungen absprechen. Zum Beispiel ein kleiner Fehler mit einem einfachen Ausweg. Dann braucht es ein Ticket und einen Termin zum Reparieren. Und was ist mit Tests, die mal klappen und mal nicht? Ich lasse einen durchgefallenen Test noch einmal laufen. Wenn er beim zweiten Mal klappt, ist er wahrscheinlich nicht stabil. Dann legen wir ihn zur Seite. Das heißt: Er stoppt die automatische Strecke nicht mehr. Aber er hat einen Besitzer und eine Frist zum Reparieren. Wir ignorieren ihn nie einfach. Sehr lange Tests laufen nachts. Nicht bei jeder Änderung. Wenn ein Release dringend ist, gebe ich eine klare Empfehlung. Zum Beispiel: Wir gehen live. Oder: Wir warten. Aber das Team entscheidet. Mit offenen Augen.

---

## 15. Mehr als "es geht" (2.5 min)

**Slide**
| Bereich | Automatisch | Von Hand | Grenze |
|---|---|---|---|
| Barrierefreiheit | Automatischer Scan bei jedem Merge Request | Tastatur und Screenreader in den Hauptabläufen bei jedem Release, einmal im Jahr eine Prüfung durch Experten | Keine großen Probleme im Checkout und bei der Buchung |
| Datenschutz und Cookie-Auswahl | Nach "Alle ablehnen" laden nur erlaubte Dienste | Texte im Banner mit dem Datenschutz-Beauftragten prüfen | Ein Werbe-Dienst nach dem Ablehnen stoppt das Release |
| Tempo der Seite | Lighthouse in der automatischen Strecke, Zeit der Buchungsschritte messen | Jede Woche die Zahlen von echten Nutzern anschauen | Echte Nutzer: LCP 2,5 s, INP 200 ms, CLS 0,1. Automatische Strecke: keine Seite langsamer als heute |

Heute, echte Nutzer, Handy: alle 3 Seiten laden schnell, alle 3 reagieren zu langsam.
Mitgliedschaft INP 227 ms, Probetraining 361 ms.

**Notes**
Neben "es geht" habe ich drei Bereiche gewählt. Erstens die Barrierefreiheit. Sie haben eine Erklärung zur Barrierefreiheit auf der Seite. Also ist sie Ihnen wichtig. Ein automatischer Scan findet nur einen Teil der Probleme. Den Rest muss ein Mensch prüfen. Kann ich den Checkout nur mit der Tastatur schaffen? Liest der Screenreader die Fehlermeldungen vor? Meine Grenze ist einfach: Kein großes Problem im Checkout und bei der Buchung. Zweitens Datenschutz und Cookie-Auswahl. Etwa fünfzehn Werbedienste laufen auf der Seite. Das ist ein echtes Risiko. Ich würde einen einfachen Check automatisieren. Ein Skript klickt auf "Alle ablehnen". Dann schauen wir, welche Dienste trotzdem laden. Wenn ein Werbe-Dienst lädt, stoppt das Release. Die rechtlichen Regeln kläre ich mit Ihrem Datenschutz-Beauftragten. Drittens das Tempo der Seite. Google nennt klare Grenzen für echte Nutzer. Ich habe Ihre Seiten gemessen. Für echte Nutzer laden sie schnell. Das ist gut. Aber alle drei Seiten reagieren zu langsam, wenn jemand etwas antippt. Auf der Seite für das Probetraining sind es 361 Millisekunden. Die Grenze ist 200. Ein interessantes Detail: Der Test im Labor sagt, die Probetraining-Seite ist Ihre schnellste. Das liegt daran: Der Labor-Test lädt nur die Seite. Er klickt nie auf den Kalender. Darum würde ich auch die Buchungsschritte selbst messen. Meine erste Regel für die automatische Strecke wäre: Keine Seite wird langsamer als heute. Später machen wir die Grenzen strenger.

---

## 16. Wo KI hilft und wo nicht (2.5 min)

**Slide**
KI hilft bei:
1. **Anforderungen:** findet Lücken und fehlende Sonderfälle in den Regeln für "fertig"
2. **Ausprobieren:** KI-Helfer probieren mit einem Ziel aus und müssen für jedes Ergebnis einen Beweis zeigen
3. **Tests, die durchfallen:** gruppiert die Fehler und sagt: "echter Fehler" oder "nicht stabil"

Immer bei Menschen:
- Wie wichtig ein Fehler wirklich ist
- Ob das Release live geht oder nicht
- Rechtliche Fragen, Barrierefreiheit und Datenschutz

Regeln: keine echten Kundendaten in KI-Werkzeugen. Jedes Ergebnis braucht einen Beweis. Die KI muss sagen, was sie nicht getestet hat.

**Animation**
[loop] Ein Kreislauf. loop: KI schlägt vor > Eine Person prüft > Das Team entscheidet. Die Person in der Mitte bleibt die ganze Zeit sichtbar.

**Notes**
Wo hilft KI? Ich nutze sie an drei Stellen. Erstens bei den Anforderungen. In meinem letzten Job habe ich KI-Helfer gebaut. Sie lesen die Regeln für "fertig" und suchen nach Lücken. Ein Mensch entscheidet dann, welche Lücken echt sind. Zweitens beim Ausprobieren. Ich habe KI-Helfer entworfen. Sie probieren eine Website mit einem klaren Ziel aus. Ich muss hier ehrlich sein. Das System ist entworfen und mit Beispieldaten getestet. Aber ich habe es noch nicht auf einer echten Website benutzt. Wichtig sind die Regeln. Jedes Ergebnis braucht einen Beweis, zum Beispiel einen Screenshot. Der Helfer muss aufschreiben, was er nicht getestet hat. Und Text auf einer Webseite ist für ihn nur Information. Es ist nie eine Anweisung. So kann eine Seite ihn nicht austricksen. Drittens bei Tests, die durchfallen. Die KI kann Fehler gruppieren. Sie kann vorschlagen: echter Fehler, oder Test nicht stabil. Aber manche Dinge bleiben immer bei Menschen. Wie wichtig ein Fehler ist. Ob ein Release live geht. Und alles Rechtliche. Und keine echten Kundendaten kommen in KI-Werkzeuge. Die KI macht Vorschläge. Das Team entscheidet.

---

# Zusatzfolien

## B1. Zahlen zum Tempo der Seite

| Seite (Handy) | Echte Nutzer: LCP | Echte Nutzer: INP | Echte Nutzer: CLS | Labor-Wert |
|---|---|---|---|---|
| Startseite | 2 s | 208 ms | 0,03 | 43 |
| Mitgliedschaft | 1,1 s | 227 ms | 0,04 | 36 |
| Probetraining | 1,3 s | 361 ms | 0,05 | 69 |

Grenzen für "gut" (75 % der Besuche): LCP 2,5 s, INP 200 ms, CLS 0,1. Quelle: PageSpeed Insights, 27. Oktober 2026. Die Labor-Werte kommen aus einzelnen Messungen und schwanken.

**Notes**
LCP heißt: Wie lange dauert es, bis man den Hauptinhalt sieht? INP heißt: Wie schnell reagiert die Seite, wenn man etwas antippt? CLS heißt: Wie stark springt die Seite beim Laden? Beim Labor-Test der Startseite dauerte es fast 29 Sekunden bis zum Hauptinhalt. Das war auf einem langsamen Handy. Echte Nutzer sehen ihn nach 2 Sekunden. Ich weiß nicht genau, warum. Vielleicht hilft der Zwischenspeicher bei Besuchern, die wiederkommen. Oder das Test-Netz war einfach langsam. Das würde ich mit Ihrem Team genauer anschauen.

## B2. Testdaten und Umgebungen

- Stage: unkenntlich gemachte Kopie der echten Daten, oder erfundene Testdaten
- Feste Testkonten und Test-Clubs, die regelmäßig zurückgesetzt werden
- Zahlungsanbieter im Test-Modus, nie echte Zahlungen
- Fremde Systeme, die wir nicht steuern können: in den Tests nachgebaut (Mock), echt nur in wenigen Tests auf Stage
- Test-E-Mails nur an reservierte Test-Adressen

**Notes**
Bei Testdaten gilt eine einfache Regel: Keine echten Kundendaten außerhalb der echten Seite. Manche Systeme kann man schlecht steuern, zum Beispiel einen Zahlungsanbieter. Die baue ich in den meisten Tests nach. Das nennt man Mocking. Nur wenige Tests nutzen den echten Test-Modus der Firma.

## B3. Meine KI-Helfer für Tests (entworfen, noch nicht auf einer echten Seite benutzt)

- 4 Helfer: Entdecker, Bauteile, Ablauf, Schnittstellen
- Regeln: nur erlaubte Test-Seiten, keine echten Käufe, Passwörter versteckt, Beweis für jedes Ergebnis
- Ergebnisse: bestanden, durchgefallen mit Wichtigkeit, oder "verdächtig" mit Grund
- Mehrere Läufe werden zusammengelegt, weil KI-Ergebnisse jedes Mal etwas anders sind
- Ein Fehler mit höchster Wichtigkeit kann die automatische Strecke stoppen. Den Rest entscheiden Menschen.

**Notes**
Das ist das System, das ich erwähnt habe. Ich sage es klar: Es ist gebaut und mit Beispieldaten getestet. Aber noch nicht auf einer echten Website. Ich bin stolz auf die Regeln. Sie beantworten Ihre Fragen zur Kontrolle. Es gibt Beweise. Das System sagt ehrlich, wo es Lücken gibt. Und Menschen treffen die letzte Entscheidung.

## B4. Meine ersten Wochen

- Woche 1 bis 2: Produkt, Team und Release-Ablauf kennenlernen. Alte Fehler lesen.
- Woche 3 bis 4: Risiko-Karte mit dem Team, erste schnelle Erfolge (Cookie-Check, Smoke-Tests)
- Monat 2 bis 3: Tests für Checkout und Buchung, feste Regeln für die automatische Strecke

**Notes**
Wenn ich anfange, ändere ich nicht am ersten Tag alles. Zuerst lerne ich, wie Sie arbeiten. Und woher die Fehler früher kamen. Dann machen wir zusammen eine Risiko-Karte. Die ersten schnellen Erfolge wären der Cookie-Check und die Smoke-Tests. Sie sind klein und schützen viel.

## B5. Eine normale Woche

**Slide**
- **Planung:** Three Amigos bei neuen Aufgaben, Risiken absprechen
- **Jeden Tag:** zu zweit arbeiten, Merge Requests anschauen, kurze Fragen
- **Im Sprint:** neue Funktionen ausprobieren
- **Vor dem Release:** alle Tests auf Stage, Abnahme mit dem Geschäft
- **Release-Tag:** Smoke-Test, beobachten
- **Nach dem Release:** schauen, was durchgerutscht ist, und einen Test dafür bauen

**Notes**
Ich zeige Ihnen eine normale Woche. So sehen Sie, dass das im Alltag funktioniert. Bei der Planung schauen wir neue Aufgaben zusammen an. Wir sprechen die Risiken ab. Jeden Tag arbeite ich mit Entwicklern zu zweit. Ich schaue mir Merge Requests an. Im Sprint probiere ich neue Funktionen aus. Vor dem Release laufen alle Tests auf Stage. Das Geschäft macht die Abnahme. Am Release-Tag gibt es einen Smoke-Test, und wir beobachten die Seite. Nach dem Release schaue ich, was durchgerutscht ist. Für jeden Fehler, der auf die echte Seite kam, bauen wir einen Test. So kommt er nicht wieder.
