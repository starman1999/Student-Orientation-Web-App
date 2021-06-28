import click
from flask import Flask, Blueprint, request, render_template, redirect, url_for, Response, jsonify
from flask.cli import with_appcontext
from flask_cors import CORS, cross_origin
from webargs.core import Request

from main.data import etudiants, specialities, modules, moyennes  # data to insert in db
from main.extensions import db, migrate, cors, ma
from main.modules import user, etudiant, speciality
from main.modules.etudiant.models import Module, Etudiant
from main.modules.etudiant.models import Moyenne
from main.modules.speciality.models import Speciality
from main.settings import DevSettings
from main.modules.etudiant.schemas import MoyenneSchema
from flask import jsonify
from pprint import pprint


# tables

MODULES = [user, etudiant, speciality]

# TODO: remove this.
main = Blueprint('main', __name__)


def create_app(settings=DevSettings):
    app = Flask(__name__)
    CORS(app)
    # CORS(app, resources={r"/api/*": {"origins": "*"}})
    cors.init_app(app, resources={r"/api/*": {"origins": "http://localhost:4200/"}})
    # app.config['CORS, HEADERS']= 'Content-Type'

    # Utilise r la configuration (settings).
    app.config.from_object(settings)
    # On initialise les libraries Python.
    # Init SQLAlchemy.
    db.init_app(app)

    # Init Migrate.
    migrate.init_app(app, db)
    app.register_blueprint(main)
    register_modules(app)
    register_shell_context(app)
    register_commands(app)
    return app


def register_shell_context(app):
    def shell_context():
        return {'db': db}

    app.shell_context_processor(shell_context)


def register_commands(app):
    app.cli.add_command(populate_etudiant)
    app.cli.add_command(populate_specialities)
    app.cli.add_command(populate_modules)
    app.cli.add_command(populate_moyennes)


def register_modules(app):
    for m in MODULES:
        if hasattr(m, 'api'):
            app.register_blueprint(m.api)


@click.command('populate:etudiant')
@with_appcontext
def populate_etudiant():
    for etudiant in etudiants:
        Moyenne(form_data=etudiant, commit=True)
    click.echo('students successfully populated.')


@click.command('populate:speciality')
@with_appcontext
def populate_specialities():
    for speciality in specialities:
        Speciality(form_data=speciality, commit=True)
    click.echo('specialities successfully populated.')


@click.command('populate:modules')
@with_appcontext
def populate_modules():
    for module in modules:
        Module(form_data=module, commit=True)
    click.echo('modules successfully populated.')


@click.command('populate:moyennes')
@with_appcontext
def populate_moyennes():
    for moyenne in moyennes:
        Moyenne(form_data=moyenne, commit=True)

    click.echo('Moyennes successfully populated.')


@main.route('/')
@main.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("usercheck.html")


# login page for a user to check his speciality
@main.route('/', methods=['GET', 'POST'])
def matricule():

    if request.method == 'POST':
        matricule = request.form.get('matricule') # get matricule from Form
        student = Etudiant.query.filter_by(matricule=matricule).first()

        if student:  # student exists
            moy = Moyenne.query.filter_by(etudiant_id=student.id).all()  # get 'moyennes' of this student
            moyenneschema = MoyenneSchema(many=True)
            output = moyenneschema.dump(moy)  # serialize data
            return jsonify({'moy01': output})
        else:
            return 'false'

    return redirect(url_for('/'))
