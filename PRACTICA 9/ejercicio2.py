from abc import ABC, abstractmethod

class Colorido(ABC):
    @abstractmethod
    def get_color(self):
        pass

class Figura(Colorido):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado, color):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def get_color(self):
        return self.color


def main():
    cuadrado = Cuadrado(5, "Rojo")
    print(f"Color: {cuadrado.get_color()}, Área: {cuadrado.area()}")

if __name__ == "__main__":
    main()