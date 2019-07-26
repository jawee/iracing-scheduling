from api.utils.database import db, ma
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
#from api.models.model_book import BookSchema
from models.track import Track

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    
    #Relationships 1:1
    # track
    track = db.Column(db.Integer, db.ForeignKey('track.id'))

    # Relationships N:N


class EventSchema(ma.ModelSchema):
    class Meta(ma.ModelSchema.Meta):
        model = Event
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    books = fields.Nested(BookSchema, many=True)