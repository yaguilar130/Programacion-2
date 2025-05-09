class Parte:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

    def mostrar_info(self):
        print(f'Parte: {self.nombre}, Peso: {self.peso} kg')

class Avion:
    def __init__(self, modelo, fabricante):
        self.modelo = modelo
        self.fabricante = fabricante
        self.partes = []

    def agregar_parte(self, parte):
        self.partes.append(parte)

    def mostrar_avion(self):
        print(f'Modelo: {self.modelo}, Fabricante: {self.fabricante}')
        for parte in self.partes:
            parte.mostrar_info()

# Creación de un avión y partes
avion = Avion("Boeing 747", "Boeing")
avion.agregar_parte(Parte("Ala", 400))
avion.agregar_parte(Parte("Motor", 300))
avion.agregar_parte(Parte("Fuselaje", 500))

# Mostrar información del avión
avion.mostrar_avion()