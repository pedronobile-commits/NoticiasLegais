from flask import render_template, request, redirect, url_for, flash
from .dao import CategoriaDAO
from .models import Categoria

class CategoriaController:
    def __init__(self):
        self.__dao = CategoriaDAO()

    def listar(self):
        categorias = self.__dao.carregar_categorias()
        return render_template("categorias.html", categorias=categorias)

    def cadastrar(self):
        if request.method == "POST":
            nome_categoria = request.form.get("nome")

            if not nome_categoria:
                flash("Nome da categoria é obrigatório!", "danger")
                return self.preparar_cadastro()

            # Verificar se categoria já existe
            if self.__dao.buscar_por_nome(nome_categoria):
                flash("Categoria já existe.", "danger")
                return self.preparar_cadastro()

            nova_categoria = Categoria(nome_categoria)
            try:
                self.__dao.salvar_categoria(nova_categoria)
                flash("Categoria cadastrada com sucesso!", "success")
                return redirect(url_for("categories.listar"))
            except Exception as e:
                flash("Erro ao cadastrar categoria. Tente novamente.", "danger")
                print(f"Erro no cadastro de categoria: {e}")
                return self.preparar_cadastro()
        return self.preparar_cadastro()

    def preparar_cadastro(self):
        return render_template("cadastrar_categoria.html")

    def preparar_edicao(self, id_categoria):
        categoria = self.__dao.buscar_por_id(id_categoria)
        if not categoria:
            flash("Categoria não encontrada.", "danger")
            return redirect(url_for("categories.listar"))
        return render_template("editar_categoria.html", categoria=categoria)

    def editar(self, id_categoria):
        nome_categoria = request.form.get("nome_categoria")
        if not nome_categoria:
            flash("Nome da categoria é obrigatório!", "danger")
            return self.preparar_edicao(id_categoria)

        if self.__dao.buscar_por_nome(nome_categoria) and self.__dao.buscar_por_nome(nome_categoria).id != id_categoria:
            flash("Nome de categoria já existe.", "danger")
            return self.preparar_edicao(id_categoria)

        categoria_atualizada = Categoria(nome_categoria, categoria_id=id_categoria)
        try:
            self.__dao.atualizar_categoria(categoria_atualizada)
            flash("Categoria atualizada com sucesso!", "success")
        except Exception as e:
            flash("Erro ao atualizar categoria.", "danger")
            print(f"Erro na edição: {e}")
            return self.preparar_edicao(id_categoria)
        return redirect(url_for("categories.listar"))

    def remover(self, id_categoria):
        try:
            self.__dao.remover_categoria(id_categoria)
            flash("Categoria removida com sucesso!", "success")
        except Exception as e:
            flash("Erro ao remover categoria. Pode ter notícias associadas.", "danger")
            print(f"Erro na remoção: {e}")
        return redirect(url_for("categories.listar"))
