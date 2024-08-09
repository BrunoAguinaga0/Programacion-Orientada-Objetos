


class Cartelera:
    def __init__(self):
        self.listado = []


    def añadir(self,estreno):
        self.listado.append(estreno)



    def imprimir(self,categoria):
        print(categoria)
        for lista in self.listado:
            print(lista.imagensg)
            print("Nuevos episodios los",lista.diasg )
            print(lista.nombresg)