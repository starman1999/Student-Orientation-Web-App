from flask import Blueprint, jsonify


from main.modules.etudiant.models import Moyenne
from main.extensions import db
from main.modules.etudiant.Schemas import MoyenneSchema
from main.shared.base_api import BaseAPI

blueprint = Blueprint('moyenne', __name__, url_prefix='/api')


class ModuleAPI(BaseAPI):
    route_base = 'moyennes'

    model = Moyenne
    schema = MoyenneSchema


ModuleAPI.register(blueprint)
