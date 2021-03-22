#!/usr/bin/env python
# coding: utf-8

#
# Webhook flask
#
from flask import Flask, request, abort, jsonify

import datetime 
import time
import requests
import json
import webex

app = Flask(__name__)

#def query_schedule_room():
    #for schedule_room in room_cursor.fetchall():
    #    participant_cursor.execute('SELECT pr.Email FROM ParticipantesReserva pr WHERE pr.idReservaSala = ' + str(schedule_room[0]))

        #
        # Define starttime
        #  
    #    print(schedule_room)

    #    starttime   = datetime.datetime.strptime(schedule_room[2] + " " + schedule_room[3][:-1], '%Y-%m-%d %H:%M:%S.%f')
    #    endtime     = datetime.datetime.strptime(schedule_room[2] + " " + schedule_room[4][:-1], '%Y-%m-%d %H:%M:%S.%f')
    #    print("starttime: " + starttime.strftime("%m/%d/%Y %H:%M:%S"))
    #    print("endtime: " + endtime.strftime("%m/%d/%Y %H:%M:%S"))
        
    #    create_webex_meeting (schedule_room[5], schedule_room[6], starttime, endtime, participant_cursor, schedule_room[7])

        #
        # Update the Schedule_room
        #
    #    room_update_cursor.execute('UPDATE ReservasSala SET Estado = 1 WHERE idReservaSala = ' + str(schedule_room[0]))
    #    connection.commit()

#
# Calendly endpoint
#
@app.route('/webex_calendly', methods=['POST'])
def get_square():
    if not request.json or 'number' not in request.json:
        abort(400)
    num = request.json['number']

    return jsonify({'answer': num ** 2})

#
# Main function
#
if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = 8080, debug = True)   

