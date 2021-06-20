from flask import Blueprint, jsonify
from main.modules.speciality.models import Speciality

blueprint = Blueprint('speciality', __name__)







@blueprint.route('/specialities')
def index():
    specialities = Speciality.query.all()
    return jsonify([{
        'id': speciality.id,
        'name': speciality.name
    } for speciality in specialities])
