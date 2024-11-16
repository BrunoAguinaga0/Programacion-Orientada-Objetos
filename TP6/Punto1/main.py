from threading import Thread


class escribir(Thread):
    def __init__(self, nro_hilo):
        super().__init__()
        self.__nro_hilo = nro_hilo

    def run(self):
        print("Hola Mundo, desde el hilo nro:", self.__nro_hilo)


if __name__ == "__main__":
    for i in range(6):
        hilo = escribir(i)
        hilo.start()
