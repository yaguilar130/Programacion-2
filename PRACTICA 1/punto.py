class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def trazar(self):
        return f"Línea desde {self.p1.x}, {self.p1.y} hasta {self.p2.x}, {self.p2.y}"

    def dibujar_linea(self):
        print(self.trazar())