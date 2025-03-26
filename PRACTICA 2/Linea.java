/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.linea;

/**
 *
 * @author Lenovo
 */
import javax.swing.*;
import java.awt.*;

class Punto {
    private int x;
    private int y;

    public Punto(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
}

class Linea extends JPanel {
    private Punto p1;
    private Punto p2;

    public Linea(Punto p1, Punto p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawLine(p1.getX(), p1.getY(), p2.getX(), p2.getY());
    }

    public static void main(String[] args) {
        Punto p1 = new Punto(100, 150);
        Punto p2 = new Punto(300, 150);
        Linea linea = new Linea(p1, p2);

        JFrame frame = new JFrame("Dibujo de Línea");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        frame.add(linea);
        frame.setVisible(true);
    }
}