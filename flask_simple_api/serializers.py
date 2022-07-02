from flask_restful import fields
from flask_restful.reqparse import RequestParser

############################################ Ouput Data ############################################
_quote_fields = {
    "id": fields.Integer,
    "text": fields.String,
    "translate": fields.String,
}

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

####################################################################################################
############################################## Parser ##############################################
celebrity_parser = RequestParser(bundle_errors=True)
celebrity_parser.add_argument("name", required=True, help="Name can not be blank!")
####################################################################################################
