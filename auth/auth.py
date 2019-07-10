from flask import Flask, request, Response, render_template
import os
import socket
import threading
import webbrowser
import subprocess
import requests

import conf

PORT_RANGE_FIRST = 5100
PORT_RANGE_LAST = 5109

app = Flask(__name__)

port = None
browser_process = None


def write_access_token(access_token):
    with open(os.open('access-token', os.O_CREAT | os.O_WRONLY, 0o600), 'w') as f:
        f.write(access_token)


def write_refresh_token(refresh_token):
    with open(os.open('refresh-token', os.O_CREAT | os.O_WRONLY, 0o600), 'w') as f:
        f.write(refresh_token)


@app.route('/keycloak.json')
def keycloak_conf():
    return render_template("keycloak.json", idp_url=conf.IDP_URL, client_name=conf.IDP_CLIENT_NAME)


@app.route('/login')
def login():
    return render_template("login.html", idp_url=conf.IDP_URL, port=port)


@app.route('/deliver-tokens', methods=['POST'])
def deliver_tokens():
    if request.is_json:
        body = request.get_json()
        write_access_token(body['access_token'])
        write_refresh_token(body['refresh_token'])

        if browser_process is not None:
            print("Terminating")
            browser_process.terminate()
        else:
            print("Browser process is None ???")

        return Response(status=200)

    else:
        return Response(status=400)


def get_free_port():
    for p in range(PORT_RANGE_FIRST, PORT_RANGE_LAST + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind(('127.0.0.1', p))
            sock.close()
            return p
        except OSError:
            # Port already in use?
            pass

    raise OSError("Unable to bind to ports {} - {}".format(PORT_RANGE_FIRST, PORT_RANGE_LAST))


def open_browser(url):
    global browser_process
    browser_name = webbrowser.get().name
    browser_process = subprocess.Popen([browser_name, url],
                                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def refresh_using_refresh() -> bool:
    if not os.path.isfile('refresh-token'):
        return False

    with open('refresh-token') as f:
        refresh_token = f.read()

    token_req_body = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': 'dev.lahendus.ut.ee'
    }

    r = requests.post("https://dev.idp.lahendus.ut.ee/auth/realms/master/protocol/openid-connect/token",
                      data=token_req_body)

    print(r.status_code)

    resp_body = r.json()

    print(resp_body)
    print(resp_body.keys())

    new_access_token = resp_body['access_token']
    new_refresh_token = resp_body['refresh_token']

    return True


def auth():
    global port

    if refresh_using_refresh():
        return

    port = get_free_port()
    url = 'http://127.0.0.1:{}/login'.format(port)

    # Assume the server starts in 1 second
    threading.Timer(1, lambda: open_browser(url)).start()

    app.run(host='127.0.0.1', port=port)


if __name__ == '__main__':
    auth()
