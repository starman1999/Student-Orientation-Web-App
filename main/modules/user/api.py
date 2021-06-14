from flask import Blueprint, jsonify

from main.modules.etudiant.models import Etudiant
from main.modules.user.models import User
from main.extensions import db

blueprint = Blueprint('user', __name__)


@blueprint.route('/users')
def index():

    users = User.query.all()
    return jsonify([{

        'matricule': user.matricule
     } for user in users])


