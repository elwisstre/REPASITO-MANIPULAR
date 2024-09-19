
print("Este es un programa en el cual tendrás que adivinar un numero del 1 al 100")

def adivinar():
    numero =  int(input("digite un numero y averigua si es o no el que pedimos: "))
    contador_intentos = 0
    if numero == 73:
        print("HAS GANADO, ADIVINASTE CON EXITO EL NUMERO")
        contador_intentos += 1

        


    while (numero != 73 and numero != "-"):
        numero =  int(input("digite otro  numero y averigua si es o no el que pedimos: "))
        contador_intentos += 1
       


        
        

        if numero >= 0 and numero <= 20:
            print("estás más frío que el corazón de tu ex")
            
        elif numero > 20 and numero <= 30:
            print("te acercas pero aun no lo logras")
        elif numero > 30 and numero <= 40:
            print("estas tibiooooo")
            
        elif numero > 40 and numero <= 50:
            print("que calor mano, pero sigue intentando")
            
        elif numero > 50 and numero <= 60:
            print("te acercas, pero tu iq aun no da con el num")
            
        elif numero > 60 and numero <= 70:
            print("uy, casi le atinas pero no, sigue por este rango menor!")
        elif numero > 100:
            print("es invalido, digite unno menor a 100")
            

        elif numero > 70 or numero == 72 or numero == 71:
            print("CASI casito, pero no")
            
        elif numero > 74 and numero <= 85:
            print("te alejaste de la verdad y no te hizo libre")
            
        elif numero > 85 and numero < 100:
            print("te alejaste mucho, frio, me aburrí")
            
        elif numero == 73:
            print("HAS GANADO, ADIVINASTE CON EXITO EL NUMERO")
            contador_intentos += 1
            
        elif numero < 0:
            print("es invalido, digita otro")
            
            
        else:
            print("invalido")
            
    print("el total de intentos que te tomó adivinar el numero: ", numero, "fueron: ", contador_intentos)
adivinar()