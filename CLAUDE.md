# Fitness First case study: rules for Claude

This repo holds Tina's preparation for the LifeFit Group (Fitness First) QA Engineer case interview.
Deadline to deliver the presentation: Thursday afternoon. Interview: Friday.

## Writing
- Plain, human language. Short sentences. Explain any QA word the first time it appears.
- Never use em dashes or en dashes as punctuation.
- No hollow phrases, no flattery, no marketing tone.
- German version: simple words, roughly B1 level, short sentences. Tina will speak it out loud.
- Speaker notes are full sentences.

## Facts
- Never invent results, numbers, tools or sources.
- Anything not verified goes in `notes/not-verified.md`, not on a slide.
- Assumptions about Fitness First's setup are written down and shown on the assumptions slide.

## The Fitness First website
- Read-only. Look at pages and network requests like a normal visitor.
- Never submit a form, never log in, never start a membership or booking.
- No automated test runs, no load tests, no security probing on www.fitnessfirst.de. It is their production site.

## Where things go
- `docs/` the case study (original PDF and English translation) and the plan
- `notes/` website analysis, risk ranking, fact checks
- `content/` slide text and speaker notes (English first, then German)
- `slides/` the finished HTML presentations and the PDF backups
- `.claude/agents/` the helpers, each with its own model
