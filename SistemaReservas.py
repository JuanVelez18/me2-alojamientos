import numpy as np


class SistemaReservas:
    def __init__(self, capacidad_usuarios, capacidad_alojamientos, capacidad_reservas):
        self.usuarios = np.empty(capacidad_usuarios, dtype=object)
        self.alojamientos = np.empty(capacidad_alojamientos, dtype=object)
        self.reservas = np.empty(capacidad_reservas, dtype=object)
        self.numero_usuarios = 0
        self.numero_alojamientos = 0
        self.numero_reservas = 0
