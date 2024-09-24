from Reserva import Reserva


class Usuario:
    def __init__(self, identificacion, nombre, apellido, email, fecha_nacimiento):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__fecha_nacimiento = fecha_nacimiento

    @property
    def identificacion(self):
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, identificacion):
        self.__identificacion = identificacion

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f'{self.__identificacion} - {self.__nombre} {self.__apellido} - {self.__email} - {self.__fecha_nacimiento}'

    def solicitar_reserva(self, estado, alojamiento, fecha_inicio, fecha_fin, valor_total):
        return Reserva(estado, alojamiento, fecha_inicio, fecha_fin, valor_total)

    def cancelar_reserva(self, reserva):
        reserva.estado = 'Cancelada'
