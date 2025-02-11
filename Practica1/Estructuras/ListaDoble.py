from .NodoDoble import NodoDoble

class ListaDoble:
    def __init__(self):
        self.head = None
        self.size = 0

    def vacia(self):
        return self.head is None
    
    def insertar(self, dato):
        nuevoNodo = NodoDoble(dato)

        if self.vacia():
            self.head = nuevoNodo
            self.head.anterior = None
            self.head.siguiente = None
        else:
            aux = self.head

            while aux.siguiente != None:
                aux = aux.siguiente

            aux.siguiente = nuevoNodo
            nuevoNodo.anterior = aux
            nuevoNodo.siguiente = None

        self.size += 1

    def eliminar(self, dato):
        if self.vacia():
            return
        
        if self.head.dato == dato:
            if self.head.siguiente is None:
                self.head = None
            else:
                self.head = self.head.siguiente
                self.head.anterior = None
            
            self.size -= 1
        aux = self.head
        while aux.siguiente is not None:
            if aux.siguiente.dato == dato:
                aux.siguiente = aux.siguiente.siguiente
                aux.siguiente.siguiente.anterior = aux
                self.size -= 1
                break
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