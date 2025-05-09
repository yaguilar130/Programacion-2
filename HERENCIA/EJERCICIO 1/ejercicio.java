class Vehiculo {
    private String marca;
    private String modelo;
    private int año;
    private double precioBase;

    public Vehiculo(String marca, String modelo, int año, double precioBase) {
        this.marca = marca;
        this.modelo = modelo;
        this.año = año;
        this.precioBase = precioBase;
    }

    public String mostrarInfo() {
        return "Marca: " + marca + ", Modelo: " + modelo + ", Año: " + año + ", Precio Base: " + precioBase;
    }
}

class Coche extends Vehiculo {
    private int numPuertas;
    private String tipoCombustible;

    public Coche(String marca, String modelo, int año, double precioBase, int numPuertas, String tipoCombustible) {
        super(marca, modelo, año, precioBase);
        this.numPuertas = numPuertas;
        this.tipoCombustible = tipoCombustible;
    }

    @Override
    public String mostrarInfo() {
        return super.mostrarInfo() + ", Número de Puertas: " + numPuertas + ", Tipo de Combustible: " + tipoCombustible;
    }
}

class Moto extends Vehiculo {
    private int cilindrada;
    private String tipoMotor;

    public Moto(String marca, String modelo, int año, double precioBase, int cilindrada, String tipoMotor) {
        super(marca, modelo, año, precioBase);
        this.cilindrada = cilindrada;
        this.tipoMotor = tipoMotor;
    }

    @Override
    public String mostrarInfo() {
        return super.mostrarInfo() + ", Cilindrada: " + cilindrada + ", Tipo de Motor: " + tipoMotor;
    }
}

// Clase principal para demostrar
public class Main {
    public static void main(String[] args) {
        Coche coche1 = new Coche("Toyota", "Corolla", 2025, 20000, 4, "Gasolina");
        Coche coche2 = new Coche("Honda", "Civic", 2025, 22000, 5, "Diésel");
        Moto moto1 = new Moto("Yamaha", "MT-07", 2025, 8000, 689, "2 Cilindros");

        System.out.println(coche1.mostrarInfo());
        System.out.println(coche2.mostrarInfo());
        System.out.println(moto1.mostrarInfo());

        // Mostrar coches con más de 4 puertas
        Coche[] coches = {coche1, coche2};
        for (Coche coche : coches) {
            if (coche.numPuertas > 4) {
                System.out.println(coche.mostrarInfo());
            }
        }

        // Mostrar coches y motos actuales
        Vehiculo[] vehiculosActuales = {coche1, coche2, moto1};
        for (Vehiculo vehiculo : vehiculosActuales) {
            System.out.println(vehiculo.mostrarInfo());
        }
    }
}
