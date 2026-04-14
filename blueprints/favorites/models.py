class Favorita:
    def __init__(self, usuario_id, noticia_id, favorita_id=None):
        self.__usuario_id = usuario_id
        self.__noticia_id = noticia_id
        self.__id = favorita_id

    @property
    def usuario_id(self):
        return self.__usuario_id

    @property
    def noticia_id(self):
        return self.__noticia_id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valor):
        self.__id = valor