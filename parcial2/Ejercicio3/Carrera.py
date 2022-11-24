class Carrera:

    def __init__(self, dist, ronda, fecha) -> None:
        self.distancia = dist
        self.ronda = ronda
        self.fecha = fecha
        self.calles = []

    def getDistancia(self):
        return self.distancia
    def setDistancia(self, valor):
        self.distancia = valor
    
    def getRonda(self):
        return self.ronda
    def setRonda(self, valor):
        self.ronda = valor

    def getFecha(self):
        return self.fecha
    def setFecha(self, valor):
        self.fecha = valor

    def insertar_calle(self, ncalle):
        self.calles.append(ncalle)
    def imprimir_calles(self):
        print("Calles")
        for c in self.calles:
            print("Numero: {0}  Atleta: {1}  Tiempo: {2}".format(c.getNumero(), c.getAtleta(), c.getTiempo()))