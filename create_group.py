import requests

import conf
import util


def create_group(course_id: str, name: str):
    body = {
        'name': name
    }

    resp = requests.post(conf.EMS_BASE_URL + '/courses/' + course_id + '/groups', json=body, headers=util.get_token_header())
    print(resp.status_code)
    j = resp.json()
    return j['id']
