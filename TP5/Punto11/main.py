from EstadosConcretos import Abierto, Cerrado, Suspendido
from Banco import Banco

if __name__ == "__main__":
    caja = Banco(1)
    # CAJA CERRADA
    print("--------- CAJA CERRADA ---------")
    caja.atender_persona(1, "Juan", 25)
    # CAJA ABIERTA
    print("--------- CAJA ABIERTA ---------")
    caja.abrir_caja()
    caja.atender_persona(2, "Pedro", 30)
    caja.atender_persona(3, "Luis", 40)
    caja.atender_persona(4, "Maria", 50)
    # CAJA SUSPENDIDA
    print("--------- CAJA SUSPENDIDA ---------")
    caja.suspender_caja()
    caja.atender_persona(5, "Pedro", 30)
    caja.atender_persona(6, "Luis", 70)
    caja.atender_persona(7, "Maria", 64)
