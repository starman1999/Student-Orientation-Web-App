from main.extensions import db
from main.shared.base_model import BaseModel, HasCreatedAt, HasUpdatedAt





class User(BaseModel, HasCreatedAt, HasUpdatedAt):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    matricule = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    phone = db.Column(db.String)
    confirmed_at = db.Column(db.DateTime)
