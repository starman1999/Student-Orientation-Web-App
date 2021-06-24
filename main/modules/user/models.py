from main.extensions import db
from main.shared.base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    matricule = db.Column(db.String, primary_key=True)



