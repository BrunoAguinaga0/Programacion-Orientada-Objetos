from EstadosConcretos import *


class Banco:
    def __init__(self, nroCaja):
        self._estado = Cerrado()
        self.__nroCaja = nroCaja

    def set_estado(self, estado):
        self._estado = estado

    def get_estado(self):
        return self._estado

    def atender_persona(self, nroTurno, Cliente, edadCliente):
        self._estado.actividad(nroTurno, Cliente, edadCliente)

    def cerrar_caja(self):
        self._estado.cerrar_caja(self)

    def abrir_caja(self):
        self._estado.abrir_caja(self)

    def suspender_caja(self):
        self._estado.suspender_caja(self)
