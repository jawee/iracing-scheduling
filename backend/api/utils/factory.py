import logging
import sys
from flask import Flask
from flask import jsonify
from api.utils.database import db, migrate, ma
from api.utils.responses import response_with
import api.utils.responses as resp
from api.routes.routes_drivers import route_path_drivers
from flask_sqlalchemy import SQLAlchemy

def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)

    app.register_blueprint(route_path_drivers)

    # START GLOBAL HTTP CONFIGURATIONS
    @app.after_request
    def add_header(response):
        return response

    @app.errorhandler(400)
    def bad_request(e):
        logging.error(e)
        return response_with(resp.BAD_REQUEST_400)

    @app.errorhandler(500)
    def server_error(e):
        logging.error(e)
        return response_with(resp.SERVER_ERROR_500)

    @app.errorhandler(404)
    def not_found(e):
        logging.error(e)
        return response_with(resp.NOT_FOUND_HANDLER_404)

    # END GLOBAL HTTP CONFIGURATIONS

    db.init_app(app)
    #with app.app_context():
        # from api.models import *
    #    db.create_all()

    logging.basicConfig(stream=sys.stdout,
                        format='%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s',
                        level=logging.DEBUG)

    migrate.init_app(app, db)
    ma.init_app(app)
    return app