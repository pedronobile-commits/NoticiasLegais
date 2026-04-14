from flask import request, render_template
from . import noticias_bp
from .controllers import NoticiaController
from utils import login_required

controller = NoticiaController()

@noticias_bp.route("/noticias")
@login_required
def listar_noticias():
    return controller.listar()

@noticias_bp.route("/sobre")
def sobre():
    return render_template("sobre.html")

@noticias_bp.route("/noticias/novo", methods=["GET", "POST"])
@login_required
def cadastrar_noticia():
    if request.method == "POST":
        return controller.cadastrar()
    return controller.preparar_cadastro()

@noticias_bp.route("/noticias/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_noticia(id):
    if request.method == "POST":
        return controller.editar(id)
    return controller.preparar_edicao(id)

@noticias_bp.route("/noticias/excluir/<int:id>", methods=["POST"])
@login_required
def excluir_noticia(id):
    return controller.remover(id)
