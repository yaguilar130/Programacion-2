import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.paint.Color;
import javafx.scene.shape.Line;
import javafx.stage.Stage;

class Punto {
    private double x;
    private double y;

    public Punto(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }
}

class Linea {
    private Punto p1;
    private Punto p2;

    public Linea(Punto p1, Punto p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    public Line dibujarLinea() {
        Line line = new Line(p1.getX(), p1.getY(), p2.getX(), p2.getY());
        line.setStroke(Color.BLACK);
        return line;
    }
}

public class Grafico extends Application {
    @Override
    public void start(Stage primaryStage) {
        Group root = new Group();

        // Crear puntos
        Punto p1 = new Punto(100, 150);
        Punto p2 = new Punto(300, 150);
        
        // Crear línea
        Linea linea = new Linea(p1, p2);
        root.getChildren().add(linea.dibujarLinea());

        Scene scene = new Scene(root, 400, 300);
        primaryStage.setTitle("Gráfico con JavaFX");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
