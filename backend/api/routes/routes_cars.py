from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.car import Car, CarSchema

route_path_cars = Blueprint("route_path_cars", __name__)


# Get Cars
@route_path_cars.route('/cars', methods=['GET'])
def get_cars():
    fetched = Car.query.all()
    car_schema = CarSchema(many=True)
    cars, error = car_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"cars": cars})


# Get Car by id
@route_path_cars.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    fetched = Car.query.filter_by(id=car_id).first()
    car_schema = CarSchema()
    car, error = car_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"car": car})

# Create car
@route_path_cars.route('/cars', methods=['POST'])
def create_car():
    try:
        data = request.get_json()
        car_schema = CarSchema()
        car, error = car_schema.load(data)
        result = car_schema.dump(car.create()).data
        return response_with(resp.SUCCESS_200, value={"car": result})
    except Exception:
        return response_with(resp.INVALID_INPUT_422)

#Update car
@route_path_cars.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    try:
        data = request.get_json()
        car_schema = CarSchema()
        car, error = car_schema.load(data, instance=Car.query.get(car_id), partial=True)
        result = car_schema.dump(car.update()).data
        if error:
            return response_with(resp.INVALID_INPUT_422)
        return response_with(resp.SUCCESS_200, value={"car": result})
    except Exception:
        response_with(resp.INVALID_INPUT_422)

#Delete car
@route_path_cars.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    fetched = Car.query.filter_by(id=car_id).first()
    car_schema = CarSchema()
    result = car_schema.dump(fetched.delete()).data
    return response_with(resp.SUCCESS_200, value={"car": result})
