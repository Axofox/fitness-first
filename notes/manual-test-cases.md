# Manual test cases for fitnessfirst.de

These are the tests behind the slides, written as steps you can follow by hand. Use them to understand and memorize the story.

**Status of every case: NOT RUN.** I wrote them from the website analysis and from reading the public pages on 28 October 2026 (read-only, nothing clicked or submitted). I did not see the checkout steps after the club choice, the payment step, the personal details step, the calendar and the booking system. Where I don't know a button name, the step says "label not checked".

## How to read the steps

- **Names in CAPITALS in quotes** (like "JETZT MITGLIED WERDEN") are written exactly like that on the site. I read them on 28 October 2026.
- **LOOK (live site):** safe on www.fitnessfirst.de. You only open pages and look, like a normal visitor. Nothing is submitted, no login, nothing booked.
- **TEST ENV:** needs a test environment (the assumption on slide 2). Never do these on the live site, because they submit forms or create bookings and contracts. The address of a test environment is not known, so the steps use the same page names.
- **Expected result:** what must be true for the test to pass.
- **Priority 1 / 2:** from the risk ranking (slide 4). Priority 1 is built and run first.

## Rules on the site that I read (28 October 2026)

These help you check expected prices and texts. Source: the small print on `/mitgliedschaft`.

- Offer banner: "TRAINIERE 12 WOCHEN GRATIS" with a countdown, "NUR BIS 31. OKTOBER".
- Germany: a 24 month membership (ALL-IN RED or BLACK) gets the first 12 weeks free, plus a half-yearly training package of 39 or 49 euro "in selected clubs". The one-time start fee of 39 euro is waived.
- Flex option: in months 1 to 3 you can end the contract for a one-time fee of 99 euro, with 4 weeks notice.
- Pause: up to 12 weeks, free. On the pause page you choose 4, 8 or 12 weeks.
- Switch offer (from another gym): the remaining term, up to 12 months in Germany and up to 6 months in Austria, is free at the start.
- Austria: a 12 month membership (ALL-IN RED), first 12 weeks free, plus a one-time training package of 39 euro.
- Student discount: valid up to and including age 25. The small print says up to 13 euro per month in Germany and up to 8.50 euro in Austria. The text above it says "2 euro off your weekly fee". I did not check if both fit together.
- The page `/mitgliedschaft/gesamtpreis` ("Gesamtpreisberechnung") shows the total price for a club after you choose it.

---

## 1. Membership checkout (risk number 1)

Flow on the site: Club, then "Laufzeit / Tarif", then "Extras", then "Deine Daten", then "Zahlungsinformationen". A side box called "Deine Übersicht" shows club and plan. The club is in the address as `club_id`.

### MC-01 Happy path up to the payment step (TEST ENV, priority 1)
- **Why:** this is where the money is made (slide 6).
- **Precondition:** a test club, test personal data.
- **Steps:**
    1. Open `/mitgliedschaft`.
    2. Under "WO WILLST DU TRAINIEREN?" find the club list. Click "CLUB AUSWÄHLEN" next to a club, for example "München - Laim". (The big button "JETZT MITGLIED WERDEN" and the top button "ANGEBOT SICHERN" lead to the same start.)
    3. The checkout page opens, with `club_id` in the address. The step "Club" is done.
    4. On "Laufzeit / Tarif" choose a plan. Look for the card with "Bestseller / Top-Preis" and the button "Mehr Tarifoptionen zeigen" for more plans.
    5. On "Extras" choose or skip extras (button label not checked).
    6. On "Deine Daten" fill in the test data (button label not checked).
    7. Stop when "Zahlungsinformationen" opens.
- **Expected:** every step opens and you can go forward. "Deine Übersicht" always shows the club and plan you chose.

### MC-02 Summary matches the choice (TEST ENV, priority 1)
- **Why:** the summary box is the classic place for wrong totals (slide 6).
- **Steps:**
    1. Reach "Laufzeit / Tarif" as in MC-01.
    2. Click "Mehr Tarifoptionen zeigen" and pick a plan.
    3. Compare plan name, contract length and price on the plan card with "Deine Übersicht".
    4. Go to "Extras", add one, and compare again.
- **Expected:** "Deine Übersicht" always equals what you picked. Compare also with the total price on `/mitgliedschaft/gesamtpreis`.

### MC-03 Change the club in the middle (TEST ENV, priority 1)
- **Why:** the case on slide 9, "change the club mid-way".
- **Steps:**
    1. Do MC-01 with club A up to "Laufzeit / Tarif". Note the plans and prices.
    2. Go back to the "Club" step (label of the back button not checked) and choose club B with "CLUB AUSWÄHLEN".
    3. Look at the plans, prices and extras, and at "Deine Übersicht".
