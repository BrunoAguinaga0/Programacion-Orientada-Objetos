from Component import Component


class Carpeta(Component):
    def __init__(self, nombre_archivo):
        self.__componentes = []
        self.__nombre_archivo = nombre_archivo

    def add(self, component):
        self.__componentes.append(component)

    def remove(self, component):
        self.__componentes.remove(component)

    def es_carpeta(self):
        return True

    def operacion(self):
        nombre_carpeta = [f"Carpeta: {self.__nombre_archivo} ⬇"]
        for componente in self.__componentes:
            nombre_carpeta.append(componente.operacion())
        return "\n".join(nombre_carpeta)
