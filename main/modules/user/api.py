from flask import Blueprint, jsonify


from main.modules.user.models import User
from main.extensions import db
from main.modules.user.schemas import UserSchema
from main.shared.base_api import BaseAPI

blueprint = Blueprint('user', __name__, url_prefix='/api')


class UserAPI(BaseAPI):
    route_base = 'users'

    model = User
    schema = UserSchema



UserAPI.register(blueprint)
