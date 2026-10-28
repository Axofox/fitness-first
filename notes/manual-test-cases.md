# Manual test cases for fitnessfirst.de

These are the tests behind the slides, written as steps you can follow by hand. Use them to understand and memorize the story.

**Status of every case: NOT RUN.** I wrote them from the website analysis (`notes/site-analysis.md`) and the risk ranking. I did not execute any of them, and I did not see the payment step, the personal details step or the booking system. Wherever an expected result depends on a rule I do not know, it says "check the real rule".

## Two kinds of cases

- **LOOK (live site):** safe on www.fitnessfirst.de. You only open pages and look, like a normal visitor. Nothing is submitted, no login, nothing booked.
- **TEST ENV:** needs a test environment (the assumption on slide 2). Never do these on the live site, because they submit forms or create bookings and contracts.

Words used here:
- **Expected result:** what must be true for the test to pass.
- **Precondition:** what must be ready before step 1.
- **Priority 1 / 2:** from the risk ranking (slide 4). Priority 1 is built and run first.

---

## 1. Membership checkout (risk number 1)

Flow on the site: Club, then Tarif (plan and contract length), then Extras, then Deine Daten, then Zahlungsinformationen. A summary box ("Deine Übersicht") sits on the side. The club is in the web address as `club_id`.

### MC-01 Happy path up to the payment step (TEST ENV, priority 1)
- **Why:** this is where the money is made (slide 6).
- **Precondition:** a test club, a test plan, test personal data.
- **Steps:** 1. Open the membership page and click "Jetzt Mitglied werden". 2. Choose a club. 3. Choose a plan. 4. Choose extras. 5. Fill in your details. 6. Stop at the payment step.
- **Expected:** every step opens, you can go forward, and the summary box always shows the club and plan you chose.

### MC-02 Summary matches the choice (TEST ENV, priority 1)
- **Why:** the summary box is the classic place for wrong totals (slide 6).
- **Steps:** 1. Pick a plan. 2. Compare plan name, contract length and price in the plan card and in the summary. 3. Add an extra. 4. Compare again.
- **Expected:** the summary always equals what you picked. Price, name and length match. Check the real price list for the right numbers.

### MC-03 Change the club in the middle (TEST ENV, priority 1)
- **Why:** this is the case on slide 9: "change the club mid-way".
- **Steps:** 1. Go to step 2 with club A. 2. Go back and choose club B. 3. Look at the plans and the summary.
- **Expected:** plans, prices and extras change to club B. The summary shows club B. Nothing from club A is left over.

### MC-04 Wrong or old club id in the address (LOOK for the page, TEST ENV for the rest, priority 2)
- **Why:** the club id in the address decides prices and extras.
- **Steps:** 1. Take a checkout address and change the club id to a made up number. 2. Open it. 3. Try an id from a club that no longer exists, if you know one.
- **Expected:** a clear message or a redirect to the club selection. No empty page, no error code, no price from a wrong club.

### MC-05 Club with the 49 euro package against 39 euro (TEST ENV, priority 1)
- **Why:** the training package costs 39 or 49 euro depending on the club (slide 6).
- **Steps:** 1. Start with a club that has the 39 euro package and note the price. 2. Do the same with a club that has the 49 euro package.
- **Expected:** each club shows its own price, in the card and in the summary. Check the real rule for which club has which price.

### MC-06 Student discount (TEST ENV, priority 2)
- **Why:** a discount for students up to age 25 is one of the price rules (slide 6).
- **Steps:** 1. Choose the student option. 2. Enter a birth date for age 24, then 25, then 26. 3. Compare the price each time.
- **Expected:** the discount applies exactly where the rule says. Check the real rule for the age limit and day.

### MC-07 Austria rules (TEST ENV, priority 2)
- **Why:** Austria has its own rules on the same website (slide 6).
- **Steps:** 1. Choose an Austrian club or country in the details. 2. Compare plans, prices and legal texts with a German club.
- **Expected:** the Austrian version shows the Austrian rules and texts. Check the real rules.

### MC-08 Campaign start and end (LOOK and TEST ENV, priority 1)
- **Why:** offers switch on and off by date, and a cache can show an old offer (slide 5).
- **Steps:** 1. On the live site, look at the countdown or end date of an offer. 2. On the test environment, set the date to the day before the end, the end day and the day after. 3. Look at the price each time.
- **Expected:** the offer shows before the end, ends exactly on the end date, and the normal price shows after it. No old offer after the end.

### MC-09 Go back, reload, change the plan (TEST ENV, priority 1)
- **Why:** exploratory idea on slide 3: change my mind often.
- **Steps:** 1. Go to step 4. 2. Use the browser back button twice. 3. Change the plan. 4. Reload the page. 5. Go forward again.
- **Expected:** no wrong or old values, no double extras, the summary is right.

