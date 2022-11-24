from Libro import Libro

libNewport = Libro("Enfocate", 182353168, "Carl Newport", 2016)
print("Título: {0}  Isbn: {1}  Autor: {2}  Año Publicación: {3}".format(libNewport.getTitulo(), libNewport.getIsbn(), libNewport.getAutor(), libNewport.getAnoPublicacion()))
libNewport.setAnoPublicacion(2014)
libNewport.agregarPagina()
libNewport.agregarPagina()
libNewport.agregarPagina()
print("Título: {0}  Isbn: {1}  Autor: {2}  Año Publicación: {3}".format(libNewport.getTitulo(), libNewport.getIsbn(), libNewport.getAutor(), libNewport.getAnoPublicacion()))
libNewport.mostrarPaginas()