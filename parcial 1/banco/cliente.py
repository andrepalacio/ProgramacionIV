#Autor: Ing(c). Andres Palacio Sanchez

class Cliente:

    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def depositar(self):
        print("Depositar Dinero")
        deposito = input("Cantidad que desea depositar: ")
        try:
            deposito = float(deposito)
        except:
            deposito = -1.0
        if deposito > 0.0:
            self.cantidad = self.cantidad + deposito
            print("Deposito realizado")
        else:
            print("Error en el valor a ingresar")

    def extraer(self):
        print("Extraer dinero")
        retiro = input("Cantidad que desea extraer: ")
        try:
            retiro = float(retiro)
        except:
            retiro = -1.0
        if retiro > 0.0:
            if self.cantidad >= retiro:
                self.cantidad = self.cantidad - retiro
                print("Retiro realizado")
            else:
                print("El saldo en la cuenta es insuficiente")
        else:
            print("Error en el valor solicitado")

    def mostrar_total(self):
        print(f"Valor total en la cuenta: $ {self.cantidad}")

    def __str__(self):
        return f"Nombre: {self.nombre}\nCantidad: {self.cantidad}\n"