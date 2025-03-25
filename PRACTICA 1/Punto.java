/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.punto;

/**
 *
 * @author Lenovo
 */
public class Punto {
    public static void main(String[] args) {
        class Main {
            private double x;
            private double y;

            public Main(double x, double y) {
                this.x = x;
                this.y = y;
            }

            public double[] coordCartesianas() {
                return new double[] {x, y};
            }

            public double[] coordPolares() {
                double r = Math.sqrt(x * x + y * y);
                double theta = Math.atan2(y, x);
                return new double[] {r, theta};
            }

            @Override
            public String toString() {
                return "Punto(" + x + ", " + y + ")";
            }
        }

        Main p = new Main(3, 4);
        double[] cartesianas = p.coordCartesianas();
        System.out.println("Coordenadas Cartesianas: (" + cartesianas[0] + ", " + cartesianas[1] + ")");
        
        double[] polares = p.coordPolares();
        System.out.println("Coordenadas Polares: (r: " + polares[0] + ", θ: " + polares[1] + ")");
        
        System.out.println("Representación String: " + p);
    }
}
