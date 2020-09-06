import requests

import util
import conf


def delete_group(course_id: str, group_id: str):
    resp = requests.delete(conf.EMS_BASE_URL + '/courses/' + course_id + '/groups/' + group_id, headers=util.get_token_header())
    print(resp.status_code)

