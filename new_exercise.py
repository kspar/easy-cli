import os

import requests

import conf
import util


def new_exercise(title: str, html_file: str, adoc_file: str, public: bool, grader: str,
                 grading_file: str, container_image: str, max_time_sec: int, max_mem_mb: int,
                 asset_files: list, executors: list):

    html = util.get_optional_file_content(html_file)
    adoc = util.get_optional_file_content(adoc_file)

    body = {
        'title': title,
        'text_html': html,
        'text_adoc': adoc,
        'public': public,
        'grader_type': grader.upper(),
        'container_image': container_image,
        'max_time_sec': max_time_sec,
        'max_mem_mb': max_mem_mb,
    }

    if grading_file is not None:
        grading_script = util.get_file_content(grading_file)
        body["grading_script"] = grading_script
    if len(asset_files) > 0:
        assets = list(map(lambda filename: {'file_name': os.path.basename(filename),
                                            'file_content': util.get_file_content(filename)},
                          asset_files)
                      )
        body["assets"] = assets
    if len(executors) > 0:
        executors = list(map(lambda e: {'executor_id': e}, executors))
        body["executors"] = executors



    resp = requests.post(conf.EMS_BASE_URL + '/exercises', json=body, headers=util.get_token_header())
    print(resp.status_code)
    j = resp.json()
    print(j)
    return j['id']


