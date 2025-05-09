class Estudiante:
    def __init__(self, nombre, carrera, semestre):
        self.nombre = nombre
        self.carrera = carrera
        self.semestre = semestre

    def mostrar_info(self):
        print(f'Nombre: {self.nombre}, Carrera: {self.carrera}, Semestre: {self.semestre}')

class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_universidad(self):
        print(f'Universidad: {self.nombre}')
        for estudiante in self.estudiantes:
            estudiante.mostrar_info()
            print('---')


universidad = Universidad("Universidad Ejemplo")
universidad.agregar_estudiante(Estudiante("Ana", "Ingeniería", 3))
universidad.agregar_estudiante(Estudiante("Luis", "Medicina", 2))
universidad.agregar_estudiante(Estudiante("Carlos", "Derecho", 1))


universidad.mostrar_universidad()