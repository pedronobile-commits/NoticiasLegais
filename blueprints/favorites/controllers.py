from flask import render_template, request, redirect, url_for, flash, session
from .dao import FavoritaDAO
from .models import Favorita

class FavoritaController:
    def __init__(self):
        self.__dao = FavoritaDAO()

    def listar(self):
        usuario_id = session.get('usuario_id')
        if not usuario_id:
            flash("Você precisa estar logado para ver suas favoritas.", "warning")
            return redirect(url_for('users.login'))
        favoritas = self.__dao.listar_favoritas_por_usuario(usuario_id)
        return render_template("favorites.html", noticias=favoritas)

    def adicionar(self):
        usuario_id = session.get('usuario_id')
        if not usuario_id:
            flash("Você precisa estar logado.", "warning")
            return redirect(url_for('users.login'))
        noticia_id = request.args.get('noticia_id')
        if not noticia_id:
            flash("Notícia não encontrada.", "danger")
            return redirect(url_for('noticias.listar_noticias'))
        favorita = Favorita(usuario_id, noticia_id)
        try:
            self.__dao.adicionar_favorita(favorita)
            flash("Notícia adicionada aos favoritos!", "success")
        except Exception as e:
            flash("Erro ao adicionar favorita.", "danger")
            print(f"Erro: {e}")
        return redirect(url_for('noticias.listar_noticias'))

    def remover(self):
        usuario_id = session.get('usuario_id')
        if not usuario_id:
            flash("Você precisa estar logado.", "warning")
            return redirect(url_for('users.login'))
        noticia_id = request.args.get('noticia_id')
        if not noticia_id:
            flash("Notícia não encontrada.", "danger")
            return redirect(url_for('noticias.listar_noticias'))
        try:
            self.__dao.remover_favorita(usuario_id, noticia_id)
            flash("Notícia removida dos favoritos!", "success")
        except Exception as e:
            flash("Erro ao remover favorita.", "danger")
            print(f"Erro: {e}")
        return redirect(url_for('noticias.listar_noticias'))