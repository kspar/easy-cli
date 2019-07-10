import os

DEBUG_ENABLED = True
WARN_ENABLED = True
EMS_BASE_URL = 'https://ems.lahendus.ut.ee/v1'
AAS_BASE_URL = 'https://aas.lahendus.ut.ee/v1'


def get_required_headers():
    access_token = get_file_content('access_token').strip()
    return {'Authorization': 'Bearer ' + access_token}


def get_file_content(file_name):
    with open(file_name, encoding='utf-8') as f:
        return f.read()


def get_optional_file_content(file_name):
    if file_name is None:
        return None
    return get_file_content(file_name)


def write_restricted_file(file_name, file_content):
    with open(os.open(file_name, os.O_CREAT | os.O_WRONLY, 0o600), 'w') as f:
        f.write(file_content)


def debug(msg):
    if DEBUG_ENABLED:
        print(msg)

def warn(msg):
    if WARN_ENABLED:
        print(msg)
