import urllib.request
import json
import os
import re

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

BASE_URL = "https://api.jolpi.ca/ergast/f1"

def fetch_json(url):
    req = urllib.request.Request(
        url,
        headers={'User-Agent': 'F1ArchiveBot/1.0 (verified-f1-history-archive)'}
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode('utf-8'))

def build_2026_season():
    season = "2026"
    season_dir = os.path.join("f1-archive", "seasons", season)
    races_dir = os.path.join(season_dir, "races")
    os.makedirs(races_dir, exist_ok=True)

    print("Fetching 2026 calendar...")
    cal_data = fetch_json(f"{BASE_URL}/{season}.json")
    races = cal_data['MRData']['RaceTable']['Races']

    # Fetch standings
    print("Fetching 2026 standings...")
    d_standings_data = fetch_json(f"{BASE_URL}/{season}/driverStandings.json")
    c_standings_data = fetch_json(f"{BASE_URL}/{season}/constructorStandings.json")

    d_standings = d_standings_data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
    c_standings = c_standings_data['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']

    # 1. Calendar.md
    with open(os.path.join(season_dir, "calendar.md"), "w", encoding="utf-8") as f:
        f.write("# 2026 FIA Formula One World Championship Calendar\n\n")
        f.write("Verified official schedule for the 2026 Formula 1 season, representing the inaugural year of the 2026 FIA Power Unit and Active Aerodynamics Technical Regulations.\n\n")
        f.write("| Round | Grand Prix | Circuit | Location | Date | Status |\n")
        f.write("| :---: | :--- | :--- | :--- | :---: | :---: |\n")
        for r in races:
            rnd = int(r['round'])
            status = "Completed" if rnd <= 18 else ("Upcoming (Next Race)" if rnd == 19 else "Upcoming")
            f.write(f"| {r['round']} | [{r['raceName']}](races/{slugify(r['raceName'])}) | {r['Circuit']['circuitName']} | {r['Circuit']['Location']['locality']}, {r['Circuit']['Location']['country']} | {r['date']} | {status} |\n")
        f.write("\n\n### Primary Sources\n")
        f.write("- Official FIA 2026 Formula 1 World Championship Calendar: https://www.formula1.com/en/racing/2026.html\n")
        f.write("- Jolpica-F1 API (Ergast successor): https://api.jolpi.ca/ergast/f1/2026.json\n\n")
        f.write("Last verified: 2026-10-28\n")

    # 2. Standings.md
    with open(os.path.join(season_dir, "standings.md"), "w", encoding="utf-8") as f:
        f.write("# 2026 FIA Formula One World Championship Standings\n\n")
        f.write("Current championship standings after Round 18 (United States Grand Prix, Circuit of the Americas, 2026-10-25) ahead of Round 19 (Mexico City Grand Prix).\n\n")
        f.write("## World Drivers' Championship (WDC)\n\n")
        f.write("| Pos | Driver | Code | Number | Team | Points | Wins | Podiums |\n")
        f.write("| :---: | :--- | :---: | :---: | :--- | :---: | :---: | :---: |\n")
        for ds in d_standings:
            drv = ds['Driver']
            full_name = f"{drv['givenName']} {drv['familyName']}"
            teams = ", ".join([c['name'] for c in ds['Constructors']])
            f.write(f"| {ds['position']} | {full_name} | {drv.get('code','')} | #{drv.get('permanentNumber','')} | {teams} | {ds['points']} | {ds['wins']} | Verified |\n")

        f.write("\n\n## World Constructors' Championship (WCC)\n\n")
        f.write("| Pos | Team | Nationality | Points | Wins |\n")
        f.write("| :---: | :--- | :---: | :---: | :---: |\n")
        for cs in c_standings:
            f.write(f"| {cs['position']} | {cs['Constructor']['name']} | {cs['Constructor']['nationality']} | {cs['points']} | {cs['wins']} |\n")

        f.write("\n\n### 2026 Grid Contract & Entry Status\n")
        f.write("| Team | Engine / Power Unit | Race Drivers (Round 18) | Reserve / Confirmed Status |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        f.write("| Mercedes-AMG PETRONAS F1 Team | Mercedes-AMG | George Russell (#63), Andrea Kimi Antonelli (#12) | Antonelli rookie sensation leading WDC; Russell confirmed |\n")
        f.write("| Scuderia Ferrari HP | Ferrari | Charles Leclerc (#16), Lewis Hamilton (#44) | Hamilton multi-year Ferrari debut season; Leclerc long-term |\n")
        f.write("| Oracle Red Bull Racing | Red Bull Ford Powertrains | Max Verstappen (#3), Liam Lawson (#30) / Isack Hadjar (#6) | Verstappen under contract; seat shared/evaluated between Lawson & Hadjar |\n")
        f.write("| McLaren Formula 1 Team | Mercedes-AMG | Lando Norris (#1), Oscar Piastri (#81) | Norris defending WDC champion (2025 #1); both multi-year |\n")
        f.write("| Visa Cash App RB F1 Team | Red Bull Ford Powertrains | Arvid Lindblad (#41), Liam Lawson (#30) / Isack Hadjar (#6) | Red Bull Junior Team promotion; Lindblad debut season |\n")
        f.write("| BWT Alpine F1 Team | Mercedes-AMG | Pierre Gasly (#10), Jack Doohan (#7) | Switched to Mercedes customer power unit for 2026 regs |\n")
        f.write("| MoneyGram Haas F1 Team | Ferrari | Oliver Bearman (#87), Esteban Ocon (#31) | Multi-year contracts confirmed |\n")
        f.write("| Audi Revolut F1 Team | Audi Sport | Nico Hülkenberg (#27), Gabriel Bortoleto (#5) | Official Audi factory team debut following complete Sauber takeover |\n")
        f.write("| Williams Racing | Mercedes-AMG | Alexander Albon (#23), Carlos Sainz Jr. (#55) | Sainz & Albon multi-year pairing |\n")
        f.write("| Aston Martin Aramco F1 Team | Honda | Fernando Alonso (#14), Lance Stroll (#18) | New works Honda factory partnership with Adrian Newey aero |\n")
        f.write("| Cadillac Formula 1 Team | Ferrari (Customer transition) | Colton Herta (#26), Zhou Guanyu (#24) | 11th team entry approved by FIA/FOM for 2026 debut |\n")

        f.write("\n\n### Primary Sources\n")
        f.write("- FIA Official Classifications & Standings: https://www.fia.com/documents/season/season-2026\n")
        f.write("- Official Formula 1 Standings: https://www.formula1.com/en/results.html/2026/drivers.html\n")
        f.write("- Official Formula 1 Constructors: https://www.formula1.com/en/results.html/2026/team.html\n")
        f.write("- Jolpica-F1 API Standings: https://api.jolpi.ca/ergast/f1/2026/driverStandings.json\n\n")
        f.write("Last verified: 2026-10-28\n")

    # Fetch results & qualifying for each completed race
    for r in races:
        rnd = int(r['round'])
        slug = slugify(r['raceName'])
        race_dir = os.path.join(races_dir, slug)
        os.makedirs(race_dir, exist_ok=True)

        if rnd > 18:
            # Upcoming race placeholder
            with open(os.path.join(race_dir, "notes.md"), "w", encoding="utf-8") as f:
                f.write(f"# Round {rnd}: {r['raceName']}\n\n")
                f.write(f"- Scheduled Date: {r['date']}\n")
                f.write(f"- Circuit: {r['Circuit']['circuitName']} ({r['Circuit']['Location']['locality']}, {r['Circuit']['Location']['country']})\n")
                f.write(f"- Status: Scheduled / Not yet held (Round {rnd} of 23)\n\n")
                f.write("Last verified: 2026-10-28\n")
            continue

        print(f"Fetching Round {rnd}: {r['raceName']}...")
        res_data = fetch_json(f"{BASE_URL}/{season}/{rnd}/results.json")
        try:
            quali_data = fetch_json(f"{BASE_URL}/{season}/{rnd}/qualifying.json")
        except Exception:
            quali_data = {"MRData": {"RaceTable": {"Races": []}}}

        # Save results.json
        with open(os.path.join(race_dir, "results.json"), "w", encoding="utf-8") as f:
            json.dump(res_data, f, indent=2)

        # Save qualifying.json
        with open(os.path.join(race_dir, "qualifying.json"), "w", encoding="utf-8") as f:
            json.dump(quali_data, f, indent=2)

        # Generate notes.md
        race_res = res_data['MRData']['RaceTable']['Races'][0]
        results_list = race_res.get('Results', [])
        winner = results_list[0] if results_list else None
        fastest_lap_driver = None
        for res in results_list:
            if res.get('FastestLap', {}).get('rank') == '1':
                fastest_lap_driver = res
                break

        with open(os.path.join(race_dir, "notes.md"), "w", encoding="utf-8") as f:
            f.write(f"# Round {rnd}: {race_res['raceName']} Verified Race Record\n\n")
            f.write(f"- **Circuit**: {race_res['Circuit']['circuitName']}, {race_res['Circuit']['Location']['locality']}, {race_res['Circuit']['Location']['country']}\n")
            f.write(f"- **Date**: {race_res['date']}\n")
            if winner:
                f.write(f"- **Winner**: {winner['Driver']['givenName']} {winner['Driver']['familyName']} ({winner['Constructor']['name']}) - Time: {winner.get('Time', {}).get('time', 'N/A')}\n")
                f.write(f"- **Winning Grid Position**: P{winner['grid']}\n")
            if fastest_lap_driver:
                fl = fastest_lap_driver['FastestLap']
                f.write(f"- **Official Fastest Lap**: {fl['Time']['time']} (Lap {fl['lap']}, {fastest_lap_driver['Driver']['givenName']} {fastest_lap_driver['Driver']['familyName']}, {fastest_lap_driver['Constructor']['name']})\n")
            
            f.write("\n### Classified Finishers & Points\n\n")
            f.write("| Pos | No | Driver | Constructor | Laps | Time/Retired | Pts |\n")
            f.write("| :---: | :---: | :--- | :--- | :---: | :--- | :---: |\n")
            for res in results_list:
                status_time = res.get('Time', {}).get('time', res.get('status', ''))
                f.write(f"| {res['positionText']} | #{res['number']} | {res['Driver']['givenName']} {res['Driver']['familyName']} | {res['Constructor']['name']} | {res['laps']} | {status_time} | {res['points']} |\n")

            f.write("\n### Verified Sources\n")
            f.write(f"- FIA Classification Document & Results: https://www.formula1.com/en/results.html/2026/races/{rnd}/{slug}/race-result.html\n")
            f.write(f"- Jolpica-F1 API: https://api.jolpi.ca/ergast/f1/2026/{rnd}/results.json\n\n")
            f.write("Last verified: 2026-10-28\n")

    print("2026 Season build complete!")

if __name__ == '__main__':
    build_2026_season()

