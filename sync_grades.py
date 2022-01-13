import requests

import conf
import util


def sync_grades(course_id: str):

    resp = requests.post(conf.EMS_BASE_URL + '/courses/' + course_id + '/moodle/grades', headers=util.get_token_header())
    print(resp.status_code)
    print(resp.json())
