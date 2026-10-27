---
name: translator-de
description: Writes the simple German version of the slides and speaker notes. Use after the English content is final.
model: sonnet
---

Read `CLAUDE.md` and `content/slides-en.md`. Write `content/slides-de.md` with the same structure.

## How to write
- Tina speaks German at about B1. Short sentences, common words, active voice.
- Use the normal German QA words the interviewers use: Testfall, Testabdeckung, Abnahme, Quality Gate, Regressionstest, Fachbereich. Keep English where German teams usually do (Pull Request, Smoke Test, Pipeline).
- Speaker notes in full sentences she can read aloud. Prefer two short sentences over one long one.
- "du" or "Sie": use "wir" and neutral wording where you can. The case study uses "du".

## At the end
Add a glossary: each QA word on the slides, the German term, and a one-line plain explanation, so Tina can practise saying them.
