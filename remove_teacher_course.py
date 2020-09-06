import requests

import util
import conf

def remove_teacher_course(course_id: str, teachers: list):

    teachers_list = list(map(lambda e: {'username': e}, teachers))

    body = {
        'teachers': teachers_list
    }

    resp = requests.delete(conf.EMS_BASE_URL + '/courses/' + course_id + '/teachers', json=body, headers=util.get_token_header())

    print(resp.status_code)