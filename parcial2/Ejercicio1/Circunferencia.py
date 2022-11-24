from Punto import Punto

class Circunferencia_Centrada:
    PI=3.1416
    def __init__(self, x=0.0, y=0.0, r=0.0) -> None:
        self.centro=Punto(x,y)
        self.radio=r
        self.diametro=2*r
        self.longitud=2*self.PI*r
        self.area=2*self.PI*(r**2)

    def getRadio(self):
        return self.radio
    def setRadio(self, r):
        self.radio=r
        self.diametro=2*r
        self.longitud=2*self.PI*r
        self.area=2*self.PI*(r**2)

    def getDiametro(self):
        return self.diametro
    def setDiametro(self, d):
        self.diametro=d
        self.radio=d/2
        self.longitud=2*self.PI*(d/2)
        self.area=2*self.PI*((d/2)**2)

    def getLongitud(self):
        return self.longitud
    def setLongitud(self, l):
        self.longitud=l
        self.radio=l/(2*self.PI)
        self.diametro=self.radio*2
        self.area=2*self.PI*(self.radio**2)

    def getArea(self):
        return self.area
    def setArea(self,a):
        self.area=a
        self.radio=(a/(2*self.PI))**0.5
        self.diametro=self.radio*2
        self.longitud=2*self.PI*self.radio

    def getXCentro(self):
        return self.centro.getX()
    def setXCentro(self, x):
        self.centro.setX(x)

    def getYCentro(self):
        return self.centro.getY()
    def setYCentro(self,y):
        self.centro.setY(y)

    def trasladarCincunferencia(self, x, y):
        self.centro.setX(x)
        self.centro.setY(y)