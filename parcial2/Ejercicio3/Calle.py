class Calle:

    def __init__(self, n) -> None:
        self.numero = n
        self.atleta = ""
        self.tiempo = 0.0

    def getNumero(self):
        return self.numero
    
    def getAtleta(self):
        return self.atleta
    
    def getTiempo(self):
        return self.tiempo
    
    def setAtleta(self, valor):
        self.atleta = valor

    def setTiempo(self, valor):
        self.tiempo = valor