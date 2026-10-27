# Not verified yet

Nothing on this list goes on a slide until it is checked. When something is checked, move it to "Verified" with its source.

## Open
- [ ] Whether the German accessibility law (BFSG) applies to the Fitness First website, and since when.
- [ ] Whether the online cancellation button rule (Kündigungsbutton) applies, and since when.
- [ ] Which payment provider the membership shop uses. (Payment step not opened.)
- [ ] Which booking system or CRM receives trial training bookings. (No separate booking host seen.)
- [ ] How Acquia names its environments (assumption: Dev, Stage, Prod).
- [ ] Content of the click-to-open panels on qama.netlify.app.

## Verified
- Core Web Vitals "good" limits, judged on 75% of page visits, same for phone and desktop: LCP up to 2.5 s, INP up to 200 ms, CLS up to 0.1. "Poor": LCP over 4 s, INP over 500 ms, CLS over 0.25. Source: https://web.dev/articles/defining-core-web-vitals-thresholds (checked 2026-10-27)
- The website runs on Drupal 10 (page metadata, checked 2026-10-27). Hosting on Acquia was stated by Fitness First in the case study.
- Cookie consent tool is Usercentrics (hosts `*.usercentrics.eu` loaded on /probetraining, checked 2026-10-27 in Chrome).
- Other services loaded: VWO (A/B testing), Google Tag Manager, many ad trackers. Likely: Baqend Speed Kit, Cloudflare. Details in `notes/site-analysis.md`.
- Page speed for homepage, membership and trial pages measured with PageSpeed Insights, mobile, 2026-10-27 (see site-analysis.md).
