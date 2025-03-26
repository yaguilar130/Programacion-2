/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.circulo;

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

class Circulo extends JPanel {
    private Punto centro;
    private int radio;

    public Circulo(Punto centro, int radio) {
        this.centro = centro;
        this.radio = radio;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawOval(centro.getX() - radio, centro.getY() - radio, radio * 2, radio * 2);
    }

    public static void main(String[] args) {
        Punto centro = new Punto(200, 150);
        Circulo circulo = new Circulo(centro, 50);

        JFrame frame = new JFrame("Dibujo de Círculo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        frame.add(circulo);
        frame.setVisible(true);
    }
}