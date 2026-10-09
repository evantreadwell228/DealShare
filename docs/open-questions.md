# Open Questions

These came up during elicitation but weren't resolved. Requirements that can't move forward until one is answered list it in their `blocked_by` field in [`backlog/requirements.yaml`](../backlog/requirements.yaml).

| ID | Question | Raised in | Owner | Blocks |
|---|---|---|---|---|
| OQ-01 | Who may merge product pages, move deals, and moderate? Everyone, trusted users above a threshold, or staff moderators only? | T3, T6 | Client | FR-025, FR-052, FR-057 |
| OQ-02 | What percentage of affiliate commission goes to the poster? | T5 | Client | FR-063 |
| OQ-03 | How are variants told apart: structured attributes from retailer APIs, title parsing, poster selection, or a mix? Which attribute differences make a new *product* rather than a *variant*? | T3, developer | Dev + Client | FR-030, FR-031 |
| OQ-04 | Which retailers are in the launch set, which affiliate programs will approve us, and which of them provide product-data APIs? | T4 | Client | FR-011, FR-060, FR-061, NFR-005 |
| OQ-05 | Do the affiliate programs' terms allow sharing commission with end users (sub-affiliate payouts)? | T5 | Legal | FR-063 |
| OQ-06 | When several users post the same deal, who gets credit: the first poster, the top-voted post, or a split? | T5, T6 | Client | FR-066 |
| OQ-07 | Legal review: is reading page metadata or fetching non-API pages permitted for each launch store? | T4 | Legal | FR-011, FR-061, NFR-006 |
| OQ-08 | Which payout provider, what minimum payout threshold, and what payout schedule? | T5 | Client + Dev | FR-064 |
| OQ-09 | Confirm the proposed performance target (p95 < 2 s) and expected user volume at launch and at 12 months. | T1, developer | Client | NFR-003 |
| OQ-10 | How many "expired" reports (or what reputation-weighted total) mark a deal as dead? Can a deal be reported back to live? | T4, T6 | Dev + Client | FR-053 |

## Explicitly out of scope for v1

- Native mobile app. The mobile web experience is required instead (NFR-002). (T6)
- Display advertising and charging users. The business model is affiliate commission only. (T4)
- Storing payout or financial details in-house. These are delegated to a provider (NFR-007). (T5)

## Deferred

- Price history (FR-080). The client wants it, but the developer parked it for a later pass (T3).
