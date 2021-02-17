from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from instance.settings import DevSettings

db = SQLAlchemy()
migrate = Migrate()

# Blueprint = Sous-App 
# L'app est divisée en plusieurs modules.
# Blueprint User -> la partie du code qui nous permettre à gérer les users.
# Blueprint Product -> // ... les produits.
main = Blueprint('main', __name__)
user = Blueprint('user', __name__)
product = Blueprint('product', __name__)

def create_app(settings=DevSettings):
    app = Flask(__name__)
    # Utiliser la configuration (settings).
    app.config.from_object(settings)
    # On initialise les libraries Python.
    # Init SQLAlchemy.
    db.init_app(app)
    # Init Migrate.
    migrate.init_app(app)
    app.register_blueprint(main)
    app.register_blueprint(user)
    app.register_blueprint(product)
    return app


@main.route('/')
@main.route('/index')
def index():
    return 'First Page, Ici sera notre projet.'

@user.route('/users')
def users():
    # Un code pour récupèrer les liste des users.
    return 'Display users list.'

# http://localhost:5000/products/1/users
@product.route('/products/1/users')
def products_users():
    return 'Display Products users'

