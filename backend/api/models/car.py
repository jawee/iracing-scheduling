from api.utils.database import db, ma
from marshmallow import fields
#from api.models.model_book import BookSchema

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)

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

    
class CarSchema(ma.ModelSchema):
    class Meta(ma.ModelSchema.Meta):
        model = Car
        sqla_session = db.session

    id = fields.Number()
    name = fields.String()
    