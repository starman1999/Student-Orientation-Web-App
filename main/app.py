import click
import numpy as np
from flask import Flask, Blueprint, request, render_template, redirect, url_for, json
from flask.cli import with_appcontext
from flask_marshmallow import fields
from sqlalchemy import select
from sqlalchemy.orm import load_only, defer, undefer, session

from main import Model

from main.data import etudiants, specialities, modules, moyennes  # data to insert in db
from main.extensions import db, migrate, cors
from main.modules import user, etudiant, speciality, moyenne, module
from main.modules.etudiant.Schemas import MoyenneSchema
from main.modules.etudiant.models import Module, Etudiant
from main.modules.etudiant.models import Moyenne
from main.modules.speciality.models import Speciality
from main.settings import DevSettings
from flask import jsonify

# tables

MODULES = [user, etudiant, speciality, moyenne, module]

# TODO: remove this.
main = Blueprint('main', __name__)


def create_app(settings=DevSettings):
    app = Flask(__name__)

    # CORS(app, resources={r"/api/*": {"origins": "*"}})

    cors.init_app(app)
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


@click.command('populate:module')
@with_appcontext
def populate_modules():
    for module in modules:
        Module(form_data=module, commit=True)
    click.echo('module successfully populated.')


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
        result = []
        if student:  # student exists



            #get only the attribute "moyennes"
            moy = Moyenne.query.with_entities(Moyenne.moyenne).filter_by(etudiant_id=student.id).all()



            # moy = moy.options(defer('etudiant_id'), defer('module_id'),undefer('moyenne'))

            #print(moy[0][0])
            for e in moy:
                result.append(e[0])
            print(result)  # moyennes filtered t3 one student brk

            moyenneschema = MoyenneSchema(many=True)
            output = moyenneschema.dump(moy) # serialize data

            y = Model.classifier.predict_proba([result])
            print("les proba kaml", y)
            lists = y.tolist()
            json_str = json.dumps(lists)

            return  json_str
        else:
            return 'false'

    return redirect(url_for('/'))
