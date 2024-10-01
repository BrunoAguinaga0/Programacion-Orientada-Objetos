

class Usuario:
    def __init__(self, nombre, apellido, email, password):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__password = password
        self.__perfil = []

    def agregar_perfil(self, perfil):
        self.__perfil.append(perfil)
    
    def imprimir_perfiles(self):
        for perfil in self.__perfil:
            perfil.imprimir()
    