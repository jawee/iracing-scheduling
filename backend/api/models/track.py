from api.utils.database import db, ma
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
#from api.models.model_book import BookSchema

class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)




class TrackSchema(ma.ModelSchema):
    class Meta(ma.ModelSchema.Meta):
        model = Track
        sqla_session = db.session

    id = fields.Number()
    name = fields.String()
    