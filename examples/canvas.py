import requests, json
from bs4 import BeautifulSoup

def get_assignments():
    file = open('canvas_token.env.txt', 'r')
    token = file.read()
    file.close()

    course_id = '64066'  #course id

    # Assignments API: List assignments
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


def get_course_info():
    file = open('canvas_token.env.txt', 'r')
    token = file.read()
    file.close()

    course_id = '64066'  # course id

    # Courses API: Get a single course
    # /api/v1/accounts/:account_id/courses/:id
    webpage = requests.get('https://una.instructure.com/api/v1/courses/'+ 
                            course_id, headers={"Authorization": "Bearer " + token})
    js = webpage.json()

    return {"course_code": js["course_code"], "start_at": js["start_at"][:10], "end_at": js["end_at"][:10]}

def get_professor_info():
    webpage = requests.get("https://cooking-reservation.herokuapp.com/api/rasp")
    return webpage.json()

# print(get_assignments())
# print(get_course_info())
# print(get_professor_info())