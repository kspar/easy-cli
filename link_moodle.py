import requests

import conf
import util

def link_moodle_course(course_id: str, moodle_short_name: str, sync_students: bool, sync_grades: bool):
    body = {
        "moodle_short_name": moodle_short_name,
        "sync_students": sync_students,
        "sync_grades": sync_grades
    }

    resp = requests.post(conf.EMS_BASE_URL + '/courses/' + course_id + '/moodle', json=body, headers=util.get_token_header())
    print(resp.status_code)

