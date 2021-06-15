from main.extensions import db
from main.shared.base_model import BaseModel


moyennes = db.Table('moyenne',
    db.Column('etudiant_id', db.Integer, db.ForeignKey('etudiants.id'), primary_key=True),
    db.Column('module_id', db.Integer, db.ForeignKey('modules.id'), primary_key=True),
    db.Column('moyenne', db.Float, nullable=False)
)


class Etudiant(BaseModel):
    __tablename__ = 'etudiants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    matricule = db.Column(db.String, unique=True, nullable=False)
    modules_id = db.relationship('Module', secondary=moyennes, backref=db.backref('moyenne', lazy='dynamic'))


class Module(BaseModel):
    __tablename__ = 'modules'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    etudiant_id = db.Column(db.Integer, db.ForeignKey('etudiants.id'))







