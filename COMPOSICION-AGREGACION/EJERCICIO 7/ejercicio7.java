import java.util.ArrayList;
import java.util.List;

class Estudiante {
    private String nombre;
    private String carrera;
    private int semestre;

    public Estudiante(String nombre, String carrera, int semestre) {
        this.nombre = nombre;
        this.carrera = carrera;
        this.semestre = semestre;
    }

    public void mostrarInfo() {
        System.out.println("Nombre: " + nombre + ", Carrera: " + carrera + ", Semestre: " + semestre);
    }
}

class Universidad {
    private String nombre;
    private List<Estudiante> estudiantes;

    public Universidad(String nombre) {
        this.nombre = nombre;
        this.estudiantes = new ArrayList<>();
    }

    public void agregarEstudiante(Estudiante estudiante) {
        estudiantes.add(estudiante);
    }

    public void mostrarUniversidad() {
        System.out.println("Universidad: " + nombre);
        for (Estudiante estudiante : estudiantes) {
            estudiante.mostrarInfo();
            System.out.println("---");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Universidad universidad = new Universidad("Universidad Ejemplo");
        universidad.agregarEstudiante(new Estudiante("Ana", "Ingeniería", 3));
        universidad.agregarEstudiante(new Estudiante("Luis", "Medicina", 2));
        universidad.agregarEstudiante(new Estudiante("Carlos", "Derecho", 1));

        // Mostrar información de la universidad
        universidad.mostrarUniversidad();
    }
}
