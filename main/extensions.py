from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
cors = CORS()
ma = Marshmallow()
migrate = Migrate(compare_type=True) # c pour appliquer des changements 3la la base de données
