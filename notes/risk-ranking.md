# Risk ranking

Risk = how bad if it breaks (impact) x how likely it is to break (likelihood).
Impact: money, legal, number of users, main path. Likelihood: complex rules, outside systems, how often it changes.

| # | Part of the site | Impact | Likelihood | Why |
|---|---|---|---|---|
| 1 | Membership checkout | Very high | High | Sells contracts. Prices depend on club, plan, campaign, age and country. Payment and contract systems behind it. |
| 2 | Cookie consent and tracking | High | High | Legal (data protection) and marketing data. About 15 ad and tracking services load. Changes with every campaign. |
| 3 | Pause, cancel, withdrawal | High | Medium | Legal flows. If they fail, the company has a legal problem, not just an unhappy user. |
| 4 | Trial training booking | High | Medium | Main way to win new members. Slots must match the club. Slowest reaction time of the three pages measured. |
| 5 | Campaigns and offers | High | High | Countdowns, free weeks, fine print. Switch on and off by date. Caching can show an expired offer. |
| 6 | Club search | Medium | Medium | Entry to both main flows. Depends on location and maps. |
| 7 | Member login | Medium | Unknown | Personal data. Not looked at (no login). |
| 8 | Course plan | Medium | Low | Members use it often, but a mistake is annoying, not costly. |
| 9 | Magazine, career, press | Low | Low | Content pages. Errors are visible but cheap. |

## Chosen flows
1. **Membership checkout**: highest risk, central conversion.
2. **Trial training booking**: second conversion path, different risks (lost leads, slots, reaction time).

## Evidence
All from `notes/site-analysis.md` (read-only visit and PageSpeed Insights, 2026-10-27). Likelihood for the member login is unknown because it was not opened.
