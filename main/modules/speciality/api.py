from flask import Blueprint, jsonify


from main.modules.speciality.models import Speciality
from main.extensions import db
from main.modules.speciality.schemas import SpecialitySchema
from main.shared.base_api import BaseAPI

blueprint = Blueprint('speciality', __name__, url_prefix='/api')


class SpecialityAPI(BaseAPI):
    route_base = 'specialities'

    model = Speciality
    schema = SpecialitySchema



SpecialityAPI.register(blueprint)
