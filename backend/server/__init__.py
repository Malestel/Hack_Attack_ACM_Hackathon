from flask import Flask
from .dbapi import DbApi

db = DbApi()

GET, PUT, POST, DELETE = ('GET',), ('PUT',), ('POST',), ('DELETE',)

app = Flask(__name__)

from . import appointment, user, volunteer
