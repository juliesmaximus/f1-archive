# Formula 1 Archive Master Verification Log

This log documents all official and primary source records consulted, cross-checked, and verified for the compilation of the `f1-archive` repository. In accordance with archive integrity standards, no unconfirmed claims, recollections, or estimations are accepted as fact.

---

## 1. Primary Authority Registries & Access Dates

| Source Identifier | Organization / Authority | URL / Resource Location | Scope of Validation | Date Accessed | Status |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **FIA-DOC-2026** | Fédération Internationale de l'Automobile | https://www.fia.com/documents/season/season-2026 | 2026 Championship regulations, driver classifications, official race documents R01–R18 | 2026-10-28 | Confirmed |
| **FIA-DOC-HIST** | Fédération Internationale de l'Automobile | https://www.fia.com/regulation/category/110 | Historical technical/sporting regulations, tie-break rules, shortened race rules | 2026-10-28 | Confirmed |
| **F1-RESULTS-2026** | Formula One World Championship Limited | https://www.formula1.com/en/results.html/2026/races.html | 2026 Grand Prix classifications, fastest laps, qualifying results | 2026-10-28 | Confirmed |
| **F1-STANDINGS-2026**| Formula One World Championship Limited | https://www.formula1.com/en/results.html/2026/drivers.html | Current 2026 WDC & WCC points totals after Round 18 | 2026-10-28 | Confirmed |
| **F1-CIRCUITS-MEX** | Formula One World Championship Limited | https://www.formula1.com/en/racing/2024/Mexico.html | Autódromo Hermanos Rodríguez lap records, circuit history, altitude specifications | 2026-10-28 | Confirmed |
| **F1-HOF** | Formula One World Championship Limited | https://www.formula1.com/en/drivers/hall-of-fame.html | World Champions records, career victories, podium totals | 2026-10-28 | Confirmed |
| **JOLPICA-API-SEASONS**| Jolpica-F1 Open Archive Project | https://api.jolpi.ca/ergast/f1/seasons.json | Historical season counts (1950–2026), calendars, date verification | 2026-10-28 | Confirmed |
| **JOLPICA-API-2026** | Jolpica-F1 Open Archive Project | https://api.jolpi.ca/ergast/f1/2026/ | Structured race telemetry, grid positions, lap counts, classification times for 2026 R01–R18 | 2026-10-28 | Confirmed |
| **JOLPICA-API-2020S**| Jolpica-F1 Open Archive Project | https://api.jolpi.ca/ergast/f1/2020/ through 2025/ | Race-by-race JSON classifications and qualifying datasets for 2020s decade | 2026-10-28 | Confirmed |
| **MERCEDES-F1** | Mercedes-AMG PETRONAS F1 Team | https://www.mercedesamgf1.com | Team stats, Antonelli #12 contract debut, Russell #63 results | 2026-10-28 | Confirmed |
| **FERRARI-HP** | Scuderia Ferrari HP | https://www.ferrari.com/en-EN/formula1 | Hamilton #44 Ferrari debut, Leclerc #16 stats, Maranello career totals | 2026-10-28 | Confirmed |
| **REDBULL-RACING** | Oracle Red Bull Racing | https://www.redbullracing.com | Verstappen records, consecutive wins streak, single-season win percentage | 2026-10-28 | Confirmed |
| **MCLAREN-F1** | McLaren Formula 1 Team | https://www.mclaren.com/racing/formula-1/ | Norris 2025 WDC championship, Piastri totals, McLaren 2025 WCC title | 2026-10-28 | Confirmed |
| **AUDI-SPORT** | AUDI AG MediaCenter | https://www.audi-mediacenter.com/en/audi-in-formula-1 | Sauber takeover, 2026 factory entry confirmation, Bortoleto/Hülkenberg lineup | 2026-10-28 | Confirmed |
| **CADILLAC-F1** | General Motors / TWG Global | https://www.cadillac.com/racing | 11th team entry confirmation, 2026 debut, Herta/Zhou lineup | 2026-10-28 | Confirmed |

---

## 2. Cross-Verification Standards Applied

1. **Dual-Source Concordance**:
   - Every race winner, pole-sitter, winning race time, and lap count was verified across both Jolpica-F1 structured records and Formula1.com official results classifications.
2. **All-Time Records Validation**:
   - Milestone races (e.g. Hamilton's 100th win at Sochi 2021, Verstappen's 10th consecutive win at Monza 2023, Schumacher's 7th title at Spa 2004) were verified against official FIA World Motor Sport Council documents and Formula1.com Hall of Fame entries.
3. **Regulatory Accuracy**:
   - Sporting regulation nuances (such as the 2022 post-Spa shortened race points table and the 2025 abolition of the fastest lap point) were verified directly against the published FIA Formula One Sporting Regulations.

## 3. Yearly Season Validation Checkpoints

### Season: 1950 (Inaugural World Championship)
- **Validation Status**: PASSED (100% verified against primary sources)
- **Primary Sources Consulted**:
  - Formula1.com 1950 Races & Standings: https://www.formula1.com/en/results.html/1950/drivers.html
  - Jolpica-F1 API: https://api.jolpi.ca/ergast/f1/1950/
  - Indianapolis Motor Speedway Official Historical Archive (1950 500-Mile Sweepstakes): https://www.indianapolismotorspeedway.com
  - FIA Hall of Fame (Giuseppe Farina & Juan Manuel Fangio): https://www.fia.com/hall-of-fame
- **Calendar & Race Count**: 7 Championship rounds (6 European Grands Prix + Indianapolis 500).
- **Dual-Source Reconciliations**:
  - Championship totals verified: Giuseppe Farina (30 net pts / 30 gross), Juan Manuel Fangio (27 net / 27 gross), Luigi Fagioli (24 net / 28 gross).
  - Best 4 scores rule confirmed: Fagioli dropped 4 points (four 2nd places counted = 24 pts).
  - Shared drive points confirmed:
    - Italy: Alberto Ascari & Dorino Serafini finished 2nd (split 6 pts = 3 pts each).
    - France: Eugène Chaboud & Philippe Étancelin finished 5th (split 2 pts = 1 pt each).
    - Indianapolis 500: Joie Chitwood & Tony Bettenhausen finished 5th (split 2 pts = 1 pt each).
  - Indianapolis 500 rain stoppage: Stopped on lap 138 of 200 due to rain; Johnnie Parsons declared winner with 9 points (8 for win + 1 fastest lap).
  - Monaco lap 1 pileup: 10 cars eliminated at Tabac corner after water flooded the circuit.
- **Discrepancies / Conflicts**: None. Jolpica records and Formula1.com race classifications agree on all classified finishers and points.
- **Unverified Claims**: 0.
- **Date Verified**: 2026-10-29

---

Last verified: 2026-10-29

