ROLE
You are performing a rigorous, independent cross-check audit of the entire existing Formula 1 archive in juliesmaximus/f1-archive. The archive has already been generated and previously validated. Your task is to treat every number, name, date, result, standing, record, controversy, weather note, stadium detail, and scenario as untrusted until you re-verify it against primary sources in this pass. Gemini models invent numbers and facts. Accuracy is the only priority. You have no time limit. Do not rely on memory.

STRICT RULES
1. Do not trust any claim already written in the repository. Re-fetch and re-check every numerical and factual claim.
2. Primary sources (strict order of preference):
   - formula1.com official results pages, standings pages, race pages, and fastest-lap pages (e.g. https://www.formula1.com/en/results.html/[year]/drivers.html and individual race result pages)
   - FIA official documents, sporting regulations, and race classifications
   - Team official sites (only for team-specific claims that cannot be found on formula1.com or FIA)
   - Jolpica-F1 API (https://api.jolpi.ca/ergast/f1/) — rate limit 4 req/s burst, 500 req/hour. Add 0.3–0.5 s delay between calls. Always cross-check critical numbers against formula1.com.
3. If a claim cannot be confirmed by a primary source in this pass, mark it UNVERIFIED and remove it from the fact body, or move it to a clearly labelled “Unverified / needs source” section. Do not leave invented or unsupported numbers as fact.
4. If sources conflict, prefer formula1.com and explicitly note the discrepancy (source A says X, source B says Y).
5. Do not use secondary articles, fan sites, social media, Wikipedia, or model memory as the sole source for any number, result, controversy, or scenario.
6. Push corrections only after the year passes all validation checkpoints below.

LOOP STRUCTURE (mandatory)
Process one year at a time. Do not jump ahead. Do not batch multiple years before completing validation for the current year.

FOR EACH YEAR present in the repository (and any incomplete year):

  STEP A — INVENTORY
  - List every file for that year (standings.md, calendar.md, every race’s results.json, qualifying.json, notes.md, and any related records).
  - Extract every numerical claim (points, wins, poles, positions, lap times, circuit length, altitude, points system values) and every narrative claim (weather, controversy, penalty, disqualification, title clinch, record, stadium/grandstand note).

  STEP B — CROSS-CHECK EVERY CLAIM
  For every claim:
  1. Existence check: Does a primary source URL still load and contain the exact claim?
  2. Substance check: Does the source state the number or event directly, or is it only implied or summarized?
  3. Dual-source check for critical items (championship points totals, race wins, poles, DNFs that changed a title, major penalties, lap records, points system for that year): Confirm against a second official or primary source. If only one source exists, mark SINGLE-SOURCE.
  4. Conflict check: Compare Jolpica JSON against formula1.com. Prefer formula1.com and log any difference.
  5. Hallucination gate: Any claim that cannot be traced to a retrieved primary source in this pass is treated as invented. Delete it or mark UNVERIFIED. Do not push it as fact.
  6. Points system verification: Confirm the points awarded in that year match the official FIA/formula1.com rules for that season (including any best-results rules, shared drives, or special regulations).

  STEP C — ENCYCLOPEDIA EXPANSION (add only verified missing details)
  For every race and the season, ensure the following are present only if a primary source exists:
  - Host country, circuit full name, location, length, altitude
  - Official race name and any historic name changes
  - Weather or track conditions that affected the result (only if officially noted or in primary reports)
  - Controversies, protests, disqualifications, penalties, stewards decisions (FIA or official race report)
  - Notable scenarios: safety cars, red flags, wet races, mechanical failures that changed the order, first-time winners, title clinches
  - Stadium or grandstand notes only if officially documented (e.g. Foro Sol / Estadio GNP Seguros at Mexico)
  - Any record set or equalled that year
  If a detail cannot be verified from a primary source, do not invent it. Note the gap instead.

  STEP D — VALIDATION SUMMARY AND PUSH
  Write a short cross-check summary for the year:
  - Number of claims checked
  - Number corrected
  - Number marked UNVERIFIED or removed
  - Discrepancies found between sources
  - Gaps that remain
  Append the summary to VERIFICATION_LOG.md under a clear “Cross-check audit” heading for that year.
  Push the corrected and expanded year to juliesmaximus/f1-archive on branch main with a clear commit message (e.g. “Cross-check and correct 1988”).
  Do not proceed to the next year until the push succeeds.

DECADE CHECKPOINT
After finishing a decade, produce a decade cross-check summary:
- Seasons that still have gaps or unresolved conflicts
- All-time records that were corrected or newly confirmed with dual sources
- Append the decade summary to VERIFICATION_LOG.md
- Then continue to the next decade.

QUALITY BAR
After this pass, a reader should be able to open any race file or standings file and trust every number and every stated event because it has been re-checked against a primary source in this run. No letter or number that cannot be traced to a primary source should remain as fact. No unsubstantiated claims. No memory. No estimates. No push before validation.

BEGIN
Start at the earliest year present in the repository. Complete one year fully, cross-check, expand only with verified details, push, then move to the next year. Continue until the present day is covered. Take the time required.
