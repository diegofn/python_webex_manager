#!/usr/bin/env python
# coding: utf-8

import datetime 
import time
import requests
import json

__name__ = 'webex'

class webex():
    def create_webex_meeting (self, title, agenda, starttime, endtime, participants, host):   
        #
        # WebEx API variables
        #
        siteUrl = "ciscobankdemocol.webex.com"
        token   = "YzNhODMxZGEtMzc4YS00ZmM1LTkyYzMtNjllNDA1YmI2MjNkYTI1OTU3MzctMmQ3_PF84_3884150c-f402-4736-b9a2-23685dc8f2b4"
        
        #
        # Create attendee child
        #
        invitees = []
        for participant in participants:
            print(participant)
            invitees.append(dict({  
                "email": participant[0],
                "displayName": participant[0]
            }))

        #
        # Create using Restful API
        #
        create_meeting_request = { "title": title,
            "agenda": agenda,
            "password": "q1w2e3r4",
            "start": starttime.isoformat(),
            "end": endtime.isoformat(),
            "timezone": "America/Bogota",
            "invitees": invitees,
            "hostEmail": host,
            "siteUrl": siteUrl
        }
        print ("create_meeting_request: " + json.dumps(create_meeting_request))
        headers = {"Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }
        web_url = "https://webexapis.com/v1/meetings"
        response = requests.post(web_url, data = json.dumps(create_meeting_request), headers = headers)
        print ("response:" + response.text)

