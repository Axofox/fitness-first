# Website analysis (2026-10-27)

Read-only, in Tina's Chrome, like a visitor. No form submitted, no login, nothing booked or bought.
Method: page text plus the list of hosts the browser loaded (`performance` entries). No screenshots.

## Trial training booking (`/probetraining`)

Steps shown on the page:
1. **Club:** search field with autocomplete, a "show map" switch, and a list of nearby clubs (8 Munich clubs were shown, so the list is location based). Each club has a "Club auswählen" button.
2. **Termin (appointment):** a month calendar and time slots split into morning, afternoon, evening (example: next day, 7:00 to 12:00 in 30-minute steps, some times missing, so slots look like real availability).
3. **Persönliche Daten (personal details):** not opened.

Also on the page: a question about training goals (7 options: weight loss, endurance, ...), FAQ, club cards.

QA notes:
- Slot times must match what the club can actually offer. Where the slots come from was not visible: no separate booking host showed up in the network list. **Unknown.**
- The club list depends on the visitor's location, so test with different locations and with location access denied.
- Date logic: today, tomorrow, weekends, month change, holidays, time zone.

## Membership shop (`/mitgliedschaft` then `/mitgliedschaft-checkout?club_id=...`)

- "Jetzt Mitglied werden" opens a club selector, then a separate checkout page with the club in the address (`club_id`).
- Checkout steps: **Club** (done) > **Laufzeit / Tarif** (contract length and plan) > **Extras** > **Deine Daten** > **Zahlungsinformationen** (payment).
- On the plan step: a "Bestseller / Top-Preis" BLACK card and "Mehr Tarifoptionen zeigen" (more plans). A summary box on the side ("Deine Übersicht") shows club and plan.
- I stopped here. Prices per plan and the payment step were not read (opening more options was blocked by my own safety check, and the payment step needs personal data).

QA notes:
- The club id in the address decides prices and extras. Test switching clubs mid-flow, a wrong or old club id, and a club with the €49 training package versus €39.
- The summary box must always match the chosen options. Classic place for wrong totals.
- The page also has links to pause and cancel, so the legal flows sit right next to the sales flow.

## Outside services seen

Hosts the browser loaded on the trial training page. "How sure" = how sure I am about what the service is.

| Host | What it is | How sure |
|---|---|---|
| `*.usercentrics.eu` | Cookie consent tool (Usercentrics) | Sure |
| `www.googletagmanager.com`, `sst.fitnessfirst.de` | Tag manager, plus server-side tracking on their own subdomain | Sure / likely |
| `dev.visualwebsiteoptimizer.com` | VWO, A/B testing (different visitors can see different versions of a page) | Sure |
| `fitnessfirst.app.baqend.com` | Baqend Speed Kit, a speed-up service that caches pages in the browser | Likely |
| `static.cloudflareinsights.com`, `/cdn-cgi/rum` | Cloudflare in front of the site, with real-user speed measurement | Likely |
| `lifefitgroup.widen.net` | Image and media library (Widen) | Likely |
| `lifefit-group-digital.com` | LifeFit's own digital platform, purpose unknown | Unsure |
| `services.crosssell.info` | Unknown | Unsure |
| `www.google.com` / maps | Club map | Likely |
| Ads and tracking | Facebook, TikTok, LinkedIn, Pinterest, Reddit, Snapchat, Spotify, Bing, Google Ads / DoubleClick, Adition, The Trade Desk (adsrvr), Awin (dwin1) | Sure they loaded |

Not seen: the payment provider and the booking system. Both are behind steps I did not open.

## Worth a closer look (not findings, just questions)

- **Consent:** many ad trackers loaded on the trial page, while the membership page showed "We need your consent to load the Adition service!". That could be normal (consent given earlier in this browser for some services) or a gap. I could not tell which, because I don't know what was accepted in this Chrome before. A clean test needs a fresh browser profile: decline all, then check which hosts still load.
- **A/B testing (VWO) and caching (Baqend):** both mean that not every visitor sees the same page. Tests and bug reports must record which version was shown. Caching can also show an expired offer (like the 27 October countdown) after it ended.
- **English text on a German site:** the consent placeholder is in English.

## Page speed

Homepage, mobile, PageSpeed Insights report from 2026-10-27, 9:00 PM. Link: https://pagespeed.web.dev/analysis/https-www-fitnessfirst-de/0djbx8pexr?form_factor=mobile

**Real users** (Chrome UX Report, last 28 days, this URL). Core Web Vitals assessment: **Failed**.

| Metric | Value | Limit for "good" | Result |
|---|---|---|---|
| LCP (main content visible) | 2 s | 2.5 s | Good |
| INP (reaction to a tap) | 208 ms | 200 ms | Just over, this is why it fails |
| CLS (page jumping) | 0.03 | 0.1 | Good |
| FCP (first content) | 0.6 s | | |
| TTFB (server answers) | 0.3 s | | |

**Lab test** (one Lighthouse 13.5.0 run, emulated Moto G Power, slow 4G, first visit). Scores: Performance 43, Accessibility 92, Best Practices 96, SEO 92.

