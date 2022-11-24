#Autor: Ing(c). Andres Palacio Sanchez

class Contacto:
    def __init__(self, nombre, telefono, email):
        self._nombre = nombre
        self._telefono = telefono
        self._email = email

    def imprimir_contacto(self):
        print("Nombre: {0}\nTelefono: {1}\nEmail: {2}\n".format(self._nombre, self._telefono, self._email))

class Agenda:
    def __init__(self):
        self.contactos = []
    
    def nuevo_contacto(self):
        nombre = input("Ingrese el nombre: ")
        if self.existe_contacto(nombre):
            print("El contacto ya existe")
        else:
            telefono = input("Ingrese el telefono: ")
            email = input("Ingrese el email: ")
            n_contacto = Contacto(nombre, telefono, email)
            self.contactos.append(n_contacto)

    def existe_contacto(self, nombre):
        for contc in self.contactos:
            if contc._nombre == nombre:
                return True
        return False

    def listar_contactos(self):
        for contc in self.contactos:
            contc.imprimir_contacto()

    def buscar_contacto(self, nombre):
        for contc in self.contactos:
            if contc._nombre == nombre:
                contc.imprimir_contacto()

    def editar_contacto(self, nombre, opcion):
        for i in range(len(self.contactos)):
            if self.contactos[i]._nombre == nombre:
                if  opcion == 1:
                    self.contactos[i]._nombre = input("Ingrese el nuevo nombre: ")
                elif opcion == 2:
                    self.contactos[i]._telefono = input("Ingrese el nuevo telefono: ")
                elif opcion == 3:
                    self.contactos[i]._email = input("Ingrese el nuevo email: ")