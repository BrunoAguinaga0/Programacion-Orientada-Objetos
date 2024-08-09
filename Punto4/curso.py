

class Curso:
    def __init__(self,nombre,instructores,imagen,valoracion,precio,descuento) -> None:
        self.__nombre = nombre
        self.__instructores = instructores
        self.__imagen = imagen
        self.valoracion = valoracion
        self.precio = precio
        self.descuento = descuento
        self.etiqueta = None
    
    
    