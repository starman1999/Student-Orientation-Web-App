import random

from flask import Flask, Blueprint, request, render_template, redirect, url_for

from main.extensions import db, migrate
from main.settings import DevSettings
from main.data import etudiants, specialities, modules, moyennes  # data to insert in db
# tables
from main.modules.etudiant.models import Moyenne
from main.modules.speciality.models import Speciality
from main.modules.etudiant.models import Module
from main.modules.etudiant.models import Moyenne
from flask.cli import with_appcontext
import click
from main.modules import user, etudiant
import link
from main.modules.user.api import blueprint

MODULES = [user, etudiant]

# TODO: remove this.
main = Blueprint('main', __name__)


def create_app(settings=DevSettings):
    app = Flask(__name__)

    # Utiliser la configuration (settings).
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
    app.cli.add_command(unpopulate_moyennes)


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


# this fuction is to remove data form table (unpopulate)
@click.command('unpopulate:moyennes')
@with_appcontext
def unpopulate_moyennes():

    Moyenne(form_data= None, commit=True)
    click.echo('Moyennes successfully populated.')


# link()


@main.route('/')
@main.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('insertStudent.html')


# login page for a user to check his speciality
@main.route('/', methods=['GET', 'POST'])
def matricule():
    if request.method == 'POST':
        matricule = request.form.get('matricule')
        etudiant = Moyenne.query.filter_by(matricule=matricule).first()
        if etudiant:
            return "user exists........Choisir une spécialité : "
        else:
            return "vous n'est pas inscrit a wesmk"

    return redirect(url_for('/'))
