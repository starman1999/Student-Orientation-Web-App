from main.extensions import db
from main.shared.base_model import BaseModel


class Speciality(BaseModel):

    __tablename__ = 'specialities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    def __init__(self, form_data=None, commit=False, *args, **kwargs):
        if form_data:
            modules_data = form_data.pop('module', None)
        super().__init__(form_data, commit, *args, **kwargs)

    def update(self, form_data=None, commit=False, **kwargs):
        if form_data:
            modules_data = form_data.pop('module', None)
        super().update(form_data, commit, **kwargs)