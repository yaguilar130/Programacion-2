import java.util.ArrayList;
import java.util.List;

// Clase Parte
class Parte {
    private String nombre;
    private double peso; // en kg

    // Constructor
    public Parte(String nombre, double peso) {
        this.nombre = nombre;
        this.peso = peso;
    }

    // Getters
    public String getNombre() {
        return nombre;
    }

    public double getPeso() {
        return peso;
    }

    // Método para mostrar información de la parte
    public void mostrarInfo() {
        System.out.println("Nombre: " + nombre + ", Peso: " + peso + " kg");
    }
}

// Clase Avion
class Avion {
    private String modelo;
    private String fabricante;
    private List<Parte> partes;

    // Constructor
    public Avion(String modelo, String fabricante) {
        this.modelo = modelo;
        this.fabricante = fabricante;
        this.partes = new ArrayList<>();
    }

    // Métodos para agregar partes
    public void agregarParte(Parte parte) {
        partes.add(parte);
    }

    // Método para mostrar información del avión y sus partes
    public void mostrarAvion() {
        System.out.println("Modelo: " + modelo);
        System.out.println("Fabricante: " + fabricante);
        System.out.println("Partes del avión:");
        for (Parte parte : partes) {
            parte.mostrarInfo();
        }
    }

    // Getters y Setters
    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getFabricante() {
        return fabricante;
    }

    public void setFabricante(String fabricante) {
        this.fabricante = fabricante;
    }
}

// Clase principal para probar la implementación
public class Main {
    public static void main(String[] args) {
        // Crear un avión
        Avion avion = new Avion("Boeing 747", "Boeing");

        // Crear partes del avión
        Parte motor = new Parte("Motor", 5000);
        Parte ala = new Parte("Ala", 1500);
        Parte trenAterrizaje = new Parte("Tren de aterrizaje", 800);

        // Agregar partes al avión
        avion.agregarParte(motor);
        avion.agregarParte(ala);
        avion.agregarParte(trenAterrizaje);

        // Mostrar información del avión y sus partes
        avion.mostrarAvion();
    }
}
