ROLE
You are continuing the verified Formula 1 archive. Phase 1 (2020–2026) is complete and already in the GitHub repository juliesmaximus/f1-archive. You do not rely on memory. Every fact, number, date, result, and claim must be cross-checked against official or primary sources before inclusion. You have no time limit. Accuracy is the only priority.

STRICT RULES (unchanged)
1. Do not invent, estimate, or recall numbers from memory. If a figure is not confirmed by an official or primary source, mark it as unverified and do not include it as fact.
2. Primary sources (in order of preference):
   - formula1.com official results and standings pages
   - FIA official documents and race classifications
   - Team official sites (only for team-specific claims)
   - Jolpica-F1 API (https://api.jolpi.ca/ergast/f1/) — still verify critical numbers against formula1.com when possible.
3. For every race result, championship total, podium, win, pole, or record, record the source URL and the date you checked it.
4. If sources conflict, note both and state which is official.
5. Do not use secondary articles, fan sites, or social media as the sole source for any number.
6. Output must match the existing repository structure so it can be pushed into juliesmaximus/f1-archive.

SCOPE FOR THIS PHASE
Continue systematically backward from 2019 to 1950. Cover every World Championship season that has official results. For each decade, pause and list gaps or conflicts before moving to the previous decade.

Priority order:
1. 2010s (2010–2019) — V8 finale, Red Bull/Vettel dominance, hybrid era start (Mercedes dominance)
2. 2000s (2000–2009) — Ferrari/Schumacher, Renault/Alonso, Hamilton/Räikkönen/Button, V10-to-V8
3. 1990s (1990–1999) — McLaren-Honda, Williams-Renault, Schumacher Benetton/Ferrari rise
4. 1980s (1980–1989) — Turbo era, Prost/Senna, ground-effect ban
5. 1970s (1970–1979) — Ford-Cosworth DFV, ground-effect birth, Lauda/Ferrari
6. 1960s (1960–1969) — Rear-engine revolution, 1.5L formula, wings, Clark/Hill
7. 1950s (1950–1959) — Foundation of the World Championship, Fangio, Ascari, Moss

For each season produce:
- seasons/[year]/standings.md (final standings with sources)
- seasons/[year]/calendar.md
- seasons/[year]/races/[race-slug]/results.json
- seasons/[year]/races/[race-slug]/qualifying.json (if available)
- seasons/[year]/races/[race-slug]/notes.md (only verified anomalies or records)

Also expand as you go:
- drivers/[driver-slug].md for major title winners and record holders of that decade
- constructors/[team-slug].md for major teams of that decade
- circuits/[circuit-slug].md for circuits that hosted championship races in that decade and are not already covered
- Update records/all-time.md if any new all-time records were set or equalled in the decade
- Append to VERIFICATION_LOG.md with sources and access dates for the decade

PROCESS
1. Start with 2019 and work backward.
2. For each season, pull the official calendar and final standings from Jolpica, then verify key totals on formula1.com.
3. For each race, pull the official classification.
4. When you finish a decade, pause, list any gaps or conflicts found, and append them to VERIFICATION_LOG.md before continuing.
5. Do not stop until every season from 1950 to 2019 that has official results is populated, or until you hit a hard source gap (note the gap explicitly).
6. Push the completed files to juliesmaximus/f1-archive on branch main when each decade is finished, or at the end if you prefer one large push.

QUALITY BAR
Same as Phase 1. A reader should be able to open any race file and see the verified result, the points awarded under that year’s system, and the source. No unsubstantiated claims. No memory. No estimates.

BEGIN
Start with the 2010s decade (2010–2019). Take the time required. Deliver files in the existing structure and push them to the repository.
