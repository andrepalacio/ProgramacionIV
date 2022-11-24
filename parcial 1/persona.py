#Autor: Ing(c). Andres Palacio Sanchez

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.mayor_de_edad = self.definir_mayor_de_edad(edad)

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad
        self.mayor_de_edad = self.definir_mayor_de_edad(edad)

    def definir_mayor_de_edad(self, edad):
        if edad >= 18:
            return "Es mayor de edad"
        else:
            return "No es mayor de edad"

    def __str__(self):
        return f"\nNombre: {self.nombre}\nEdad: {self.edad}\nEstado: {self.mayor_de_edad}"

persona1 = Persona("Laura Benjumea", 17)
persona2 = Persona("Fabio Walteros", 22)
print(f"Datos de las personas\n {persona1}\n {persona2}")