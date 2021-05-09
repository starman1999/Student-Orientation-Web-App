from main.extensions import db
from main.shared.base_model import BaseModel, HasCreatedAt, HasUpdatedAt


class Product(BaseModel, HasCreatedAt, HasUpdatedAt):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
