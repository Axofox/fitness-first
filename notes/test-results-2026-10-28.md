# Test run results, 28 Oct 2026

Who ran it: Claude, in a desktop Chrome window, as a normal visitor.
What "run" means here: I only looked, clicked links and opened pages. I did not enter any data, submit a form, log in, book, buy, pause or cancel. This follows the rules in CLAUDE.md.

Important: this is a small look-only run, not a full test. It does not prove that the checkout works. Everything that needs data entry or a real booking was NOT run.

## Summary

- Cases run (look only): 6
- Passed: 4
- Open questions (not bugs): 4
- Confirmed bugs: 0
- Not run: all cases that enter data, submit, book, pay, pause or cancel (TEST ENV cases)

## Results per case

| Case | What I did | Result |
|---|---|---|
| MC-03 change club | In the checkout I clicked "ändern", then CLUB AUSWÄHLEN for München - Sendling. | PASS. Step 1 shows München - Sendling. "Deine Übersicht" shows München - Sendling and BLACK. Nothing from München - Laim was left on the page. |
| MC-02 summary box | Compared the summary box with the chosen club. | PARTLY RUN. Club and club type match. I did not select a plan, so plan and price lines in the summary were not checked. |
| Plans and prices (part of MC-01) | Opened "Mehr Tarifoptionen zeigen" and "Tarifdetails anzeigen". | PASS for what is shown: 24 months with 12 weeks free then 19,90 euro per week; 12 months 21,90 euro per week; 1 month 27,90 euro per week. The same prices show for Laim and Sendling. That can be correct, because both are BLACK clubs. I cannot say it is correct. |
| MC-04 made-up club number | Opened the checkout with a club number that does not exist (club_id=99999999). Page load only. | INCONCLUSIVE. The address was cleaned to /mitgliedschaft-checkout and the club from before (Sendling) stayed selected. No error page. Because the browser remembered my earlier club, I cannot tell what a first-time visitor sees. Needs a fresh browser with no saved state. |
| MC-12 and PC-01 footer and cancel pages | Opened /kuendigung and /rechtliches/widerrufsbelehrung. | PASS. Both pages load and show the expected content: pause options 4, 8, 12 weeks, the buttons WEITER, TRAINING PAUSIEREN, VERTRAG HIER KÜNDIGEN, and the withdrawal page with VERTRAG HIER WIDERRUFEN. |
| TB-01 and TB-02 trial page | Opened /probetraining and read the club list. | PASS for the list. 8 clubs in Munich are listed with address and distance. The steps "Termin" and "Persönliche Daten" are shown as later steps. I did not choose a club or a date. |

## Open questions (not bugs)

I cannot say if these are errors. They need someone who knows the intended behaviour.

1. Pause time: the checkout plan text says "bis zu 12 Wochen pro Kalenderjahr". The page /kuendigung offers pauses of 4, 8 or 12 weeks. Are these the same rule?
2. Student discount: the plan text says "bis zu 13 euro Rabatt pro Monat". Earlier I noted a different wording in the small print. Which one is meant?
3. Offer date: the trial page says "nur bis 31. Oktober" and "Verlängerung vorbehalten" (extension reserved). That fits the countdown, but I cannot know if it ends on time. Cannot be checked before it happens.
4. The text "86% unserer Mitglieder entscheiden sich dafür, ihre Mitgliedschaft einfach zu pausieren" on /kuendigung has no source on the page. This is a content question, not a software bug. It is also listed in notes/not-verified.md.

## Seen once, not confirmed

During this run, after a click on a wrong spot (the window had changed size), the page looked blurred and dimmed and the Escape key did not clear it. A reload fixed it. I saw it once, could not repeat it, and the cause may be my own click. It is not a bug report. Next time: try to repeat it in a fresh browser.

## Not run, and why

- All cases marked TEST ENV (real sign-up, payment, trial booking, pause, cancel, withdrawal). These need a test system or test accounts. Doing them on www.fitnessfirst.de is not allowed.
- Cookie consent cases (CC-01 to CC-05). I did not change consent choices on the live site in this run.
- Accessibility and page speed cases (AC, PS). These need tools, and automated runs on the production site are not allowed.
- A/B test case (AB-01) and cache case (CA-01). I cannot control which version the site shows me.
- Device cases (DV-01). Only one desktop window size was used in this run.
- Exploratory sessions.

## What this means for Friday

I can say honestly: "I walked the public pages like a visitor and found no confirmed bug. I found four questions I would ask the team. The real checkout tests need a test system."
