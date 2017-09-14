# blynk_http.py
# A python library for communicating with Blynk that uses RESTful APIs.
# http://docs.blynkapi.apiary.io/

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


def report(msg):
    if opt_report_on:
        print('<blynk> info: ', end='')
        print(msg)


def report_err(err_msg):
    if opt_report_err_on:
        print('<blynk> error: ', end='')
        print(err_msg)


def write(pin, value):
    if ~isinstance(pin, str):
        #report_err('pin must be a string');
        #return
        pass
    url = base_url + auth_token + '/update/' + pin + '?value=' + value
    response = requests.get(url)
    report(response)


def read(pin):
    url = base_url + auth_token + '/get/' + pin
    response = requests.get(url)
    report(response.text)


def read_history(pin):
    pass


def set_property(pin, property_name, property_val):
    pass


def send_notification(notify_msg):
    url = base_url + auth_token + '/notify'
    payload = {'body': notify_msg}
    response = requests.post(url, json=payload)
    report(response)


def set_email_address(addr):
    global email_address
    email_address = addr


def send_email(email_payload):
    if email_address == ' ':
        report_err("destination email address is empty. Use set_email_address('your_email') first!")
        return

    url = base_url + auth_token + '/email'
    payload = {'to': email_address, 'subj': 'Blynk Notification', 'title': email_payload}
    response = requests.post(url, json=payload)
    report(response)


def get_project_details():
    url = base_url + auth_token + '/project'
    response = requests.get(url)
    report(response.text)
    return
