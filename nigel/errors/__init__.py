from flask import Blueprint

bp = Blueprint('errors', __name__)

from nigel.errors import handlers