from flask import Blueprint

noticias_bp = Blueprint("noticias", __name__)

from . import routes 