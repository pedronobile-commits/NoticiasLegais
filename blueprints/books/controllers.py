from flask import render_template, request, redirect, url_for, flash, session
from .dao import NoticiaDAO
from .models import Noticia
import base64


class NoticiaController:
    def __init__(self):
        self.__dao = NoticiaDAO()

    def listar(self):
        query = request.args.get('q', '').strip()
        if query:
            noticias = self.__dao.buscar_por_titulo(query)
        else:
            noticias = self.__dao.carregar_noticias()
        usuario_id = session.get('usuario_id')
        try:
            from blueprints.favorites.dao import FavoritaDAO
            favorita_dao = FavoritaDAO()
            for noticia in noticias:
                noticia.is_favorita = favorita_dao.is_favorita(usuario_id, noticia.id) if usuario_id else False
        except:
            for noticia in noticias:
                noticia.is_favorita = False
        return render_template("noticias.html", noticias=noticias, query=query)

    def cadastrar(self):
        titulo = request.form.get("titulo")
        autor = request.form.get("autor")
        conteudo = request.form.get("conteudo")
        nome_categoria = request.form.get("nome_categoria")
        fonte = request.form.get("fonte")
        imagem_arquivo = request.files.get("imagem")
        data_publicacao = request.form.get("data_publicacao")

        if not titulo or not autor or not conteudo or not nome_categoria or not fonte or not imagem_arquivo or imagem_arquivo.filename == "":
            flash("Erro: Todos os campos, incluindo a imagem, são obrigatórios!", "danger")
            return self.preparar_cadastro()
        
        # Validar se categoria existe
        from blueprints.categories.dao import CategoriaDAO
        dao_categoria = CategoriaDAO()
        categoria_existente = dao_categoria.buscar_por_nome(nome_categoria)
        if not categoria_existente:
            flash(f"Categoria '{nome_categoria}' não existe. Cadastre primeiro em /categorias.", "danger")
            return self.preparar_cadastro()

        # Validar tamanho da imagem (max 5MB)
        imagem_arquivo.seek(0)
        if len(imagem_arquivo.read()) > 5 * 1024 * 1024:
            flash("Imagem muito grande! Máximo 5MB.", "danger")
            return self.preparar_cadastro()
        imagem_arquivo.seek(0)

        imagem_bytes = imagem_arquivo.read()
        if not imagem_bytes:
            flash("Erro: O arquivo de imagem não pôde ser lido.", "danger")
            return self.preparar_cadastro()

        imagem_data_uri = f"data:{imagem_arquivo.mimetype};base64,{base64.b64encode(imagem_bytes).decode('utf-8')}"
        nova_noticia = Noticia(titulo, autor, conteudo, data_publicacao, nome_categoria, fonte, imagem_data_uri)
        try:
            self.__dao.salvar_noticia(nova_noticia)
            flash(f"Notícia '{titulo}' publicada com sucesso!", "success")
            return redirect(url_for("noticias.listar_noticias"))
        except Exception as e:
            flash("Erro ao salvar notícia. Tente novamente.", "danger")
            print(f"Erro no cadastro de notícia: {e}")
            return self.preparar_cadastro()

    def preparar_cadastro(self):
        from blueprints.categories.dao import CategoriaDAO
        dao_categoria = CategoriaDAO()
        lista_categorias = dao_categoria.carregar_categorias()
        return render_template("cadastrar.html", categorias=lista_categorias)

    def preparar_edicao(self, id):
        noticia = self.__dao.buscar_por_id(id)
        if noticia is None:
            flash("Notícia não encontrada.", "danger")
            return redirect(url_for("noticias.listar_noticias"))
        
        from blueprints.categories.dao import CategoriaDAO
        dao_categoria = CategoriaDAO()
        lista_categorias = dao_categoria.carregar_categorias()
        return render_template("editar.html", noticia=noticia, categorias=lista_categorias)

    def editar(self, id):
        titulo = request.form.get("titulo")
        autor = request.form.get("autor")
        conteudo = request.form.get("conteudo")
        nome_categoria = request.form.get("nome_categoria")
        fonte = request.form.get("fonte")
        data_publicacao = request.form.get("data_publicacao")
        imagem_file = request.files.get("imagem")

        if not titulo or not autor or not conteudo or not nome_categoria or not fonte:
            flash("Erro: Todos os campos são obrigatórios!", "danger")
            return self.preparar_edicao(id)

        # Validar se categoria existe
        from blueprints.categories.dao import CategoriaDAO
        dao_categoria = CategoriaDAO()
        categoria_existente = dao_categoria.buscar_por_nome(nome_categoria)
        if not categoria_existente:
            flash(f"Categoria '{nome_categoria}' não existe. Cadastre primeiro em /categorias.", "danger")
            return self.preparar_edicao(id)

        imagem_data_uri = None
        if imagem_file and imagem_file.filename != "":
            if len(imagem_file.read()) > 5 * 1024 * 1024:
                flash("Imagem muito grande! Máximo 5MB.", "danger")
                return self.preparar_edicao(id)
            imagem_file.seek(0)
            imagem_bytes = imagem_file.read()
            if imagem_bytes:
                imagem_data_uri = f"data:{imagem_file.mimetype};base64,{base64.b64encode(imagem_bytes).decode('utf-8')}"

        if imagem_data_uri is None:
            noticia_existente = self.__dao.buscar_por_id(id)
            imagem_data_uri = noticia_existente.imagem if noticia_existente else None

        noticia_atualizada = Noticia(titulo, autor, conteudo, data_publicacao, nome_categoria, fonte, imagem_data_uri, noticia_id=id)
        try:
            self.__dao.atualizar_noticia(noticia_atualizada)
            flash("Notícia atualizada com sucesso!", "success")
            return redirect(url_for("noticias.listar_noticias"))
        except Exception as e:
            flash("Erro ao atualizar notícia. Tente novamente.", "danger")
            print(f"Erro na edição de notícia: {e}")
            return self.preparar_edicao(id)

    def remover(self, id):
        try:
            self.__dao.remover_noticia(id)
            flash("Notícia removida com sucesso!", "success")
        except Exception as e:
            flash("Erro ao remover notícia. Tente novamente.", "danger")
            print(f"Erro na remoção de notícia: {e}")
        return redirect(url_for("noticias.listar_noticias"))

