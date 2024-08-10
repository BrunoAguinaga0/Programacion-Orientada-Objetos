from nis import match
import random


def numeroaleatorios():
    num1 = 0
    num2 = 0
    while num1 == num2:
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
    return num1,num2

jugar = True
while jugar:
    num1,num2 = numeroaleatorios()
    eleccion = int(input("Elija el numero 1 o 2: "))
    match eleccion:
        case 1:
            if num1 < num2:
                print("Perdiste, numero 1: ",num1," numero 2: ",num2)
                
            


