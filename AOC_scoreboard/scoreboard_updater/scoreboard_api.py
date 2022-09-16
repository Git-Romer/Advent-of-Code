from scoreboard.api_secrets import *
import requests
from scoreboard.models import jsoncrawler

def get_scoreboard_json():
    SCOREBOARD_URL = 'https://adventofcode.com/2021/leaderboard/private/view/2203592.json'

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}
    return requests.get(SCOREBOARD_URL, headers=headers, cookies=SESSION_COOKIE).json()

def update():

    response = get_scoreboard_json()

    for member in response["members"].keys():
        member_id = response["members"][member]["id"]
        name = response["members"][member]["name"]
        stars = response["members"][member]["stars"]
        global_score = response["members"][member]["global_score"]
        local_score = response["members"][member]["local_score"]
        last_star_ts = response["members"][member]["last_star_ts"]
        completition_day_level = response["members"][member]["completion_day_level"]
        event = response["event"]

        res = jsoncrawler(
            member_id=member_id,
            name=name,
            stars=stars,
            global_score=global_score,
            local_score=local_score,
            last_star_ts=last_star_ts,
            completition_day_level=completition_day_level,
            event=event
        )
        res.save()
    print("Updated scoreboard!")

if __name__ == "__main__":
    import os, sys
    sys.path.append('./')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'AOC_scoreboard.settings'
    import django
    django.setup()
    update()