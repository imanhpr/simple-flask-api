from flask import Blueprint

from .constant import DB as db

models_bl = Blueprint("models", __name__)


class Celebrity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    quotes = db.relationship("Quote", backref="celebrity", lazy=True)

    def dict(self):
        return {"id": self.id, "name": self.name}

    def __str__(self) -> str:
        return self.name


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    translate = db.Column(db.Text, nullable=False)
    celebrity_id = db.Column(db.Integer, db.ForeignKey("celebrity.id"), nullable=False)

    def dict(self):
        return {"id": self.id, "text": self.name , 'translate':self.translate}
    def __str__(self) -> str:
        return self.text
