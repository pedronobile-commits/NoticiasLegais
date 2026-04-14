class Noticia:

    def __init__(self, titulo_noticia, autor_noticia, conteudo_noticia, data_noticia, categoria_noticia, fonte_noticia, imagem_noticia, noticia_id=None):
        self.__titulo = titulo_noticia
        self.__autor = autor_noticia
        self.__conteudo = conteudo_noticia
        self.__categoria = categoria_noticia
        self.__data_publicacao = data_noticia
        self.__fonte = fonte_noticia
        self.__imagem = imagem_noticia
        self.__id = noticia_id

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "conteudo": self.conteudo,
            "categoria": self.categoria,
            'data': self.data_publicacao,
            'fonte': self.fonte,
            'imagem': self.imagem,
            "id": self.id
        }

    @property
    def titulo(self):
        return str.capitalize(self.__titulo)

    @titulo.setter
    def titulo(self, valor):
        self.__titulo = str.capitalize(valor)

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, valor):
        self.__autor = str.upper(valor)

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, valor):
        self.__categoria = valor

    @property
    def conteudo(self):
        return self.__conteudo

    @conteudo.setter
    def conteudo(self, v):
        self.__conteudo = v

    @property
    def data_publicacao(self):
        return self.__data_publicacao

    @data_publicacao.setter
    def data_publicacao(self, valor):
        self.__data_publicacao = valor

    @property
    def fonte(self):
        return self.__fonte

    @fonte.setter
    def fonte(self, valor):
        self.__fonte = valor

    @property
    def imagem(self):
        return self.__imagem

    @imagem.setter
    def imagem(self, valor):
        self.__imagem = valor

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, v):
        self.__id = v
    

