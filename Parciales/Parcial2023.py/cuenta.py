from abc import ABC, abstractmethod


class Cuenta(ABC):
    def __init__(self, nombre, saldo, nroCuenta):
        self._nombre = nombre
        self._saldo = saldo
        self._nroCuenta = nroCuenta

    @abstractmethod
    def pagarDebito(self, monto):
        pass
    
    @abstractmethod
    def pagarCredito(self, monto):
        pass
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def nroCuenta(self):
        return self._nroCuenta