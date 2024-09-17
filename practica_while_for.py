def list_num():
    lista = ""   
    numero = int(input("porfavor digite un numero: "))

    while numero >= 0:
        lista = lista + " numero: " + str(numero)
        numero = int(input("porfavor digite un numero: "))
       
    print(lista)



list_num()
    
    