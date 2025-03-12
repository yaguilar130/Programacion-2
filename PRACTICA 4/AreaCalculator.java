/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.areacalculator;

/**
 *
 * @author Lenovo
 */
public class AreaCalculator {

    public double area(double radio) {
        return Math.PI * radio * radio; // Círculo
    }

    public double area(double base, double altura) {
        return base * altura; // Rectángulo
    }

    public double area(double base, double altura, boolean esTriangulo) {
        if (esTriangulo) {
            return (base * altura) / 2; // Triángulo
        }
        return 0;
    }

    public double area(double baseMenor, double baseMayor, double altura, String tipo) {
        if (tipo.equals("trapecio")) {
            return ((baseMenor + baseMayor) * altura) / 2; // Trapecio
        }
        return 0;
    }

    public double areaPentagono(double lado) {
        return (5 * lado * lado) / (4 * Math.tan(Math.PI / 5)); // Pentágono
    }

    public static void main(String[] args) {
        AreaCalculator calc = new AreaCalculator();
        System.out.println("Área del círculo: " + calc.area(5));
        System.out.println("Área del rectángulo: " + calc.area(4, 6));
        System.out.println("Área del triángulo: " + calc.area(4, 3, true));
        System.out.println("Área del trapecio: " + calc.area(3, 5, 4, "trapecio"));
        System.out.println("Área del pentágono: " + calc.areaPentagono(3));
    }
}