class Jugador:
    def __init__(self, nombre, numero, posicion):
        self.nombre = nombre
        self.numero = numero
        self.posicion = posicion

    def mostrar_info(self):
        print(f'Nombre: {self.nombre}, Número: {self.numero}, Posición: {self.posicion}')

class Portero(Jugador):
    def __init__(self, nombre, numero, habilidad_especial):
        super().__init__(nombre, numero, "Portero")
        self.habilidad_especial = habilidad_especial

    def mostrar_info(self):
        super().mostrar_info()
        print(f'Habilidad Especial: {self.habilidad_especial}')

class Defensa(Jugador):
    def __init__(self, nombre, numero, habilidad_especial):
        super().__init__(nombre, numero, "Defensa")
        self.habilidad_especial = habilidad_especial

    def mostrar_info(self):
        super().mostrar_info()
        print(f'Habilidad Especial: {self.habilidad_especial}')

class Mediocampista(Jugador):
    def __init__(self, nombre, numero, habilidad_especial):
        super().__init__(nombre, numero, "Mediocampista")
        self.habilidad_especial = habilidad_especial

    def mostrar_info(self):
        super().mostrar_info()
        print(f'Habilidad Especial: {self.habilidad_especial}')

class Delantero(Jugador):
    def __init__(self, nombre, numero, habilidad_especial):
        super().__init__(nombre, numero, "Delantero")
        self.habilidad_especial = habilidad_especial

    def mostrar_info(self):
        super().mostrar_info()
        print(f'Habilidad Especial: {self.habilidad_especial}')

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def mostrar_equipo(self):
        print(f'Equipo: {self.nombre}')
        for jugador in self.jugadores:
            jugador.mostrar_info()
            print('---')


equipo = Equipo("Leones FC")
equipo.agregar_jugador(Portero("Juan", 1, "Atajadas"))
equipo.agregar_jugador(Defensa("Carlos", 2, "Marcaje"))
equipo.agregar_jugador(Mediocampista("Luis", 8, "Pases"))
equipo.agregar_jugador(Delantero("Pedro", 9, "Goles"))


equipo.mostrar_equipo()