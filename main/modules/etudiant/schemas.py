from flask import request
from marshmallow import fields, pre_load

from main.extensions import ma
from main.modules.etudiant.models import Etudiant


class StudentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Etudiant

    name = fields.Str()
    matricule = fields.Str()





    @pre_load
    def lower_user_ids(self, data, **kwargs):
        email = data.get('email', None)
        if email:
            data['email'] = email.lower()

        return data
