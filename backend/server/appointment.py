from . import app, GET, PUT, POST, DELETE
from flask import request, abort, jsonify

BASE = '/api/appointment'

@app.route(BASE, methods=GET)
@app.route(BASE + '/<id>', methods=GET)
def get_appointment(id=None):
    # GET APPOINTMENTS FROM DATABASE
    # if id_not_found:
    #     abort(404, "Appointment not found")
    appointments = []
    return jsonify(appointments), 200

@app.route(BASE, methods=POST)
def new_appointment():
    # CREATE APPOINTMENT IN DATABASE

    # if time_conflict:
    #     abort(405, "Time not available")

    appt = request.json

    ret_payload = dict(
        location=BASE+f'/{id}'
    )
    return jsonify(ret_payload), 200

@app.route(BASE + '/<id>', methods=PUT)
def update_appointment(id):
    # UPDATE APPOINTMENT IN DATABASE
    # if id_not_found:
    #     abort(404, "Appointment not found")

    ret_payload = dict(
        location=BASE+f'/{id}'
    )
    return jsonify(ret_payload), 200

@app.route(BASE + '/<id>', methods=DELETE)
def delete_appointment(id):
    # DELETE APPOINTMENT IN DATABASE
    # if id_not_found:
    #     abort(404, "Appointment not found")
    
    return "OK", 200