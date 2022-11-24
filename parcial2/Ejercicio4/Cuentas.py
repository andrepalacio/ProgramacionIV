class Cuenta_Bancaria:

    def __init__(self, numero, nombre) -> None:
        self.numero_cuenta = numero
        self.nombre_titular = nombre
        self.saldo = 0.0
        self.numero_operaciones = 0
        self.MAXIMO_REINTEGRO = 5000
        self.cuentas_creadas = 1

    def get_numero_cuenta(self):
        return self.numero_cuenta
    def get_nombre_titular(self):
        return self.nombre_titular
    
    def get_saldo(self):
        return self.saldo
    def set_saldo(self, valor):
        self.saldo = valor
    
    def get_numero_operaciones(self):
        return self.numero_operaciones
    def ingresar_cantidad(self, cant):
        if cant > 0:
            self.saldo += cant
            self.numero_operaciones += 1
            return True
        else:
            print("Valor a ingresar erróneo")
            return False
    def retirar_cantidad(self, cant):
        if cant > self.MAXIMO_REINTEGRO:
            print("La cantidad supera el máximo de reintegro")
        else:
            if cant > self.saldo:
                print("La cantidad supera el saldo disponible")
            else:
                self.saldo -= cant
                self.numero_operaciones += 1
                return True
        return False

    def get_cuentas_creadas(self):
        return self.cuentas_creadas
    def set_cuentas_creadas_null(self):
        self.cuentas_creadas = 0
    def set_cuentas_creadas(self, x):
        self.cuentas_creadas = x

class Cuenta_Joven(Cuenta_Bancaria):

    def __init__(self, numero, nombre):
        super().__init__(numero, nombre)

    def ingresar_cantidad(self, cant):
        return super().ingresar_cantidad(cant)

    def retirar_cantidad(self, cant):
        return super().retirar_cantidad(cant)
