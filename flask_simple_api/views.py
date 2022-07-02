from flask_restful import Resource, marshal_with

from .constant import DB as db
from .models import Celebrity, Quote
from .serializers import celebrity_fields, celebrity_parser, quote_fields


class CelebrityView(Resource):
    @marshal_with(celebrity_fields, envelope="celebrities")
    def get(self) -> list[Celebrity]:
        celebrities = Celebrity.query.all()
        return celebrities

    def post(self):
        data = celebrity_parser.parse_args()
        if Celebrity.query.filter_by(name=data["name"]).first():
            return {
                "message": {"name": "This Celebrity name had already existed."}
            }, 400
        new_celebrity = Celebrity(name=data["name"])
        db.session.add(new_celebrity)
        db.session.commit()
        return new_celebrity.dict(), 201


class QuoteView(Resource):
    @marshal_with(quote_fields, envelope="quotes")
    def get(self):
        return Quote.query.all()
