import random


def numeroaleatorios():
    num1 = 0
    num2 = 0
    while num1 == num2:
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        return num1,num2

perdidas = 0
ganadas = 0
jugar = True
while jugar:
    num1,num2 = numeroaleatorios()
    eleccion = int(input("Elija el numero 1 o 2: "))
    match eleccion:
        case 1:
            if num1 < num2:
                print("Perdiste, numero 1:",num1," numero 2:",num2)
                perdidas = perdidas + 1
            else:
                print("Ganaste, numero 1:",num1,"numero 2:",num2)
                ganadas = ganadas + 1
        case 2:
            if num2 < num1:
                print("Perdiste, numero 1:",num1," numero 2:",num2)
                perdidas = perdidas + 1
            else:
                print("Ganaste, numero 1:",num1,"numero 2:",num2)
                ganadas = ganadas + 1
    rta = input("Desea seguir jugando? S/N: ")
    if rta == 'n' or rta == 'N':
        jugar = False
print("Partidas ganadas:",ganadas,"Partidas perdidas:",perdidas)


