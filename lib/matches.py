import os
import re
import json
from lib.util import generate_fixture_urls, competition_ids

def extract(team_id, driver):    
    all_urls = generate_fixture_urls(team_id, driver)

    for url in all_urls:
        match = re.search(r'/Matches/(\d+)/Live/([^/]+?)-(\d{4}-\d{4})-([^/]+)', url)
        if match:
            natural_key = int(match.group(1))
            competition_key = match.group(2)
            competition_name = ' '.join(competition_key.split('-')[1:])
            season = match.group(3)
            country = competition_key.split('-', 1)[0]
            name = match.group(4)
            
            if competition_key in competition_ids:
                json_object = {
                    'naturalKey': natural_key,
                    'name': name,
                    'competitionNaturalKey': competition_ids[competition_key],
                    'competitionName': competition_name,
                    'season': season,
                    'country': country
                }
                if not os.path.exists(f'data/{team_id}'):
                    os.makedirs(f'data/{team_id}')
                with open(f'data/{team_id}/catalog.jsonl', 'a+') as file:
                    file.write(json.dumps(json_object) + '\n')
            else:
                print(f'{competition_key} not found - skipping {name}')

    return print(f'{team_id}/catalog.jsonl successfully created')