
from Movistar import Movistar
from Claro import Claro
from Personal import Personal

movistar = Movistar("Movistar",5000,150,5)
claro = Claro("Claro",3000,200,8)
personal = Personal("Personal",4000,180,6)

print(f"Compañia: {claro.getNombre()} - Valor de los 5000 mensajes: ${claro.calcularSMS()} - Valor de las llamadas realizadas: ${claro.calcularConsumoLlamada()} - Valor de los GIGAS: ${claro.calcularGigas()}")
print(f"Compañia: {personal.getNombre()} - Valor de los 5000 mensajes: ${personal.calcularSMS()} - Valor de las llamadas realizadas: ${personal.calcularConsumoLlamada()} - Valor de los GIGAS: ${personal.calcularGigas()}")
print(f"Compañia: {movistar.getNombre()} - Valor de los 5000 mensajes: ${movistar.calcularSMS()} - Valor de las llamadas realizadas: ${movistar.calcularConsumoLlamada()} - Valor de los GIGAS: ${movistar.calcularGigas()}")