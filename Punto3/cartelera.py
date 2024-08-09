


class Cartelera:
    def __init__(self):
        self.__listado = []


    def añadir(self,estreno):
        self.__listado.append(estreno)



    def imprimir(self,categoria):
        print(categoria)
        for lista in self.__listado:
            print(lista.imagensg)
            print("Nuevos episodios los",lista.diasg )
            print(lista.nombresg)