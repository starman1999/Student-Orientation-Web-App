from main.extensions import db
from main.shared.base_model import BaseModel


class Speciality(BaseModel):

    __tablename__ = 'specialities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True,nullable=False)
