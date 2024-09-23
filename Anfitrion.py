from Usuario import Usuario


class Anfitrion(Usuario):
    def __init__(self, identificacion, nombre, apellido, email, fecha_nacimiento, cuenta):
        super().__init__(identificacion, nombre, apellido, email, fecha_nacimiento)
        self.__cuenta = cuenta

    @property
    def cuenta(self):
        return self.__cuenta

    @cuenta.setter
    def cuenta(self, cuenta):
        self.__cuenta = cuenta

    def aceptar_reserva(self, reserva):
        pass

    def crear_alojamiento(self, pais, ciudad, direccion, anfitrion, hora_ingreso, hora_salida, valor_noche, tipo_alojamiento, tipo_alojamiento_entero, acceso_banio, acceso_cocina):
        pass
