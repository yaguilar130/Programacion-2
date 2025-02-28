/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.cola;

/**
 *
 * @author Lenovo
 */
public class Cola {
    private long[] arreglo;
    private int inicio;
    private int fin;
    private int n;
    private int size;

    public Cola(int n) {
        this.n = n;
        this.inicio = 0;
        this.fin = -1;
        this.arreglo = new long[n];
        this.size = 0;
    }

    public void insert(long e) {
        if (isFull()) {
            System.out.println("La cola está llena.");
            return;
        }
        fin = (fin + 1) % n;
        arreglo[fin] = e;
        size++;
    }

    public Long remove() {
        if (isEmpty()) {
            System.out.println("La cola está vacía.");
            return null;
        }
        long e = arreglo[inicio];
        inicio = (inicio + 1) % n;
        size--;
        return e;
    }

    public Long peek() {
        if (isEmpty()) {
            System.out.println("La cola está vacía.");
            return null;
        }
        return arreglo[inicio];
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == n;
    }

    public int size() {
        return size;
    }

    public static void main(String[] args) {
        
        Cola cola = new Cola(5);

        cola.insert(10);
        cola.insert(20);
        cola.insert(30);

        System.out.println("Elemento en la parte delantera: " + cola.peek());
        System.out.println("Elemento removed: " + cola.remove());  
        System.out.println("¿Está vacía? " + cola.isEmpty());  

       
        cola.insert(40);
        cola.insert(50);
        cola.insert(60); 
        System.out.println("Tamaño actual de la cola: " + cola.size());  
    }
}