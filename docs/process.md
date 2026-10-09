# Process: How This Backlog Was Produced

## 1. Simulated elicitation (LLM as client)

There was no real client, so a large language model (Anthropic's Claude) played one: "Dana," a non-technical founder with funding and a loosely defined vision. The model was told to behave like a realistic client: give vague answers at first, state *wants* rather than *needs*, and not volunteer information the developer didn't ask for. The developer ran the session as an **unstructured interview**, mostly with open-ended questions.

The full session is in [`elicitation-transcript.md`](elicitation-transcript.md).

What the elicitation surfaced:

| Moment | Elicitation outcome |
|---|---|
| T2 | Vague "self-contained posts" became a **product-aggregation** model, which exposed the duplicate problem |
| T3 | Developer asked about product identifiers. Client ruled out any manual SKU entry and proposed suggest-and-confirm matching |
| T3 | Developer **deferred** price history to keep the meeting in scope |
| T4 | Developer named product identification as the highest-risk item. Client relaxed "fully automatic" into "automatic where possible" (a **want vs. need** distinction) |
| T4 | Asking about business processes revealed the **business model** (affiliate commissions), which reshaped the data-acquisition approach |
| T5 | Revenue-share question exposed abuse risks and the gated trust-level model |
| T6 | Client added items missing from the developer's summary, plus a new nonfunctional need (mobile) |

## 2. Backlog generation

After the session, the same model was asked to turn the transcript into a requirements backlog:

> Using the elicitation transcript, produce a backlog of requirements representing the outcome of this initial pass. Separate functional and nonfunctional requirements. Make every requirement measurable. Tag each with metadata: type, category, high vs. low level (with parent), MoSCoW priority, status, risk, and the client statement it came from. Identify dependencies between requirements and link unresolved decisions to open questions. Mark anything the client implied but didn't say as "inferred."

The developer reviewed the output, and `tools/build_backlog.py` checks its structure: no duplicate IDs, no dangling references, and no dependency cycles.

## 3. Conventions

- **Functional vs. nonfunctional.** Functional requirements are described as inputs and outputs. Nonfunctional ones have measurable targets. For example, the client's "fast" became *p95 < 2 s* and is marked pending confirmation (OQ-09).
- **High vs. low level.** Low-level items (specifications) name the high-level requirement they refine in `parent`.
- **Risk.** "High" marks requirements expected to be volatile or hard to build. They are the first candidates for change-frequency tracking and focused testing.
- **Traceability.** Every requirement cites its source turn (T1–T6) or is marked `inferred`.

## 4. Next iteration

- Review the backlog with the client. Confirm the inferred items and the proposed numeric targets.
- Resolve the open questions, starting with OQ-04 and OQ-07, since they block the core posting pipeline.
- Track **requirements velocity** (new requirements per session) and **volatility** (changed requirements per session) across later sessions. Design work should start once both are trending down.
