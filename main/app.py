from flask import Flask, Blueprint, request, render_template, redirect, url_for

from main.extensions import db, migrate
from main.settings import DevSettings
from main.modules.etudiant.models import Etudiant
from flask.cli import with_appcontext
import click
from main.modules import user, etudiant
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
    app.cli.add_command(populate_etudiants)


def register_modules(app):
    for m in MODULES:
        if hasattr(m, 'api'):
            app.register_blueprint(m.api)


@click.command('populate:etudiants')
@with_appcontext
def populate_etudiants():
    etudiants = [
        {
            'name': 'Mounir',
            'matricule': '171736003461',
        },
        {
            'name': 'Assem',
            'matricule': '171835027186',
        },
        {
            'name': 'Djouss',
            'matricule': '1718212121',
        },

    ]
    for etudiant in etudiants:
        Etudiant(form_data=etudiant, commit=True)
    click.echo('Foods successfully populated.')

@main.route('/')
@main.route('/index', methods=['GET', 'POST'])
def index():

    return render_template('insertStudent.html')

# login page for a user to check his speciality
@main.route('/', methods=['GET', 'POST'])
def matricule():
    if request.method =='POST':
        matricule = request.form.get('matricule')
        etudiant = Etudiant.query.filter_by(matricule= matricule).first()
        if etudiant:
            return "user exists"
        else:
            return "vous n'est pas inscrit a wesmk"

    return redirect(url_for('user.index'))









