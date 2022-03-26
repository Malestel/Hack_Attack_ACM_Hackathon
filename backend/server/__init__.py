from flask import Flask
from .dbapi import DbApi
from flask_login import LoginManager

login_manager = LoginManager()

db = DbApi()

GET, PUT, POST, DELETE = ('GET',), ('PUT',), ('POST',), ('DELETE',)

app = Flask(__name__)
login_manager.init_app(app)


from . import routes
