from ProductoComponent import ProductoComponent


class ProductoConcreto(ProductoComponent):
    def __init__(self, id_producto, nombre, precio):
        super().__init__(id_producto, nombre, precio)

    def get_precio(self):
        return f"{self._precio:.2f}"
