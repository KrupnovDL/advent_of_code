import requests
from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
session = open("session.txt", "r").read()
headers["Cookie"] = f"session={session}"

url = "https://adventofcode.com/2015/day/1/input"
input_data = requests.get(url, headers=headers).text

answer = 0
# answer += input_data.count('(')
# answer -= input_data.count(')')
#
# print(answer)

for position, bracket in enumerate(input_data, start=1):
    if bracket == '(':
        answer += 1
    else:
        answer -= 1
    if answer < 0:
        break

print(position)
