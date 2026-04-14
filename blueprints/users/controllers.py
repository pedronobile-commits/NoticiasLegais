from flask import render_template, request, redirect, url_for, flash, session
from .dao import UsuarioDAO
from .models import Usuario
from werkzeug.security import generate_password_hash, check_password_hash
from ..favorites.dao import FavoritaDAO
import re

class UsuarioController:
    def __init__(self):
        self.__dao = UsuarioDAO()

    def login(self):
        if 'usuario_id' in session:
            return redirect(url_for("noticias.listar_noticias"))
        if request.method == "POST":
            email = request.form.get("email")
            senha = request.form.get("senha")

            if not email or not senha:
                flash("Email e senha são obrigatórios!", "danger")
                return self.preparar_login()

            usuario = self.__dao.buscar_por_email(email)
            if usuario and check_password_hash(usuario.senha, senha):
                session['usuario_id'] = usuario.id
                session['usuario_nome'] = usuario.nome
                flash("Login realizado com sucesso!", "success")
                return redirect(url_for("noticias.listar_noticias"))
            else:
                flash("Email ou senha incorretos.", "danger")
                return self.preparar_login()
        return self.preparar_login()

    def preparar_login(self):
        return render_template("login.html")

    def cadastrar(self):
        if request.method == "POST":
            nome = request.form.get("nome")
            email = request.form.get("email")
            senha = request.form.get("senha")

            if not nome or not email or not senha:
                flash("Todos os campos são obrigatórios!", "danger")
                return self.preparar_cadastro()

            # Validar email
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                flash("Email inválido!", "danger")
                return self.preparar_cadastro()

            # Validar senha (mínimo 6 caracteres)
            if len(senha) < 6:
                flash("Senha deve ter pelo menos 6 caracteres!", "danger")
                return self.preparar_cadastro()

            # Verificar se email já existe
            if self.__dao.buscar_por_email(email):
                flash("Email já cadastrado.", "danger")
                return self.preparar_cadastro()

            # Hash da senha
            senha_hash = generate_password_hash(senha)
            novo_usuario = Usuario(nome, email, senha_hash)
            try:
                self.__dao.salvar_usuario(novo_usuario)
                flash("Usuário cadastrado com sucesso! Faça login.", "success")
                return redirect(url_for("noticias.listar_noticias"))
            except Exception as e:
                flash("Erro ao cadastrar usuário. Tente novamente.", "danger")
                print(f"Erro no cadastro: {e}")
                return self.preparar_cadastro()
        return self.preparar_cadastro()

    def preparar_cadastro(self):
        return render_template("cadastro_usuario.html")

    def logout(self):
        session.clear()
        flash("Logout realizado.", "info")
        return redirect(url_for("users.login"))

    def perfil(self):
        usuario_id = session.get('usuario_id')
        if not usuario_id:
            flash("Você precisa estar logado.", "warning")
            return redirect(url_for('users.login'))
        usuario = self.__dao.buscar_por_id(usuario_id)
        try:
            from ..favorites.dao import FavoritaDAO
            favorita_dao = FavoritaDAO()
            favoritas = favorita_dao.listar_favoritas_por_usuario(usuario_id)
        except:
            favoritas = []
        return render_template("usuario.html", usuario=usuario, favoritas=favoritas)
