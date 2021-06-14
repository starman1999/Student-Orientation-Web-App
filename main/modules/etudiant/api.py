from flask import Blueprint, jsonify

from main.modules.etudiant.models import Etudiant

blueprint = Blueprint('etudiant', __name__)


@blueprint.route('/etudiants')
def index():
    etudiants = Etudiant.query.all()
    return jsonify([{
        'id': etudiant.id,
        'name': etudiant.name
    } for etudiant in etudiants])
