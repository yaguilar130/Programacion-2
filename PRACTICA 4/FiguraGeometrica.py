import math

class AreaCalculator:
    def area(self, shape, *args):
        if shape == 'círculo':
            return self.area_circulo(args[0])
        elif shape == 'rectángulo':
            return self.area_rectangulo(args[0], args[1])
        elif shape == 'triángulo':
            return self.area_triangulo(args[0], args[1])
        elif shape == 'trapecio':
            return self.area_trapecio(args[0], args[1], args[2])
        elif shape == 'pentágono':
            return self.area_pentagono(args[0])
        else:
            return "Forma no reconocida"

    def area_circulo(self, radio):
        return math.pi * radio ** 2

    def area_rectangulo(self, base, altura):
        return base * altura

    def area_triangulo(self, base, altura):
        return (base * altura) / 2

    def area_trapecio(self, base_menor, base_mayor, altura):
        return ((base_menor + base_mayor) * altura) / 2

    def area_pentagono(self, lado):
        return (5 * lado ** 2) / (4 * math.tan(math.pi / 5))

calc = AreaCalculator()
print("Área del círculo:", calc.area('círculo', 5))
print("Área del rectángulo:", calc.area('rectángulo', 4, 6))
print("Área del triángulo:", calc.area('triángulo', 4, 3))
print("Área del trapecio:", calc.area('trapecio', 3, 5, 4))
print("Área del pentágono:", calc.area('pentágono', 3))
