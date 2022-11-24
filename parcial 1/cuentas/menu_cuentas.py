#Autor: Ing(c). Andres Palacio Sanchez

import os #se importa os para limpiar y pausar la consola
from cuentas import * #se importan las clases utilizadas

#Clase que gestiona las cuentas creadas y validez de datos ingresados
class Gestor:
    def __init__(self) -> None:
       self.cuentas = []

    def validador_int(self, dato) -> int:
        try:
            dato = int(dato)
        except:
            dato = 0
        return dato

    def validador_float(self, dato) -> float:
        try:
            dato = float(dato)
        except:
            dato = -1.0
        return dato

    def validador_titular(self, titular) -> bool:
        for ct in self.cuentas:
            if ct.titular == titular:
                return False
        return True

gestor = Gestor()
opcion = 1 #opcion del menu
#Declaracion del menu
while 0<=opcion and opcion<3:
   os.system("cls")
   print(" Gestor de cuentas\n1. Crear una cuenta\n2. Mostrar cuentas\n3. Salir")
   opcion = input("Elija una opcion: ")
   opcion = gestor.validador_int(opcion)
   if opcion == 1:
      print(" Tipos de cuentas\n1. Caja ahorro\n2. Plazo Fijo")
      tipo = input("Seleccione el tipo: ")
      tipo = gestor.validador_int(tipo)
      if tipo == 1:
         titular = input("Nombre del titular: ")
         if gestor.validador_titular(titular):
            cantidad = input("Cantidad inicial de la cuenta: ")
            cantidad = gestor.validador_float(cantidad)
            if cantidad >= 0.0:
                  cuenta = CajaAhorro(titular, cantidad)
                  gestor.cuentas.append(cuenta)
            else:
               print("Error: cantidad inicial no valida")
         else:
            print("El titular ya se encuentra resgistrado")
      elif tipo == 2:
         titular = input("Nombre del titular: ")
         if gestor.validador_titular(titular):
            cantidad = input("Cantidad inicial de la cuenta: ")
            cantidad = gestor.validador_float(cantidad)
            if cantidad >= 0.0:
               plazo = input("Plazo de la cuenta: ")
               interes = input("Interes de la cuenta: ")
               interes = gestor.validador_float(interes)
               if interes >= 0.0:
                  cuenta = PlazoFijo(titular, cantidad, plazo, interes)
                  gestor.cuentas.append(cuenta)
               else:
                  print("Error: interse de cuenta no valido")   
            else:
               print("Error: cantidad inicial no valida")
         else:
            print("El titular ya se encuentra resgistrado")
      else:
         print("Error en la seleccion de cuenta")
   elif opcion == 2:
      if len(gestor.cuentas) > 0:
         print("Cuentas registradas")
         for ct in gestor.cuentas:
            ct.imprimir_cuenta()
      else:
         print("No hay cuentas registradas")
   elif opcion == 3:
      print("Gracias por usar el aplicativo")
   else:
      print("La opcion seleccionada no es valida")
   os.system("pause")