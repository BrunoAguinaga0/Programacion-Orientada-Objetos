
class Medicamentos:
    def __init__(self,nombre,precio,dosis,unidad):
        self.nombre = nombre
        self.precio = precio
        self.dosis = dosis
        self.unidad = unidad

class Ticket:
    def __init__(self,medicamento,fecha,nro):
        self.medicamento = medicamento
        self.fecha = fecha
        self.nro = nro
        self.total = 0
        for medicamentos in self.medicamento:
            self.total += medicamentos.precio
    def imprimir (self):
        print("")
        print(f"Nro de venta:{self.nro}                      Fecha: {self.fecha} ")
        print("")
        print(f"Articulos:                 Dosis:                Precio:")
        for medi1 in self.medicamento:
            print(f"{medi1.nombre}                   {medi1.dosis}                  ${medi1.precio}")
        print("")
        print(f"                                             Total: ${self.total}")
medicamento = [Medicamentos("Ibuprofeno",1800,"10","gr"),Medicamentos("Paracetamo",2000,10,"mg"),Medicamentos("Aspirinass",2500,20,"Mg")]
ticket = Ticket(medicamento,"06/08/24",549831)
ticket.imprimir()