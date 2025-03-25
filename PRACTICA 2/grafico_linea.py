import turtle

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def dibujar(self):
        turtle.penup()
        turtle.goto(self.p1.x, self.p1.y)
        turtle.pendown()
        turtle.goto(self.p2.x, self.p2.y)

def main():
    turtle.title("Dibujo de Línea")
    turtle.speed(1)
    
    p1 = Punto(100, 150)
    p2 = Punto(300, 150)

    linea = Linea(p1, p2)
    linea.dibujar()

    turtle.done()

if __name__ == "__main__":
    main()
