#Autor: Ing(c). Andres Palacio Sanchez

class Cuenta():
   def __init__(self, titular, cantidad) -> None:
      self.titular = titular
      self.cantidad = cantidad
   
   def imprimir_cuenta(self) -> None:
      print("\nTitular: {0}\nCantidad: {1}".format(self.titular, self.cantidad))

class CajaAhorro(Cuenta):
   def __init__(self, titular, cantidad) -> None:
      super().__init__(titular, cantidad)
   
   def imprimir_cuenta(self) -> None:
      super().imprimir_cuenta()

class PlazoFijo(Cuenta):
   def __init__(self, titular, cantidad, plazo, interes) -> None:
      super().__init__(titular, cantidad)
      self.plazo = plazo
      self.interes = interes
      self.interes_total = self.calcular_interes(interes, cantidad)

   def calcular_interes(self, interes, cantidad) -> float:
      return (cantidad*interes/100)

   def imprimir_cuenta(self) -> None:
      super().imprimir_cuenta()
      print(f"Plazo: {self.plazo}\nInteres: {self.interes}\nTotal de interes: {self.interes_total}")