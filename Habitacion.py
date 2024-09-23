from Alojamiento import Alojamiento


class Habitacion(Alojamiento):
    def __init__(self, pais, ciudad, direccion, anfitrion, hora_ingreso, hora_salida, valor_noche, banio_privado, cocina):
        super().__init__(pais, ciudad, direccion, anfitrion,
                         hora_ingreso, hora_salida, valor_noche)
        self.__banio_privado = banio_privado
        self.__cocina = cocina

    @property
    def banio_privado(self):
        return self.__banio_privado

    @banio_privado.setter
    def banio_privado(self, banio_privado):
        self.__banio_privado = banio_privado

    @property
    def cocina(self):
        return self.__cocina

    @cocina.setter
    def cocina(self, cocina):
        self.__cocina = cocina
