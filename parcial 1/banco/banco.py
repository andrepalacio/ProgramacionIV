#Autor: Ing(c). Andres Palacio Sanchez

from cliente import Cliente

class Banco:

    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, nombre, cantidad):
        n_cliente = Cliente(nombre, cantidad)
        self.clientes.append(n_cliente)

    def existe_cliente(self, cliente):
        for cli in self.clientes:
            if cli.nombre == cliente:
                return True
        return False

    #modulo de llamado del metodo del cliente que se operara
    #el parametro operar es la accion seleccionada por el ciente
    def operar(self, cliente, operar):
        for cli in self.clientes:
            if cli.nombre == cliente:
                if operar == 1:
                    cli.depositar()
                elif operar == 2:
                    cli.extraer()
                elif operar == 3:
                    cli.mostrar_total()
                else:
                    print("Tipo de operacion erronea")
                return True
        return False

    def deposito_total(self):
        total = 0
        for cli in self.clientes:
            total = total + cli.cantidad
        print(f"Deposito total del dia: $ {total}")

    def listar_clientes(self):
        print("Datos de todos los clientes\n")
        for cli in self.clientes:
            print(cli)