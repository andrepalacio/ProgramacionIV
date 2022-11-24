#Autor: Ing(c). Andres Palacio Sanchez

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.lado_mayor = self.encontrar_lado_mayor(lado1, lado2, lado3)
        self.tipo = self.analizar_triangulo()

    def encontrar_lado_mayor(self, lado1, lado2, lado3):
        if lado1 >= lado2 and lado1 >= lado3:
            return lado1
        elif lado2 >= lado1 and lado2 >= lado3:
            return lado2
        elif lado3 >= lado1 and lado3 >= lado2:
            return lado3

    #funcion auxiliar para los tipos de triangulo
    def auxiliar_casos(self, ladoA, ladoB):
        if ladoA == ladoB or ladoA == self.lado_mayor or ladoB == self.lado_mayor:
            return "Isoceles"
        else:
            return "Escaleno"

    def analizar_triangulo(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            return "Equilatero"
        elif self.lado1 == self.lado_mayor:
            return self.auxiliar_casos(self.lado2, self.lado3)
        elif self.lado2 == self.lado_mayor:
            return self.auxiliar_casos(self.lado1, self.lado3)
        elif self.lado3 == self.lado_mayor:
            return self.auxiliar_casos(self.lado1, self.lado2)
    
    def __str__(self):
        return f"\nDatos del triangulo\nLado 1 = {self.lado1}   Lado 2 = {self.lado2}   Lado 3 = {self.lado3}\nLado mayor = {self.lado_mayor}\nTipo de triangulo: {self.tipo}"

triang1 = Triangulo(2, 4, 4)
triang2 = Triangulo(8, 4, 6)
triang3 = Triangulo(2, 2, 4)
triang4 = Triangulo(5, 5, 5)
triang5 = Triangulo(5, 3, 5)
print(triang1, triang2, triang3, triang4, triang5)
