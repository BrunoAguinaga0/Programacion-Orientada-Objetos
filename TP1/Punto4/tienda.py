

class Tienda:
    def __init__(self):
        self.__lista_cursos = []
    
    
    def agregarcursos(self, curso):
        self.__lista_cursos.append(curso)
    
    def imprimir (self):
        for lista in self.__lista_cursos:
            print("")
            print("Curso:",lista.nombre)
            print("Instructor/es:",lista.instructores)
            print("Imagen:",lista.imagen)
            print("Valoracion:",lista.valoracion)
            print("Precio: $",lista.precio,"Descuento: $",lista.descuento)
            print(lista.etiqueta)