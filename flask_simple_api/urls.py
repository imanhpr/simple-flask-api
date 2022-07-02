from flask import Blueprint

import flask_simple_api.views as vs

from .constant import API

urls_bl = Blueprint("urls", __name__)

API.add_resource(vs.CelebrityView, "/celebrity")
API.add_resource(vs.QuoteView, "/quote")
