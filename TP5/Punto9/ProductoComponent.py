from abc import ABC, abstractmethod


class ProductoComponent(ABC):
    def __init__(self, id_producto, nombre, precio):
        self._id_producto = id_producto
        self._nombre = nombre
        self._precio = precio

    @abstractmethod
    def get_precio(self):
        pass
