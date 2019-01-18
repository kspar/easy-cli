#!/usr/bin/env python3

import argparse

import requests

import util


def update_exercise(ex_id, ex_title, ex_text, ex_public):
    body = {
        'title': ex_title,
        'text_html': ex_text,
        'public': ex_public
    }
    util.debug(body)
    resp = requests.put(util.BASE_URL + '/teacher/exercises/' + ex_id, json=body, headers=util.get_required_headers())
    print(resp.status_code)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', required=True)
    parser.add_argument('--title', required=True)
    parser.add_argument('--text-file')
    parser.add_argument('--public', action='store_true')
    args = parser.parse_args()

    exercise_text = util.get_file_content(args.text_file)

    update_exercise(args.id, args.title, exercise_text, args.public)
