import time
from bs4 import BeautifulSoup

def generate_fixture_urls(team_id, driver):
    driver.get(f"https://www.whoscored.com/Teams/{team_id}/Fixtures")
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    return list(
        set(['https://www.whoscored.com' + x.attrs['href'] for x in soup.select('a[href*="\/Live\/"]')])
    )

competition_ids = {
    'England-Premier-League': 2,
    'England-FA-Cup': 26,
    'Spain-LaLiga': 4,
    'Italy-Serie-A': 5,
    'Germany-Bundesliga': 3,
    'France-Ligue-1': 22,
    'Europe-Champions-League': 12,
    'Europe-Europa-League': 30
}