import requests
import datetime
import json
import os
from slack import WebClient
from slack.errors import SlackApiError
import webhook

day = datetime.date.today().strftime("%m-%d-%Y")

url = 'https://foreupsoftware.com/index.php/api/booking/times'

i = 0
while i <= 4:
    day = datetime.date.today() + datetime.timedelta(days=i)
    payload = {
        'time': 'all'
        ,'date': day
        , 'holes': '9'
        , 'players': '1'
        , 'booking_class': 'false'
        , 'schedule_id': '331'
        , 'specials_only': '0'
        , 'api_key': 'no_limits'
    }
    i += 1

    r = requests.get(url, params=payload)
    if (r.status_code == 200):
        res = r.json()
        if (len(res) > 0):
            post = {
                'text': 'got one - ' + day + ' - https://foreupsoftware.com/index.php/booking/index/18723#/teetimes'
            }
            headers = {
                'Content-type': 'application/json'
            }
            sr = requests.post(webhook.url, headers=headers, data=json.dumps(post))
    else:
        post = {
                'text': 'failing'
            }
        headers = {
            'Content-type': 'application/json'
        }
        sr = requests.post(webhook.url, headers=headers, data=json.dumps(post))