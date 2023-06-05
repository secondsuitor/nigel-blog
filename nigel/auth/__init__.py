from flask import Blueprint

bp = Blueprint('auth', __name__)

from nigel.auth import routes