from flask_sqlalchemy import SQLAlchemy
from app import app
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow(app)
class InfoModel(db.Model):
    __tablename__ = 'info_table'

    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String())
    password = db.Column(db.Integer())

    def __init__(self, username,password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"{self.username}:{self.password}"


class InfoModelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = InfoModel