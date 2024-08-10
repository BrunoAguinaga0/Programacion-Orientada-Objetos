

import random

numeroaleatorio = random.randint(1,10)

numero = int(input("Ingrese un numero:"))

def mayorigual(numero,numeroaleatorio):
    if numero < numeroaleatorio:
        print(numero,"es menor a",numeroaleatorio)
    elif numero > numeroaleatorio:
        print(numero,"es mayor a",numeroaleatorio)
    else:
        print(numero,"es igual a",numeroaleatorio)

print("el numero aleatorio es:",numeroaleatorio)
mayorigual(numero,numeroaleatorio)