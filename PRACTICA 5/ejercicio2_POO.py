class Estadisticas:
    def __init__(self, valores):
        self.valores = valores

    def promedio(self):
        return sum(self.valores) / len(self.valores)

    def desviacion(self):
        prom = self.promedio()
        varianza = sum((x - prom) ** 2 for x in self.valores) / (len(self.valores) - 1)
        return varianza ** 0.5

def main():
    numeros = []
    print("Introduce 10 números:")
    
    for _ in range(10):
        num = float(input())
        numeros.append(num)
    
    estadisticas = Estadisticas(numeros)
    
    prom = estadisticas.promedio()
    desv = estadisticas.desviacion()
    
    print(f"El promedio es {prom:.2f}")
    print(f"La desviacion estandar es {desv:.5f}")

if __name__ == "__main__":
    main()