- **Expected:** plans, prices and extras are those of club B. "Deine Übersicht" shows club B. Nothing from club A is left over.

### MC-04 Wrong or old club id in the address (LOOK for the first part, priority 2)
- **Why:** the club id in the address decides prices and extras.
- **Steps:**
    1. Open a checkout address from MC-01. In the address bar, replace the number after `club_id=` with a made up number, and press Enter.
    2. Try also an empty `club_id=`.
- **Expected:** a clear message or a redirect to the club selection. No empty page, no error code, no prices from a wrong club. (Opening the page is safe on the live site. Do not continue the flow there.)

### MC-05 Training package 39 against 49 euro (TEST ENV, priority 1)
- **Why:** the package costs 39 or 49 euro "in selected clubs" (slide 6).
- **Steps:**
    1. Start MC-01 with the club "München - Laim" and note the price and the package amount.
    2. Repeat with "München - Moosach" (a RED club) and with "München - Sendling" (a BLACK club).
    3. Compare.
- **Expected:** each club shows its own price and package, on the plan card and in "Deine Übersicht". Which club has 39 and which 49 is not known to me, so ask the team for the list.

### MC-06 Student discount (TEST ENV, priority 2)
- **Why:** the student discount is valid up to and including age 25 (slide 6).
- **Steps:**
    1. Look on `/mitgliedschaft` at "EXKLUSIVE ANGEBOTE FÜR: Studierende, Schüler:innen & Azubis".
    2. In the checkout, find the student option (where it is: not checked).
    3. Enter a birth date for age 24, then 25, then 26 and compare the price.
- **Expected:** the discount applies up to and including age 25 and not at 26. The amount equals the rule (see the rules above, which do not fully agree: ask the team).

### MC-07 Austria rules (TEST ENV, priority 2)
- **Why:** Austria has its own rules (slide 6).
- **Steps:**
    1. Start the checkout with an Austrian club (the small print has a separate part marked "AT").
    2. Compare plan length, training package and texts with a German club.
- **Expected:** the Austrian club shows a 12 month ALL-IN RED plan with a one-time package of 39 euro, and Austrian texts. The German club shows 24 months.

### MC-08 Campaign start and end (LOOK and TEST ENV, priority 1)
- **Why:** offers switch on and off by date, and a cache can show an old offer (slide 5).
- **Steps:**
    1. LOOK: on `/mitgliedschaft` read the countdown ("Tage, Stunden, Minuten, Sekunden") and the text "NUR BIS 31. OKTOBER". Check that the countdown agrees with the date.
    2. TEST ENV: set the date to 30 October, 31 October and 1 November. Open `/mitgliedschaft` each time.
- **Expected:** the offer shows until the end date, then the banner, the countdown and the free weeks are gone and the normal price shows. No old offer after the end. (I also saw "27 October" in my first notes, but the page now says 31 October. I did not find out why.)

### MC-09 Go back, reload, change the plan (TEST ENV, priority 1)
- **Why:** exploratory idea on slide 3, change my mind often.
- **Steps:**
    1. Go to "Deine Daten".
    2. Click the browser back button twice.
    3. Choose another plan.
    4. Reload the page (F5).
    5. Go forward again.
- **Expected:** no wrong or old values, no double extras, "Deine Übersicht" is right.

### MC-10 Personal details form (TEST ENV, priority 2)
- **Steps:**
    1. On "Deine Daten" leave the required fields empty and click the button to continue.
    2. Type a wrong email, like `abc`.
    3. Type a wrong postcode.
    4. Fill in correct data and continue.
- **Expected:** every error shows a clear message next to its field. You can fix it and continue. Correct data goes through.

### MC-11 Contract and confirmation arrive (TEST ENV, priority 1)
- **Why:** the worst case is a contract that never arrives (slide 6).
- **Precondition:** payment provider in test mode (assumption), a test email on a reserved test domain.
- **Steps:**
    1. Complete a test membership up to the end.
    2. Open the test mailbox.
    3. Ask the team to confirm that the contract exists in the member system.
- **Expected:** a confirmation email arrives (the FAQ on `/mitgliedschaft` asks "Wird mir der Vertrag zugeschickt?", so check the answer there). The contract exists with the right plan, price and club.

### MC-12 Legal texts (LOOK, priority 1)
- **Steps:**
    1. On `/mitgliedschaft`, scroll to the small print that starts with "*DE:".
    2. Scroll to the footer. In the SERVICE part, click "Widerruf".
    3. In the checkout, look at each step for links to the terms and privacy (TEST ENV).
