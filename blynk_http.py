# ------------------------------------------------------------------------------
# blynk_http.py
# Author: Xiaotian Dai
# Published: Sep, 2017
# Version: v1.0
# Notes:
#   A python library for updating Blynk widgets with RESTful APIs.
#   See reference: http://docs.blynkapi.apiary.io/
# ------------------------------------------------------------------------------

import requests

base_url = 'http://blynk-cloud.com/'

auth_token = ' '
email_address = ' '

opt_report_on = True
opt_report_err_on = True


def init(token):
    global auth_token
    auth_token = token
    report('initialized with token: ' + auth_token)


def set_email_address(addr):
    global email_address
    email_address = addr


def report(msg):
    if opt_report_on == True:
        print('<blynk> info: ', end='')
        print(msg)


def report_error(err_msg):
    if opt_report_err_on == True:
        print('<blynk> error: ', end='')
        print(err_msg)


def write(pin, value):
    if ~isinstance(pin, str):
        #report_err('pin must be a string');
        #return
        pass
    url = base_url + auth_token + '/update/' + pin + '?value=' + value
    response = requests.get(url)
    if (response.status_code == requests.codes.ok):
        report('write pin ok')
    else:
        report_error('write pin failed')


def read(pin):
    url = base_url + auth_token + '/get/' + pin
    response = requests.get(url)
    report('read pin:' + response.text)
    return response.text


def read_history(pin):
    pass


def set_property(pin, property_name, property_val):
    pass


def send_notification(notify_msg):
    url = base_url + auth_token + '/notify'
    payload = {'body': notify_msg}
    response = requests.post(url, json=payload)
    report(response.status_code)


def send_email(email_payload):
    if email_address == ' ':
        report_error("destination email address is empty. Use set_email_address('your_email') first!")
        return

    url = base_url + auth_token + '/email'
    payload = {'to': email_address, 'subj': 'Blynk Notification', 'title': email_payload}
    response = requests.post(url, json=payload)
    report(response.status_code)


def get_project_property():
    url = base_url + auth_token + '/project'
    response = requests.get(url)
    report(response.text)
    return
