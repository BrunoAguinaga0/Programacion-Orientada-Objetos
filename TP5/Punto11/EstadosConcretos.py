from Estado import Estado


class Abierto(Estado):
    def actividad(self, nroTurno, nombreCliente, edadCliente):
        print(f"Siguiente Turno: {nroTurno} - {nombreCliente}")

    def abrir_caja(self):
        print("Caja Abierta")

    def cerrar_caja(self, Banco):
        Banco.set_estado(Cerrado())

    def suspender_caja(self, Banco):
        Banco.set_estado(Suspendido())


class Suspendido(Estado):
    def actividad(self, nroTurno, nombreCliente, edadCliente):
        if edadCliente < 60:
            print(
                f"Turno {nroTurno} - Caja Suspendida - Atencion a personas mayores a 60 Años"
            )
        else:
            print(f"Siguiente Turno: {nroTurno} - {nombreCliente}")

    def abrir_caja(self, Banco):
        Banco.set_estado(Abierto())

    def cerrar_caja(self, Banco):
        print("Caja Cerrada")

    def suspender_caja(self, Banco):
        Banco.set_estado(Suspendido())


class Cerrado(Estado):
    def actividad(self, nroTurno, nombreCliente, edadCliente):
        print("La caja esta cerrada, no se pueden atender personas.")

    def abrir_caja(self, Banco):
        Banco.set_estado(Abierto())

    def cerrar_caja(self, Banco):
        Banco.set_estado(Cerrado())

    def suspender_caja(self, Banco):
        print("Caja Suspendida")
