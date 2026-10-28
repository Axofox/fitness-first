# Not verified yet

Nothing on this list goes on a slide until it is checked. When something is checked, move it to "Verified" with its source.

## Open
- [ ] Whether the German accessibility law (BFSG) applies to the Fitness First website, and since when.
- [ ] Whether the online cancellation button rule (Kündigungsbutton) applies, and since when.
- [ ] Which payment provider the membership shop uses. (Payment step not opened.)
- [ ] Which booking system or CRM receives trial training bookings. (No separate booking host seen.)
- [ ] How Acquia names its environments (assumption: Dev, Stage, Prod).
- [ ] Content of the click-to-open panels on qama.netlify.app.

- [ ] Tina said a new accessibility law starts in January. Not found: the BFSG has applied since 28 June 2025 and the one source read (e-recht24.de) names no January deadline. Ask Tina where the January date comes from. Also not checked: whether the BFSG applies to Fitness First specifically.
- [ ] Whether the site is responsive and ready for mobile: Tina's own observation, not measured by Claude.

## Verified
- Core Web Vitals "good" limits, judged on 75% of page visits, same for phone and desktop: LCP up to 2.5 s, INP up to 200 ms, CLS up to 0.1. "Poor": LCP over 4 s, INP over 500 ms, CLS over 0.25. Source: https://web.dev/articles/defining-core-web-vitals-thresholds (checked 2026-10-27)
- The website runs on Drupal 10 (page metadata, checked 2026-10-27). Hosting on Acquia was stated by Fitness First in the case study.
- Cookie consent tool is Usercentrics (hosts `*.usercentrics.eu` loaded on /probetraining, checked 2026-10-27 in Chrome).
- Other services loaded: VWO (A/B testing), Google Tag Manager, many ad trackers. Likely: Baqend Speed Kit, Cloudflare. Details in `notes/site-analysis.md`.
- Page speed for homepage, membership and trial pages measured with PageSpeed Insights, mobile, 2026-10-27 (see site-analysis.md).
- BFSG (German accessibility law for online services, B2C, including online shops and booking sites) in force since 28 June 2025, no grace period; micro-enterprises with services only are exempt. Source: https://www.e-recht24.de/ecommerce/13236-barrierefreiheitsstaerkungsgesetz.html (secondary source, not the law text, checked 2026-10-27).
- Automatic accessibility scores (Lighthouse, mobile, 2026-10-27): homepage 92, membership 93, trial training 100. Automatic tools find only part of the problems.

## Added 2026-10-28
- The offer end date: the page says 31 October now. My first notes said 27 October. Not clarified (a different banner, or a changed date).
- Student discount: the text says "2 euro off your weekly fee", the small print says "up to 13 euro per month" (DE) and "up to 8.50 euro" (AT). Not checked if they agree.
- The pause page claims "86% of our members choose a pause". Source unknown.
- Which clubs have the 39 euro and which the 49 euro training package: not known. The small print only lists the "selected clubs".
- Button names after the club choice in the checkout, and in the trial booking (calendar, confirm button): not seen.
- Usercentrics banner button names on a first visit: not seen (my browser had a saved choice).
