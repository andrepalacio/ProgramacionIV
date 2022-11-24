#Autor: Ing(c). Andres Palacio Sanchez
from banco import Banco
import os #se importa os para limpiar y pausar la consola

opcion = 1 #opcion del menu
banco = Banco()
while opcion != 5:
    os.system("cls")
    print("Menu Banco\n1. Crear nuevo cliente\n2. Operar funcion bancaria\n3. Mostrar deposito total\n4. Listar todos los clientes\n5. Cerrar menu")
    opcion = input("Elija una opcion: ")
    try:
        opcion = int(opcion)
    except:
        opcion == 0
    if opcion == 1:
        print("\nRegistrar nuevo cliente")
        nombre = input("Nombre del cliente: ")
        if banco.existe_cliente(nombre):
            print("El cliente ya esta registrado")
        else:
            cant = input("Cantidad al abrir la cuenta: ")
            try:
                cant = float(cant)
            except:
                cant = -1.0
            if cant > 0.0:
                banco.agregar_cliente(nombre, cant)
            else:
                print("Error: el valor inicial de la cuenta no es valido")
    elif opcion == 2:
        if len(banco.clientes) == 0:
            print("No hay clientes registrados\nRegistre un cliente para poder operar")
        else:
            print("\nOperaciones Bancarias")
            cliente = input("Ingrese el nombre del cilente: ")
            if banco.existe_cliente(cliente):
                print("Operacion que desea realizar\n1. Depositar\n2. Extraer\n3. Mostrar saldo total")
                operar = input("Elija una opcion: ")
                try:
                    operar = int(operar)
                except:
                    operar = 0
                banco.operar(cliente, operar)
            else:
                print("El cliente no existe")
    elif opcion == 3:
        if len(banco.clientes) == 0:
            print("No hay clientes registrados\nEl deposito total es $ 0")
        else:
            banco.deposito_total()
    elif opcion == 4:
        if len(banco.clientes) == 0:
            print("No hay clientes registrados\n")
        else:
            banco.listar_clientes()
    elif opcion == 5:
        print("Adios, regrese pronto")
    else:
        print("Opcion erronea")
    os.system("pause")