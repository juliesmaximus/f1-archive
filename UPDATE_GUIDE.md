# F1 Archive Continuous Update & Verification Protocol

This guide outlines the operational workflow for maintaining the `f1-archive` repository as the definitive, textbook-grade Formula 1 historical and statistical database.

---

## 1. Automation Architecture

```
                    ┌───────────────────────────────────┐
                    │ Scheduled Cron / Manual Trigger   │
                    │ Every Monday at 06:00 UTC         │
                    └─────────────────┬─────────────────┘
                                      │
                                      ▼
                    ┌───────────────────────────────────┐
                    │ GitHub Actions Workflow Runner    │
                    │ (.github/workflows/update-f1.yml) │
                    └─────────────────┬─────────────────┘
                                      │
               ┌──────────────────────┴──────────────────────┐
               ▼                                             ▼
  ┌─────────────────────────┐                   ┌─────────────────────────┐
  │  Jolpica-F1 API Query   │                   │ Formula1.com Scraper &  │
  │ (Structured JSON data)  │                   │ FIA PDF Classification  │
  └────────────┬────────────┘                   └────────────┬────────────┘
               │                                             │
               └──────────────────────┬──────────────────────┘
                                      │
                                      ▼
                    ┌───────────────────────────────────┐
                    │ Dual-Source Reconciliation Engine │
                    │ - Reconciles times, laps, points  │
                    │ - Highlights conflicts / penalties│
                    └─────────────────┬─────────────────┘
                                      │
                                      ▼
                    ┌───────────────────────────────────┐
                    │ File Generation & Verification    │
                    │ - Update season standings.md      │
                    │ - Write race results.json/notes   │
                    │ - Update career driver totals     │
                    │ - Log entries in VERIFICATION_LOG │
                    └─────────────────┬─────────────────┘
                                      │
                                      ▼
                    ┌───────────────────────────────────┐
                    │ Git Commit & Pull Request         │
                    │ (Auto-merge if 0 discrepancies)   │
                    └───────────────────────────────────┘
```

---

## 2. Step-by-Step Post-Race Weekend Procedure

1. **Jolpica Ingestion**:
   - The Jolpica-F1 API updates its Ergast-compatible endpoint early on the Monday following each Grand Prix weekend (`https://api.jolpi.ca/ergast/f1/current/last/results.json`).
   - The GitHub Action executes a synchronization script to download the race results, qualifying classification, sprint results (if applicable), and current championship standings.

2. **Official FIA / Formula1.com Verification**:
   - The workflow cross-checks:
     - Winning time and gap deltas against the official **FIA Document Classification**.
     - Bonus points (fastest lap, sprint points) to ensure no post-race penalties (e.g. track limits, technical exclusions, restart time additions) alter the final result.
     - Fastest lap driver: confirms the driver was classified in the top 10 (for 2019–2024 regulations) or verifies that no bonus point was awarded (2025+).

3. **Discrepancy Escalation**:
   - If Jolpica and FIA/formula1.com diverge (e.g. pending appeals, steward investigations that conclude after provisional classification), the automation creates a GitHub Issue tagged `needs-human-verification` and flags the race as `[Provisional — Under Review]`.

4. **Directory Structure Convention**:
   - New races are saved to `f1-archive/seasons/[YYYY]/races/[grand-prix-slug]/`:
     - `results.json`: Complete JSON classification from Jolpica.
     - `qualifying.json`: Complete Q1/Q2/Q3 qualifying classification.
     - `notes.md`: Human-readable summary including pole time, winning margin, fastest lap, retirements with official causes, and verified source URLs.
   - Updates are applied to:
     - `f1-archive/seasons/[YYYY]/standings.md`
     - `f1-archive/drivers/[driver-slug].md`
     - `f1-archive/constructors/[team-slug].md`
     - `f1-archive/records/all-time.md` (if any all-time record is broken or tied)
     - `f1-archive/VERIFICATION_LOG.md`

---

## 3. Rate Limit Handling

- The Jolpica-F1 API enforces rate limits on burst traffic. All scripts must implement:
  - Minimum request inter-arrival time of 0.3 to 0.5 seconds.
  - Exponential backoff with a minimum of 5 retries on HTTP 429 status codes.
  - Batching season ingestion to avoid concurrent request saturation.

Last verified: 2026-10-28

