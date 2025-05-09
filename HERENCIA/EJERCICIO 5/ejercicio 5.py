class Empleado:
    def __init__(self, nombre, apellido, salario_base, años_antigüedad):
        self.nombre = nombre
        self.apellido = apellido
        self.salario_base = salario_base
        self.años_antigüedad = años_antigüedad

    def calcular_salario(self):
        bono_antigüedad = self.salario_base * 0.05 * self.años_antigüedad
        return self.salario_base + bono_antigüedad

class Gerente(Empleado):
    def __init__(self, nombre, apellido, salario_base, años_antigüedad, departamento, bono_gerencial):
        super().__init__(nombre, apellido, salario_base, años_antigüedad)
        self.departamento = departamento
        self.bono_gerencial = bono_gerencial

    def calcular_salario(self):
        salario_base_con_bono = super().calcular_salario()
        return salario_base_con_bono + self.bono_gerencial

class Desarrollador(Empleado):
    def __init__(self, nombre, apellido, salario_base, años_antigüedad, lenguaje_programacion, horas_extras):
        super().__init__(nombre, apellido, salario_base, años_antigüedad)
        self.lenguaje_programacion = lenguaje_programacion
        self.horas_extras = horas_extras

    def calcular_salario(self):
        salario_base_con_bono = super().calcular_salario()
        return salario_base_con_bono + (self.horas_extras * 20)  


gerente1 = Gerente("Carlos", "Pérez", 5000, 10, "Ventas", 1200)
desarrollador1 = Desarrollador("Ana", "García", 4000, 5, "Python", 12)


print(f"Salario Gerente: {gerente1.calcular_salario()}")
print(f"Salario Desarrollador: {desarrollador1.calcular_salario()}")


gerentes = [gerente1]
gerentes_con_bono_mayor_a_1000 = [gerente for gerente in gerentes if gerente.bono_gerencial > 1000]
for gerente in gerentes_con_bono_mayor_a_1000:
    print(f"Gerente con bono mayor a 1000: {gerente.nombre} {gerente.apellido}")


desarrolladores = [desarrollador1]
desarrolladores_con_mas_10_horas = [desarrollador for desarrollador in desarrolladores if desarrollador.horas_extras > 10]
for desarrollador in desarrolladores_con_mas_10_horas:
    print(f"Desarrollador con más de 10 horas extras: {desarrollador.nombre} {desarrollador.apellido}")