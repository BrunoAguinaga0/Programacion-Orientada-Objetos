from threading import Thread


class contador(Thread):
    def __init__(self, nro_hilo):
        super().__init__()
        self.__nro_hilo = nro_hilo

    def run(self):
        global contadorNum
        for i in range(250):
            contadorNum += 1
            print(
                f"Contador:{contadorNum} - Se sumo +1 al contador desde el hilo:{self.__nro_hilo}"
            )


if __name__ == "__main__":
    contadorNum = 0
    for i in range(4):
        hilo = contador(i)
        hilo.start()
        hilo.join()
print(contadorNum)
