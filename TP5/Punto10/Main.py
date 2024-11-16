from SistemaMetereologico import SistemaMetereologico
from Reportero import Reportero

sistema = SistemaMetereologico()
reportero1 = Reportero("Juan", "Perez", 25, 5000, "Informatica")

sistema.suscribirse(reportero1)
sistema.set_clima("soleado")
sistema.set_clima("nublado")
sistema.set_clima("lluvioso")
