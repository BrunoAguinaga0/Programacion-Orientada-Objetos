from Observador import Observador


class Reportero(Observador):
    def __init__(self, nombre, apellido, edad, sueldo, area):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._sueldo = sueldo
        self._area = area

    def actualizar(self, clima):
        print("El clima actual es:", clima)
