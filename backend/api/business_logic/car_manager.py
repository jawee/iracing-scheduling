from api.utils.database import db, ma
from api.models.car import Car, CarSchema
from flask import request

class CarManager:
    def get_cars(self):
        fetched = Car.query.all()
        car_schema = CarSchema(many=True)
        cars, error = car_schema.dump(fetched)
        return cars
    
    def create_car(self, request):
        data = request.get_json()
        car_schema = CarSchema()
        car, error = car_schema.load(data)
        result = car_schema.dump(car.create()).data
        return result
