import random

def numeroaleatorios():
    num1 = 0
    num2 = 0
    while num1 == num2:
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
    return num1,num2

