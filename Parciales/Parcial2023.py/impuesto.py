

class Impuesto:
    def __init__(self, nombre,periodo,monto,estado):
        self._nombre = nombre
        self._monto = monto
        self._estado = False
        self._periodo = periodo
        self._comprobante = None

    def validarPago(self,monto,periodo,comprobante):
        if monto == self._monto and self._periodo == periodo:
            self._estado = True
            self._comprobante = comprobante
