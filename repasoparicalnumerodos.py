"""Descripción: Crea una aplicación GUI en Python utilizando Tkinter. La aplicación debe tener
las siguientes características:
Un campo de entrada donde el usuario pueda ingresar un número.
Un botón que, cuando se presione, agregue el número ingresado a una lista.
Un área de texto que muestre todos los números en la lista, cada uno en una nueva línea.
Un botón que, cuando se presione, muestre el número más grande, el más pequeño y
la suma de todos los números en la lista en un cuadro de mensaje."""

from tkinter import *
app = Tk()
app.geometry("500x400")
app.title("Manejo de Numeros")
numeros = []
arriba = Frame(app)
medio = Frame(app)
abajo = Frame(app)
masabajo = Frame(app)

def agregarNum():
    global numeros
    num = int(entradaNum.get())
    numeros.append(num)
    areaApp.delete('1.0', END)  
    areaApp.insert(END,str(numeros))

def mayorMenor8():
    menor = min(numeros)
    mayor = max(numeros)
    areaApp.delete('1.0', END)
    areaApp.insert(END, f"el numero más grande es: {mayor}\nY el numero más pequeño es: {menor}")
def suma():
    suma = sum(numeros)
    areaApp.delete('1.0',END)
    areaApp.insert(END, f"la suma de todos los numeros INGRESADOS en la lista es: {suma}")
    
    




#Texto y entradas
nNum = Label(arriba, text = "Por favor Ingresar un Numero: ")
nNum.grid(row = 0, column = 0)
entradaNum = Entry(arriba, width = 20)
entradaNum.grid(row = 1, column = 0)
#Botones
botonAgg = Button(medio, text = "Ingresar número a la lista.", command = agregarNum )
botonAgg.grid(row = 2, column = 0)
botonMostrar = Button(medio, text = "Mostrar número más peque y grande de la lista.", command = mayorMenor8)
botonMostrar.grid(row = 2, column = 1)
botonSuma = Button(abajo, text = "La suma de todos los números.", command = suma)
botonSuma.grid(row = 3, column = 1)

#impresion
areaApp = Text(masabajo, height = 10, width = 40)
areaApp.grid(row = 4, column = 0, columnspan = 3)




arriba.pack()
medio.pack()                                                                   
abajo.pack()
masabajo.pack()
