from Cuenta import Cuenta

class CuentaBancaria(Cuenta):
    def __init__(self, nombre, saldo, nroCuenta, cbu):
        super().__init__(nombre, saldo, nroCuenta)
        self._cbu = cbu
    
    
    def pagarDebito(self, monto):
        if super().pagarDebito(monto):
            self._saldo += monto * 0.1
            return True
        else:
            return False
        
    
    
    def pagarCredito(self, monto, cuotas):
        if cuotas > 3:
            monto = (monto * (1 + (0.02 * cuotas))) / cuotas
            if self._saldo >= monto:
                self._saldo -= monto
                return True
            else:
                return False
        else:
            if self._saldo >= (monto / cuotas):
                self._saldo -= monto / cuotas
                return True
            else:
                return False