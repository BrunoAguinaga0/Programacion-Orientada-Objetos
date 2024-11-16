from DecoratorBase import DecoratorBase


class DecoratorARS(DecoratorBase):
    def __init__(self, producto):
        self.__component = producto

    def get_precio(self):
        return f"$ARS {self.__component.get_precio()}"
