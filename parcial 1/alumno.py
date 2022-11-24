#Autor: Ing(c). Andres Palacio Sanchez

class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def get_nombre(self):
        return self.nombre

    def get_nota(self):
        return self.nota

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_nota(self, nota):
        self.nota = nota

    def __str__(self):
        if self.nota >= 3.0:
            estado = "Aprobado"
        else:
            estado = "Reprobado"
        return f"Nombre: {self.nombre}\nNota: {self.nota}\nEstado: {estado}"

alumno1 = Alumno("Andres Palacio", 4.1)
alumno2 = Alumno("Joaquin Jimenez", 3.8)
alumno3 = Alumno("Mario Gutierrez", 2.7)
print("Estudiantes\n",alumno1,"\n",alumno2,"\n",alumno3)
