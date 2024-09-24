from datetime import date

import numpy as np


from Alojamiento import Alojamiento
from Reserva import Reserva
from Usuario import Usuario
from Anfitrion import Anfitrion
from Cuenta import Cuenta


class SistemaReservas:
    def __init__(self, capacidad_usuarios, capacidad_alojamientos, capacidad_reservas):
        self.usuarios = np.empty(capacidad_usuarios, dtype=object)
        self.alojamientos = np.empty(capacidad_alojamientos, dtype=object)
        self.reservas = np.empty(capacidad_reservas, dtype=object)
        self.numero_usuarios = 0
        self.numero_alojamientos = 0
        self.numero_reservas = 0

    def buscar_usuario(self, identificacion):
        usuario_no_encontrado_mensaje = f'El usuario con identificacion {identificacion} no existe'

        if self.numero_usuarios == 0:
            print(usuario_no_encontrado_mensaje)
            return

        indice = 0
        while indice < self.numero_usuarios and self.usuarios[indice].identificacion != identificacion:
            indice += 1

        if indice == self.numero_usuarios:
            print(usuario_no_encontrado_mensaje)
        else:
            return self.usuarios[indice]

    def buscar_alojamiento(self, identificador) -> 'Alojamiento':
        alojamiento_no_encontrado_mensaje = f'El alojamiento con identificador {identificador} no existe'

        if self.numero_alojamientos == 0:
            print(alojamiento_no_encontrado_mensaje)
            return

        indice = 0
        while indice < self.numero_alojamientos and self.alojamientos[indice].identificador != identificador:
            indice += 1

        if indice == self.numero_alojamientos:
            print(alojamiento_no_encontrado_mensaje)
        else:
            return self.alojamientos[indice]

    def buscar_reserva(self, identificador):
        reseversa_no_encontrada_mensaje = f'La reserva con identificador {identificador} no existe'

        if self.numero_reservas == 0:
            print(reseversa_no_encontrada_mensaje)
            return

        indice = 0
        while indice < self.numero_reservas and self.reservas[indice].identificador != identificador:
            indice += 1

        if indice == self.numero_reservas:
            print(reseversa_no_encontrada_mensaje)
        else:
            return self.reservas[indice]

    def agregar_usuario(self, identificacion, nombre, apellido, email, fecha_nacimiento, tipo, numero_cuenta, banco, tipo_cuenta):
        existe_usuario = self.buscar_usuario(identificacion) != None
        if existe_usuario:
            print(f'El usuario con identificacion {identificacion} ya existe')
            return

        if len(self.usuarios) == self.numero_usuarios:
            print('No hay capacidad para más usuarios')
            return

        if tipo == 'Anfitrion':
            cuenta = Cuenta(numero_cuenta, tipo_cuenta, banco)
            usuario = Anfitrion(identificacion, nombre,
                                apellido, email, fecha_nacimiento, cuenta)
        else:
            usuario = Usuario(identificacion, nombre,
                              apellido, email, fecha_nacimiento)

        self.usuarios[self.numero_usuarios] = usuario
        self.numero_usuarios += 1

    def agregar_alojamiento(self, identificacion_anfitrion, pais, ciudad, direccion, hora_ingreso, hora_salida, valor_noche, tipo_alojamiento, tipo_alojamiento_entero, acceso_banio, acceso_cocina):
        anfitrion = self.buscar_usuario(identificacion_anfitrion)
        if anfitrion == None:
            print(
                f'El anfitrion con identificacion {identificacion_anfitrion} no existe')
            return

        if len(self.alojamientos) == self.numero_alojamientos:
            print('No hay capacidad para más alojamientos')
            return

        alojamiento = anfitrion.crear_alojamiento(pais, ciudad,
                                                  direccion, hora_ingreso, hora_salida, valor_noche, tipo_alojamiento, tipo_alojamiento_entero, acceso_banio, acceso_cocina)

        self.alojamientos[self.numero_alojamientos] = alojamiento
        self.numero_alojamientos += 1

    def __verificar_disponibilidad(self, identificador_alojamiento: str, fecha_inicio: date, fecha_fin: date) -> bool:
        alojamiento = self.buscar_alojamiento(identificador_alojamiento)
        if alojamiento == None:
            print(
                f'El alojamiento con identificador {identificador_alojamiento} no existe')
            return False

        indice = 0
        while True:
            if indice == self.numero_reservas:
                break

            reserva = self.reservas[indice]
            es_mismo_alojamiento = reserva.alojamiento.identificador == identificador_alojamiento
            esta_ocupado = max(reserva.fecha_inicio, fecha_inicio) < min(
                reserva.fecha_fin, fecha_fin)

            if es_mismo_alojamiento and esta_ocupado:
                return False

            indice += 1

        return True

    def __definir_estado_inicial(self, fecha_inicio: date, fecha_fin: date) -> str:
        if fecha_inicio > fecha_fin:
            print('La fecha de inicio no puede ser mayor a la fecha de fin')
            return ''

        fecha_actual = date.today()

        if fecha_actual < fecha_inicio:
            return 'Pendiente'
        elif fecha_actual >= fecha_inicio and fecha_actual <= fecha_fin:
            return 'En Curso'
        else:
            return 'Finalizada'

    def __calcular_valor_total(self, alojamiento: 'Alojamiento', fecha_inicio: date, fecha_fin: date) -> float:
        if fecha_inicio > fecha_fin:
            print('La fecha de inicio no puede ser mayor a la fecha de fin')
            return 0

        COMISION = 0.1
        noches = (fecha_fin - fecha_inicio).days

        return noches * alojamiento.valor_noche * (1 + COMISION)

    def reservar_alojamiento(self, identificacion_usuario: str, identificador_alojamiento: str, fecha_inicio: date, fecha_fin: date):
        if len(self.reservas) == self.numero_reservas:
            print('No hay capacidad para más reservas')
            return

        usuario = self.buscar_usuario(identificacion_usuario)
        if usuario == None:
            print(
                f'El usuario con identificacion {identificacion_usuario} no existe')
            return

        alojamiento = self.buscar_alojamiento(identificador_alojamiento)
        if alojamiento == None:
            print(
                f'El alojamiento con identificador {identificador_alojamiento} no existe')
            return

        if not self.__verificar_disponibilidad(identificador_alojamiento, fecha_inicio, fecha_fin):
            print(
                f'El alojamiento con identificador {identificador_alojamiento} no está disponible en las fechas solicitadas')
            return

        estado_inicial = self.__definir_estado_inicial(fecha_inicio, fecha_fin)
        valor_total = self.__calcular_valor_total(
            alojamiento, fecha_inicio, fecha_fin)
        reserva = usuario.solicitar_reserva(
            estado_inicial, alojamiento, fecha_inicio, fecha_fin, valor_total)

        self.reservas[self.numero_reservas] = reserva
        self.numero_reservas += 1

    def cancelar_reserva(self, identificacion_usuario: str, identificador_reserva: str):
        usuario = self.buscar_usuario(identificacion_usuario)
        if usuario == None:
            print(
                f'El usuario con identificacion {identificacion_usuario} no existe')
            return

        reserva = self.buscar_reserva(identificador_reserva)
        if reserva == None:
            print(
                f'La reserva con identificador {identificador_reserva} no existe')
            return

        if reserva.estado != 'Pendiente' and reserva.estado != 'Aceptada':
            print('Solo se pueden cancelar reservas pendientes o aceptadas')
            return

        usuario.cancelar_reserva(reserva)

    def aceptar_reserva(self, identificacion_anfitrion: str, identificador_reserva: str, aceptar: bool):
        anfitrion = self.buscar_usuario(identificacion_anfitrion)
        if anfitrion == None:
            print(
                f'El usuario con identificacion {identificacion_anfitrion} no existe')
            return

        if not isinstance(anfitrion, Anfitrion):
            print(
                f'El usuario con identificacion {identificacion_anfitrion} no es un anfitrion')
            return

        reserva = self.buscar_reserva(identificador_reserva)
        if reserva == None:
            print(
                f'La reserva con identificador {identificador_reserva} no existe')
            return

        if reserva.alojamiento.anfitrion.identificacion != identificacion_anfitrion:
            print(
                f'La reserva con identificador {identificador_reserva} no corresponde al anfitrion con identificacion {identificacion_anfitrion}')
            return

        if reserva.estado != 'Pendiente':
            print('Solo se pueden aceptar reservas pendientes')
            return

        anfitrion.aceptar_reserva(reserva, aceptar)

    def eliminar_usuario(self, identificacion: str) -> 'Usuario' | None:
        indice = 0
        while indice < self.numero_usuarios and self.usuarios[indice].identificacion != identificacion:
            indice += 1

        if indice == self.numero_usuarios:
            print(f'El usuario con identificacion {identificacion} no existe')
            return

        usuario = self.usuarios[indice]
        while indice < self.numero_usuarios - 1:
            self.usuarios[indice] = self.usuarios[indice + 1]
            indice += 1

        self.usuarios[self.numero_usuarios - 1] = None
        self.numero_usuarios -= 1

        return usuario

    def eliminar_alojamiento(self, identificador: str) -> 'Alojamiento' | None:
        indice = 0
        while indice < self.numero_alojamientos and self.alojamientos[indice].identificador != identificador:
            indice += 1

        if indice == self.numero_alojamientos:
            print(
                f'El alojamiento con identificador {identificador} no existe')
            return

        alojamiento = self.alojamientos[indice]
        while indice < self.numero_alojamientos - 1:
            self.alojamientos[indice] = self.alojamientos[indice + 1]
            indice += 1

        self.alojamientos[self.numero_alojamientos - 1] = None
        self.numero_alojamientos -= 1

        return alojamiento

    def eliminar_reserva(self, identificador: str) -> 'Reserva' | None:
        indice = 0
        while indice < self.numero_reservas and self.reservas[indice].identificador != identificador:
            indice += 1

        if indice == self.numero_reservas:
            print(f'La reserva con identificador {identificador} no existe')
            return

        reserva = self.reservas[indice]
        while indice < self.numero_reservas - 1:
            self.reservas[indice] = self.reservas[indice + 1]
            indice += 1

        self.reservas[self.numero_reservas - 1] = None
        self.numero_reservas -= 1

        return reserva
