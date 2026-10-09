# DealShare: Requirements Backlog (Elicitation Pass 1)

**DealShare** (working name) is a community-driven deal-sharing website, like *YouTube for deals*. Real shoppers post deals they've found at any store. Deals for the same product are grouped on one product page with the best price at the top. The community votes, flags, and keeps listings honest. The business earns affiliate commission on outbound purchases and shares part of it with trusted posters.

This repository is the output of a first requirements-elicitation pass. An LLM played the client, and the developer ran the interview.

## Contents

| Path | What it is |
|---|---|
| [`backlog/BACKLOG.md`](backlog/BACKLOG.md) | **Start here.** Readable backlog with a summary table, dependency graph, highest-risk items, and full details |
| [`backlog/requirements.yaml`](backlog/requirements.yaml) | Source of truth: every requirement with its metadata, dependencies, and acceptance criteria |
| [`docs/open-questions.md`](docs/open-questions.md) | Unresolved decisions (OQ-xx) and the requirements they block, plus scope exclusions |
| [`docs/elicitation-transcript.md`](docs/elicitation-transcript.md) | Full simulated client interview. Requirements cite its turns (T1–T6) |
| [`docs/process.md`](docs/process.md) | How the backlog was produced: LLM role, prompts, conventions, next steps |
| [`tools/build_backlog.py`](tools/build_backlog.py) | Validates the YAML (unique IDs, valid references, no cycles) and regenerates `BACKLOG.md` |

## Backlog at a glance

- **53 requirements:** 43 functional, 10 nonfunctional.
- **MoSCoW:** 27 must, 21 should, 5 could.
- **Status:** 7 blocked on open questions, 1 deferred (price history).
- **Highest-risk area:** automatic product identification and matching (FR-011, FR-021, FR-061), followed by variants (FR-030/031) and the poster revenue share (FR-063, FR-066).

### Metadata on each requirement

`id` · `type` (functional / nonfunctional) · `category` · `epic` · `level` (high / low + `parent`) · `priority` (MoSCoW) · `status` · `risk` · `source` (transcript turn, or `inferred`) · `depends_on` · `blocked_by` (open questions) · user `story` · measurable `acceptance` criteria

### Epics

Accounts & Profiles · Deal Posting · Product Catalog & Matching · Variants & Condition · Discovery · Community Quality & Moderation · Affiliate & Monetization · Trust & Disclosure · Price History · Nonfunctional

## Regenerating the backlog

```bash
pip install pyyaml
python3 tools/build_backlog.py
```

## Tools used

Elicitation simulation and backlog drafting: Claude (Anthropic). The developer reviewed and edited the output. See [`docs/process.md`](docs/process.md).
