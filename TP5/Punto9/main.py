from ProductoConcreto import ProductoConcreto
from DecoratorARS import DecoratorARS
from DecoratorUSD import DecoratorUSD

Producto1 = ProductoConcreto(1, "Coca Cola", 1200.456)
precioARS = DecoratorARS(Producto1)
precioUSD = DecoratorUSD(Producto1)

print(Producto1.get_precio())
print(precioARS.get_precio())
print(precioUSD.get_precio())
