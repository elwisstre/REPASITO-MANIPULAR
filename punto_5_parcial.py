"""Se está realizando una encuesta sobre las actividades que realizan las personas 
en su tiempo libre. A cada persona se le pregunta el tiempo libre que tiene semanalmente y la actividad principal 
que realiza. Usted debe desarrollar un programa que permita registrar los datos de la encuesta. Para ingresar 
los datos de cada persona se utilizan los siguientes códigos
Tenga en cuenta que el programa debe permitir registrar la información de n personas, donde n es un número 
entero digitado por el usuario. Una vez se termine de ingresar la información, debe aparecer la siguiente 
información estadística: 
• La cantidad de personas que tienen entre 6 y 9 horas libres y que prefieren leer. 
• El porcentaje de personas que prefieren ver televisión en su tiempo lib"""

def encuesta():
    n=int(input("Porfavor digite la cantidad de encuestados: "))
    menosseis = 0
    sixnine = 0
    masnueve = 0
    leer = 0
    tivi = 0
    aprieta = 0
    duo = 0
    
#contadores necesarios para los condicionales dentro del for.

    

    for i in range(0,n,1):
#Al pedir  variables por orden se programan las condiciones, OJO!!!, no revolver. OoO
        tiempo= int(input("¿cuanto tiempo cree usted que tiene libre semanalmente?:\nmenos de seis horas: 1 \nentre seis horas y nueve horas: 2 \nmas de nueve horas: 3 \n: "))
        if tiempo == 1:
            menosseis += 1
        elif tiempo == 2:
            sixnine += 1
        elif tiempo == 3:
            masnueve += 1
#implementamos while como bucle para cuando el usuario digita un valor incorrecto Y ESTÁ OBLIGADO A INGRESAR UNO CORRECTO (N <= 3)
        while (tiempo > 3):
            print("es invalido!!!")
            tiempo= int(input("¿cuanto tiempo cree usted que tiene libre semanalmente?:\nmenos de seis horas: 1 \nentre seis horas y nueve horas: 2 \nmas de nueve horas: 3 \n: "))
            




        actividad=input("que haces en tu tiempo libre?: \nLeer : L \nver television: TV \nhacer deporte: DP \ndormir: D \n")
#Al ingresar la actividad es posible que se ingrese en minuscula o una mezcla de mayuscula y minuscula, usando .upper() se cambia forzadamente a MAYUSCULA, evitando errores y haciendolo más fácil de manipular, además a eso hay que asignarle una variable, ej: mayus_actividad = actividad.upper()//

        mayus_actividad = actividad.upper()

        if tiempo == 2 and mayus_actividad == "L":
            duo += 1

        elif mayus_actividad == "L":
            leer += 1
        elif mayus_actividad == "TV":
            tivi += 1
        elif mayus_actividad == "DP" or actividad == "D":
            aprieta += 1
        
        while (mayus_actividad != "L"and mayus_actividad != "TV"and mayus_actividad != "DP"and mayus_actividad != "D"):
            print("es invalido!!!")
            actividad=input("que haces en tu tiempo libre?: \nLeer : L \nver television: TV \nhacer deporte: DP \ndormir: D \n")
    print("la cantidad de personas que leen y tienen un promedio de tiempo libre de 6 y 9 horas es: ", duo)
#programamos la formula del porcentaje de los que ven tv acá abajo para que los contadores aumenten su valor, OJO!!!, si se pone arriba antes del for, estarías dandole los valores que esten ahí como constantes, ej: tivi = 0//
    total_viewers = tivi/n * 100
    print("el porcentaje total de personas que ven television parchados es: ", total_viewers,"%")




encuesta()
#no se olvide de INVOCAR la funcion :)