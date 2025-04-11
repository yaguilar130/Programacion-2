/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.d;

/**
 *
 * @author Lenovo
 */
class A {
    protected int x;
    protected int z;

    public A(int x, int z) {
        this.x = x;
        this.z = z;
    }

    public void incrementaXZ() {
        x++;
        z++;
    }

    public void incrementaZ() {
        z++;
    }
}

class B {
    protected int y;
    protected int z;

    public B(int y, int z) {
        this.y = y;
        this.z = z;
    }

    public void incrementaYZ() {
        y++;
        z++;
    }

    public void incrementaZ() {
        z++;
    }
}

class D extends A {
    B b;

    public D(int x, int y, int z) {
        super(x, z);
        b = new B(y, z);
    }

    public void incrementar() {
        incrementaXZ();  
        b.incrementaYZ(); 
        System.out.println("x: " + x + ", y: " + b.y + ", z: " + z);
    }

    public static void main(String[] args) {
        D d = new D(1, 2, 3);
        d.incrementar();
    }
}