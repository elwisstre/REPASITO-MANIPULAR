from tkinter import *
from tkinter import ttk
import numpy as np



def practica():
    global matrizUnica
    matrizUnica = []
    
    matriz = Tk()
    matriz.geometry("500x400")
    matriz.title("manejo de matriz")

    #funcion para la matriz
    def imprimir():
        columnas = int(entradaColum.get())
        filas = int(entradaFilas.get())
        matrizUnica = [[0 for i in range(columnas)] for i in range(filas)]
        areaMatriz.delete('1.0', END)
        for fila in matrizUnica:
            linea = " ".join(str(valor) for valor in fila)
            areaMatriz.insert(END, linea + '\n')
    def ingresarNUm():
        global matrizUnica
        col = int(entradaPosCol.get())
        fila = int(entradaPosFil.get())
        num = int(entradaNum.get())
        if 0 <= fila < len(matrizUnica) and 0 <= col < len(matrizUnica[0]):
            matrizUnica[fila][col] = num
            areaMatriz.delete('1.0', END)
            for fila in matrizUnica:
                linea = " ".join(str(valor) for valor in fila)
                areaMatriz.insert(END, linea + '\n')
            
        

    #crear notebook (pestañas)
    notebook = ttk.Notebook(matriz)
    notebook.pack(expand=True, fill="both")
    #crear las pestañas
    ingreso = Frame(notebook)
    operaciones = Frame(notebook)
    #agregar las pestañas al notebook
    notebook.add(ingreso, text="Ingresar Datos")
    notebook.add(operaciones, text="Operaciones")
    #contenido primera pestaña
    nColum = Label(ingreso, text = "Numero de Columnas: ").grid(row = 0, column = 0)
    nFilas = Label(ingreso, text = "Numero de Filas: ").grid(row = 1, column = 0 )
    entradaColum = Entry(ingreso, width = 20)
    entradaColum.grid(row = 0, column = 1)
    entradaFilas = Entry(ingreso, width = 20)
    entradaFilas.grid(row = 1, column = 1)
    #centrar primera pestaña
    ingreso.grid_columnconfigure(0, weight=1)
    ingreso.grid_columnconfigure(2, weight=1)
    ingreso.grid_columnconfigure(1, weight=0)
    #punto de impresion matriz
    areaMatriz = Text(ingreso, height=10, width=40)
    areaMatriz.grid(row=5, column=0, columnspan=3)
    areasecond = Text(operaciones, height=10, width=40)
    areasecond.grid(row=5, column=0, columnspan=3)

    
    #texto en la segunda pestaña
   
    manejo = Label(operaciones, text = "AHORA A PONER NUMEROS!!").grid(row = 0, column = 1)
    CambioColum = Label(operaciones, text = "Posicion Columna: ").grid(row = 1, column = 0)
    cambioFila = Label(operaciones, text = "Posicion Fila: ").grid(row = 2, column = 0)
    numero = Label(operaciones, text = "Numero: ").grid(row = 3, column = 0)
    
    #entradas segunda pestaña
    entradaPosCol = Entry(operaciones, width = 20)
    entradaPosCol.grid(row = 1, column = 1)
    entradaPosFil = Entry(operaciones, width = 20)
    entradaPosFil.grid(row = 2, column = 1)
    entradaNum = Entry(operaciones, width = 20)
    entradaNum.grid(row = 3, column = 1)
    #centrar segunda pestaña
    operaciones.grid_columnconfigure(0, weight=1)
    operaciones.grid_columnconfigure(2, weight=1)
    operaciones.grid_columnconfigure(1, weight=0)
    #botones
    botonImprimir = Button(ingreso, text = "mostrar matriz", command = imprimir)
    botonImprimir.grid(row=3, column=1)
    botonIngresar = Button(operaciones, text = "Ingresar Numero", command = ingresarNUm)
    botonIngresar.grid(row=4, column = 0)
    botonImp = Button(operaciones, text = "Refrescar matriz", command = imprimir)
    botonImp.grid(row=4, column = 1)
    #funcion para la matriz
   
        
                 
 
    
    














practica()
    
