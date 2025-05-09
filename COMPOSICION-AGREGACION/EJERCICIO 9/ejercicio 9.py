class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        print(f'Producto: {self.nombre}, Precio: ${self.precio:.2f}')

class CarritoCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if len(self.productos) < 10:
            self.productos.append(producto)
        else:
            print("No se puede agregar más de 10 productos al carrito.")

    def mostrar_carrito(self):
        if not self.productos:
            print("El carrito está vacío.")
            return
        print("Productos en el carrito:")
        for producto in self.productos:
            producto.mostrar_info()

# Creación de un carrito de compras y productos
carrito = CarritoCompras()
carrito.agregar_producto(Producto("Manzana", 0.50))
carrito.agregar_producto(Producto("Pan", 1.20))
carrito.agregar_producto(Producto("Leche", 0.80))
carrito.agregar_producto(Producto("Huevos", 2.50))
carrito.agregar_producto(Producto("Queso", 3.00))
carrito.agregar_producto(Producto("Tomate", 0.90))
carrito.agregar_producto(Producto("Cereal", 2.30))
carrito.agregar_producto(Producto("Arroz", 1.50))
carrito.agregar_producto(Producto("Azúcar", 1.00))
carrito.agregar_producto(Producto("Sal", 0.50))  
carrito.agregar_producto(Producto("Pasta", 1.00))  


carrito.mostrar_carrito()