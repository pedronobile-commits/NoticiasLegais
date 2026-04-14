class Usuario:

    def __init__(self, nome, email, senha, usuario_id=None):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__id = usuario_id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        self.__email = valor

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, valor):
        self.__senha = valor

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, v):
        self.__id = v