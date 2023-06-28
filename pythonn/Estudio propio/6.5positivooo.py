print("##### EJERCICIO POSITIVOS #####")
#Crear un codigo donde solo acepte numeros positivos

num=(float(input("Digite un numero: (Solo se aceptan positivos)\n")))

if num <= 0:
    print("El numero debe ser positivo")
    while num <= 0:
        print("No es un numero positivo")
        num=(float(input("Digite un numero positivo: \n")))
        if num > 0:
            continue
elif num == 0:
    while 0 == num:
        print("No es un numero positivo")
        num=(float(input("Digite un numero positivo: \n")))
        if num > 0:
            continue
        

print("El numero es positivo")

    