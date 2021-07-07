from marshmallow import fields, pre_load

from main.extensions import ma
from main.modules.speciality.models import Speciality


class SpecialitySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Speciality
    id = fields.Integer()
    name = fields.Str()


