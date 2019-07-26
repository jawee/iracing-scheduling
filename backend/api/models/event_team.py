from api.utils.database import db, ma
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
#from api.models.model_book import BookSchema

class EventTeam(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Relationship 1:1
    # event
    # car 

    # Relationship N:N
    # EventTeam - Driver