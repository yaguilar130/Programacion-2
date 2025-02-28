class Pila:
    def __init__(self, n):
        self.n = n
        self.top = -1
        self.arreglo = [0] * n

    def push(self, e):
        if self.isFull():
            print("La pila está llena.")
            return
        self.top += 1
        self.arreglo[self.top] = e

    def pop(self):
        if self.isEmpty():
            print("La pila está vacía.")
            return None
        e = self.arreglo[self.top]
        self.top -= 1
        return e

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.n - 1

if __name__ == "__main__":
    
    pila = Pila(5)

    pila.push(10)
    pila.push(20)
    pila.push(30)

    print("Elemento pop:", pila.pop())  
    print("¿Está vacía?", pila.isEmpty())  #

    pila.push(40)
    pila.push(50)
    pila.push(60) 

    print("Elemento en la parte superior:", pila.arreglo[pila.top])