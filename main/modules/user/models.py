from main.extensions import db
from main.shared.base_model import BaseModel, HasCreatedAt, HasUpdatedAt





class User(BaseModel, HasCreatedAt, HasUpdatedAt):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    matricule = db.Column(db.Integer, primary_key=True)



