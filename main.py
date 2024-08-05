import argparse
from selenium import webdriver
import lib.matches as matches
import lib.events as events

parser = argparse.ArgumentParser()
driver = webdriver.Chrome()

if __name__ == "__main__":
    parser.add_argument("-t", "--team_id", help="whoscored.com ID of the team")
    parser.add_argument("-e", "--extract", help="one of either matches or events")
    args = parser.parse_args()
    if args.extract == "matches":
        resp = matches.extract(args.team_id, driver)
        print(resp)
    elif args.extract == "events":
        resp = events.extract(args.team_id, driver)
        print(resp)
    else:
        print("--extract must be one of either matches or events")
