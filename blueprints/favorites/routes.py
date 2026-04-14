from flask import request
from . import favorites_bp
from .controllers import FavoritaController
from utils import login_required

controller = FavoritaController()

@favorites_bp.route("/favoritas")
@login_required
def listar():
    return controller.listar()

@favorites_bp.route("/favoritas/adicionar")
@login_required
def adicionar():
    return controller.adicionar()

@favorites_bp.route("/favoritas/remover")
@login_required
def remover():
    return controller.remover()