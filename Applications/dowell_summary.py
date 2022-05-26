import json
import requests
from datetime import datetime


def get_event_id():
    dd = datetime.now()
    time = dd.strftime("%d:%m:%Y,%H:%M:%S")
    url = "https://100003.pythonanywhere.com/event_creation"
    data = {
        "platformcode": "FB",
        "citycode": "101",
        "daycode": "0",
        "dbcode": "pfm",
        "ip_address": "192.168.0.41",
        "login_id": "lav",
        "session_id": "new",
        "processcode": "1",
        "regional_time": time,
        "dowell_time": time,
        "location": "22446576",
        "objectcode": "1",
        "instancecode": "100051",
        "context": "afdafa ",
        "document_id": "3004",
        "rules": "some rules",
        "status": "work"
    }

    r = requests.post(url, json=data)
    return r.text


def get_dowellclock():
    response_dowell = requests.get(
        'https://100009.pythonanywhere.com/dowellclock')
    data = response_dowell.json()
    return data['t1']


def save_jobs_entries(applications):
    url = "http://100002.pythonanywhere.com/"
    #   searchstring="ObjectId"+"("+"'"+"6139bd4969b0c91866e40551"+"'"+")"

    event_id = get_event_id()
    dowelltime = get_dowellclock()
    print("EVENT_ID", event_id)
    print("DOWELLTIME", dowelltime)
    payload = json.dumps({
        "cluster": "hr_hiring",
        "database": "hr_hiring",
        "collection": "hr_view",
        "document": "hr_view",
        "team_member_ID": "4646111",
        "function_ID": "ABCDE",
        "command": "insert",
        "field": {
            'event_id': event_id,
            'dowelltime': dowelltime,
        },
        "update_field": {
            "order_nos": 21
        },

        "platform": "bangalore"
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text


def save_job_application_entries(jobapplication):
    url = "http://100002.pythonanywhere.com/"
    #   searchstring="ObjectId"+"("+"'"+"6139bd4969b0c91866e40551"+"'"+")"

    event_id = get_event_id()
    dowelltime = get_dowellclock()

    payload = json.dumps({
        "cluster": "hr_hiring",
        "database": "hr_hiring",
        "collection": "accounts_view",
        "document": "accounts_view",
        "team_member_ID": "1000551",
        "function_ID": "ABCDE",
        "command": "insert",
        "field": {
            'event_id': event_id,
            'dowelltime': dowelltime,
            'created_by': jobapplication.applicant
        },
        "update_field": {
            "order_nos": 21
        },

        "platform": "bangalore"
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text
