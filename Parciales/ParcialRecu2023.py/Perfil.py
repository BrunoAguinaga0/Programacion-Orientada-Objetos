

class Perfil:
    def __init__(self, nombre, controlParental):
        self.__nombrePerfil = nombre
        self.__controlParental = controlParental
        self.__multimedia = []
        
    def agregar_multimedia(self, serie):
        self.__multimedia.append(serie)
    
    def nombre(self):
        return self.__nombre
    
    def controlParental(self):
        if self.__controlParental == True:
            return "Si"
        else:
            return "No"
    
    def multimedias(self):
        return self.__multimedia
    
    def imprimir(self):
        print(f"Nombre: {self.__nombrePerfil}")
        print(f"Control parental: {self.controlParental()}")
        for multimedia in self.__multimedia:
            multimedia.imprimirMultimedia()