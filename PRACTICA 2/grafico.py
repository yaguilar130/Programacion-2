import pygame
import sys

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def dibujar(self, screen):
        pygame.draw.line(screen, (0, 0, 0), (self.p1.x, self.p1.y), (self.p2.x, self.p2.y), 3)

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def dibujar(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.centro.x, self.centro.y), self.radio, 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Gráfico con Pygame")

    # Crear puntos
    p1 = Punto(100, 150)
    p2 = Punto(300, 150)

    # Crear línea y círculo
    linea = Linea(p1, p2)
    centro = Punto(200, 150)
    circulo = Circulo(centro, 50)

    # Bucle principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))  # Fondo blanco
        linea.dibujar(screen)
        circulo.dibujar(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()