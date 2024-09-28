from cuenta import Cuenta

class BilleteraVirtual(Cuenta):
    def __init__(self, nombre, saldo, nroCuenta,cvu):
        super().__init__(nombre, saldo, nroCuenta)
        self._cvu = cvu
        
    def pagarDebito(self, monto):
        self._saldo -= monto
        
    def pagarCredito(self, monto, cuotas):
        match cuotas:
            case 1:
                self._saldo -= monto
            case (3,6,9,12):
                self._saldo -= (monto  * (1 + (0.08 * cuotas))) / cuotas
                