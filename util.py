import os
import json
import time

import conf
import auth


def get_token_header():
    # TODO: refactor if you're feeling lucky
    access_token_file = None
    expires_at = 0

    if os.path.isfile('access_token'):
        access_token_file = json.loads(get_file_content('access_token').strip())
        expires_at = access_token_file['expires_at']

    if access_token_file is None or time.time() > expires_at + conf.AUTH_TOKEN_MIN_VALID_SEC:
        auth.auth()

        if os.path.isfile('access_token'):
            access_token_file = json.loads(get_file_content('access_token').strip())
            expires_at = access_token_file['expires_at']

        if access_token_file is None or time.time() > expires_at + conf.AUTH_TOKEN_MIN_VALID_SEC:
            raise RuntimeError("Could not get/refresh tokens")

    return {'Authorization': 'Bearer ' + access_token_file['access_token']}


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
    if conf.DEBUG_ENABLED:
        print(msg)


def warn(msg):
    if conf.WARN_ENABLED:
        print(msg)
