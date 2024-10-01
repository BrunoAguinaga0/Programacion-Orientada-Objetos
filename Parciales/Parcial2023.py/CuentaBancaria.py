from cuenta import Cuenta


class CuentaBancaria(Cuenta):
    def __init__(self, nombre, saldo, nroCuenta, cbu):
        super().__init__(nombre, saldo, nroCuenta)
        self._cbu = cbu
        
    def pagarDebito(self, monto):
        self._saldo += monto
        self._saldo += monto * 0.1
        
    def pagarCredito(self, monto, cuotas):
        match cuotas:
            case 1:
                self._saldo -= monto
            case 3: 
                self._saldo -= monto / 3
            case (6,9,12):
                self._saldo -= (monto  * (1 + (0.02 * cuotas))) / cuotas