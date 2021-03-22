import requests
from bs4 import BeautifulSoup
import json

name = input('Name: ')

data = {'method': 'retrieveEmployees',
        'searchTerm': name,
        'searchType': 0}


webpage = requests.post(
    'https://una.edu/directory/api/api.php', data=data)
soup = BeautifulSoup(webpage.content, features='html.parser')

for i in soup:
    employee_data = json.loads(i)['employees']
    for i in employee_data:
        print(i)
        print('------------------------------------\n')