- **Expected:** every legal text is present, opens, and is in the right language. The "Widerruf" page opens at `/rechtliches/widerrufsbelehrung`.

---

## 2. Trial training booking (risk number 4)

Flow on the site: Club (search and club list), then Termin (calendar and time slots), then "Persönliche Daten". Page: `/probetraining`.

### TB-01 Club search (LOOK, priority 2)
- **Steps:**
    1. Open `/probetraining`. Scroll to "WÄHLE EINEN CLUB & VEREINBARE DEIN PROBETRAINING!".
    2. If the browser asks for your location, click Allow. Look at the list: "8 Clubs in München gefunden", sorted by distance.
    3. Reload and click Block. Click "STUDIO FINDEN" and type a city, for example "Dresden". Press Enter.
- **Expected:** with location, nearby clubs show. Without location, the search still works and nothing breaks. Each club has a "CLUB AUSWÄHLEN" button and a label BLACK or RED.

### TB-02 Calendar and time slots (priority 1)
- **Why:** the slot must exist at the club (slide 7).
- **Steps:**
    1. On `/probetraining` click "CLUB AUSWÄHLEN" next to a club. (This only opens the next step. On the live site stop here and do not enter any data.)
    2. Look at the calendar: today, tomorrow, the next weekend.
    3. Click the arrow for the next month (label not checked) and back.
    4. Look at a public holiday.
- **Expected:** past times are not offered. Slots look like real availability. Month change and holidays do not break the calendar. Check the real opening hours and holiday rules with the club.

### TB-03 Booking arrives at the club (TEST ENV, priority 1)
- **Why:** the biggest risk is a booking that never reaches the club (slide 7).
- **Steps:**
    1. Complete a test booking: club, day and time, "Persönliche Daten".
    2. Ask the test club system to show the booking.
- **Expected:** the booking is there with the right club, day, time and name. A confirmation email arrives.

### TB-04 Double click and reload after submit (TEST ENV, priority 1)
- **Why:** you asked about double bookings. What can go wrong here is my assumption.
- **Steps:**
    1. At the last step, double click the button that confirms the booking (label not checked).
    2. In a second try, press F5 right after confirming.
- **Expected:** exactly one booking, not two. The person sees one confirmation.

### TB-05 Last spot booked twice (TEST ENV, priority 2)
- **Open question:** I do not know if a slot has a limit of spots. Ask the team before testing this.
- **Steps (only if there is a limit):**
    1. Fill a slot up to one free spot.
    2. Open the booking in two browsers and select that slot in both.
    3. Confirm both at the same time.
- **Expected:** only one booking succeeds. The other person gets a clear message and can pick another time. A full slot disappears from the list.

### TB-06 Time zone and date edge cases (TEST ENV, priority 2)
- **Steps:**
    1. Book on the last day of a month.
    2. Book at 23:30 for the next day.
    3. Change your computer to another time zone and book again.
- **Expected:** the date and time in the confirmation equal what you chose.

### TB-07 Reaction when tapping (LOOK on a phone, priority 2)
- **Why:** real users on the trial page are slow to react (slide 7).
- **Steps:**
    1. On a real phone open `/probetraining`.
    2. Tap "CLUB AUSWÄHLEN", then a calendar day, then a time slot.
    3. Notice if there is a delay before the page reacts.
- **Expected:** the page reacts right away. A noticeable delay is a finding. Note the phone type and network.

### TB-08 Minors (LOOK first, priority 2)
- **Why:** the FAQ on `/probetraining` has a question "Kann ich als Minderjährige:r ein Probetraining abschließen und was brauche ich dafür?"
- **Steps:**
    1. On `/probetraining` scroll to "FAQ ZU DEINEM PROBETRAINING".
    2. Click that question and read the answer.
    3. TEST ENV: enter a birth date under 18 in the personal details.
- **Expected:** the form behaves as the FAQ says (for example, it asks for what the answer requires). Check the real rule.

---

## 3. Cookie consent and tracking (risk number 2)

Tool seen: Usercentrics. About 15 ad and tracking services loaded on the trial page. In the footer, under SERVICE, there is a link "Cookie-Einstellungen" (opens `/rechtliches/datenschutz#privacy-settings`).

### CC-01 First visit shows the banner (LOOK, priority 1)
- **Precondition:** a private window (File, New Private Window), so no earlier choice is saved.
- **Steps:**
    1. Open `https://www.fitnessfirst.de`.
    2. Look at the banner.
- **Expected:** the banner shows before any marketing tracker loads. The decline button is as easy to find as accept. (The exact button names are not checked: my browser already had a saved choice.)

