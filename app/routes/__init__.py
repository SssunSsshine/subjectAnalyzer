from flask import Blueprint
routes_bp = Blueprint('routes', __name__)

from . import main_route, about_route, websites_route
