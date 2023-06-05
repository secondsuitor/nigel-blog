from flask import Blueprint

bp = Blueprint('main', __name__)

from nigel.main import routes