### CC-02 Decline all (LOOK, priority 1)
- **Why:** this is the check behind the gate on slide 15.
- **Steps:**
    1. Open a new private window and press F12 (developer tools), then click the tab "Network".
    2. Open `https://www.fitnessfirst.de`.
    3. In the banner, click the button that declines everything.
    4. Open `/mitgliedschaft` and `/probetraining`.
    5. In "Network" look at the list of hosts.
- **Expected:** no marketing or ad hosts load (for example Facebook, TikTok, LinkedIn, Pinterest, Google Ads). Only allowed services load. If a marketing tracker loads after decline, that is a release stopper.

### CC-03 Accept all (LOOK, priority 2)
- **Steps:**
    1. New private window, open the homepage.
    2. Click the button that accepts everything.
    3. Open `/mitgliedschaft` and `/probetraining`.
- **Expected:** the pages work. Marketing services may load now.

### CC-04 Change the choice later (LOOK, priority 2)
- **Steps:**
    1. Accept all as in CC-03.
    2. Scroll to the footer. Under SERVICE click "Cookie-Einstellungen".
    3. In the settings turn the marketing choices off and save (button label not checked).
    4. Reload the page and look at "Network".
- **Expected:** the setting can be changed, and after saving the marketing hosts stop loading.

### CC-05 Banner texts (LOOK, priority 2)
- **Why:** I saw an English text, "We need your consent to load the Adition service!", on a German page.
- **Steps:**
    1. Read the banner and the settings texts.
    2. Open `/mitgliedschaft` and look for placeholder texts where a service is blocked.
- **Expected:** the texts are in the right language and clear. Check the wording with the data protection officer.

---

## 4. Pause, cancel, withdrawal (risk number 3)

Good to know: you do not need a login to reach these pages. The footer, under SERVICE, has the links "Mitgliedschaft hier pausieren", "Mitgliedschaft hier kündigen" and "Widerruf".

### PC-01 The links exist and open (LOOK, priority 1)
- **Steps:**
    1. Open any page, scroll to the footer.
    2. Under SERVICE click "Mitgliedschaft hier pausieren". It opens `/kuendigung`.
    3. Go back. Click "Mitgliedschaft hier kündigen". It opens `/kuendigung/antrag`.
    4. Go back. Click "Widerruf". It opens `/rechtliches/widerrufsbelehrung`.
- **Expected:** all three links work and lead to the right page.

### PC-02 Pause page (LOOK for reading, TEST ENV for sending, priority 1)
- **Steps:**
    1. Open `/kuendigung`. The headline asks "BIST DU SICHER, DASS DU KÜNDIGEN MÖCHTEST?".
    2. Under "Wie lange möchtest du deinen Vertrag pausieren?" look at the choices "4 Wochen", "8 Wochen", "12 Wochen" and the field "Dein Club".
    3. TEST ENV: choose "8 Wochen", choose a club, click "WEITER", and finish with "TRAINING PAUSIEREN".
- **Expected:** the three pause lengths work. The page text says that no fees apply during the pause and that the contract term moves by the length of the pause. Check this with the member system (does the new end date move by 8 weeks?). The page says "86%" of members choose a pause: ask where this number comes from.

### PC-03 Cancel form (LOOK for reading, TEST ENV for sending, priority 1)
- **Steps:**
    1. On `/kuendigung` scroll down to "Du möchtest wirklich gehen?" and click "VERTRAG HIER KÜNDIGEN". The form opens at `/kuendigung/antrag`.
    2. Look at the fields: "Dein Club", "Mitgliedsnummer?", "Dein Vorname", "Dein Nachname", "Deine E-Mail-Adresse", "Art der Kündigung", "Grund für den Kündigungsantrag (optional)", "Telefonnummer bei Rückfragen (optional)", "DATEI HOCHLADEN (OPTIONAL)".
    3. TEST ENV: fill the form with a test member and click "JETZT KÜNDIGEN". Never do this on the live site.
    4. TEST ENV: leave "Mitgliedsnummer?" empty and click "JETZT KÜNDIGEN". Upload a file bigger than 2 MB, then a file that is not jpg, jpeg or png.
- **Expected:** a confirmation appears, and the team confirms by email (the page says so). Empty fields and wrong files show a clear message. The page says that a file must be max 2 MB and jpg, jpeg or png.

### PC-04 Keyboard on the cancel and pause pages (LOOK, priority 1)
- **Steps:**
    1. Open `/kuendigung`. Press Tab repeatedly and watch the focus.
    2. Select a pause length with the keyboard. Reach the buttons "WEITER" and "VERTRAG HIER KÜNDIGEN" and press Enter (on the live site stop before a real submit).
