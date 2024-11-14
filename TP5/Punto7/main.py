from fecade import fachada
from helper1 import helper1
from helper2 import helper2

helper1 = helper1()
helper2 = helper2()
fachada = fachada(helper1, helper2)

# print(fachada.operation("perro"))
print(fachada.operation("zorro"))
