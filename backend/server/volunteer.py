from flask import request, abort, jsonify
from . import app, GET, PUT, POST, DELETE
from .dbapi import DbApi

BASE = '/api/volunteer'


@app.route(BASE, methods=GET)
@app.route(BASE + '/<id>', methods=GET)
def get_Volunteer(id=None):
    # GET Volunteer FROM DATABASE
    VolunteerGrab = DbApi()
    volunteers = VolunteerGrab.get_volunteer(id)
    # if id_not_found:
    #     abort(404, "Appointment not found")

    return jsonify(volunteers), 200


@app.route(BASE, methods=POST)
def new_volunteer():
    # CREATE VOLUNTEER IN DATABASE

    # if time_conflict:
    #     abort(405, "Time not available")
    appt = request.json

    ret_payload = dict(
        location=BASE + f'/{id}'
    )
    return jsonify(ret_payload), 200


@app.route(BASE + '/<id>', methods=PUT)
def update_volunteer(id):
    # UPDATE VOLUNTEER IN DATABASE
    # if id_not_found:
    #     abort(404, "Volunteer not found")

    ret_payload = dict(
        location=BASE + f'/{id}'
    )
    return jsonify(ret_payload), 200


@app.route(BASE + '/<id>', methods=DELETE)
def delete_volunteer(id):
    # DELETE VOLUNTEER IN DATABASE
    # if id_not_found:
    #     abort(404, "Volunteer not found")

    return
