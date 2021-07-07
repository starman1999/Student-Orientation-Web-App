from flask import Blueprint, jsonify


from main.modules.etudiant.models import Module
from main.extensions import db
from main.modules.etudiant.Schemas import ModuleSchema
from main.shared.base_api import BaseAPI

blueprint = Blueprint('module', __name__, url_prefix='/api')


class ModuleAPI(BaseAPI):
    route_base = 'modules'

    model = Module
    schema = ModuleSchema


ModuleAPI.register(blueprint)
