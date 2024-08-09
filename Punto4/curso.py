

class Curso:
    def __init__(self,nombre,instructores,imagen,valoracion,precio,descuento) -> None:
        self.__nombre = nombre
        self.__instructores = instructores
        self.__imagen = imagen
        self.__valoracion = valoracion
        self.__precio = precio
        self.__descuento = descuento
        self.__etiqueta = None
    
    
    @property
    def etiqueta(self):
        return self.__etiqueta
    
    
    @etiqueta.setter
    def etiqueta(self,etiquetaEntrada):
        self.__etiqueta = etiquetaEntrada
        
    @property
    def nombre(self):
        return self.__nombre
    
    
    @property
    def instructores(self):
        return self.__instructores
    
    
    @property
    def imagen(self):
        return self.__imagen
    
    
    @property
    def valoracion(self):
        return self.__valoracion
    
    
    @property
    def precio(self):
        return self.__precio
    
    
    @property
    def descuento(self):
        return self.__descuento