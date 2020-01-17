import requests

import conf
import util


def reorder_exercises(course_id: str, course_exercise_id: str, new_index: int):
    body = {
        "new_index": new_index
    }

    resp = requests.post(conf.EMS_BASE_URL + '/courses/' + course_id + '/exercises/' + course_exercise_id + '/reorder', json=body, headers=util.get_token_header())
    print(resp.status_code)
