from . import app, GET, PUT, POST, DELETE
from flask import request, abort, jsonify

BASE = '/api/appointment'

@app.route(BASE, methods=GET)
@app.route(BASE + '/<id>')
def get_appointment(id=None):
    # GET APPOINTMENTS FROM DATABASE
    # if id_not_found:
    #     return "Unknown appointment", 404
    appointments = []
    return appointments, 200

@app.route(BASE, methods=POST)
def new_appointment():
    # CREATE APPOINTMENT IN DATABASE

    # if time_conflict:
    #     return "Time not available", 405

    ret_payload = dict(
        location=BASE+f'/{id}'
    )
    return ret_payload, 200

@app.route(BASE + '/<id>', methods=PUT)
def update_appointment(id):
    # UPDATE APPOINTMENT IN DATABASE
    # if id_not_found:
    #     return "Unknown appointment", 404

    ret_payload = dict(
        location=BASE+f'/{id}'
    )
    return ret_payload, 200

@app.route(BASE + '/<id>', methods=DELETE)
def delete_appointment(id):
    # DELETE APPOINTMENT IN DATABASE
    # if id_not_found:
    #     return "Unknown appointment", 404
    
    return "OK", 200