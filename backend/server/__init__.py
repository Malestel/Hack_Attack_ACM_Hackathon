from flask import Flask

GET, PUT, POST, DELETE = ('GET',), ('PUT',), ('POST',), ('DELETE',)

app = Flask(__name__)

from . import appointment, user, volunteer
