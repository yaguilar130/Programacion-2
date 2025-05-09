from datetime import datetime

class Persona:
    def __init__(self, ci, nombre, apellido, celular, fecha_nac):
        self.ci = ci
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.fecha_nac = datetime.strptime(fecha_nac, '%Y-%m-%d')

    def mostrar_info(self):
        return f"CI: {self.ci}, Nombre: {self.nombre}, Apellido: {self.apellido}, Celular: {self.celular}, Fecha de Nac: {self.fecha_nac.date()}"

class Estudiante(Persona):
    def __init__(self, ci, nombre, apellido, celular, fecha_nac, ru, fecha_ingreso, semestre):
        super().__init__(ci, nombre, apellido, celular, fecha_nac)
        self.ru = ru
        self.fecha_ingreso = datetime.strptime(fecha_ingreso, '%Y-%m-%d')
        self.semestre = semestre

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, RU: {self.ru}, Fecha de Ingreso: {self.fecha_ingreso.date()}, Semestre: {self.semestre}"

class Docente(Persona):
    def __init__(self, ci, nombre, apellido, celular, fecha_nac, nit, profesion, especialidad):
        super().__init__(ci, nombre, apellido, celular, fecha_nac)
        self.nit = nit
        self.profesion = profesion
        self.especialidad = especialidad

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, NIT: {self.nit}, Profesión: {self.profesion}, Especialidad: {self.especialidad}"


estudiante1 = Estudiante("12345678", "Juan", "Pérez", "987654321", "2000-05-01", "RU001", "2022-01-10", 3)
estudiante2 = Estudiante("87654321", "Ana", "Pérez", "123456789", "1995-06-15", "RU002", "2022-01-10", 2)
docente1 = Docente("23456789", "Luis", "García", "456789123", "1980-03-20", "NIT001", "Ingeniero", "Sistemas")
docente2 = Docente("34567890", "María", "García", "654321987", "1985-07-25", "NIT002", "Arquitecto", "Diseño")


print(estudiante1.mostrar_info())
print(estudiante2.mostrar_info())
print(docente1.mostrar_info())
print(docente2.mostrar_info())


estudiantes = [estudiante1, estudiante2]
estudiantes_mayores_25 = [estudiante for estudiante in estudiantes if (datetime.now() - estudiante.fecha_nac).days > 25 * 365]
for estudiante in estudiantes_mayores_25:
    print(estudiante.mostrar_info())


docentes = [docente1, docente2]
docente_ingeniero_mas_mayor = max(
    (docente for docente in docentes if docente.profesion == "Ingeniero"),
    key=lambda d: d.fecha_nac
)
print(docente_ingeniero_mas_mayor.mostrar_info())


mismo_apellido = [estudiante for estudiante in estudiantes if estudiante.apellido in [docente.apellido for docente in docentes]]
for persona in mismo_apellido:
    print(persona.mostrar_info())