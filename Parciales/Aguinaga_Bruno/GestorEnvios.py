

class GestorEnvios:
    def __init__(self):
        self.__nombreGestor = "Gestor de Envios"
        self.__versionGestor = 4.1

    def gestionarEnvios(self,transportes,paquete):
        print("Gestionando envio del paquete pesado:"	)
        for transporte in transportes:
            if transporte.transportarPaquete(paquete.getDistancia(),paquete.getPesoVolumetrico()) == -1:
                print(f"El/la {transporte.getTipoTransporte()} no puede transportar el paquete")
            else:
                if transporte.getTipoTransporte() == "Cartero":
                    costo1 = transporte.transportarPaquete(paquete.getDistancia(),paquete.getPesoVolumetrico())
                    print(f"El Cartero tarda {paquete.getDistancia() / transporte.getVelocidadPromedio()} hs, con un costo de {costo1}, indicador de costo de {costo1/paquete.getDistancia()}")
                    print("El mejor indicador de costo es: ",costo1/paquete.getDistancia())
                else:
                    costo2 = transporte.transportarPaquete(paquete.getDistancia(),paquete.getPesoVolumetrico())
                    print(f"La Furgoneta tarda {paquete.getDistancia() / transporte.getVelocidadPromedio()} hs, con un costo de {costo2}, indicador de costo de {costo2/paquete.getDistancia()}")
                    print("El mejor indicador de costo es: ",costo2/paquete.getDistancia())
