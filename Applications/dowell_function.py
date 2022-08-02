import requests
import json
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
        "status": "work",
        "data_type": "learn",
        "purpose_of_usage": "add",
        "colour": "color value",
        "hashtags": "hash tag alue",
        "mentions": "mentions value",
        "emojis": "emojis",

    }

    r = requests.post(url, json=data)
    return r.text


def get_dowellclock():
    response_dowell = requests.get(
        'https://100009.pythonanywhere.com/dowellclock')
    data = response_dowell.json()
    return data['t1']


def save_candidate(request, candidate):
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


# testing data
def targeted_population(database, collection, fields, period):
    url = 'http://100032.pythonanywhere.com/api/targeted_population/'
    database_details = {
        'database_name': 'mongodb',
        'collection': collection,
        'database': database,
        'fields': fields
    }
    # number of variables for sampling rule
    number_of_variables = -1
    time_input = {
        'column_name': 'Date',
        'split': 'week',
        'period': period,
        'start_point': '2021/01/08',
        'end_point': '2021/01/25',
    }
    stage_input_list = [
    ]
    # distribution input
    distribution_input = {
        'normal': 1,
        'poisson': 0,
        'binomial': 0,
        'bernoulli': 0

    }
    request_data = {
        'database_details': database_details,
        'distribution_input': distribution_input,
        'number_of_variable': number_of_variables,
        'stages': stage_input_list,
        'time_input': time_input,
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, json=request_data, headers=headers)
    return response.text


response = targeted_population('hr_hiring', 'dowelltraining',  [
                               'full_name'], 'life_time')
print(response)