# Fitness First case interview

Preparation for the LifeFit Group (Fitness First) QA Engineer case study.
Private repo.

- **Deliver the presentation:** Thursday afternoon
- **Interview:** Friday (30 min presentation, 30 min questions)
- **Language:** German in the interview. We build an English version first, then a simple German one.

## Folders

| Folder | What is in it |
|---|---|
| `docs/` | The case study (original PDF, English translation) and the plan |
| `notes/` | Website analysis, risk ranking, fact checks |
| `content/` | Slide text and speaker notes |
| `slides/` | Finished HTML presentations and PDF backups |
| `.claude/agents/` | The helpers, each fixed to one model |

## The helpers

| Helper | Model | Job |
|---|---|---|
| `site-analyst` | Sonnet | Reads fitnessfirst.de read-only, lists flows and outside services |
| `risk-strategist` | Opus | Turns notes into risks and priorities, writes slide text and speaker notes |
| `fact-checker` | Sonnet | Checks everything in `notes/not-verified.md` with searches |
| `slide-builder` | Sonnet | Builds the HTML presentation from `content/` |
| `translator-de` | Sonnet | Writes the simple German version |

Not checked yet: whether a helper can use the Chrome browser. If it can't, the main conversation reads the website and the helpers do the rest.

## Timeline

| When | What | Model |
|---|---|---|
| Tuesday evening | Repo set up, website analysis, page speed numbers | Sonnet + Opus |
| Wednesday morning | Slide text and speaker notes (English) | Opus |
| Wednesday afternoon | Build the English HTML presentation | Sonnet |
| Thursday morning | German version, PDF backups | Sonnet |
| Thursday afternoon | Deliver | |
| Friday before the interview | Practice run | |
