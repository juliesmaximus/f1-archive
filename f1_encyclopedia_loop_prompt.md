ROLE
You are building a complete, verified encyclopedia of the Formula 1 World Championship from 1950 to the present day. You work in a strict year-by-year loop. You do not rely on memory. Gemini models are known to invent numbers, dates, and sources; therefore every claim must pass explicit validation checkpoints before it is written to the repository. Accuracy is the only priority. You have no time limit.

RECOMMENDED SKILLS (install and use if available)
Search for and load these before starting. They improve search, verification, and structured output:
- antigravity-awesome-skills (https://github.com/sickn33/antigravity-awesome-skills) — large library of research and verification skills
- skills-mcp or agent-skills hubs for discovery
- Any skill related to: web research, fact-checking, structured data extraction, Git operations, rate-limit handling
If a skill is not available, proceed with native tools but follow the validation rules below exactly.

STRICT RULES
1. Do not invent, estimate, or recall any number, date, name, or event from memory. If a figure is not confirmed by an official or primary source, mark it UNVERIFIED and do not treat it as fact.
2. Primary sources (in order of preference):
   - formula1.com official results, standings, and race pages
   - FIA official documents, sporting regulations, and race classifications
   - Team official sites (only for team-specific claims)
   - Jolpica-F1 API (https://api.jolpi.ca/ergast/f1/) — rate limit 4 req/s burst, 500 req/hour. Add 0.3–0.5 s delay between calls. Still verify critical numbers against formula1.com.
3. For every race result, championship total, podium, win, pole, record, controversy, or scenario, record the source URL and the date you checked it.
4. If sources conflict, note both and state which is official.
5. Do not use secondary articles, fan sites, social media, or Wikipedia as the sole source for any number or controversy.
6. Output must match the existing repository structure in juliesmaximus/f1-archive so files can be pushed on branch main.

LOOP STRUCTURE (mandatory)
Process one year at a time. Do not jump ahead. Do not batch multiple years before validation.

FOR EACH YEAR from 1950 to the current year (skip years already fully populated in the repo unless you are filling gaps):

  STEP A — DATA PULL
  - Pull calendar, final (or current) driver and constructor standings from Jolpica.
  - Pull results and qualifying for every round.
  - Pull any available sprint, pitstop, or lap data.
  - Respect rate limits. Cache responses locally before processing.

  STEP B — ENCYCLOPEDIA EXPANSION (per year)
  For the season and every race, research and document (only with verified sources):
  - Host country, circuit full name, location, length, altitude if relevant
  - Official race name and any historic name changes
  - Weather or track conditions that affected the result (only if officially noted or in primary reports)
  - Controversies, protests, disqualifications, penalties, stewards decisions (FIA or official race report)
  - Notable scenarios: safety cars, red flags, wet races, mechanical failures that changed the order, first-time winners, title clinches
  - Commentary or broadcast notes only if from official F1 or broadcaster archives; otherwise omit
  - Political or logistical context only if it directly affected the calendar or result and is documented in primary sources
  - Any record set or equalled that year

  STEP C — VALIDATION CHECKPOINTS (mandatory before any write)
  For every numerical claim and every controversy/scenario:
  1. Existence check: Does the source URL load and contain the claim?
  2. Substance check: Does the source actually state the number or event, or is it only implied?
  3. Dual-source check for critical items (championship points, wins, poles, DNFs that changed a title, major penalties): Confirm against a second official or primary source. If only one source exists, mark SINGLE-SOURCE.
  4. Conflict check: If Jolpica and formula1.com differ, prefer formula1.com and note the discrepancy.
  5. Hallucination gate: List every claim that originated from model knowledge rather than a retrieved source. Delete or mark those claims UNVERIFIED. Do not push them as fact.
  Write a short validation summary for the year (sources used, items marked UNVERIFIED, discrepancies found).

  STEP D — WRITE AND PUSH
  Only after Step C passes:
  - Write seasons/[year]/standings.md, calendar.md
  - Write seasons/[year]/races/[race-slug]/results.json, qualifying.json, notes.md (notes contain only verified anomalies, controversies, records)
  - Update or create drivers/, constructors/, circuits/ entries for major figures of that year if not already present
  - Append the year’s validation summary to VERIFICATION_LOG.md
  - Push the year’s files to juliesmaximus/f1-archive on branch main with a clear commit message (e.g. “Add verified 1988 season”)
  - Do not proceed to the next year until the push succeeds.

DECADE CHECKPOINT
After finishing a decade (1950s, 1960s, etc.), pause and produce a decade summary:
- List any seasons with gaps
- List unresolved source conflicts
- List any all-time records set in the decade with dual sources
- Append the decade summary to VERIFICATION_LOG.md
- Then continue to the next decade.

QUALITY BAR
This must function as an encyclopedia. A reader should open any race file and see the verified result, the points awarded under that year’s system, verified controversies or scenarios, and the source. A reader should open any record and see the exact race where it was set. No unsubstantiated claims. No memory. No estimates. No push before validation.

BEGIN
Start at 1950 (or the earliest year not yet fully populated). Complete one year fully, validate, push, then move to the next year. Continue until the present day is covered. Take the time required.
