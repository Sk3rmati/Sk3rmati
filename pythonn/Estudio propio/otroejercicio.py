print("##### EJERCICIO FACTORIALES #####")

num = int(input("Ingresa un número entero positivo: \n"))

if num < 0:
    print("Debe ser un numero entero positivo")

else:
    factorial = 1
    i=1

    while i <= num:
        factorial *= i
        i += 1
        print(factorial)
   
