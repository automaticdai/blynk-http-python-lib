# blynk_http.py
# A python library for comunicating with Blynk that uses RESTful APIs.
# http://docs.blynkapi.apiary.io/

import requests

base_url = 'http://blynk-cloud.com/'
auth_token = ''

def init(token):
    global auth_token
    auth_token = token
    report(auth_token)


def report(msg):
    print('>>blynk ', end='')
    print(msg)


def write(pin, value):
    if ~isinstance(pin, str):
        #report('error: pin must be a string');
        #return
        pass
    url = base_url + auth_token + '/update/' + pin + '?value=' + value
    report('url: ' + url)

    response = requests.get(url)
    report(response)


def read(pin):
    url = base_url + auth_token + '/get/' + pin
    response = requests.get(url)
    report(response.text)
