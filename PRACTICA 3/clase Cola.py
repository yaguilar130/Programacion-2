class Cola:
    def __init__(self, n):
        self.n = n
        self.inicio = 0
        self.fin = -1
        self.arreglo = [0] * n
        self.size = 0

    def insert(self, e):
        if self.isFull():
            print("La cola está llena.")
            return
        self.fin = (self.fin + 1) % self.n
        self.arreglo[self.fin] = e
        self.size += 1

    def remove(self):
        if self.isEmpty():
            print("La cola está vacía.")
            return None
        e = self.arreglo[self.inicio]
        self.inicio = (self.inicio + 1) % self.n
        self.size -= 1
        return e

    def peek(self):
        if self.isEmpty():
            print("La cola está vacía.")
            return None
        return self.arreglo[self.inicio]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.n

    def size(self):
        return self.size

if __name__ == "__main__":
    
    cola = Cola(5)

    cola.insert(10)
    cola.insert(20)
    cola.insert(30)

    print("Elemento en la parte delantera:", cola.peek()) 
    print("Elemento removido:", cola.remove())  

    print("¿Está vacía?", cola.isEmpty())  
    cola.insert(40)
    cola.insert(50)
    cola.insert(60)  
    print("Tamaño actual de la cola:", cola.size)  