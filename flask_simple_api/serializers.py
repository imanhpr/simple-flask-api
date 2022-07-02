from flask_restful import fields

_quote_fields = {"id": fields.Integer, "text": fields.String}

_celebrity_fields = {
    "id": fields.Integer,
    "name": fields.String,
}
celebrity_fields = _celebrity_fields | {
    "quotes": fields.List(fields.Nested(_quote_fields))
}
quote_fields = _quote_fields | {
    "celebrity": fields.Nested(_celebrity_fields),
}
