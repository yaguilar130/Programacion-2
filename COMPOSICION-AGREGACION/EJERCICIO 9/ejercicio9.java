import java.util.ArrayList;
import java.util.List;

class Producto {
    private String nombre;
    private double precio;

    public Producto(String nombre, double precio) {
        this.nombre = nombre;
        this.precio = precio;
    }

    public void mostrarInfo() {
        System.out.printf("Producto: %s, Precio: $%.2f%n", nombre, precio);
    }
}

class CarritoCompras {
    private List<Producto> productos;

    public CarritoCompras() {
        this.productos = new ArrayList<>();
    }

    public void agregarProducto(Producto producto) {
        if (productos.size() < 10) {
            productos.add(producto);
        } else {
            System.out.println("No se puede agregar más de 10 productos al carrito.");
        }
    }

    public void mostrarCarrito() {
        if (productos.isEmpty()) {
            System.out.println("El carrito está vacío.");
            return;
        }
        System.out.println("Productos en el carrito:");
        for (Producto producto : productos) {
            producto.mostrarInfo();
        }
    }
}

public class Main {
    public static void main(String[] args) {
        CarritoCompras carrito = new CarritoCompras();
        carrito.agregarProducto(new Producto("Manzana", 0.50));
        carrito.agregarProducto(new Producto("Pan", 1.20));
        carrito.agregarProducto(new Producto("Leche", 0.80));
        carrito.agregarProducto(new Producto("Huevos", 2.50));
        carrito.agregarProducto(new Producto("Queso", 3.00));
        carrito.agregarProducto(new Producto("Tomate", 0.90));
        carrito.agregarProducto(new Producto("Cereal", 2.30));
        carrito.agregarProducto(new Producto("Arroz", 1.50));
        carrito.agregarProducto(new Producto("Azúcar", 1.00));
        carrito.agregarProducto(new Producto("Sal", 0.50));  // Esto debería ser permitido
        carrito.agregarProducto(new Producto("Pasta", 1.00)); // Esto debería mostrar un mensaje de error

        // Mostrar información del carrito
        carrito.mostrarCarrito();
    }
}
