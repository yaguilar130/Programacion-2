import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

class Persona {
    private String ci;
    private String nombre;
    private String apellido;
    private String celular;
    private LocalDate fechaNac;

    public Persona(String ci, String nombre, String apellido, String celular, String fechaNac) {
        this.ci = ci;
        this.nombre = nombre;
        this.apellido = apellido;
        this.celular = celular;
        this.fechaNac = LocalDate.parse(fechaNac);
    }

    public String mostrarInfo() {
        return "CI: " + ci + ", Nombre: " + nombre + ", Apellido: " + apellido + ", Celular: " + celular + ", Fecha de Nac: " + fechaNac;
    }

    public LocalDate getFechaNac() {
        return fechaNac;
    }

    public String getApellido() {
        return apellido;
    }
}

class Estudiante extends Persona {
    private String ru;
    private LocalDate fechaIngreso;
    private int semestre;

    public Estudiante(String ci, String nombre, String apellido, String celular, String fechaNac, String ru, String fechaIngreso, int semestre) {
        super(ci, nombre, apellido, celular, fechaNac);
        this.ru = ru;
        this.fechaIngreso = LocalDate.parse(fechaIngreso);
        this.semestre = semestre;
    }

    @Override
    public String mostrarInfo() {
        return super.mostrarInfo() + ", RU: " + ru + ", Fecha de Ingreso: " + fechaIngreso + ", Semestre: " + semestre;
    }
}

class Docente extends Persona {
    private String nit;
    private String profesion;
    private String especialidad;

    public Docente(String ci, String nombre, String apellido, String celular, String fechaNac, String nit, String profesion, String especialidad) {
        super(ci, nombre, apellido, celular, fechaNac);
        this.nit = nit;
        this.profesion = profesion;
        this.especialidad = especialidad;
    }

    @Override
    public String mostrarInfo() {
        return super.mostrarInfo() + ", NIT: " + nit + ", Profesión: " + profesion + ", Especialidad: " + especialidad;
    }

    public String getProfesion() {
        return profesion;
    }
}

// Clase principal para demostrar
public class Main {
    public static void main(String[] args) {
        Estudiante estudiante1 = new Estudiante("12345678", "Juan", "Pérez", "987654321", "2000-05-01", "RU001", "2022-01-10", 3);
        Estudiante estudiante2 = new Estudiante("87654321", "Ana", "Pérez", "123456789", "1995-06-15", "RU002", "2022-01-10", 2);
        Docente docente1 = new Docente("23456789", "Luis", "García", "456789123", "1980-03-20", "NIT001", "Ingeniero", "Sistemas");
        Docente docente2 = new Docente("34567890", "María", "García", "654321987", "1985-07-25", "NIT002", "Arquitecto", "Diseño");

        System.out.println(estudiante1.mostrarInfo());
        System.out.println(estudiante2.mostrarInfo());
        System.out.println(docente1.mostrarInfo());
        System.out.println(docente2.mostrarInfo());

        // Mostrar estudiantes mayores de 25 años
        List<Estudiante> estudiantes = new ArrayList<>();
        estudiantes.add(estudiante1);
        estudiantes.add(estudiante2);
        for (Estudiante estudiante : estudiantes) {
            if (java.time.Period.between(estudiante.getFechaNac(), LocalDate.now()).getYears() > 25) {
                System.out.println(estudiante.mostrarInfo());
            }
        }

        // Mostrar el docente que es "Ingeniero" y masculino con mayor edad
        List<Docente> docentes = new ArrayList<>();
        docentes.add(docente1);
        docentes.add(docente2);
        Docente docenteIngenieroMasMayor = docentes.stream()
                .filter(docente -> docente.getProfesion().equals("Ingeniero"))
                .max(Comparator.comparing(Persona::getFechaNac))
                .orElse(null);
        if (docenteIngenieroMasMayor != null) {
            System.out.println(docenteIngenieroMasMayor.mostrarInfo());
        }

        // Mostrar estudiantes y docentes con el mismo apellido
        for (Estudiante estudiante : estudiantes) {
            for (Docente docente : docentes) {
                if (estudiante.getApellido().equals(docente.getApellido())) {
                    System.out.println(estudiante.mostrarInfo());
                    System.out.println(docente.mostrarInfo());
                }
            }
        }
    }
}
