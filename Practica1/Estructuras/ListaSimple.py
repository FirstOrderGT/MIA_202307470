from .Nodo import Nodo

class ListaSimple:
    def __init__(self):
        self.head = None
        self.size = 0

    def vacia(self):
        return self.head is None

    def insertar(self, dato):
        nuevoNodo = Nodo(dato)

        if self.vacia():
            self.head = nuevoNodo
        else:
            aux = self.head

            while aux.siguiente != None:
                aux = aux.siguiente

            aux.siguiente = nuevoNodo

        self.size += 1

    def eliminar(self, dato):
        if self.vacia():
            return

        if self.head.dato == dato:
            self.head = self.head.siguiente
            self.size -= 1
            return
        
        aux = self.head

        while aux.siguiente is not None:
            if aux.siguiente.dato == dato:
                aux.siguiente = aux.siguiente.siguiente
                self.size -= 1
                return

            aux = aux.siguiente

    def mostrar(self):
        if not self.head:
            return "Lista vacía"

        contenido = []
        aux = self.head
        while aux:
            contenido.append(str(aux.dato))
            aux = aux.siguiente

        return "\n".join(contenido)    