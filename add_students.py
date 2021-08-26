import requests

import util
import conf

def add_students(course_id: str, students: list, group_id: str):

    students_list = list(map(lambda e: {'email': e, 'groups': [{'id': group_id}]}, students))

    body = {
        'students': students_list
    }

    resp = requests.post(conf.EMS_BASE_URL + '/courses/' + course_id + '/students', json=body, headers=util.get_token_header())
    print(resp.status_code)
