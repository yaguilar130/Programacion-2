import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_discriminante(self):
        return self.b**2 - 4 * self.a * self.c

    def get_raiz1(self, discriminante):
        return (-self.b + math.sqrt(discriminante)) / (2 * self.a)

    def get_raiz2(self, discriminante):
        return (-self.b - math.sqrt(discriminante)) / (2 * self.a)

    def resolver(self):
        discriminante = self.get_discriminante()
        if discriminante > 0:
            r1 = self.get_raiz1(discriminante)
            r2 = self.get_raiz2(discriminante)
            return f"La ecuación tiene dos raíces: {r1:.5f} y {r2:.5f}"
        elif discriminante == 0:
            r1 = self.get_raiz1(discriminante)
            return f"La ecuación tiene una raíz: {r1:.5f}"
        else:
            return "La ecuación no tiene raíces reales"

def main():
    a, b, c = map(float, input("Ingrese a, b, c: ").split())
    ecuacion = EcuacionCuadratica(a, b, c)
    print(ecuacion.resolver())

if __name__ == "__main__":
    main()