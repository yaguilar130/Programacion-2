/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.pila;

/**
 *
 * @author Lenovo
 */
public class Pila {
    private long[] arreglo;
    private int top;
    private int n;

    public Pila(int n) {
	this.n = n;
	this.top = -1;
	this.arreglo = new long[n];
    }

    public void push(long e) {
	if (isFull()) {
	    System.out.println("La pila está llena.");
	    return;
	}
	top++;
	arreglo[top] = e;
    }

    public Long pop() {
	if (isEmpty()) {
	    System.out.println("La pila está vacía.");
	    return null;
	}
	long e = arreglo[top];
	top--;
	return e;
    }

    public boolean isEmpty() {
	return top == -1;
    }

    public boolean isFull() {
	return top == n - 1;
    }

    public static void main(String[] args) {
	
	Pila pila = new Pila(5);

	
	pila.push(10);
	pila.push(20);
	pila.push(30);

	
	System.out.println("Elemento pop: " + pila.pop());  

	
	System.out.println("¿Está vacía? " + pila.isEmpty());  
       
	pila.push(40);
	pila.push(50);
	pila.push(60);  

	
	System.out.println("Elemento en la parte superior: " + pila.arreglo[pila.top]);
    }
}
