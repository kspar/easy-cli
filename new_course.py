import requests

import conf
import util


def new_course(title: str):
    body = {
        'title': title
    }
    resp = requests.post(conf.EMS_BASE_URL + '/admin/courses', json=body, headers=util.get_token_header())
    print(resp.status_code)
    print(resp.json())
