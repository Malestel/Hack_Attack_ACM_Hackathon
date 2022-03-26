from .. import app, GET, PUT, POST, DELETE, db
from flask import request, abort, jsonify

BASE = '/api/user'

@app.route(BASE, methods=GET)
@app.route(BASE + '/<id>', methods=GET)
def get_user(id=None):
    users = db.get_user(id)
    return jsonify(users)

@app.route(BASE, methods=POST)
def add_user():

    user = request.json

    user_id = db.create_user(**user)

    ret_payload = dict(
        location=BASE+f'/{user_id}'
    )

    return jsonify(ret_payload), 200
    # if user_id > 0:
    #     return jsonify(ret_payload), 200
    # else:
    #     abort(500, "Error creating user")
        

@app.route(BASE + '/<id>', methods=PUT)
def modify_user():
    pass
