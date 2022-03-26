from .. import login_manager, app, GET, PUT, POST, DELETE
from flask import session, request, abort, jsonify
from ..user import User
from flask_login import login_user

BASE = '/login'

@app.route(BASE, methods=POST)
def login_route():
    info = request.json
    phone_num = info['Phone_Number']
    
    user = User.get(phone_num)

    if user:
        login_user(user)
        return jsonify(user)
    else:
        abort(401, "Invalid phone number.")

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


