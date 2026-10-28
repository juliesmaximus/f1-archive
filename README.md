# F1 Archive

Verified Formula 1 history and statistics archive (1950–present).

## Structure
```
seasons/
  [year]/
    standings.md
    calendar.md
    races/
      [race-slug]/
        results.json
        qualifying.json
        notes.md
drivers/
constructors/
circuits/
records/
```

## Sources
- Jolpica-F1 API (https://api.jolpi.ca/ergast/f1/) for structured data
- formula1.com official pages for verification
- FIA documents where available

## Update process
GitHub Action (to be added) pulls the current season from Jolpica every Monday after a race. Manual verification against formula1.com before committing new records or standings.

## Prompt
See `f1_archive_antigravity_prompt.md` for the full research instructions given to Antigravity.
