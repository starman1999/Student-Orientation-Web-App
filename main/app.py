from flask import Flask, Blueprint

from main.extensions import db, migrate
from main.settings import DevSettings

from main.modules import user, product

MODULES = [user, product]

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
    return app


def register_modules(app):
    for m in MODULES:
        if hasattr(m, 'api'):
            app.register_blueprint(m.api)


@main.route('/')
@main.route('/index')
def index():
    return 'First Page, Ici sera notre projet.'
