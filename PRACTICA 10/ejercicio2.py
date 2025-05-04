class LineaTeleferico:
    def __init__(self, color, tramo, nroCabinas):
        self.color = color
        self.tramo = tramo
        self.nroCabinas = nroCabinas
        self.empleados = []
        self.edades = []
        self.sueldos = []

    def agregarEmpleado(self, nombre, edad, sueldo):
        self.empleados.append(nombre)
        self.edades.append(edad)
        self.sueldos.append(sueldo)

    def eliminarEmpleadoPorEdad(self, edad):
        for i in range(len(self.edades) - 1, -1, -1):
            if self.edades[i] == edad:
                del self.empleados[i]
                del self.edades[i]
                del self.sueldos[i]

    def transferirEmpleado(self, otro, nombre):
        if nombre in self.empleados:
            index = self.empleados.index(nombre)
            otro.agregarEmpleado(self.empleados[index], self.edades[index], self.sueldos[index])
            self.eliminarEmpleadoPorEdad(self.edades[index])

    def mostrarMayorEdad(self):
        if not self.edades:
            return []
        max_edad = max(self.edades)
        return [self.empleados[i] for i in range(len(self.empleados)) if self.edades[i] == max_edad]

    def mostrarMayorSueldo(self):
        if not self.sueldos:
            return []
        max_sueldo = max(self.sueldos)
        return [self.empleados[i] for i in range(len(self.empleados)) if self.sueldos[i] == max_sueldo]


teleferico1 = LineaTeleferico("Rojo", "Estación Central, Estación Cementerio, Estación 16 de Julio", 20)
teleferico2 = LineaTeleferico("Verde", "Estación A, Estación B, Estación C", 15)


teleferico1.agregarEmpleado("Pedro Rojas Luna", 35, 2500)
teleferico1.agregarEmpleado("Lucy Sosa Rios", 43, 3250)
teleferico1.agregarEmpleado("Ana Perez Rojas", 26, 2700)
teleferico1.agregarEmpleado("Saul Arce Calle", 29, 2500)


teleferico1.eliminarEmpleadoPorEdad(43)


teleferico2.agregarEmpleado("Carlos Mendez", 30, 3000)
teleferico1.transferirEmpleado(teleferico2, "Carlos Mendez")


mayor_edad = teleferico1.mostrarMayorEdad()
print("Empleados con la mayor edad:", mayor_edad)


mayor_sueldo = teleferico1.mostrarMayorSueldo()
print("Empleados con el mayor sueldo:", mayor_sueldo)