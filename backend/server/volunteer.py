from flask import request, abort, jsonify
from . import app, GET, PUT, POST, DELETE, db

BASE = '/api/volunteer'


@app.route(BASE, methods=GET)
@app.route(BASE + '/<id>', methods=GET)
def get_Volunteer(id=None):
    # GET Volunteer FROM DATABASE
    volunteers = db.get_volunteer(id)

    return jsonify(volunteers), 200


@app.route(BASE, methods=POST)
def new_volunteer():
    # CREATE VOLUNTEER IN DATABASE

    # if time_conflict:
    #     abort(405, "Time not available")
    appt = request.json

    result = db.create_volunteer(**appt)

    ret_payload = dict(
        location=BASE + f'/{result}'
    )
    if result > 0:
        return jsonify(ret_payload), 200
    else:
        abort(500, "Error creating volunteer")


@app.route(BASE + '/<vol_id>', methods=PUT)
def update_volunteer(vol_id):

    vol = request.json

    result = db.update_volunteer(vol_id, **vol)

    ret_payload = dict(
        location=BASE + f'/{vol_id}'
    )
    return jsonify(ret_payload), 200


@app.route(BASE + '/<id>', methods=DELETE)
def delete_volunteer(id):
    # DELETE VOLUNTEER IN DATABASE
    # if id_not_found:
    #     abort(404, "Volunteer not found")

    return
