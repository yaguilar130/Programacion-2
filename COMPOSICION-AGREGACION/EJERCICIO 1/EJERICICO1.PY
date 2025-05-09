class Habitacion:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano

    def mostrar_info(self):
        print(f'Habitación: {self.nombre}, Tamaño: {self.tamano} m²')

class Casa:
    def __init__(self, direccion):
        self.direccion = direccion
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_casa(self):
        print(f'Dirección: {self.direccion}')
        for habitacion in self.habitaciones:
            habitacion.mostrar_info()


casa = Casa("Calle Falsa 123")
casa.agregar_habitacion(Habitacion("Sala", 30))
casa.agregar_habitacion(Habitacion("Cocina", 20))
casa.agregar_habitacion(Habitacion("Dormitorio", 25))


casa.mostrar_casa()