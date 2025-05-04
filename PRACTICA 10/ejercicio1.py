class Ministerio:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.nroEmpleados = 0
        self.empleados = []
        self.edades = []
        self.sueldos = []

    def agregarEmpleado(self, nombre, edad, sueldo):
        self.empleados.append(nombre)
        self.edades.append(edad)
        self.sueldos.append(sueldo)
        self.nroEmpleados += 1

    def eliminarEmpleadoPorEdad(self, edad):
        for i in range(self.nroEmpleados - 1, -1, -1):
            if self.edades[i] == edad:
                del self.empleados[i]
                del self.edades[i]
                del self.sueldos[i]
                self.nroEmpleados -= 1

    def transferirEmpleado(self, otro, nombre):
        if nombre in self.empleados:
            index = self.empleados.index(nombre)
            otro.agregarEmpleado(self.empleados[index], self.edades[index], self.sueldos[index])
            self.eliminarEmpleadoPorEdad(self.edades[index])

    def mostrarMenorEdad(self):
        if self.nroEmpleados == 0:
            return []
        min_edad = min(self.edades)
        return [self.empleados[i] for i in range(self.nroEmpleados) if self.edades[i] == min_edad]

    def mostrarMenorSueldo(self):
        if self.nroEmpleados == 0:
            return []
        min_sueldo = min(self.sueldos)
        return [self.empleados[i] for i in range(self.nroEmpleados) if self.sueldos[i] == min_sueldo]


ministerio1 = Ministerio("Ministerio de Salud", "Av. 6 de Agosto")
ministerio2 = Ministerio("Ministerio de Educación", "Calle Sucre")


ministerio1.agregarEmpleado("Pedro Rojas Luna", 35, 2500)
ministerio1.agregarEmpleado("Lucy Sosa Rios", 43, 3250)
ministerio1.agregarEmpleado("Ana Perez Rojas", 26, 2700)
ministerio1.agregarEmpleado("Saul Arce Calle", 29, 2500)


ministerio1.eliminarEmpleadoPorEdad(43)


ministerio2.agregarEmpleado("Carlos Mendez", 30, 3000)
ministerio1.transferirEmpleado(ministerio2, "Carlos Mendez")


menor_edad = ministerio1.mostrarMenorEdad()
print("Empleados con la menor edad:", menor_edad)


menor_sueldo = ministerio1.mostrarMenorSueldo()
print("Empleados con el menor sueldo:", menor_sueldo)