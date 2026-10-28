# Formula 1 World Championship Historical Archive (1950–Present)

Welcome to the verified, textbook-grade digital repository of Formula 1 World Championship history, race results, championship classifications, regulatory eras, circuit histories, and all-time records.

Every single result, time, lap count, point total, and statistic in this archive is cross-checked against primary official governing bodies (Fédération Internationale de l'Automobile - FIA, Formula One World Championship Limited - Formula1.com) and the Jolpica-F1 open statistical database.

---

## 1. Repository Directory Hierarchy

```
f1-archive/
├── seasons/
│   └── [YYYY]/
│       ├── calendar.md                # Official calendar, circuits, dates, round status
│       ├── standings.md               # Final or active Drivers' and Constructors' Championship standings
│       └── races/
│           └── [race-slug]/
│               ├── results.json       # Full official race classification JSON
│               ├── qualifying.json    # Q1/Q2/Q3 qualifying grid classification JSON
│               └── notes.md           # Classified finishers, fastest lap, retirements & sources
├── drivers/
│   └── [driver-slug].md               # Career totals, titles, maiden/latest race, win lists & sources
├── constructors/
│   └── [team-slug].md                 # Factory history, titles, starts, wins, leadership & sources
├── circuits/
│   └── [circuit-slug].md              # Complete track history, altitude, length changes, lap records, all past winners
├── records/
│   └── all-time.md                    # Verified all-time records (wins, poles, titles, streaks) with exact setting races
├── regulations/
│   └── eras-and-points-systems.md     # Technical eras, engine formulas, points tables, tie-breakers, red flags
├── VERIFICATION_LOG.md                # Master log of all primary sources and access dates
└── UPDATE_GUIDE.md                    # Protocol for weekly post-race automation via GitHub Actions & Jolpica
```

---

## 2. Archival Standards & Verification Policy

1. **Zero Estimation Rule**:
   - No numbers, race times, points, or milestones are recorded from unverified recollections.
   - Any unconfirmed data is explicitly cataloged as unverified or excluded.
2. **Primary Source Precedence**:
   - **Tier 1 (Governing Body)**: FIA Official Classifications, World Motor Sport Council Bulletins, Technical Regulations.
   - **Tier 1 (Commercial Rights Holder)**: Formula1.com Official Results Database and Hall of Fame.
   - **Tier 2 (Open Structured DB)**: Jolpica-F1 API (successor to Ergast), used by FastF1 and motorsport analysts.
   - **Tier 3 (Factory Teams)**: Scuderia Ferrari, Mercedes-AMG, Red Bull Racing, McLaren archives (only for team-specific heritage claims).
3. **Traceability**:
   - Every markdown summary and race record specifies exact primary source URLs and concludes with:
     `Last verified: [YYYY-MM-DD]`

---

## 3. Current Active Phase: The 2020s Decade (2020–2026)

- **2026 Season**: Current season, Round 18 (United States Grand Prix) completed. Championship leader: Andrea Kimi Antonelli (Mercedes). Next race: Round 19 (Mexico City Grand Prix at Autódromo Hermanos Rodríguez).
- **2025 Season**: Won by Lando Norris (McLaren, 423 pts) over Max Verstappen (Red Bull, 421 pts). Constructors' Champions: McLaren (833 pts).
- **2024 Season**: Won by Max Verstappen (Red Bull, 429 pts) over Lando Norris (McLaren, 374 pts). Constructors' Champions: McLaren (666 pts).
- **2023 Season**: Record-shattering season by Max Verstappen (19 wins from 22 races, 86.36% win rate, 10 consecutive wins). Constructors' Champions: Red Bull Racing (21 wins out of 22 races).
- **2022 Season**: Return of ground effect aerodynamics. Won by Max Verstappen (15 wins). Constructors' Champions: Red Bull Racing.
- **2021 Season**: Historic 22-round battle between Max Verstappen and Lewis Hamilton, decided on the final lap at Abu Dhabi. Drivers' Champion: Max Verstappen; Constructors' Champions: Mercedes (8th consecutive title).
- **2020 Season**: Pandemic-shortened 17-round season. Lewis Hamilton equalled Michael Schumacher's all-time record of 7 World Drivers' Championships.

---

Last verified: 2026-10-28

