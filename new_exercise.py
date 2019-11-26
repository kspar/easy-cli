import os

import requests

import conf
import util


def new_exercise(title: str, text_file: str, public: bool, grader: str,
                 grading_file: str, container_image: str, max_time_sec: int, max_mem_mb: int,
                 asset_files: list, executors: list):
    grading_script = util.get_file_content(grading_file)
    text = util.get_file_content(text_file)
    assets = list(map(lambda filename: {'file_name': os.path.basename(filename),
                                        'file_content': util.get_file_content(filename)},
                      asset_files)
                  )

    executors = list(map(lambda e: {'executor_id': e}, executors))

    body = {
        'title': title,
        'text_html': text,
        'public': public,
        'grader_type': grader.upper(),
        'grading_script': grading_script,
        'container_image': container_image,
        'max_time_sec': max_time_sec,
        'max_mem_mb': max_mem_mb,
        'assets': assets,
        'executors': executors
    }
    #print(body)
    resp = requests.post(conf.EMS_BASE_URL + '/exercises', json=body, headers=util.get_token_header())
    print(resp.status_code)
    j = resp.json()
    return j['id']


