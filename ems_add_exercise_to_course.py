#!/usr/bin/env python3

import argparse

import requests

import util


def create_course_exercise(course_id, ex_id, ex_threshold, ex_soft_deadline, ex_hard_deadline, ex_visible, ex_ass_visible):
    body = {
        "exercise_id": ex_id,
        "threshold": ex_threshold,
        "soft_deadline": ex_soft_deadline,
        "hard_deadline": ex_hard_deadline,
        "student_visible": ex_visible,
        "assessments_student_visible": ex_ass_visible
    }
    util.debug(body)
    resp = requests.post(util.BASE_URL + '/teacher/courses/' + course_id + '/exercises',
                         json=body, headers=util.get_required_headers())
    print(resp.status_code)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--course-id', required=True)
    parser.add_argument('--exercise-id', required=True)
    parser.add_argument('--threshold', required=True)
    parser.add_argument('--visible', action='store_true')
    parser.add_argument('--ass-visible', action='store_true')
    parser.add_argument('--soft-deadline')
    parser.add_argument('--hard-deadline')
    args = parser.parse_args()

    create_course_exercise(args.course_id, args.exercise_id, args.threshold, args.soft_deadline, args.hard_deadline,
                           args.visible, args.ass_visible)
