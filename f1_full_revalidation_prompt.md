ROLE
You are performing a full, independent re-validation of the existing Formula 1 archive in juliesmaximus/f1-archive. The archive was generated earlier and may contain errors, missing details, or claims that came from model memory. Your only job is to test every existing file, correct every error, and expand every season and race with missing verified details. You do not rely on memory. Gemini models invent numbers and facts; treat every existing claim as untrusted until you re-verify it against a primary source. Accuracy is the only priority. You have no time limit.

STRICT RULES
1. Do not trust any number, date, name, or event already written in the repository. Re-fetch and re-check every one.
2. Primary sources (in order of preference):
   - formula1.com official results, standings, race pages, and fastest-lap pages
   - FIA official documents, sporting regulations, and race classifications
   - Team official sites (only for team-specific claims)
   - Jolpica-F1 API (https://api.jolpi.ca/ergast/f1/) — rate limit 4 req/s burst, 500 req/hour. Add 0.3–0.5 s delay. Still verify critical numbers against formula1.com.
3. If a claim cannot be confirmed by a primary source, mark it UNVERIFIED and remove it from the fact body, or move it to a clearly labelled “Unverified / needs source” section.
4. If sources conflict, prefer formula1.com and note the discrepancy.
5. Do not use secondary articles, fan sites, social media, or Wikipedia as the sole source for any number or controversy.
6. Push corrections only after the year passes all validation checkpoints below.

LOOP STRUCTURE (mandatory)
Process one year at a time. Do not jump ahead.

FOR EACH YEAR that already exists in the repository (and any year that is incomplete):

  STEP A — INVENTORY
  - List every file for that year (standings, calendar, every race results.json, qualifying.json, notes.md).
  - List every numerical claim and every narrative claim (weather, controversy, penalty, title clinch, record).

  STEP B — RE-VERIFY EVERY CLAIM
  For every claim:
  1. Existence check: Does a primary source URL still load and contain the exact claim?
  2. Substance check: Does the source state the number or event directly, or is it only implied?
  3. Dual-source check for critical items (championship points, wins, poles, DNFs that changed a title, major penalties, lap records): Confirm against a second official or primary source. If only one source exists, mark SINGLE-SOURCE.
  4. Conflict check: Compare Jolpica and formula1.com. Prefer formula1.com.
  5. Hallucination gate: Any claim that cannot be traced to a retrieved source in this pass is treated as invented. Delete it or mark UNVERIFIED.

  STEP C — ENCYCLOPEDIA EXPANSION (add anything missing)
  For every race and the season, ensure the following are present if a primary source exists:
  - Host country, circuit full name, location, length, altitude
  - Official race name and any historic name changes
  - Weather or track conditions that affected the result (only if officially noted or in primary reports)
  - Controversies, protests, disqualifications, penalties, stewards decisions (FIA or official race report)
  - Notable scenarios: safety cars, red flags, wet races, mechanical failures that changed the order, first-time winners, title clinches
  - Stadium or grandstand notes only if officially documented (e.g. Foro Sol / Estadio GNP Seguros at Mexico)
  - Any record set or equalled that year
  If a detail cannot be verified, do not invent it. Note the gap instead.

  STEP D — VALIDATION SUMMARY AND PUSH
  Write a short validation summary for the year:
  - Number of claims checked
  - Number corrected
  - Number marked UNVERIFIED or removed
  - Discrepancies found
  - Gaps that remain
  Append the summary to VERIFICATION_LOG.md.
  Push the corrected and expanded year to juliesmaximus/f1-archive on branch main with a clear commit message (e.g. “Re-validate and expand 1988”).
  Do not proceed to the next year until the push succeeds.

DECADE CHECKPOINT
After finishing a decade, produce a decade re-validation summary:
- Seasons that still have gaps
- Unresolved source conflicts
- All-time records that were corrected or newly confirmed
- Append the decade summary to VERIFICATION_LOG.md
- Then continue.

QUALITY BAR
After this pass, a reader should be able to open any race file and trust every number and every stated event because it has been re-checked against a primary source in this run. No letter or number that cannot be traced to a source should remain as fact. No unsubstantiated claims. No memory. No estimates. No push before validation.

BEGIN
Start at the earliest year present in the repository. Complete one year fully, validate, expand, push, then move to the next year. Continue until the present day is covered. Take the time required.