### MC-10 Personal details form (TEST ENV, priority 2)
- **Steps:** 1. Leave required fields empty and continue. 2. Enter a wrong email. 3. Enter a wrong postcode. 4. Fill in correct data.
- **Expected:** every error shows a clear message next to the field. You can fix it and continue. Correct data goes through.

### MC-11 Contract and confirmation arrive (TEST ENV, priority 1)
- **Why:** the worst case is a contract that never arrives (slide 6).
- **Precondition:** payment provider in test mode (assumption), a test email on a reserved test domain.
- **Steps:** 1. Complete a test membership. 2. Check the test mailbox. 3. Ask the team to confirm the contract exists in the member system.
- **Expected:** a confirmation email arrives, and the contract exists in the member system with the right plan, price and club.

### MC-12 Legal texts (LOOK, priority 1)
- **Steps:** 1. On each checkout step, look for the legal texts and links (terms, privacy, withdrawal). 2. Open each link.
- **Expected:** every legal text is present, opens, and is in the right language.

---

## 2. Trial training booking (risk number 4)

Flow on the site: Club (search field, map switch, list of nearby clubs), then Termin (month calendar and time slots in morning, afternoon, evening), then Persönliche Daten. There is also a question about training goals.

### TB-01 Club search with location (LOOK, priority 2)
- **Steps:** 1. Open `/probetraining`. 2. Allow location. 3. Look at the club list. 4. Block location and reload. 5. Type a city in the search field.
- **Expected:** with location, nearby clubs show. Without location, the search field still works and nothing breaks.

### TB-02 Calendar and time slots (LOOK, priority 1)
- **Why:** the slot must exist at the club (slide 7).
- **Steps:** 1. Choose a club. 2. Look at today, tomorrow and the weekend. 3. Go to the next month and back. 4. Look at a public holiday.
- **Expected:** past times are not offered. Slots look like real availability. Month change and holidays do not break the calendar. Check the real opening hours and holiday rules with the club.

### TB-03 Booking arrives at the club (TEST ENV, priority 1)
- **Why:** the biggest risk is a booking that never reaches the club (slide 7).
- **Steps:** 1. Complete a test booking. 2. Ask the test club system to show the booking.
- **Expected:** the booking is there with the right club, day, time and name. A confirmation email arrives.

### TB-04 Double click and reload after submit (TEST ENV, priority 1)
- **Why:** you asked about double bookings. This one is my assumption about what can go wrong.
- **Steps:** 1. At the last step, double click the confirm button. 2. In a second try, reload the page right after confirming.
- **Expected:** exactly one booking, not two. The person sees one confirmation.

### TB-05 Last spot booked twice (TEST ENV, priority 2)
- **Open question:** I do not know if a slot has a limit of spots. Ask the team before testing this.
- **Steps (if there is a limit):** 1. Fill a slot to one free spot. 2. Open the booking in two browsers. 3. Confirm both at the same time.
- **Expected:** only one booking succeeds. The other person gets a clear message and can pick another time. A full slot disappears from the list.

### TB-06 Time zone and date edge cases (TEST ENV, priority 2)
- **Steps:** 1. Book on the last day of the month. 2. Book at 23:30 for the next day. 3. Change your computer clock to the time zone of another country and book again.
- **Expected:** the date and time in the confirmation equal what you chose.

### TB-07 Reaction when tapping (LOOK on a phone, priority 2)
- **Why:** real users on the trial page are slow to react (slide 7).
- **Steps:** 1. On a real phone, tap a calendar day and a time slot. 2. Notice if there is a delay before the page reacts.
- **Expected:** the page reacts right away. A noticeable delay is a finding. Note the phone type and network.

---

## 3. Cookie consent and tracking (risk number 2)

Tool seen: Usercentrics. About 15 ad and tracking services loaded on the trial page.

### CC-01 First visit shows the banner (LOOK, priority 1)
- **Precondition:** a fresh browser profile or a private window, so no earlier choice is saved.
- **Steps:** 1. Open the homepage. 2. Look at the banner.
- **Expected:** the banner shows before any marketing tracker loads. "Alle ablehnen" (decline all) is as easy to find as accept.

### CC-02 Decline all (LOOK, priority 1)
- **Why:** this is the check behind the gate on slide 15.
- **Steps:** 1. Fresh profile. 2. Open the developer tools, Network tab. 3. Click decline all. 4. Click through the homepage, the membership page and the trial page. 5. Look at which hosts load.
- **Expected:** no marketing or ad hosts load (for example Facebook, TikTok, Google Ads). Only allowed services load. If a marketing tracker loads after decline, that is a release stopper.

### CC-03 Accept all (LOOK, priority 2)
- **Steps:** 1. Fresh profile. 2. Accept all. 3. Use the pages.
- **Expected:** the pages work. Marketing services may load now.

