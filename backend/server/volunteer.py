from flask import request, abort, jsonify
from . import app, GET, PUT, POST, DELETE
from .dbapi import DbApi

BASE = '/api/volunteer'


@app.route(BASE, methods=GET)
@app.route(BASE + '/<id>')
def get_Volunteer(id=1):
    # GET Volunteer FROM DATABASE
    VolunteerGrab = DbApi()
    volunteers = VolunteerGrab.get_volunteer()
    # if id_not_found:
    #     abort(404, "Appointment not found")

    return jsonify(volunteers), 200


def Get_User(id=None):
    # GET Volunteer FROM DATABASE
    Users = DbApi()
    MyUsers = Users.get_user()

    # if id_not_found:
    #     abort(404, "Appointment not found")
    user = MyUsers
    return jsonify(get_Volunteer), 200


@app.route(BASE, methods=POST)
def new_appointment():
    # CREATE APPOINTMENT IN DATABASE

    # if time_conflict:
    #     abort(405, "Time not available")

    appt = request.json

    ret_payload = dict(
        location=BASE + f'/{id}'
    )
    return jsonify(ret_payload), 200


# @app.route(BASE + '/<id>', methods=PUT)
# def set_appointments(id):
#     # Set Appointments
#
#     ret_payload = dict(
#         location=BASE + f'/{id}'
#     )
#     return jsonify(ret_payload), 200


@app.route(BASE + '/<id>', methods=PUT)
def update_appointments(id):
    # UPDATE APPOINTMENT IN DATABASE
    # if id_not_found:
    #     abort(404, "Appointment not found")

    ret_payload = dict(
        location=BASE + f'/{id}'
    )
    return jsonify(ret_payload), 200


@app.route(BASE + '/<id>', methods=DELETE)
def delete_appointment(id):
    # DELETE APPOINTMENT IN DATABASE
    # if id_not_found:
    #     abort(404, "Appointment not found")

    return
