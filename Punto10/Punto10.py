

peso = float(input("Ingrese su peso en kg, por ej 75,4 kg: "))
altura = float(input("Ingrese su altura en mts y centimetros, por ej: 1,71 mts: "))

def calculo(peso,altura):
    masacorporal = peso / (altura ** 2)
    print("Su indice de masa corporal es: ",masacorporal)

calculo(peso,altura)

