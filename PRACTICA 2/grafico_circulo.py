import turtle

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def dibujar(self):
        turtle.penup()
        turtle.goto(self.centro.x, self.centro.y - self.radio)  # Mueve a la posición inicial
        turtle.pendown()
        turtle.circle(self.radio)

def main():
    turtle.title("Dibujo de Círculo")
    turtle.speed(1)

    # Crear círculo
    centro = Punto(200, 150)
    circulo = Circulo(centro, 50)

    # Dibujar círculo
    circulo.dibujar()

    turtle.done()

if __name__ == "__main__":
    main()