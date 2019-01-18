
DEBUG_ENABLED = True
BASE_URL = 'https://ems.lahendus.ut.ee/v1'


def get_required_headers():
    access_token = get_file_content('access_token').strip()
    return {'Authorization': 'Bearer ' + access_token}


def get_file_content(file_name):
    with open(file_name, encoding='utf-8') as f:
        return f.read()


def debug(msg):
    if DEBUG_ENABLED:
        print(msg)
