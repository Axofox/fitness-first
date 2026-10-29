# Slides (English)

Format per slide: **Slide** = what is on screen. **Animation** = only where the plan says so. **Notes** = what Tina says.
Target: about 30 minutes. Shorten slides 7, 8 and 15 first if the practice run is too long.

---

---

## 1. Title (0.5 min)

**Slide**
- Quality for fitnessfirst.de
- Find the expensive mistakes first, and find them early.

**Notes**
Thank you for the invitation. My presentation has one idea. I want to find the mistakes that cost the most money and trust first. And I want to find them as early as possible, when they are still cheap to fix. Everything I show today comes back to this idea.

---

## 2. My starting point (1.5 min)

**Slide**
How I prepared:
- Explored the website as a visitor to understand the flows
- Checked if it feels slow as a user, or unusually slow (PageSpeed Insights, mobile)
- Looked at whether the site is responsive and ready for mobile
- Looked at accessibility: only a quick automatic scan (Google's tool), no manual check
- Nothing submitted, no login, no tests on your live site

What I assumed:
- You have test environments next to production
- Payments are tested only in the provider's test mode, never on the live site (real money)
- Most users use a phone, not a laptop

**Notes**
Before I start, I want to be open about what I did and what I assumed. First I explored your website like a normal visitor, to understand the flows. I did not submit any form and I did not log in, because it is your live system. Then I asked myself: does the site feel slow for a user, or is it unusually slow? I measured it with Google's PageSpeed tool on mobile. I also looked at whether the site is responsive and ready for mobile. And I looked at accessibility, because the rules for accessible online services are getting more important. Here I only ran a quick automatic scan with Google's tool. That is not a check by hand. I also made three assumptions. First, you have test environments next to production. Second, payments go through an outside provider. I test them only in its test mode, never on the live system, because there it is real money. Third, most of your users use a phone and not a laptop. If an assumption is wrong, please tell me. I am happy to adapt.

---

## 3. How I explore (2 min)

**Slide**
Exploratory testing: short sessions with a clear goal.

Example goal: "Explore the checkout by changing my mind often, to find wrong totals."

What I write down every time:
- Goal and setup (device, browser, which version of the page in an A/B test)
- What I covered
- Bugs, with steps and screenshots
- Open questions
- What I did NOT test

Saved next to the ticket, so the team can see it.

**Notes**
I always start with exploratory testing. That means I don't follow a script. I explore with a clear goal and a time limit, usually 60 to 90 minutes. For your website my goals were simple. First, understand the flows. Second, see if the site feels slow for a user. Third, see if it works well on a phone. A goal for the checkout could be: explore it by changing my mind often, to find wrong totals. I go back, I change the club, I change the plan, I reload the page. While I test, I take notes. I always write down the goal, the device and browser, and which version of the page I saw, because with A/B tests not everyone sees the same page. Then what I covered, the bugs with exact steps and screenshots, my open questions, and also what I did not test. That last part is important. It shows the team where the gaps are, instead of hiding them. The notes are saved next to the ticket, so anyone can read them later.

---

## 4. What I learned: the areas that matter most (2 min)

**Slide**
Risk = how bad if it breaks x how likely it breaks

1. Membership checkout
2. Cookie consent and tracking
3. Pause, cancel, withdrawal
4. Trial training booking
5. Campaigns and offers
6. Club search
7. Member login
8. Course plan
9. Magazine, career

**Animation**
[rank] The 9 parts appear one by one in random order, then slide into the ranked order. The top 4 turn teal.

**Notes**
After exploring, I knew which areas matter most. I ranked them with one question: how bad is it if this breaks, and how likely is it to break? I looked at money, legal problems and how many users are affected. And at complex rules, outside systems and frequent changes. The membership checkout is clearly number one. It sells contracts, and the prices depend on many rules. Cookie consent is number two, because it is a legal topic and about fifteen tracking services load on your pages. Pause and cancel are legal flows too. The trial booking brings new members. The magazine is at the bottom. A mistake there is visible, but cheap. This ranking decides where I spend my time. I will look closely at the two flows that bring in members: the checkout and the trial booking.

---

## 5. My plan for each risk (2.5 min)

**Slide**
| Area | Main risk | My plan |
|---|---|---|
| Membership checkout | Wrong price, or a contract that never arrives | Price rule tests, end-to-end tests on staging, automatic run on every push and every night |
| Cookie consent and tracking | Marketing trackers load after "decline" | Automatic check after "decline all", review with the data protection officer |
| Pause, cancel, withdrawal | A legal flow stops working | End-to-end test on every release, texts checked by hand |
| Trial training booking | Slot does not exist, booking never reaches the club | One end-to-end booking per phone type, check that it arrives |
| Campaigns and offers | An old offer still shows after it ended | Date tests, look at what the cache shows |

The other areas: lighter checks, mostly by hand.

**Notes**
For each area I make a plan for its main risk. I plan by risk, not by page. For the membership checkout the main risk is a wrong price or a contract that never arrives. So I test the price rules with many small tests, and I add end-to-end tests that click through the whole flow. These tests run automatically on every push, and again every night. For cookie consent the risk is that marketing trackers still load after a visitor says no. So an automatic check clicks decline and looks at which services load. Cancel and pause are legal flows. They get an end-to-end test on every release, and I read the texts by hand. For the trial booking the risks are a slot that does not exist and a booking that never reaches the club. So I test one booking per phone type and check that it arrives. For offers, the risk is an old offer that still shows after it ended. So I test the dates, and I look at what the cache shows. The other areas get lighter checks, mostly by hand. I build the end-to-end tests in this order. Priority one is the membership checkout, the trial booking, pause and cancel, and the cookie consent check. Priority two is campaigns and offers, club search and the member login.

---

## 6. Flow 1: Membership checkout, the risks (2.5 min)

**Slide**
5 steps: Club > Plan > Extras > Your details > Payment

What can go wrong:
- Wrong price: club, plan, campaign, age, country
- Summary does not match the choice
- Customer gets stuck and leaves
- Contract or payment does not reach your systems
- Legal text missing or wrong

Most expensive: a wrong price or a contract that was never created.

**Notes**
Why is this flow so important? It is the place where you earn money. And the rules are complex. A 24-month contract with 12 free weeks. A training package that costs 39 or 49 euro, depending on the club. A start fee that is sometimes waived. A student discount up to age 25. And Austria has its own rules on the same website. Every rule is a place where a price can be wrong. The worst mistakes are a wrong price, because that is a legal and trust problem, and a contract that the customer signed but that never reached your system. Then you lose the customer and you don't even know it. Another risk: the checkout uses the club in the web address. If someone changes the club in the middle, the summary must update correctly.

---

## 7. Flow 2: Trial training booking, the risks (1.5 min)

**Slide**
3 steps: Club > Date and time > Your details

What can go wrong:
- Booked slot does not exist at the club
- Booking never reaches the club
- Date mistakes: today, weekend, month change, holidays
- Slow to react when someone taps (real users, mobile)

Automate: slot rules, booking arrives at the club, one end-to-end booking per phone type.

**Notes**
The second flow is the trial training. The risks are different. Here nobody pays, but you lose a future member if it fails. The biggest risk is a booking that never reaches the club. The person comes to the gym and nobody expects them. That is a bad first impression. Dates are also risky: today, the weekend, the change of month, holidays. And one surprise from the page speed test: here the page reacts slowly when real users tap something, slower than Google's limit for good. I'll come back to this.

---

## 8. Devices, users, outside systems (1.5 min)

**Slide**
Devices: desktop browser first, then the mobile browser view. Real phones: iPhone Safari, Android Chrome.
Screen widths: 360, 390, 768, 1280 pixels.

Users: new visitors, students, people switching gyms, visitors from Austria, keyboard and screen reader users, slow mobile internet, people who decline cookies.

Outside systems I saw:
- Usercentrics (cookie consent)
- VWO (A/B tests: not everyone sees the same page)
- Google Tag Manager and about 15 ad services
- Probably Baqend and Cloudflare (speed and caching)
- Unknown to me: payment, booking, member system

**Notes**
Which devices? I assume most of your visitors use a phone. I check that in your analytics. I build the end-to-end tests in a desktop browser first, because that is the fastest place to build and fix them. Then I run the same tests in the mobile browser view, on a phone-sized screen. Before big releases I also check on real phones. I also think in user groups, not only devices. A student sees a different price. Someone from Austria sees different rules. Someone who declines cookies must still be able to buy. And people who use a keyboard or a screen reader must get through the checkout too. I also looked at which outside services your pages load. Two are important for testing. First, VWO, an A/B testing tool. It means different visitors can see different versions of a page. So every bug report must say which version was shown. Second, caching services. They make the site fast, but they can also show an old offer after it has ended.

---

## 9. Checkout tests: what each one expects (3 min)

**Slide**
Test pyramid: many small fast tests at the bottom, few slow ones at the top.

- **Exploratory (manual):** new offers, odd combinations (student, other club), Austria. Expected: no wrong price or text.
- **End-to-end (few):** pick club and plan, reach payment, on iPhone and Android. Change club mid-way. Expected: every step opens, price updates.
- **Visual and accessibility:** Expected: looks right, keyboard reaches every step, errors are read out.
- **API and integration:** plans, prices, contract, payment test mode. Expected: right data, contract arrives.
- **Unit (many):** every price rule and campaign date. Expected: same input, same exact price.

**Animation**
[pyramid]

**Notes**
Here is what I would automate for the membership checkout, and what each test expects. Think of a pyramid. At the bottom are many small and fast tests. These are unit tests, meaning tests of one small piece of code. Every price rule gets its own test, and so does the campaign end date, because offers that switch on and off by date are a classic source of bugs. Expected: the same input always gives the exact price. In the middle are API and integration tests. They check that the systems talk to each other correctly. For this club, do we get the right plans and prices? Does the contract arrive in the member system? For outside systems like payment, I use their test mode. Expected: the right data comes back and the contract arrives. Then come the visual and accessibility checks. Expected: it looks right, the keyboard reaches every step, and errors are read out. At the top are only a few end-to-end tests. End-to-end means a script clicks through the real flow like a customer. I would do the main path on an iPhone and an Android phone, and the case where someone changes the club. Expected: every step opens, and the summary and price update. Above that is manual exploratory testing, for things that are new or need human judgement. These tests run on staging, never on the live site.

---

## 10. What I automate, and what I don't (1.5 min)

**Slide**
Automate when:
- it runs often, matters a lot, and the expected result is clear
- it is stable and cheap to maintain
- Example: price rules (unit tests)

Keep manual when:
- it is new or still changing
- it needs human judgement: look, wording, screen reader
- Examples: a new campaign page, the screen reader on checkout

What I would not test:
- Outside services themselves: payment provider, cookie tool, ad services. I test only our side.
- Load and security attacks on the live site
- Low-risk areas in depth, like the magazine: a quick look is enough

**Notes**
How do I decide what to automate? I ask three questions. Will this test run often? Is it important? And do we know exactly what the right result is? If yes, I automate it. If a feature is new and still changing, I test it by hand first. Otherwise we spend more time fixing tests than finding bugs. A flaky test, meaning a test that sometimes passes and sometimes fails for no real reason, costs more than the manual check it replaced. Some things always need a human. How does a page look? Is the wording clear? Does a screen reader make sense? Those stay manual. I also say clearly what I would not test. First, the outside services themselves. We cannot test the payment provider or the cookie tool. Their own teams do that. I test our side: that our site sends the right data, that it shows a clear message when the service fails, and that nothing breaks when the service is slow or down. For payments I assume a test mode on a test environment, never the live system. Second, I do not run load or security attacks on the live site. It is production, so that needs a test environment and an agreement first. Third, low-risk areas like the magazine get only a quick look. A mistake there is visible, but cheap. Saying what I skip is part of the plan, because then everybody knows where the gaps are.

---

## 11. The quality process I would encourage (2.5 min)

**Slide**
Six phases, one question: what could go wrong, and how do we prevent it?
Bugs cost less when we find them early.
1. Requirements: understand the why
2. Risk: decide together what matters most
3. Development: explore and pair early
4. Automation: automate the right things
5. Release: done is a criterion, not a feeling
6. After release: learn from what got through

**Animation**
[cycle] The six phases sit on a circle. A dot travels around it and each phase lights up in turn.

**Notes**
Now the quality process I would encourage, to make bugs cheaper. The idea is simple. The earlier we find a bug, the cheaper it is. A bug found in a conversation costs minutes. A bug found in production costs money and trust. So I ask the same question in every phase: what could go wrong, and how do we prevent it, not only catch it? In requirements I ask why we build something and for whom. In the risk phase we decide as a team what matters most. During development I test early and pair with developers. Then I automate what is worth it. At release, done has clear criteria. And after the release I look at what we missed, because that is the most honest feedback we get. Then the circle starts again.

---

## 12. Quality is the team's job (2 min)

**Slide**
- **Product:** clear goals and acceptance criteria. Decides on risk together with the team.
- **Developers:** unit and API tests for their code. Fix what breaks the pipeline.
- **Business departments:** check that it is right for the business (acceptance).
- **QA:** gate keeper at release, and a resource for everyone:
  - helps write acceptance criteria
  - pairs with developers
  - keeps the test cases alive
  - coaches the team on testing

**Notes**
I believe quality is the job of the whole team, not only of QA. If QA is the only one responsible, quality becomes a check at the end. And then bugs are found late, when they are expensive. So everyone has a part. Product owners write clear goals and acceptance criteria. Acceptance criteria are the conditions that say when a feature is done. Developers write unit and API tests for their own code. The business departments check that the result is right for the business. And my role has two sides. On one side I am the gate keeper. At release I say clearly what is tested, what is not, and what the risk is. On the other side I am a resource. The team can come to me. I help write acceptance criteria, I pair with developers, I maintain the test cases so they stay useful, and I help the team get better at testing. We often do this in a short meeting called Three Amigos: product, development and QA look at a story together before anyone starts building.

---

## 13. From idea to live website (2 min)

**Slide**
Feature > Push and merge request > Dev > Stage > Release

- **Feature:** acceptance criteria and risks agreed
- **Push and merge request:** unit and API tests run on every push. They must pass before the code reaches master.
- **Dev:** integration tests. Smoke test after each deployment.
- **Stage:** smoke test after each deployment, then end-to-end regression, visual, accessibility, page speed, consent check, acceptance by business. Plus a full run every night.
- **Release:** all green, then live, with a smoke test after the deployment. Rollback ready.

Test data: no real customer data on Stage. Copied data is anonymised.

**Animation**
[pipe] A feature card moves from left to right. At each checkpoint a light turns green. In a second run, the light at Stage turns red and the card stops.

**Notes**
Here is the release path from a feature to the live website. On Acquia I assume three environments: development, staging and production. The tests run before anything gets there. Every time a developer pushes code, the fast tests run automatically: unit tests, API tests and code checks. They must pass before the change is allowed into master. A merge request means a request to add their change to the main code, and there we also have a code review. On development we run the integration tests. After each deployment we also run a smoke test. A smoke test is a short check that the most important things still work, like switching on a machine and seeing if smoke comes out. On staging we run a smoke test after each deployment, then the end-to-end tests and the full regression. Regression tests check that old features still work after a change. We also check the look, accessibility, page speed and consent there. The business departments do their acceptance on staging too. On top of that I would set up a nightly run. A scheduler starts the whole test suite every night. So we find problems that slip in during the day, and in the morning we see what broke. When everything is green, we release, and a smoke test runs after that deployment too. If something goes wrong, we roll back to the last good version. One important point about test data: Drupal sites often copy the production database to staging. That copy must not contain real customer data. It has to be anonymised.

---

## 14. When do we stop a release? (2 min)

**Slide**
**Stops the release:**
- Wrong price, checkout or booking broken
- Cancel or pause broken
- Cookie decline does not work
- Security problem, or someone sees another person's data
- Main flow not usable with a keyboard

**Can go, with conditions:**
- Small bug with an easy workaround, ticket and fix date
- Problem on a low-traffic page
- New feature switched off with a feature flag

**Unreliable tests:** run once more. If it passes, it goes to quarantine with an owner and a deadline. Never just ignored.


**Notes**
When do we stop a release? Some things always stop it: a wrong price, a broken checkout or booking, a broken cancel button, a cookie banner where "decline" does not work, any security problem, or a main flow that a keyboard user cannot finish. Other bugs can go live if we agree on conditions. For example a small bug with an easy workaround, if there is a ticket and a fix date. What about unreliable tests? I run a failed test once more. If it passes the second time, it is probably flaky. Then it goes into quarantine. That means it does not block the pipeline anymore, but it has an owner and a deadline to fix it. It is never just ignored. I give a clear recommendation when a release is urgent, for example if we should go live or wait. But the decision is made by the team, with open eyes.

---

## 15. Three more areas: accessibility, privacy, speed (2.5 min)

**Slide**
| Area | Automated | Manual | Limit (gate) |
|---|---|---|---|
| Accessibility | Accessibility scan on every merge request | Keyboard and screen reader on main flows every release, expert audit once a year | No critical issues on checkout and booking |
| Data protection and consent | After "decline all", only allowed services load | Check banner texts with the data protection officer | Any marketing tracker after decline stops the release |
| Page speed | Lighthouse in the pipeline, timing of booking steps | Look at real-user data every week | Real users: content in 2.5 s, reaction to a tap in 200 ms. Pipeline: no page slower than today |


**Notes**
Besides "does it work", I chose three areas. First, accessibility. You publish an accessibility statement, so it matters to you. An automatic scan finds only part of the problems. The rest needs a human: can I finish the checkout with only a keyboard? Does a screen reader read the error messages? My gate is simple: no critical problem on the checkout and the booking. Second, data protection and cookie consent. With about fifteen ad services on the page, this is a real risk. I would automate one simple check: a script clicks "decline all", and then we look at which services still load. If a marketing tracker loads after decline, the release stops. The legal rules themselves I would clarify with your data protection officer. Third, page speed. Google gives clear limits for real users. I measured your pages. They load fast for real users. But all three react too slowly when someone taps. The trial page is the slowest. A test that only loads the page misses this, because it never clicks the calendar. So I would also measure the booking steps themselves. In the pipeline, my first rule would be: no page gets slower than today. Later we can make the limits stricter.

---

## 16. How can AI help us, and where? (2.5 min)

**Slide**
AI helps with:
1. **Requirements:** finds gaps and missing edge cases in acceptance criteria
2. **Exploratory testing:** agents explore with a goal and must show evidence for every result
3. **Failed tests:** groups failures, suggests "real bug" or "flaky"

Always with people:
- Final priority of bugs
- Release or stop
- Legal, accessibility and data protection decisions

Rules: no real customer data in AI tools. Every result needs evidence. AI must list what it did not test.

**Animation**
[loop] A loop: AI suggests > a person checks > the team decides. The person in the middle stays visible the whole time.

**Notes**
How can AI help us? I use it in three places. First, requirements. In my last job I built AI agents that read acceptance criteria and look for gaps and missing edge cases. A person then decides which gaps are real. Second, exploratory testing. I designed a set of AI testing agents that explore a website with a clear goal. I have to be honest here: this system is designed and tested on sample data, but I have not run it on a live website yet. The important part is the rules. Every result needs evidence, like screenshots. The agent must write down what it did not test. And text on a web page is treated as data, never as an instruction, so a page cannot trick the agent. Third, failed tests. AI can group failures and suggest whether it's a real bug or a flaky test. But some things always stay with people: the final priority of a bug, the go or no-go decision, and anything legal. And no real customer data goes into AI tools. AI makes suggestions. The team decides. So we come back to my one idea: find the expensive mistakes first, and find them early. Thank you.

---

# Extra slides

## B1. Page speed details

| Page (mobile) | Real users: LCP | Real users: INP | Real users: CLS |
|---|---|---|---|
| Homepage | 2 s | 208 ms | 0.03 |
| Membership | 1.1 s | 227 ms | 0.04 |
| Trial training | 1.3 s | 361 ms | 0.05 |

Limits for good (75% of visits): LCP 2.5 s, INP 200 ms, CLS 0.1. Source: PageSpeed Insights, 27 October 2026.

**Notes**
LCP means: how long until the main content is visible. INP means: how fast the page reacts to a tap. CLS means: how much the page jumps while loading.

## B2. Test data and environments

- Stage: anonymised copy of production, or generated test data
- Fixed test accounts and test clubs, reset regularly
- Payment provider in test mode, never real payments
- Outside systems we cannot control: simulated (mocked) in API tests, real only in a few end-to-end tests on Stage
- Test emails only on reserved test domains

**Notes**
For test data I follow a simple rule: no real customer data outside production. When a system is hard to control, like a payment provider, I simulate it in most tests. That is called mocking. Only a few end-to-end tests use the real test mode of the provider.

## B3. My AI testing agents

- 4 agents: explorer, component, flow, API
- Rules: only allowed test sites, no real purchases, secrets hidden, evidence for every result
- Results: pass, fail with priority, or "suspicious" with a reason
- Several runs are merged, because AI results vary from run to run
- A top-priority failure (P1), like a broken checkout, can stop the pipeline. Humans decide on the rest.

**Notes**
This is the system I mentioned. I want to be clear: it is built and tested on sample data, but not yet on a real website. What I'm proud of is the rule set, because it answers the questions you asked about control: evidence, honesty about gaps, and people making the final decisions.

## B4. My first weeks

- Weeks 1 to 2: learn the product, the team and the release process. Read the bug history.
- Weeks 3 to 4: risk map with the team, first quick wins (consent check, smoke tests)
- Month 2 to 3: regression suite for checkout and booking, quality gates in the pipeline

**Notes**
If I join, I would not change everything on day one. First I learn how you work and where bugs came from in the past. Then we agree on a risk map together. The first quick wins would be the consent check and smoke tests, because they are small and protect a lot.

## B5. One normal week

**Slide**
- **Planning:** Three Amigos on new stories, risks agreed
- **Every day:** pairing, merge request checks, quick questions
- **During the sprint:** exploratory sessions on new features
- **Before release:** regression on Stage, acceptance with business
- **Release day:** check that all gates are green, then release
- **After release:** look at what got through, add a test for it

**Notes**
To show that this works in real life, here is a normal week. At planning we look at new stories together and agree on the risks. Every day I pair with developers and look at merge requests. During the sprint I run exploratory sessions on the new features. Before the release we run the regression on staging and the business does acceptance. On release day, we check that all gates are green, and then we release. And after the release I look at what got through. For every bug that reached production, we add a test, so it cannot come back.
