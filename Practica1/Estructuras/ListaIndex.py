from .NodoIndex import NodoIndex

class ListaIndex:
    def __init__(self):
        self.head = None
        self.contador = 0

    def insertar(self, dato):
        nuevo_nodo = NodoIndex(self.contador, dato)
        if not self.head:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.contador += 1

    def eliminar(self, indice):
        if not self.head:
            return False
        
        try:
            indice = int(indice)
        except ValueError:
            print("Error: El índice no es un número válido")
            return

        if self.head.indice == indice:
            self.head = self.head.siguiente
            return True

        actual = self.head
        while actual.siguiente and actual.siguiente.indice != indice:
            actual = actual.siguiente

        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente
            return True
        return False
    
    def mostrar(self):
        if not self.head:
            return "Lista vacía"

        elementos = []
        actual = self.head
        while actual:
            elementos.append(f"{actual.indice}: {actual.dato}")
            actual = actual.siguiente

        return "\n".join(elementos) 