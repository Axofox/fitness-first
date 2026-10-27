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

Not measured. The PageSpeed Insights API refused with "429" (too many requests without an API key). Next try: pagespeed.web.dev by hand, mobile, for `/`, `/mitgliedschaft`, `/probetraining`.

## Not seen
- Prices on the plan step, extras, the data form, the payment step
- The personal details step of the trial booking
- Club search page, course plan, member login, cancellation page
