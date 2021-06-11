from flask_classful import FlaskView

class BaseAPI(FlaskView):
    model = None
    # schemas
    # pagination here

    # get the list of ressources (users, specialities...)

    def index(self):
        items = self.medel.query.all()


    def get(self, id):
        pass


    # create new ressource

    def post(self):
        pass


    # update a ressource by id
    def patch(self):
        pass


    def delete(self):
        pass
