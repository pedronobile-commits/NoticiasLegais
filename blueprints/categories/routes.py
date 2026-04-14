from flask import request
from . import categories_bp
from .controllers import CategoriaController
from utils import login_required

controller = CategoriaController()

@categories_bp.route("/categorias")
@login_required
def listar():
    return controller.listar()

@categories_bp.route("/categorias/novo", methods=["GET", "POST"])
@login_required
def cadastrar():
    return controller.cadastrar()

@categories_bp.route("/categorias/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_categoria(id):
    if request.method == "POST":
        return controller.editar(id)
    return controller.preparar_edicao(id)

@categories_bp.route("/categorias/excluir/<int:id>", methods=["POST"])
@login_required
def excluir_categoria(id):
    return controller.remover(id)
