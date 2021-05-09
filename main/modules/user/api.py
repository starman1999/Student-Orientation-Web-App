from flask import Blueprint, jsonify

from main.modules.product.models import Product
from main.modules.user.models import User

blueprint = Blueprint('user', __name__)


@blueprint.route('/users')
def index():
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'email': user.email,
        'password': user.password
    } for user in users])
