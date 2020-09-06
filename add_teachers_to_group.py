import requests

import conf
import util


def add_teachers_to_group(course_id: str, teachers: list, group_id: str):

    teachers_list = list(map(lambda e: {'username': e}, teachers))

    body = {
        'teachers': teachers_list
    }

    resp = requests.post(conf.EMS_BASE_URL + '/courses/' + course_id + '/groups/' + group_id + '/teachers', json=body, headers=util.get_token_header())

    print(resp.status_code)