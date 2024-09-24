from datetime import date

from Alojamiento import Alojamiento
from Cuenta import Cuenta
from Entero import Entero
from Habitacion import Habitacion
from Reserva import Reserva
from Usuario import Usuario


class Anfitrion(Usuario):
    def __init__(self, identificacion: str, nombre: str, apellido: str, email: str, fecha_nacimiento: date, cuenta: 'Cuenta'):
        super().__init__(identificacion, nombre, apellido, email, fecha_nacimiento)
        self.__cuenta = cuenta

    @property
    def cuenta(self):
        return self.__cuenta

    @cuenta.setter
    def cuenta(self, cuenta: 'Cuenta'):
        self.__cuenta = cuenta

    def aceptar_reserva(self, reserva: 'Reserva', aceptar: bool):
        if aceptar:
            reserva.estado = 'Aceptada'
        else:
            reserva.estado = 'Rechazada'

    def crear_alojamiento(self, pais, ciudad, direccion, hora_ingreso, hora_salida, valor_noche, tipo_alojamiento, tipo_alojamiento_entero, acceso_banio, acceso_cocina) -> 'Alojamiento':
        if tipo_alojamiento == 'Habitacion':
            alojamiento = Habitacion(pais, ciudad, direccion, self, hora_ingreso,
                                     hora_salida, valor_noche, not acceso_banio, acceso_cocina)
        elif tipo_alojamiento == 'Entero':
            alojamiento = Entero(pais, ciudad, direccion, self, hora_ingreso,
                                 hora_salida, valor_noche, tipo_alojamiento_entero)
        else:
            print('Tipo de alojamiento no válido')
            alojamiento = None

        return alojamiento
