class Categoria:

    def __init__(self, nome, categoria_id=None):
        self.__nome = nome
        self.__id = categoria_id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, v):
        self.__id = v