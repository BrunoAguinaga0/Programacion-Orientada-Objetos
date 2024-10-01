from Cuenta import Cuenta

class CuentaBancaria(Cuenta):
    def __init__(self, dueño, saldo, nroCuenta, cvu):
        super().__init__(dueño, saldo, nroCuenta)
        self._cvu = cvu
    
    
    def pagarCredito(self, monto, cuotas):
        if cuotas > 1:
            self._saldo -= monto
        else: 
            monto = monto * (1 + (0.08 * cuotas))
            self._saldo -= monto / cuotas