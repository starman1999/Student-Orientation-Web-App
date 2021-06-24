from marshmallow import fields, pre_load

from main.extensions import ma
from main.modules.speciality.models import Speciality


class SpecialitySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Speciality

    name = fields.Str()

    @pre_load
    def lower_user_ids(self, data, **kwargs):
        email = data.get('email', None)
        if email:
            data['email'] = email.lower()

        return data
