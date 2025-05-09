import java.util.ArrayList;
import java.util.List;

class Jugador {
    private String nombre;
    private int numero;
    private String posicion;

    public Jugador(String nombre, int numero, String posicion) {
        this.nombre = nombre;
        this.numero = numero;
        this.posicion = posicion;
    }

    public void mostrarInfo() {
        System.out.println("Nombre: " + nombre + ", Número: " + numero + ", Posición: " + posicion);
    }
}

class Portero extends Jugador {
    private String habilidadEspecial;

    public Portero(String nombre, int numero, String habilidadEspecial) {
        super(nombre, numero, "Portero");
        this.habilidadEspecial = habilidadEspecial;
    }

    public void mostrarInfo() {
        super.mostrarInfo();
        System.out.println("Habilidad Especial: " + habilidadEspecial);
    }
}

class Defensa extends Jugador {
    private String habilidadEspecial;

    public Defensa(String nombre, int numero, String habilidadEspecial) {
        super(nombre, numero, "Defensa");
        this.habilidadEspecial = habilidadEspecial;
    }

    public void mostrarInfo() {
        super.mostrarInfo();
        System.out.println("Habilidad Especial: " + habilidadEspecial);
    }
}

class Mediocampista extends Jugador {
    private String habilidadEspecial;

    public Mediocampista(String nombre, int numero, String habilidadEspecial) {
        super(nombre, numero, "Mediocampista");
        this.habilidadEspecial = habilidadEspecial;
    }

    public void mostrarInfo() {
        super.mostrarInfo();
        System.out.println("Habilidad Especial: " + habilidadEspecial);
    }
}

class Delantero extends Jugador {
    private String habilidadEspecial;

    public Delantero(String nombre, int numero, String habilidadEspecial) {
        super(nombre, numero, "Delantero");
        this.habilidadEspecial = habilidadEspecial;
    }

    public void mostrarInfo() {
        super.mostrarInfo();
        System.out.println("Habilidad Especial: " + habilidadEspecial);
    }
}

class Equipo {
    private String nombre;
    private List<Jugador> jugadores;

    public Equipo(String nombre) {
        this.nombre = nombre;
        this.jugadores = new ArrayList<>();
    }

    public void agregarJugador(Jugador jugador) {
        jugadores.add(jugador);
    }

    public void mostrarEquipo() {
        System.out.println("Equipo: " + nombre);
        for (Jugador jugador : jugadores) {
            jugador.mostrarInfo();
            System.out.println("---");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Equipo equipo = new Equipo("Leones FC");
        equipo.agregarJugador(new Portero("Juan", 1, "Atajadas"));
        equipo.agregarJugador(new Defensa("Carlos", 2, "Marcaje"));
        equipo.agregarJugador(new Mediocampista("Luis", 8, "Pases"));
        equipo.agregarJugador(new Delantero("Pedro", 9, "Goles"));

        // Mostrar información del equipo
        equipo.mostrarEquipo();
    }
}
