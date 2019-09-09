import requests

import conf
import util


def new_course_exercise(course_id, exercise_id, threshold, soft_deadline, hard_deadline, visible, ass_visible,
                        instructions, title_alias):
    body = {
        'exercise_id': exercise_id,
        'threshold': threshold,
        'soft_deadline': soft_deadline,
        'hard_deadline': hard_deadline,
        'student_visible': visible,
        'assessments_student_visible': ass_visible,
        'instructions_html': instructions,
        'title_alias': title_alias
    }

    resp = requests.post(conf.EMS_BASE_URL + '/teacher/courses/' + course_id + '/exercises', json=body,
                         headers=util.get_token_header())
    print(resp.status_code)
