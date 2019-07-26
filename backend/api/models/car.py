from api.utils.database import db, ma
from marshmallow import fields
#from api.models.model_book import BookSchema

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    