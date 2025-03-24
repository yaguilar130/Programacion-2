def promedio(valores):
    return sum(valores) / len(valores)

def desviacion(valores, prom):
    varianza = sum((x - prom) ** 2 for x in valores) / (len(valores) - 1)
    return varianza ** 0.5

def main():
    numeros = []
    print("Introduce 10 números:")
    
    for _ in range(10):
        num = float(input())
        numeros.append(num)
    
    prom = promedio(numeros)
    desv = desviacion(numeros, prom)
    
    print(f"El promedio es {prom:.2f}")
    print(f"La desviacion estandar es {desv:.5f}")

if __name__ == "__main__":
    main()