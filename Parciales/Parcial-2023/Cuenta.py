from abc import ABC,abstractmethod

class Cuenta(ABC):
    def __init__(self, dueño, saldo, nroCuenta):
        self._dueño = dueño 
        self._saldo = saldo
        self._nroCuenta = nroCuenta
    
    
    def pagarDebito(self, monto):
        if self._saldo < monto:
            return False
        else:
            self._saldo -= monto
            return True
    
    @abstractmethod
    def pagarCredito(self, monto, cuotas):
        pass