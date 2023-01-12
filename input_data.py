import requests
from requests.structures import CaseInsensitiveDict


def input_data(year, day):
    headers = CaseInsensitiveDict()
    session = open("session.txt", "r").read()
    headers["Cookie"] = f"session={session}"
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    return requests.get(url, headers=headers).text
