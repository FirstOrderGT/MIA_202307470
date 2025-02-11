class ListaContigua:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.datos = [None] * capacidad  
        self.tamaño = 0  

    def insertar(self, dato):
        if self.tamaño < self.capacidad:
            self.datos[self.tamaño] = dato
            self.tamaño += 1
        else:
            print("Error: Lista llena")

    def eliminar(self, indice):
        try:
            indice = int(indice)
        except ValueError:
            print("Error: El índice no es un número válido")
            return
        
        if 0 <= indice < self.tamaño:
            
            for i in range(indice, self.tamaño - 1):
                self.datos[i] = self.datos[i + 1]
            self.datos[self.tamaño - 1] = None 
            self.tamaño -= 1
        else:
            print("Error: Índice fuera de rango")

    def mostrar(self):
        if self.tamaño == 0:
            return "Lista vacía"

        elementos = [f"{i}: {self.datos[i]}" for i in range(self.tamaño)]
        return "\n".join(elementos) 