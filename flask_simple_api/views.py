from flask_restful import Resource, marshal_with

from .models import Celebrity, Quote
from .serializers import celebrity_fields, quote_fields


class CelebrityView(Resource):
    @marshal_with(celebrity_fields, envelope="celebrities")
    def get(self):
        celebrities = Celebrity.query.all()
        return celebrities


class QuoteView(Resource):
    @marshal_with(quote_fields, envelope="quotes")
    def get(self):
        return Quote.query.all()
