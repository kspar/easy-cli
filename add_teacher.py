import requests

import conf
import util


def add_teacher(course_id: str, teachers: list):

    teachers_list = list(map(lambda e: {'email': e}, teachers))

    body = {
        'teachers': teachers_list
    }

    resp = requests.post(conf.EMS_BASE_URL + '/courses/' + course_id + '/teachers', json=body, headers=util.get_token_header())
    print(resp.status_code)

