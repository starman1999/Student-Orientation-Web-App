from flask import Blueprint, jsonify

from main.modules.product.models import Product

blueprint = Blueprint('product', __name__)


@blueprint.route('/products')
def index():
    products = Product.query.all()
    return jsonify([{
        'id': product.id,
        'name': product.name
    } for product in products])
