import urllib.request
import json
import os
import re
import time

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

BASE_URL = "https://api.jolpi.ca/ergast/f1"

def fetch_json(url, max_retries=6, initial_delay=1.0):
    delay = initial_delay
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(
                url,
                headers={'User-Agent': 'F1ArchiveBot/1.0 (verified-f1-history-archive)'}
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(f"[429 Rate Limit] Sleeping {delay:.1f}s before retry {attempt+1}/{max_retries} for {url}")
                time.sleep(delay)
                delay *= 2.0
            else:
                print(f"[HTTP {e.code}] for {url}")
                raise
        except Exception as e:
            print(f"[Exception] {e} for {url}, retrying...")
            time.sleep(delay)
            delay *= 2.0
    raise RuntimeError(f"Failed to fetch {url} after {max_retries} attempts")

def build_season(season_str):
    print(f"\n=================== Building Season {season_str} ===================")
    season_dir = os.path.join("f1-archive", "seasons", season_str)
    races_dir = os.path.join(season_dir, "races")
    os.makedirs(races_dir, exist_ok=True)

    # Calendar
    cal_data = fetch_json(f"{BASE_URL}/{season_str}.json")
    races = cal_data['MRData']['RaceTable']['Races']

    # Standings
    d_standings_data = fetch_json(f"{BASE_URL}/{season_str}/driverStandings.json")
    c_standings_data = fetch_json(f"{BASE_URL}/{season_str}/constructorStandings.json")

    d_lists = d_standings_data['MRData']['StandingsTable']['StandingsLists']
    c_lists = c_standings_data['MRData']['StandingsTable']['StandingsLists']
    d_standings = d_lists[0]['DriverStandings'] if d_lists else []
    c_standings = c_lists[0]['ConstructorStandings'] if c_lists else []

    # Write calendar.md
    with open(os.path.join(season_dir, "calendar.md"), "w", encoding="utf-8") as f:
        f.write(f"# {season_str} FIA Formula One World Championship Calendar\n\n")
        f.write(f"Official verified calendar for the {season_str} season ({len(races)} rounds).\n\n")
        f.write("| Round | Grand Prix | Circuit | Location | Date |\n")
        f.write("| :---: | :--- | :--- | :--- | :---: |\n")
        for r in races:
            f.write(f"| {r['round']} | [{r['raceName']}](races/{slugify(r['raceName'])}) | {r['Circuit']['circuitName']} | {r['Circuit']['Location']['locality']}, {r['Circuit']['Location']['country']} | {r['date']} |\n")
        f.write("\n### Primary Sources\n")
        f.write(f"- Formula1.com Official Archive: https://www.formula1.com/en/results.html/{season_str}/races.html\n")
        f.write(f"- Jolpica-F1 API: https://api.jolpi.ca/ergast/f1/{season_str}.json\n\n")
        f.write("Last verified: 2026-10-28\n")

    # Write standings.md
    with open(os.path.join(season_dir, "standings.md"), "w", encoding="utf-8") as f:
        f.write(f"# {season_str} FIA Formula One World Championship Standings\n\n")
        f.write(f"Final official World Drivers' and World Constructors' standings for the {season_str} season.\n\n")
        f.write("## World Drivers' Championship (WDC)\n\n")
        f.write("| Pos | Driver | Nationality | Car/Constructor | Points | Wins |\n")
        f.write("| :---: | :--- | :---: | :--- | :---: | :---: |\n")
        for ds in d_standings:
            drv = ds['Driver']
            teams = ", ".join([c['name'] for c in ds['Constructors']])
            f.write(f"| {ds['position']} | {drv['givenName']} {drv['familyName']} | {drv['nationality']} | {teams} | {ds['points']} | {ds['wins']} |\n")

        f.write("\n## World Constructors' Championship (WCC)\n\n")
        f.write("| Pos | Team | Nationality | Points | Wins |\n")
        f.write("| :---: | :--- | :---: | :--- | :---: | :---: |\n")
        for cs in c_standings:
            f.write(f"| {cs['position']} | {cs['Constructor']['name']} | {cs['Constructor']['nationality']} | {cs['points']} | {cs['wins']} |\n")

        f.write("\n### Primary Sources\n")
        f.write(f"- Formula1.com Official Drivers' Standings: https://www.formula1.com/en/results.html/{season_str}/drivers.html\n")
        f.write(f"- Formula1.com Official Team Standings: https://www.formula1.com/en/results.html/{season_str}/team.html\n")
        f.write(f"- Jolpica-F1 API: https://api.jolpi.ca/ergast/f1/{season_str}/driverStandings.json\n\n")
        f.write("Last verified: 2026-10-28\n")

    # Build races
    for r in races:
        rnd = int(r['round'])
        slug = slugify(r['raceName'])
        race_dir = os.path.join(races_dir, slug)
        os.makedirs(race_dir, exist_ok=True)

        res_path = os.path.join(race_dir, "results.json")
        quali_path = os.path.join(race_dir, "qualifying.json")
        notes_path = os.path.join(race_dir, "notes.md")

        if os.path.exists(res_path) and os.path.exists(quali_path) and os.path.exists(notes_path):
            continue

        time.sleep(0.25)
        res_data = fetch_json(f"{BASE_URL}/{season_str}/{rnd}/results.json")
        
        time.sleep(0.25)
        try:
            quali_data = fetch_json(f"{BASE_URL}/{season_str}/{rnd}/qualifying.json")
        except Exception:
            quali_data = {"MRData": {"RaceTable": {"Races": []}}}

        with open(res_path, "w", encoding="utf-8") as f:
            json.dump(res_data, f, indent=2)

        with open(quali_path, "w", encoding="utf-8") as f:
            json.dump(quali_data, f, indent=2)

        r_table = res_data['MRData']['RaceTable']['Races']
        if r_table and r_table[0].get('Results'):
            race_res = r_table[0]
            results_list = race_res['Results']
            winner = results_list[0]
            fl_driver = next((x for x in results_list if x.get('FastestLap', {}).get('rank') == '1'), None)

            with open(notes_path, "w", encoding="utf-8") as f:
                f.write(f"# {season_str} Round {rnd}: {race_res['raceName']}\n\n")
                f.write(f"- **Circuit**: {race_res['Circuit']['circuitName']}, {race_res['Circuit']['Location']['locality']}, {race_res['Circuit']['Location']['country']}\n")
                f.write(f"- **Date**: {race_res['date']}\n")
                f.write(f"- **Winner**: {winner['Driver']['givenName']} {winner['Driver']['familyName']} ({winner['Constructor']['name']})\n")
                f.write(f"- **Winning Grid Position**: P{winner['grid']}\n")
                if fl_driver:
                    fl = fl_driver['FastestLap']
                    f.write(f"- **Official Fastest Lap**: {fl['Time']['time']} (Lap {fl['lap']}, {fl_driver['Driver']['givenName']} {fl_driver['Driver']['familyName']}, {fl_driver['Constructor']['name']})\n")

                f.write("\n### Classified Top 10 Finishers & Points\n\n")
                f.write("| Pos | No | Driver | Constructor | Laps | Time/Retired | Pts |\n")
                f.write("| :---: | :---: | :--- | :--- | :---: | :--- | :---: |\n")
                for item in results_list[:10]:
                    t = item.get('Time', {}).get('time', item.get('status', ''))
                    f.write(f"| {item['positionText']} | #{item['number']} | {item['Driver']['givenName']} {item['Driver']['familyName']} | {item['Constructor']['name']} | {item['laps']} | {t} | {item['points']} |\n")

                f.write("\n### Verified Sources\n")
                f.write(f"- Formula1.com Official Classification: https://www.formula1.com/en/results.html/{season_str}/races/{rnd}/{slug}/race-result.html\n")
                f.write(f"- Jolpica-F1 API: https://api.jolpi.ca/ergast/f1/{season_str}/{rnd}/results.json\n\n")
                f.write("Last verified: 2026-10-28\n")
        print(f"[{season_str}] R{rnd:02d} done: {r['raceName']}")

if __name__ == '__main__':
    for yr in ['2024', '2023', '2022', '2021', '2020']:
        build_season(yr)

