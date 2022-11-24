#Autor: Ing(c). Andres Palacio Sanchez

import os #se importa la libreria para limpiar la consola y pausarla

class Calculadora:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.suma = self.sumar()
        self.resta = self.restar()
        self.mult = self.multiplicar()
        self.divi = self.dividir()
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x
        self.suma = self.sumar()
        self.resta = self.restar()
        self.mult = self.multiplicar()
        self.divi = self.dividir()
    
    def set_y(self, y):
        self.y = y
        self.suma = self.sumar()
        self.resta = self.restar()
        self.mult = self.multiplicar()
        self.divi = self.dividir()

    def __str__(self) -> str:
        return "\nx = {0}  y = {1}\nsuma = {2}\nresta = {3}\nmultiplicacion = {4}\ndivision = {5}\n".format(self.x, self.y, self.suma, self.resta, self.mult, self.divi)

    def sumar(self):
        return self.x + self.y
    
    def restar(self):
        return self.x - self.y
    
    def multiplicar(self):
        return self.x * self.y

    def dividir(self):
        return self.x // self.y

calc = None #esta variable guardara el objeto de clase calculadora
opcion = 1 #opcion del menu
#Declaracion del menu
while opcion != 5:
    os.system("cls")
    if calc == None: #verifica si existe un objeto calculadora
        print("Calculadora Basica\nLa calculadora no ha sido inicializada")
    else:    
        print("Calculadora Basica\nLa calculadora esta activa\nx = {0}  y = {1}".format(calc.x, calc.y))
    print("1. Inicializar calculadora\n2. Ingresar valor para x\n3. Ingresar valor para y\n4. Mostrar operaciones\n5. Salir")
    opcion = input("Elija una opcion: ")
    try: 
        opcion = int(opcion)
    except:
        opcion = 0 #el valor 0 se toma como caso error por defecto
    if opcion == 1:
        while True:
            x = input("Ingrese valor para x: ")
            try:
                x = int(x)
                break
            except:
                print("Error: El dato ingresado no es un numero entero")
        while True:
            y = input("Ingrese valor para y: ")
            try:
                y = int(y)
                break
            except:
                print("Error: El dato ingresado no es un numero entero")
        calc = Calculadora(x, y)
        print(calc)
    elif opcion == 2:
        if calc != None:
            while True:
                x = input("Ingrese valor para x: ")
                try:
                    x = int(x)
                    break
                except:
                    print("Error: El dato ingresado no es un numero entero")
            calc.set_x(x)
        else:
            print("Error: La calculadora no ha sido inicializada")
    elif opcion == 3:
        if calc != None:
            while True:
                y = input("Ingrese valor para y: ")
                try:
                    y = int(y)
                    break
                except:
                    print("Error: El dato ingresado no es un numero entero")
            calc.set_y(y)
        else:
            print("Error: La calculadora no ha sido inicializada")
    elif opcion == 4:
        if calc != None:
            print(calc)
        else:
            print("Error: La calculadora no ha sido inicializada")
    elif opcion == 5:
        print("Gracias por utilizar el aplicativo")
    else:
        print("Opcion seleccionada erronea")
    os.system("pause")