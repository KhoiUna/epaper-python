import requests
from bs4 import BeautifulSoup
import json

token = "<USER_TOKEN>"

webpage = requests.get(
    'https://una.instructure.com/api/v1/courses/57087/assignments', headers={"Authorization": "Bearer " + token})
soup = BeautifulSoup(
    webpage.content, features="html.parser")

for i in soup:
    js = json.loads(i)
    for k in js:
        print(k['name'])
