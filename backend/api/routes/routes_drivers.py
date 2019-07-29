from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.driver import Driver, DriverSchema

route_path_drivers = Blueprint("route_path_drivers", __name__)


# Get Drivers
@route_path_drivers.route('/drivers', methods=['GET'])
def get_drivers():
    fetched = Driver.query.all()
    driver_schema = DriverSchema(many=True)
    drivers, error = driver_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"drivers": drivers})


# Get Driver by id
@route_path_drivers.route('/drivers/<int:driver_id>', methods=['GET'])
def get_driver(driver_id):
    fetched = Driver.query.filter_by(id=driver_id).first()
    driver_schema = DriverSchema()
    driver, error = driver_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"driver": driver})

# Create driver
@route_path_drivers.route('/drivers', methods=['POST'])
def create_driver():
    try:
        data = request.get_json()
        driver_schema = DriverSchema()
        driver, error = driver_schema.load(data)
        result = driver_schema.dump(driver.create()).data
    #return jsonify({'driver': result})
        return response_with(resp.SUCCESS_200, value={"driver": result})
    except Exception:
        return response_with(resp.INVALID_INPUT_422)

#Update driver
@route_path_drivers.route('/drivers/<int:driver_id>', methods=['PUT'])
def update_driver(driver_id):
    try:
        data = request.get_json()
        driver_schema = DriverSchema()
        driver, error = driver_schema.load(data, instance=Driver.query.get(driver_id), partial=True)
        result = driver_schema.dump(driver.update()).data
        if error:
            return response_with(resp.INVALID_INPUT_422)
        return response_with(resp.SUCCESS_200, value={"driver": result})
    except Exception:
        response_with(resp.INVALID_INPUT_422)

#Delete driver
@route_path_drivers.route('/drivers/<int:driver_id>', methods=['DELETE'])
def delete_driver(driver_id):
    fetched = Driver.query.filter_by(id=driver_id).first()
    driver_schema = DriverSchema()
    result = driver_schema.dump(fetched.delete()).data
    return response_with(resp.SUCCESS_200, value={"driver": result})
