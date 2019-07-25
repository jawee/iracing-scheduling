from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
#from api.models.model_book import BookSchema

class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)




class TrackSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Track
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    