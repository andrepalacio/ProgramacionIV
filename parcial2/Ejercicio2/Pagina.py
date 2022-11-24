class Pagina:

    def __init__(self, cont, pag) -> None:
        self.contenido = cont
        self.pagina = pag

    def getContenido(self):
        return self.contenido
    def setContenido(self,ncont):
        self.contenido = ncont

    def getPagina(self):
        return self.pagina
    def setPagina(self, npag):
        self.pagina = npag
