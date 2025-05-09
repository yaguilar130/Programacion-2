import java.util.ArrayList;
import java.util.List;

class Habitacion {
    private String nombre;
    private double tamano;

    public Habitacion(String nombre, double tamano) {
        this.nombre = nombre;
        this.tamano = tamano;
    }

    public void mostrarInfo() {
        System.out.println("Habitación: " + nombre + ", Tamaño: " + tamano + " m²");
    }
}

class Casa {
    private String direccion;
    private List<Habitacion> habitaciones;

    public Casa(String direccion) {
        this.direccion = direccion;
        this.habitaciones = new ArrayList<>();
    }

    public void agregarHabitacion(Habitacion habitacion) {
        habitaciones.add(habitacion);
    }

    public void mostrarCasa() {
        System.out.println("Dirección: " + direccion);
        for (Habitacion habitacion : habitaciones) {
            habitacion.mostrarInfo();
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Casa casa = new Casa("Calle Falsa 123");
        casa.agregarHabitacion(new Habitacion("Sala", 30));
        casa.agregarHabitacion(new Habitacion("Cocina", 20));
        casa.agregarHabitacion(new Habitacion("Dormitorio", 25));

        // Mostrar información de la casa
        casa.mostrarCasa();
    }
}
