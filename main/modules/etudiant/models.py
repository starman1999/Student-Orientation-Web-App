from main.extensions import db
from main.shared.base_model import BaseModel


# Moyenne = db.Table('moyennes',
#     db.Column('etudiant_id', db.Integer, db.ForeignKey('etudiants.id'), primary_key=True),
#     db.Column('module_id', db.Integer, db.ForeignKey('modules.id'), primary_key=True),
#     db.Column('moyenne', db.Float, nullable=False)
#                                 )


class Moyenne(BaseModel):
    _tablename_ = 'Moyenne'

    etudiant_id = db.Column(db.Integer, db.ForeignKey(
        'etudiants.id'), primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey(
        'modules.id'), primary_key=True)
    moyenne = db.Column(db.Float)
    etudiant = db.relationship("Etudiant", back_populates="modules")
    module = db.relationship("Module", back_populates="etudiants")


class Etudiant(BaseModel):
    __tablename__ = 'etudiants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    matricule = db.Column(db.String, unique=True, nullable=False)
    choix = db.Column(db.String, nullable=True)
    modules = db.relationship("Moyenne", back_populates="etudiant")


class Module(BaseModel):
    __tablename__ = 'modules'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    etudiants = db.relationship("Moyenne", back_populates="module")
