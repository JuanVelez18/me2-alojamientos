from datetime import date
from uuid import uuid4

from Alojamiento import Alojamiento


class Reserva:
    def __init__(self, estado: str, alojamiento: 'Alojamiento', fecha_inicio: date, fecha_fin: date, valor_total: float):
        self.identificador = str(uuid4())
        self.__estado = estado
        self.__alojamiento = alojamiento
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__valor_total = valor_total

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @property
    def alojamiento(self):
        return self.__alojamiento

    @alojamiento.setter
    def alojamiento(self, alojamiento):
        self.__alojamiento = alojamiento

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    @property
    def fecha_fin(self):
        return self.__fecha_fin

    @fecha_fin.setter
    def fecha_fin(self, fecha_fin):
        self.__fecha_fin = fecha_fin

    @property
    def valor_total(self):
        return self.__valor_total

    @valor_total.setter
    def valor_total(self, valor_total):
        self.__valor_total = valor_total

    def __str__(self):
        return f'{self.identificador} - {self.__estado} - {self.__fecha_inicio} - {self.__fecha_fin} - {self.__valor_total}'
