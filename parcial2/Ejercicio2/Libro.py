from Pagina import Pagina

class Libro:

    def __init__(self, titulo, isbn, autor, publicacion) -> None:
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        self.anopublicacion = publicacion
        self.paginas = []

    def getTitulo(self):
        return self.titulo
    def setTitulo(self, valor):
        self.titulo = valor
    def getIsbn(self):
        return self.isbn
    def setIsbn(self, valor):
        self.isbn = valor
    def getAutor(self):
        return self.autor
    def setAutor(self, valor):
        self.autor = valor
    def getAnoPublicacion(self):
        return self.anopublicacion
    def setAnoPublicacion(self, valor):
        self.anopublicacion = valor

    def agregarPagina(self):
        contenido = input("Ingrese el contenido de la pagina: ")
        npagina = input("Digite numero de pagina: ")
        nueva = Pagina(contenido, npagina)
        self.paginas.append(nueva)
    
    def mostrarPaginas(self):
        for i in self.paginas:
            print("Contenido: {0}\nNumero de pagina: {1}".format(i.getContenido(), i.getPagina()))
