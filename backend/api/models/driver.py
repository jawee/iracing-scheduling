from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
#from api.models.model_book import BookSchema

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)

    def __init__(self, name):
        self.name = name

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    
class DriverSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Driver
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    #surname = fields.String(required=True)
    #created = fields.String(dump_only=True)
    #books = fields.Nested(BookSchema, many=True)
    