#Autor: Ing(c). Andres Palacio Sanchez

from agenda import *
import os #se importa os para limpiar y pausar la consola

agenda = Agenda()
opcion = 1 #opcion del menu
while(0<opcion) and (opcion<5):
    os.system("cls")
    print(" Menú \n1. Añadir contacto\n2. Listar contactos\n3. Buscar contacto\n4. Editar contacto\n5. Cerrar agenda")
    opcion = int(input("Elija una opción: "))
    if opcion == 1:
        print("\nCrear nuevo contacto")
        agenda.nuevo_contacto()
    elif opcion == 2:
        print("Contactos en la agenda\n")
        agenda.listar_contactos()
    elif opcion == 3:
        print("Buscar contacto")
        nombre = input("Ingrese nombre del contacto a buscar: ")
        if agenda.existe_contacto(nombre):
            agenda.buscar_contacto(nombre)
        else:
            print("El contacto no se encuentra guardado en la agenda")
    elif opcion == 4:
        print("Editar contacto")
        nombre = input("Ingrese nombre del contacto a editar: ")
        if agenda.existe_contacto(nombre):
            print("¿Qué información desea editar?\n1. Nombre\n2. Telefono\n3. Email")
            op = int(input("Elija una opción: "))
            agenda.editar_contacto(nombre, op)
        else:
            print("El contacto no se encuentra guardado en la agenda")
    else:
        print("Adiós...")
    os.system("pause")

