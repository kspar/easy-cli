#!/usr/bin/env python3
import argparse
import os

import requests

import util


def update_exercise(ex_id, grading_script, image_name, max_time, max_mem, assets, executors):
    body = {
        "grading_script": grading_script,
        "container_image": image_name,
        "max_time_sec": max_time,
        "max_mem_mb": max_mem,
        "assets": assets,
        "executors": executors
    }
    util.debug(body)
    resp = requests.put(util.AAS_BASE_URL + '/exercises/' + ex_id, json=body, headers=util.get_required_headers())
    print(resp.status_code)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', required=True)
    parser.add_argument('--grading-file', required=True)
    parser.add_argument('--image-name', required=True)
    parser.add_argument('--max-time', required=True, type=int)
    parser.add_argument('--max-mem', required=True, type=int)
    parser.add_argument('--asset-files', nargs='*', default=[])
    parser.add_argument('--executors', nargs='+', required=True)
    args = parser.parse_args()

    grading_script = util.get_file_content(args.grading_file)

    assets = list(
        map(lambda filename: {'file_name': os.path.basename(filename),
                              'file_content': util.get_file_content(filename)},
            args.asset_files)
    )

    update_exercise(args.id, grading_script, args.image_name, args.max_time, args.max_mem, assets, args.executors)