- **Expected:** every field and button can be reached in a sensible order. The focus is visible.

---

## 5. Accessibility (non-functional area 1)

Only the automatic scores were seen: 92, 93 and 100 on the three pages. These cases are the manual part that the score cannot show. The footer has a link "Barrierefreiheitserklärung" (accessibility statement), which opens `/rechtliches/barrierefreiheitserklaerung`.

### AC-01 Whole checkout with keyboard only (TEST ENV, priority 1)
- **Steps:**
    1. Use only Tab, Shift+Tab, Enter and Space (no mouse).
    2. Go through the checkout from the club choice up to "Zahlungsinformationen".
- **Expected:** every field and button can be reached in a sensible order. The focus is always visible. You can finish.

### AC-02 Screen reader reads the errors (TEST ENV, priority 1)
- **Steps:**
    1. Turn on VoiceOver on a Mac (Command + F5).
    2. On "Deine Daten" leave a required field empty and continue.
- **Expected:** the error message is read out, and you know which field it belongs to.

### AC-03 Zoom and contrast (LOOK, priority 2)
- **Steps:**
    1. Open `/mitgliedschaft`. Press Command and + until the zoom shows 200 percent.
    2. Look at text and buttons.
- **Expected:** nothing is cut off or overlapping. Text is readable.

### AC-04 Accessibility statement (LOOK, priority 2)
- **Steps:**
    1. Scroll to the footer and click "Barrierefreiheitserklärung".
    2. Read what it says about known problems and about how to report one.
- **Expected:** the page opens. Compare its claims with what you find in AC-01 to AC-03.

---

## 6. Page speed (non-functional area 3)

### PS-01 Measure the three pages (LOOK, priority 2)
- **Steps:**
    1. Open `https://pagespeed.web.dev`.
    2. Enter `https://www.fitnessfirst.de`, click "Analyze", then click "Mobile" and look at the section for real users.
    3. Repeat with `/mitgliedschaft` and `/probetraining`.
- **Expected:** the real-user results are at or under Google's limits: main content in 2.5 s, reaction to a tap in 200 ms. Compare with the numbers on extra slide B1.

### PS-02 Time the booking steps (TEST ENV, priority 2)
- **Why:** a test that only loads the page never clicks the calendar (slide 15).
- **Steps:**
    1. Open the booking on a phone or in a phone-sized browser.
    2. Time how long the page needs to react after each tap.
- **Expected:** every step reacts fast. Slow steps are written down.

---

## 7. A/B tests and caching

### AB-01 Different versions of the page (LOOK, priority 2)
- **Why:** VWO is an A/B testing tool, so different visitors may see different versions of a page (slide 8). I saw VWO load, but I did not check if a test is running right now.
- **Steps:**
    1. Open `/mitgliedschaft` in two private windows.
    2. Compare the text, the buttons and the prices.
- **Expected:** if the versions differ, note which one each window showed. Every bug report must say which version it saw.

### CA-01 Old offer after the end (LOOK and TEST ENV, priority 1)
- **Steps:**
    1. After 31 October, open `/mitgliedschaft` in a fresh private window and in a browser you used before the end.
    2. Compare the banner "TRAINIERE 12 WOCHEN GRATIS".
- **Expected:** neither shows the old offer.

---

## 8. Devices

### DV-01 Same flows on different screens (priority 1 for MC-01 and TB-02)
- **Steps:**
    1. Run MC-01 and TB-02 in a desktop browser.
    2. In Chrome press F12, click the phone icon (device toolbar) and set the widths 360, 390 and 768 pixels. Repeat.
    3. Before big releases, repeat on a real iPhone (Safari) and a real Android phone (Chrome).
- **Expected:** the same result on every screen. Buttons can be tapped, nothing is cut off.

---

## 9. Three exploratory sessions (slide 3)

Exploratory means you explore with a goal and a time limit, without a fixed script. Write down: goal, device and browser, which version of the page you saw (only if the site shows different A/B versions, see AB-01), what you covered, bugs with steps and screenshots, open questions, what you did NOT test.

1. **Checkout, change my mind often.** 60 to 90 minutes. Goal: find wrong totals. Change club, plan and extras, go back, reload.
2. **Strange combinations.** 60 minutes. Goal: find prices that look wrong. Student plus another club, an Austrian club, an offer on its last day.
3. **Booking on a phone.** 60 minutes. Goal: find slots or dates that look wrong, and slow reactions. Real phone, bad network, location blocked.

---

## One sentence to remember

I find the expensive mistakes first, by risk, and I find them early: the checkout and the booking first, then consent, then the rest.
