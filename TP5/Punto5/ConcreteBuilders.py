from BuilderTorta import BuilderTorta
from Torta import Torta


class ConcreteBuilderTortaVainilla(BuilderTorta):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.__torta = Torta()

    def get_torta(self) -> Torta:
        torta = self.__torta
        self.reset()
        return torta

    def produce_masa(self) -> None:
        self.__torta.set_masa("Vainilla")

    def produce_relleno(self) -> None:
        self.__torta.set_relleno("Frutillas")


class ConcreteBuilderTortaChocolate(BuilderTorta):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.__torta = Torta()

    def get_torta(self) -> Torta:
        torta = self.__torta
        self.reset()
        return torta

    def produce_masa(self) -> None:
        self.__torta.set_masa("Chocolate")

    def produce_relleno(self) -> None:
        self.__torta.set_relleno("Bananas")


class ConcreteBuilderTortaCoco(BuilderTorta):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.__torta = Torta()

    def get_torta(self) -> Torta:
        torta = self.__torta
        self.reset()
        return torta

    def produce_masa(self) -> None:
        self.__torta.set_masa("Coco")

    def produce_relleno(self) -> None:
        self.__torta.set_relleno("Durazno")
