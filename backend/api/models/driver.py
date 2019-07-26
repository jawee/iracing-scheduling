from api.utils.database import db, ma
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
#from api.models.model_book import BookSchema

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def __init__(self, name):
        self.name = name

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self
    def update(self):
        db.session.add(self)
        db.session.commit()
        return self

    
class DriverSchema(ma.ModelSchema):
    class Meta(ma.ModelSchema.Meta):
        model = Driver
        sqla_session = db.session

    id = fields.Number()
    name = fields.String()
    