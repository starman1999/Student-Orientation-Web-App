from marshmallow import fields

from main.extensions import ma
from main.modules.etudiant.models import Etudiant, Module, Moyenne


class MoyenneSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Moyenne
        dump_only = ('module',)

    etudiant_id = fields.Integer()
    module_id = fields.Integer()
    moyenne = fields.Float()


class ModuleSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Module

    id = fields.Int()
    name = fields.Str()
    # moyenne = ma.Nested(MoyenneSchema)


class StudentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Etudiant
        dump_only = ('module',)

    id = fields.Int()
    name = fields.Str()
    matricule = fields.Str()
    modules = ma.Nested(MoyenneSchema, many=True)
