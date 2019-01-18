#!/usr/bin/env python3

import argparse

import requests

import util


def create_exercise(ex_title, ex_text, ex_public, ex_grader, ex_aas):
    body = {
        'title': ex_title,
        'text_html': ex_text,
        'public': ex_public,
        'grader_type': ex_grader,
        'aas_id': ex_aas
    }
    util.debug(body)
    resp = requests.post(util.BASE_URL + '/teacher/exercises', json=body, headers=util.get_required_headers())
    print(resp.status_code)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--title', required=True)
    parser.add_argument('--text-file')
    parser.add_argument('--public', action='store_true')
    parser.add_argument('--grader-type', required=True, choices=['AUTO', 'TEACHER'])
    parser.add_argument('--aas-id')
    args = parser.parse_args()

    exercise_text = util.get_file_content(args.text_file)

    create_exercise(args.title, exercise_text, args.public, args.grader_type, args.aas_id)
