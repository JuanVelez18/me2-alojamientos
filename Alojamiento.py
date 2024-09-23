from uuid import uuid4


class Alojamiento:
    def __init__(self, pais, ciudad, direccion, anfitrion, hora_ingreso, hora_salida, valor_noche):
        self.__identificador = str(uuid4())
        self.__pais = pais
        self.__ciudad = ciudad
        self.__direccion = direccion
        self.__anfitrion = anfitrion
        self.__hora_ingreso = hora_ingreso
        self.__hora_salida = hora_salida
        self.__valor_noche = valor_noche

    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self, id):
        self.__identificador = id

    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self, pais):
        self.__pais = pais

    @property
    def ciudad(self):
        return self.__ciudad

    @ciudad.setter
    def ciudad(self, ciudad):
        self.__ciudad = ciudad

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    @property
    def anfitrion(self):
        return self.__anfitrion

    @anfitrion.setter
    def anfitrion(self, anfitrion):
        self.__anfitrion = anfitrion

    @property
    def hora_ingreso(self):
        return self.__hora_ingreso

    @hora_ingreso.setter
    def hora_ingreso(self, hora_ingreso):
        self.__hora_ingreso = hora_ingreso

    @property
    def hora_salida(self):
        return self.__hora_salida

    @hora_salida.setter
    def hora_salida(self, hora_salida):
        self.__hora_salida = hora_salida

    @property
    def valor_noche(self):
        return self.__valor_noche

    @valor_noche.setter
    def valor_noche(self, valor_noche):
        self.__valor_noche = valor_noche

    def __str__(self):
        return f'{self.__identificador} - {self.__pais} - {self.__ciudad} - {self.__direccion} - {self.__anfitrion} - {self.__hora_ingreso} - {self.__hora_salida} - {self.__valor_noche}'
