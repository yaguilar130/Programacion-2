import random

class Juego:
    def __init__(self, numero_de_vidas):
        self.numero_de_vidas = numero_de_vidas
        self.record = 0

    def reinicia_partida(self):
        self.numero_de_vidas = 3  

    def actualiza_record(self):
       
        self.record = max(self.record, self.numero_de_vidas)

    def quita_vida(self):
        self.numero_de_vidas -= 1
        return self.numero_de_vidas > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, numero_de_vidas):
        super().__init__(numero_de_vidas)
        self.numero_a_adivinar = 0

    def juega(self):
        self.reinicia_partida()
        self.numero_a_adivinar = random.randint(0, 10)
        print("Adivina un número entre 0 y 10")

        while True:
            try:
                intento = int(input("Introduce tu intento: "))
            except ValueError:
                print("Por favor, introduce un número válido.")
                continue

            if intento == self.numero_a_adivinar:
                print("¡Acertaste!!")
                self.actualiza_record()
                break
            else:
                if not self.quita_vida():
                    print("¡Te has quedado sin vidas!")
                    break
                elif intento < self.numero_a_adivinar:
                    print("El número a adivinar es mayor.")
                else:
                    print("El número a adivinar es menor.")

class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()

if __name__ == "__main__":
    Aplicacion.main()