from DecoratorBase import DecoratorBase


class DecoratorUSD(DecoratorBase):
    def __init__(self, producto):
        self.__component = producto

    def get_precio(self):
        return f"$USD {self.__component.get_precio()}"
