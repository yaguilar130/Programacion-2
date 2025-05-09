class Empleado {
    private String nombre;
    private String apellido;
    private double salarioBase;
    private int añosAntigüedad;

    public Empleado(String nombre, String apellido, double salarioBase, int añosAntigüedad) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.salarioBase = salarioBase;
        this.añosAntigüedad = añosAntigüedad;
    }

    public double calcularSalario() {
        double bonoAntigüedad = salarioBase * 0.05 * añosAntigüedad;
        return salarioBase + bonoAntigüedad;
    }

    public String getNombre() {
        return nombre;
    }

    public String getApellido() {
        return apellido;
    }
}

class Gerente extends Empleado {
    private String departamento;
    private double bonoGerencial;

    public Gerente(String nombre, String apellido, double salarioBase, int añosAntigüedad, String departamento, double bonoGerencial) {
        super(nombre, apellido, salarioBase, añosAntigüedad);
        this.departamento = departamento;
        this.bonoGerencial = bonoGerencial;
    }

    @Override
    public double calcularSalario() {
        double salarioBaseConBono = super.calcularSalario();
        return salarioBaseConBono + bonoGerencial;
    }
}

class Desarrollador extends Empleado {
    private String lenguajeProgramacion;
    private int horasExtras;

    public Desarrollador(String nombre, String apellido, double salarioBase, int añosAntigüedad, String lenguajeProgramacion, int horasExtras) {
        super(nombre, apellido, salarioBase, añosAntigüedad);
        this.lenguajeProgramacion = lenguajeProgramacion;
        this.horasExtras = horasExtras;
    }

    @Override
    public double calcularSalario() {
        double salarioBaseConBono = super.calcularSalario();
        return salarioBaseConBono + (horasExtras * 20); // Suponiendo que cada hora extra se paga a 20
    }
}

// Clase principal para demostrar
public class Main {
    public static void main(String[] args) {
        Gerente gerente1 = new Gerente("Carlos", "Pérez", 5000, 10, "Ventas", 1200);
        Desarrollador desarrollador1 = new Desarrollador("Ana", "García", 4000, 5, "Python", 12);

        // Mostrar salario calculado
        System.out.println("Salario Gerente: " + gerente1.calcularSalario());
        System.out.println("Salario Desarrollador: " + desarrollador1.calcularSalario());

        // Mostrar gerentes con bono gerencial mayor a 1000
        Gerente[] gerentes = {gerente1};
        for (Gerente gerente : gerentes) {
            if (gerente.bonoGerencial > 1000) {
                System.out.println("Gerente con bono mayor a 1000: " + gerente.getNombre() + " " + gerente.getApellido());
            }
        }

        // Mostrar desarrolladores con más de 10 horas extras
        Desarrollador[] desarrolladores = {desarrollador1};
        for (Desarrollador desarrollador : desarrolladores) {
            if (desarrollador.horasExtras > 10) {
                System.out.println("Desarrollador con más de 10 horas extras: " + desarrollador.getNombre() + " " + desarrollador.getApellido());
            }
        }
    }
}
