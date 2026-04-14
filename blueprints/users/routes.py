from flask import request
from . import users_bp
from .controllers import UsuarioController
from utils import login_required

controller = UsuarioController()

@users_bp.route("/login", methods=["GET", "POST"])
def login():
    return controller.login()

@users_bp.route("/cadastro", methods=["GET", "POST"])
def cadastrar():
    return controller.cadastrar()

@users_bp.route("/logout")
def logout():
    return controller.logout()

@users_bp.route("/perfil")
@login_required
def perfil():
    return controller.perfil()
