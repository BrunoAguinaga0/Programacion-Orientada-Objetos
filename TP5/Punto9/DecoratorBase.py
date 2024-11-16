from ProductoComponent import ProductoComponent


class DecoratorBase(ProductoComponent):
    def __init__(self, producto):
        self.__producto = producto

    def get_precio(self):
        pass
