from flask import Blueprint
models_bp = Blueprint('models', __name__)

from . import data_types, website, page, data_item
