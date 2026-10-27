# The plan (version 2, with Tina's answers)

## Decisions

| Question | Answer |
|---|---|
| Language | Interview in German. Two presentations: English, then German with very simple words. |
| Setting | Online. Screen share is fine. Fitness First knows Tina's German level. |
| Flows | Membership signup and trial training booking |
| Non-functional areas | Accessibility, data protection and cookie consent, page speed |
| Speaker notes | Full sentences |
| Look | Tina's own calm style, teal like her CV. Not the Fitness First design. |
| Deadline | Deliver Thursday afternoon, interview Friday |

### What Tina wants to show about herself
- Her own way of thinking, independent of the team: exploratory testing, what she documents and how.
- How she brings QA into the team: **the team owns quality**. QA is the gate keeper at release, and at the same time a resource the team can use: helping, advising, maintaining the test cases.

## Format
HTML presentation, mostly static, with 3 animations: risk ranking, release path, AI loop. Points can appear one at a time on click. PDF backup of each version.

## The story, slide by slide (about 30 minutes)

| # | Slide | What it says | Min |
|---|---|---|---|
| 1 | Title | "Find the expensive mistakes first, and find them early." | 0.5 |
| 2 | My assumptions | What I don't know about your setup, and what I assumed instead | 1.5 |
| 3 | How I work | The 6 phases from the portfolio, in one picture | 1.5 |
| 4 | Where the money is | Main parts of the website ranked by "how bad if it breaks" (animated) | 2 |
| 5 | Flow 1: Membership signup, the risks | Why it matters most. Wrong price, lost signups, legal problems | 2.5 |
| 6 | Flow 1: what I'd automate | Test layers as a pyramid with real example tests per layer | 3 |
| 7 | Flow 2: Trial training booking | Lost leads, booking not reaching the club | 1.5 |
| 8 | Devices, users, outside systems | Phones first, browsers, payment, maps, cookie banner, booking system | 1.5 |
| 9 | How I test on my own | Exploratory testing in short sessions with a goal. What I write down: goal, what I covered, bugs, open questions, what I did NOT test | 2 |
| 10 | Manual or automated? | A simple rule for deciding, with 3 examples | 1.5 |
| 11 | Quality is the team's job | Who does what: Dev, Product, business departments, QA. QA as gate keeper and as a resource (helping, coaching, keeping the test cases alive) | 2 |
| 12 | From idea to live website | The release path on Acquia with the checks at each step (animated) | 2.5 |
| 13 | When do we stop a release? | What blocks, what can go out with conditions, unreliable tests, quick go/no-go | 2 |
| 14 | Beyond "does it work" | Accessibility, data protection and consent, page speed, each with a clear limit | 3 |
| 15 | Where AI helps, and where it doesn't | 3 uses of AI, what stays with people, data safety (animated) | 2.5 |
| 16 | One normal week | Everything as one routine, so it's doable in real life | 1 |
| 17 | Thank you / questions | Plus backup slides | 0.5 |

Total: about 31 minutes. Slides 7, 8 and 16 are the first to shorten if the practice run is too long.

## Sources of content

| Source | Used on slides |
|---|---|
| Portfolio qama.netlify.app (6 phases) | 3, 9, 11 |
| qa-agents repo (rules, evidence, P1 gate, human decides) | 13, 15 |
| enmacc agents (acceptance criteria gap finding) | 15 |
| Fitness First website analysis (`notes/`) | 4 to 8, 14 |

Be careful: the qa-agents repo has never run on a live site. Say "this is how I designed it", not "this is what it found".

## Fitness First details from the homepage
- Membership shop in 5 steps: club, contract length, extras, your details, payment.
- Many price rules: 24 months with 12 weeks free, training package €39 or €49 depending on the club, start fee sometimes waived, €99 early exit option, switch offer, student discount up to age 25. Austria has its own rules on the same website.
- A campaign countdown ending 27 October. Offers that switch on and off by date are a classic source of bugs.
- Footer: pause, cancel, withdrawal, cookie settings. These are legal flows, not just pages.
