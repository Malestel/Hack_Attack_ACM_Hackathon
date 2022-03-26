from . import app, GET, PUT, POST, DELETE
from flask import request, abort, jsonify

BASE = '/api/user'

@app.route(BASE, methods=GET)
@app.route(BASE + '/<id>', methods=GET)
def get_user(id=None):
    pass

@app.route(BASE, methods=POST)
def add_user():
    pass

@app.route(BASE + '/<id>', methods=PUT)
def modify_user():
    pass
