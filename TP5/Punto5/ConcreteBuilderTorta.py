from BuilderTorta import BuilderTorta
from Torta import Torta


class ConcreteBuilderTortaVainilla(BuilderTorta):
    def __init__(self) -> None:
        self.reset()
    
    def reset(self) -> None:
        self.__torta = Torta()
    
    @property
    def get_torta(self) -> Torta:
        torta = self.__torta
        self.reset()
        return torta
    
    def produce_masa(self) -> None:
        print("Elige el sabor de la masa: \n"
            "1. Vainilla\n"
            "2. Chocolate\n"
            "3. Coco\n")
        eleccion = int(input())
        if eleccion == 1:
            self.__torta.add("Masa: Vainilla")
            self.__torta.set_masa("Vainilla")
        elif eleccion == 2:
            self.__torta.add("Masa: Chocolate")
            self.__torta.set_masa("Chocolate")
        else:
            self.__torta.add("Masa: Coco")
            self.__torta.set_masa("Coco")
    
    def produce_relleno(self) -> None:
        self.__torta.add("Relleno: Frutillas")
        self.__torta.set_relleno("Frutillas")
    
    def produce_decoracion(self) -> None:
        self.__torta.add("Decoracion: Glaseado")