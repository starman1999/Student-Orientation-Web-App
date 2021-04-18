from main.extensions import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    phone = db.Column(db.String)
    confirmed_at = db.Column(db.DateTime)


# class Job(db.Model):
#     __tablename__ = 'jobs'
#
#     name = db.Column(db.String)
