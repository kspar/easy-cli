import requests

import conf
import util


def autoass(course_id: str, exercise_id: str, solution_file: str):
    solution = util.get_file_content(solution_file)
    body = {
        'solution': solution
    }
    resp = requests.post(
        conf.EMS_BASE_URL + '/teacher/courses/' + course_id + '/exercises/' + exercise_id + '/autoassess', json=body,
        headers=util.get_token_header())
    print(resp.status_code)
    print(resp.json())
