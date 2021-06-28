from marshmallow import fields, pre_load

from main.extensions import ma
from main.modules.user.models import User



class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_only = ('password',)

    matricule = fields.Str()





    @pre_load
    def lower_user_ids(self, data, **kwargs):
        email = data.get('email', None)
        if email:
            data['email'] = email.lower()

        return data
