from flask import Blueprint

from .constant import DB as db

models_bl = Blueprint("models", __name__)


class Celebrity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    quotes = db.relationship("Quote", backref="celebrity", lazy=True)


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), unique=True, nullable=False)
    celebrity_id = db.Column(db.Integer, db.ForeignKey("celebrity.id"), nullable=False)
