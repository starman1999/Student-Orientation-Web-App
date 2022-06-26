from flask import Blueprint, request, redirect, url_for
from flask_cors import cross_origin

from main.extensions import db

from main.modules.etudiant.models import Etudiant, Moyenne, Module
from main.shared.base_api import BaseAPI
from main.modules.etudiant.Schemas import StudentSchema, MoyenneSchema, ModuleSchema

blueprint = Blueprint('etudiant', __name__, url_prefix='/api')


class StudentApi(BaseAPI):

    route_base = "students"

    model = Etudiant
    schema = StudentSchema


StudentApi.register(blueprint)