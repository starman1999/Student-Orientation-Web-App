from main.extensions import db
from main.shared.base_model import BaseModel, HasCreatedAt, HasUpdatedAt


moyennes = db.Table('moyenne',
    db.Column('etudiant_id', db.Integer, db.ForeignKey('etudiants.id'), primary_key=True),
    db.Column('module_id', db.Integer, db.ForeignKey('modules.id'), primary_key=True),
    db.Column('moy', db.Float, nullable=False)
)


class Etudiant(BaseModel, HasCreatedAt, HasUpdatedAt):
    __tablename__ = 'etudiants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    matricule = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String,unique=True)
    modules_id = db.relationship('Module', secondary=moyennes, backref=db.backref('moyenne', lazy='dynamic'))


class Module(BaseModel, HasCreatedAt, HasUpdatedAt):
    __tablename__ = 'modules'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    etudiant_id = db.Column(db.Integer, db.ForeignKey('etudiants.id'), nullable=False)
    moyenne_module = db.Column(db.Float, db.ForeignKey('moyennes.id'), nullable=False)






