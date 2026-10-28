import urllib.request
import json
import time

def check_2026():
    req = urllib.request.urlopen('https://api.jolpi.ca/ergast/f1/2026.json')
    data = json.loads(req.read())
    races = data['MRData']['RaceTable']['Races']
    print(f"Total races in 2026: {len(races)}")
    for r in races:
        round_no = r['round']
        url = f"https://api.jolpi.ca/ergast/f1/2026/{round_no}/results.json"
        try:
            req_r = urllib.request.urlopen(url)
            data_r = json.loads(req_r.read())
            r_list = data_r['MRData']['RaceTable']['Races']
            has_res = len(r_list) > 0 and len(r_list[0].get('Results', [])) > 0
            winner = r_list[0]['Results'][0]['Driver']['familyName'] if has_res else 'Not Held Yet'
            pole = r_list[0]['Results'][0]['grid'] if has_res else '-'
            print(f"R{round_no:02s} {r['raceName']:<32} {r['date']} Winner: {winner}")
        except Exception as e:
            print(f"R{round_no:02s} {r['raceName']}: {e}")
        time.sleep(0.1)

if __name__ == '__main__':
    check_2026()

