class Cuenta:
    def __init__(self, numero, tipo, banco):
        self.__numero = numero
        self.__tipo = tipo
        self.__banco = banco

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def banco(self):
        return self.__banco

    @banco.setter
    def banco(self, banco):
        self.__banco = banco
