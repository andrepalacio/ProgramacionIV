class Punto:
    
    def __init__(self, x=0.0, y=0.0) -> None:
        self.coord_x=x
        self.coord_y=y

    def getX(self):
        return self.coord_x
    def setX(self, value):
        self.coord_x=value
    def getY(self):
        return self.coord_y
    def setY(self, value):
        self.coord_y=value