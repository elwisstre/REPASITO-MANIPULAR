
""" Cómo definir una matriz 
nombre = numpy.array([[0]*n]*m)
numeros = numpy.zeros((m,n))
insertar datos en un arreglo bi
nombreMatriz[posicionFila][posicionColumna] = valor
O
nombreMatriz[posicionFila , posicionColumna] = valor
"""
"""import numpy    
numeros = numpy.zeros((4,3))
print(numeros)"""
import numpy    
"""numeros = numpy.array([[0]*3]*4)
print(numeros)"""
"""✓ nombreMatriz.sum(): suma todos los elementos de la matriz
 ✓ numpy.sort(matriz): devuelve una matriz ordenada los elementos 
por fila
 ✓ numpy.add(matriz1, matriz2): suma componente a componente 
los datos de las matrices pasadas como parámetro
 ✓ numpy.greater(matriz1, matriz2): retorna una matriz de booleanos 
que indica si componente a componente un valor es mayor que el 
otr"""

def holi():
        kolu = int(input("digite el numero de columnas que desea en el arreglo: "))
        fool = int(input("digite el numero de filas que desea en el arreglo: "))
        if fool > 1 and kolu > 2:
            numeros = numpy.zeros((fool,kolu))
            for fila in range(fool):
                for column in range (kolu):
                    numeros[fila][column] = float(input(f"digite un numero para la posicion, fila:{fila},y columna: {column} :"))
                
                calculo1 = (numeros[0][1] * numeros[0][2]) - numeros[1][2]
                calculo2 = numeros[1][1] + (numeros[1][0]/2) - (numeros[0][0]*4)
                calculo3 = (4* numeros[1][2]) - (10 * numeros[1][0])
            print("Valor1",calculo1)
            print("Valor2",calculo2)
            print("Valor3",calculo3)
            for j in range(min(fool,kolu)):
                    print(numeros[j][j])
                
        else:
            print("los valores en en arreglo no son sufucientemente grandes para realizar las operacion, intenta con filas mayores a 1 y columnas a 2")
                
        print(numeros)



""" Ejercicio: Se requiere un programa para almacenar los resultados 
de las últimas elecciones de rector de la universidad del Valle. 
Los datos deben almacenarse en una matriz donde cada fila 
corresponde a una sede y cada columna corresponde a un 
candidato. El programa debe mostrar la tabla con los nombres 
de las sedes y los nombres de los candidatos y cada uno de los 
resultados. La aplicación también debe mostrar el candidato 
ganador."""

def arr():
    
    cant = int(input("digite la cantidad de candidatos: "))
    sed = int(input("ingrese la cantidad de sedes: "))
    candidatos = [None]*cant
    sedes = [None]*sed

    for i in range(cant):
            candidatos[i] = input(f"digite el nombre del candidato numero, {[i+1]}")

    for u in range(sed):
            sedes[u] = input(f"digite el nombre de la sede numero, {[u+1]}")

    resultados = numpy.zeros( (sed, cant), dtype=int)
    for pr in range(sed):
        for ui in range(cant):
            resultados[pr][ui] = int(input(f"Digite los votos para el candidato {candidatos[ui]} en la sede {sedes[pr]}: "))
    totales = resultados.sum(axis=0)

    
    print("total votos para cada candidato")
    for y in range(cant):
        print(f"{candidatos[y]} : {totales[y]} votos")
    max_votos = totales.max()
    ganador = candidatos[totales.argmax()]
    print(f"el candidatos ganador es {ganador}, con un total de: {max_votos}")
        


    #filas = input(f"ingrese el nombre de la sede, {[u]}")
    print("los candidatos son: ", candidatos)
    print("las sedes son: ", sedes)
    print("total votos: ", "\n", resultados)
    
    

arr()

