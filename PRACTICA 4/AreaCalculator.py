import math

class Figura:
    def area(self):
        raise NotImplementedError("Este método debe ser implementado por subclases")

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

class Trapecio(Figura):
    def __init__(self, base_menor, base_mayor, altura):
        self.base_menor = base_menor
        self.base_mayor = base_mayor
        self.altura = altura

    def area(self):
        return ((self.base_menor + self.base_mayor) * self.altura) / 2

class Pentagono(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return (5 * self.lado ** 2) / (4 * math.tan(math.pi / 5))

# Ejemplo de uso
figuras = [
    Circulo(5),
    Rectangulo(4, 6),
    Triangulo(4, 3),
    Trapecio(3, 5, 4),
    Pentagono(3)
]

for figura in figuras:
    print(f"Área de la figura: {figura.area()}")