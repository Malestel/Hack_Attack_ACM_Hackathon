from flask import Flask
from .dbapi import DbApi
from flask_login import LoginManager
from flask_cors import CORS

GET, PUT, POST, DELETE = ('GET',), ('PUT',), ('POST',), ('DELETE',)

db = DbApi()

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.secret_key = b'4e621bd9807f0aa91af391157b6c12572cb5ff2255244f6cb74cb96f1d107d21'

login_manager = LoginManager()
login_manager.init_app(app)


from . import routes
