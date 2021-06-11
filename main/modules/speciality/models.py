from main.extensions import db
from main.shared.base_model import BaseModel, HasCreatedAt, HasUpdatedAt
class Speciality(BaseModel, HasCreatedAt, HasUpdatedAt):

    __tablename__ = 'spécialités'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
