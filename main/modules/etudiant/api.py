from flask import Blueprint, request, redirect, url_for
from main.extensions import db

from main.modules.etudiant.models import Etudiant

blueprint = Blueprint('etudiant', __name__)


# @blueprint.route('/', methods=['POST'])
# def index():
#     if request.form == ['POST']:
#         name = request.form['name']
#         matricule = request.form['matricule']
#
#         my_data = Etudiant(name, matricule)
#         db.session.add(my_data)
#         db.session.commit()
#
#         return redirect(url_for('etudiants'))
#
#     # etudiants = Etudiant.query.all()
#     # return jsonify([{
#     #     'id': etudiant.id,
#     #     'name': etudiant.name
#     # } for etudiant in etudiants])
