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
| `slides/` | Finished HTML presentations and PDF copies |
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

## Build the presentation

The slides are generated from the markdown text, so the wording is never retyped. Do not edit the HTML by hand.

```
python3 tools/build_slides.py content/slides-en.md slides/presentation-en.html --lang en
```

Keys in the presentation: arrows or click = next and back, F = full screen, P = presenter window (notes and timer), N = notes panel, B = points appear one by one, R = replay animation, H = help.
For Teams: share only the slides window, never the whole screen, and keep the notes in the presenter window (P).

## Timeline

| When | What | Model |
|---|---|---|
| Tuesday evening | Repo set up, website analysis, page speed numbers | Sonnet + Opus |
| Wednesday morning | Slide text and speaker notes (English) | Opus |
| Wednesday afternoon | Build the English HTML presentation | Sonnet |
| Thursday morning | German version, PDF copies | Sonnet |
| Thursday afternoon | Deliver | |
| Friday before the interview | Practice run | |
