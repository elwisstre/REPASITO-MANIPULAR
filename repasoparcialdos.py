"""Problema 1: Arreglos Unidimensionales
Descripción: Escribe un programa en Python que lea una lista de números enteros introducidos por el usuario y 
luego realice las siguientes operaciones:
Calcule y muestre la suma de todos los números.
Calcule y muestre el promedio de los números.
Encuentre y muestre el número más grande y el más pequeño de la lista."""

def puntouno():

    cant = int(input("digite el tamaño del arreglo: "))
    lista = [None]*cant
    cont = 0
    for i in range(0, len(lista),1):
        lista[i] = int(input(f"ingrese un numero en la posicion {i}: "))
        cont += lista[i]
    promedio = cont/cant
    maximo = max(lista)
    mini = min(lista)

    print("El arreglo es: ",lista)
    print("la suma de todos los valores ingresados es: ",cont)
    print("el promedio del arreglo es: ",promedio)
    print(f"El numero más grande del arreglo es: {maximo},\nY el numero más pequeño es: {mini}")

"""Problema 2: Arreglos Bidimensionales
Descripción: Escribe un programa en Python que cree una matriz de 3x3, lea los valores introducidos por el usuario para llenar la matriz y
luego realice las siguientes operaciones:
Calcule y muestre la suma de todos los elementos de la matriz.
Calcule y muestre el promedio de los elementos de la matriz.
Encuentre y muestre el número más grande y el más pequeño de la matriz."""
import numpy as np
def puntodos():
    colum = int(input("digite el numero de columnas del arreglo: "))
    fila = int(input("digite el numero de filas del arreglo: "))
    matriz = np.zeros((fila,colum))
    cont = 0
    for i in range(fila):
        for u in range(colum):
            matriz[i][u] = int(input(f"ingrese un numero en la posicion{[i]}{[u]}: "))
            cont += matriz[i][u]
    promedio = cont/(colum*fila)
    maximo = np.max(matriz)
    minimo = np.min(matriz)
    print(matriz)
    print("la suma de todos los numeros es: ",cont)
    print("el promedio de los numeros es: ",promedio)
    print(f"el numero mas grande es: {maximo}, y el más pequeño es: {minimo}")

puntodos()
