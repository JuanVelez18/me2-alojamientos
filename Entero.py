from Alojamiento import Alojamiento


class Entero(Alojamiento):
    def __init__(self, pais, ciudad, direccion, anfitrion, hora_ingreso, hora_salida, valor_noche, tipo):
        super().__init__(pais, ciudad, direccion, anfitrion,
                         hora_ingreso, hora_salida, valor_noche)
        self.__tipo = tipo

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
