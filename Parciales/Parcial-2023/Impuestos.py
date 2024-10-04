

class Impuestos():
    def __init__(self, nombre, monto, periodo):
        self._nombre = nombre
        self._monto = monto
        self._periodo = periodo
        self._estado = False
        self._comprobante = None
    
    
    def validarPago(self,monto,periodo):
        pass