### CC-04 Change the choice later (LOOK, priority 2)
- **Steps:** 1. Accept all. 2. Find the link to change the cookie settings. 3. Decline. 4. Reload.
- **Expected:** the setting can be changed, and after decline the trackers stop loading.

### CC-05 Banner texts (LOOK, priority 2)
- **Why:** I saw an English placeholder text on a German page.
- **Steps:** 1. Read the banner and the settings texts. 2. Switch the page language if there is an option.
- **Expected:** the texts are in the right language, and clear. Check the wording with the data protection officer.

---

## 4. Pause, cancel, withdrawal (risk number 3)

### PC-01 The links exist and open (LOOK, priority 1)
- **Steps:** 1. Find the links to pause and cancel on the membership page. 2. Open each one.
- **Expected:** the links work and lead to the right page.

### PC-02 Full flow (TEST ENV, priority 1)
- **Precondition:** a test member (I did not look at the login).
- **Steps:** 1. Log in as the test member. 2. Pause the membership. 3. Cancel a second test membership. 4. Check the confirmation text and email.
- **Expected:** each flow works to the end, the confirmation shows the right date, and the member system shows the new status. Check the real rules for notice periods.

### PC-03 Texts and keyboard (LOOK and TEST ENV, priority 1)
- **Steps:** 1. Read the texts of both flows. 2. Do the flows with only the keyboard.
- **Expected:** the legal texts are present and clear. The cancel button can be reached and used with the keyboard.

---

## 5. Accessibility (non-functional area 1)

Only the automatic scores were seen: 92, 93 and 100 on the three pages. These cases are the manual part that the score cannot show.

### AC-01 Whole checkout with keyboard only (TEST ENV, priority 1)
- **Steps:** 1. Use only Tab, Shift+Tab, Enter and Space. 2. Go through the checkout up to the payment step.
- **Expected:** every field and button can be reached in a sensible order. The focus is always visible. You can finish.

### AC-02 Screen reader reads the errors (TEST ENV, priority 1)
- **Steps:** 1. Turn on VoiceOver (Mac) or NVDA (Windows). 2. Leave a required field empty and continue.
- **Expected:** the error message is read out, and you know which field it belongs to.

### AC-03 Zoom and contrast (LOOK, priority 2)
- **Steps:** 1. Zoom the page to 200 percent. 2. Look at text and buttons.
- **Expected:** nothing is cut off or overlapping. Text is readable.

---

## 6. Page speed (non-functional area 3)

### PS-01 Measure the three pages (LOOK, priority 2)
- **Steps:** 1. Open PageSpeed Insights. 2. Enter the homepage, the membership page and the trial training page, mobile. 3. Write down the real-user results.
- **Expected:** the real-user results are at or under Google's limits: main content in 2.5 s, reaction to a tap in 200 ms. Compare with the numbers on extra slide B1.

### PS-02 Time the booking steps (TEST ENV, priority 2)
- **Why:** a test that only loads the page never clicks the calendar (slide 15).
- **Steps:** 1. Open the booking on a phone or in a phone-sized browser. 2. Time how long the page needs to react after each tap.
- **Expected:** every step reacts fast. Slow steps are written down.

---

## 7. A/B tests and caching

### AB-01 Different versions of the page (LOOK, priority 2)
- **Why:** VWO shows different visitors different versions (slide 8).
- **Steps:** 1. Open the same page in two private windows. 2. Compare text, buttons and prices.
- **Expected:** if the versions differ, note which one each window showed. Every bug report must say which version it saw.

### CA-01 Old offer after the end (LOOK and TEST ENV, priority 1)
- **Steps:** 1. After an offer has ended, open the page in a fresh browser and in one you used before. 2. Compare.
- **Expected:** neither shows the old offer.

---

## 8. Devices

### DV-01 Same flows on different screens (priority 1 for MC-01 and TB-02)
- **Steps:** 1. Run MC-01 and TB-02 in a desktop browser. 2. Repeat in the mobile browser view with widths 360, 390 and 768 pixels. 3. Before big releases, repeat on a real iPhone (Safari) and a real Android phone (Chrome).
- **Expected:** the same result on every screen. Buttons can be tapped, nothing is cut off.

---

## 9. Three exploratory sessions (slide 3)

Exploratory means you explore with a goal and a time limit, without a fixed script. Write down: goal, device and browser, page version, what you covered, bugs with steps and screenshots, open questions, what you did NOT test.

1. **Checkout, change my mind often.** 60 to 90 minutes. Goal: find wrong totals. Change club, plan and extras, go back, reload.
2. **Strange combinations.** 60 minutes. Goal: find prices that look wrong. Student plus another club, an Austrian club, an offer on its last day.
3. **Booking on a phone.** 60 minutes. Goal: find slots or dates that look wrong, and slow reactions. Real phone, bad network, location blocked.

---

## One sentence to remember

I find the expensive mistakes first, by risk, and I find them early: the checkout and the booking first, then consent, then the rest.
