from . import app, GET, PUT, POST, DELETE, db
from flask import request, abort, jsonify

BASE = '/api/appointment'

@app.route(BASE, methods=GET)
@app.route(BASE + '/<id>', methods=GET)
def get_appointment(id=None):
    appointments = db.get_appointment(id)
    return jsonify(appointments), 200

@app.route(BASE, methods=POST)
def new_appointment():

    appt = request.json

    appt_id = db.create_apppointment(**appt)

    ret_payload = dict(
        location=BASE+f'/{appt_id}'
    )

    if appt_id > 0:
        return jsonify(ret_payload), 200
    else:
        abort(500, "Error creating appointment")

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