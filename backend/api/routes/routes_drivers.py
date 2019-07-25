from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
#from api.models.model_author import Author, AuthorSchema

route_path_drivers = Blueprint("route_path_drivers", __name__)