import time
import json
from bs4 import BeautifulSoup
import os
import re
from lib.util import generate_fixture_urls, competition_ids

def extract(team_id, driver):
    all_urls = generate_fixture_urls(team_id, driver)
    
    for url in all_urls:
        match = re.search(r'/Matches/(\d+)/Live/([^/]+?)-(\d{4}-\d{4})', url)
        if match:
            match_id = int(match.group(1))
            driver.get(url)
            time.sleep(1)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            element = soup.select_one('script:-soup-contains("matchCentreData")')
            if element:
                match_centre_data = element.text.split("matchCentreData: ")[1].split(',\n')[0]
                if not os.path.exists(f'data/{team_id}'):
                    os.makedirs(f'data/{team_id}')
                with open(f'data/{team_id}/{match_id}.json', 'w') as file:
                    match_centre_data_decoded = json.loads(match_centre_data)
                    file.write(json.dumps(match_centre_data_decoded))
                print(f'{team_id}/{match_id}.json successfully created')
            else:
                print(f'No matchCentreData found for URL: {url}')
        else:
            print(f'Invalid URL format: {url}')