| Metric | Value |
|---|---|
| FCP | 5.5 s |
| LCP | 28.8 s |
| Total Blocking Time | 530 ms |
| CLS | 0 |
| Speed Index | 10.6 s |

Suggestions shown: better cache lifetimes (about 2.6 MB to save), better image delivery (about 2.4 MB), render-blocking requests (about 180 ms).

**What this shows:** real users get a fast page (2 s), but a first visit on a slow phone in the lab takes almost 29 seconds for the main content. Why the gap is so big is not known. Possible reasons, not verified: real users are often returning visitors with cached files (Baqend, Cloudflare), the lab run is a cold first visit on a throttled network, and one lab run can vary a lot. This is exactly the "lab versus field" point for slide 14.

### Membership page (`/mitgliedschaft`), mobile

Report from 2026-10-27, 9:00 PM. Link: https://pagespeed.web.dev/analysis/https-www-fitnessfirst-de-mitgliedschaft/i69cmpiges?form_factor=mobile

**Real users** (this URL, last 28 days). Assessment: **Failed**.

| Metric | Value | Limit for "good" | Result |
|---|---|---|---|
| LCP | 1.1 s | 2.5 s | Good |
| INP | 227 ms | 200 ms | Too slow, the reason it fails |
| CLS | 0.04 | 0.1 | Good |
| FCP | 1 s | | |
| TTFB | 0.6 s | | |

**Lab test** (same setup as the homepage). Scores: Performance 36, Accessibility 93, Best Practices 96, SEO 85.

| Metric | Value |
|---|---|
| FCP | 4.4 s |
| LCP | 9.2 s |
| Total Blocking Time | 970 ms |
| CLS | 0 |
| Speed Index | 9.6 s |

**Pattern across both pages:** loading is fine for real users, but reacting to taps (INP) is too slow on both, and worse on the membership page, which is the main sales page. High Total Blocking Time in the lab (970 ms) points the same way: the phone is busy running scripts. A possible cause, not verified: the many tracking and ad scripts listed above.

### Trial training page (`/probetraining`), mobile

Report from 2026-10-27, 9:04 PM. Link: https://pagespeed.web.dev/analysis/https-www-fitnessfirst-de-probetraining/3xzcxxuaht?form_factor=mobile

**Real users** (this URL, last 28 days). Assessment: **Failed**.

| Metric | Value | Limit for "good" | Result |
|---|---|---|---|
| LCP | 1.3 s | 2.5 s | Good |
| INP | 361 ms | 200 ms | Clearly too slow (close to "poor" at 500 ms) |
| CLS | 0.05 | 0.1 | Good |
| FCP | 1.2 s | | |
| TTFB | 0.8 s | | |

**Lab test.** Scores: Performance 69, Accessibility 100, Best Practices 96, SEO 85.

| Metric | Value |
|---|---|
| FCP | 3.1 s |
| LCP | 4.8 s |
| Total Blocking Time | 130 ms |
| CLS | 0 |
| Speed Index | 6.9 s |

**Why lab and field disagree here:** the lab says this is the best of the three pages (score 69, little blocking). Real users say it reacts the worst (361 ms). The lab only measures the first page load and never taps anything. The slow reactions probably happen later, when people use the club search, map, calendar and time slots. Not verified, but it is a strong example of why a flow-based measurement (for example Playwright clicking through the booking steps) adds something a page-load test cannot see.

## Page speed summary

| Page | Real users: LCP | Real users: INP | Real users: CLS | Lab score |
|---|---|---|---|---|
| Homepage | 2 s | 208 ms | 0.03 | 43 |
| Membership | 1.1 s | 227 ms | 0.04 | 36 |
| Trial training | 1.3 s | 361 ms | 0.05 | 69 |

All three load fast for real users and all three fail on reaction time (INP). Single lab runs, numbers will vary on a re-run.

## Not seen
- Prices on the plan step, extras, the data form, the payment step
- The personal details step of the trial booking
- Club search page, course plan, member login, cancellation page

## Public pages read again (2026-10-28, read-only, text only, nothing clicked)

- `/mitgliedschaft`: offer banner "NUR BIS 31. OKTOBER" with a countdown. Club list with "CLUB AUSWÄHLEN" and BLACK or RED labels. Small print for DE (24 months, 12 free weeks, package 39 or 49 euro in selected clubs, start fee 39 euro waived, Flex option 99 euro, switch offer up to 12 months) and AT (12 months, package 39 euro, switch offer up to 6 months). Student discount valid up to and including age 25.
- `/probetraining`: club list with "CLUB AUSWÄHLEN", FAQ including a question about minors.
- `/mitgliedschaft/gesamtpreis`: total price page, asks for a club first.
- `/kuendigung` (pause, 4, 8 or 12 weeks, button "WEITER" and "TRAINING PAUSIEREN", link "VERTRAG HIER KÜNDIGEN") and `/kuendigung/antrag` (cancel form with member number, button "JETZT KÜNDIGEN"). No login needed to reach them. Footer links under SERVICE: "Mitgliedschaft hier pausieren", "Mitgliedschaft hier kündigen", "Widerruf", "Cookie-Einstellungen"; footer link "Barrierefreiheitserklärung".
