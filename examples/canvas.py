import requests, json
from bs4 import BeautifulSoup

def get_assignments():
    file = open('canvas_token.env.txt', 'r')
    token = file.read()
    file.close()

    course_id = '64066'  #course id

    webpage = requests.get('https://una.instructure.com/api/v1/courses/' +
                           course_id + '/assignments', headers={"Authorization": "Bearer " + token})
    soup = BeautifulSoup(webpage.content, features="html.parser")

    assignment_list= []
    for i in soup:
        js = json.loads(i)
        assignment_list.append(js)

    output_string = ''
    count = 1
    for k in assignment_list[0][::-1]:
        # print(k['name'])
        # print(k['due_at'])
        output_string += '- Title: ' + \
            k['name'] + '\n  Due date: ' + k['due_at'][:10] + '\n\n'
        count += 1
        if count > 3:
            break
     

    return output_string


# print(get_assignments())
