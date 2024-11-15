from Component import Component


class Archivo(Component):  # Hoja del Arbol
    def __init__(self, nombre_archivo):
        self.__nombre_archivo = nombre_archivo

    def operacion(self):
        return f"Archivo: {self.__nombre_archivo}"
