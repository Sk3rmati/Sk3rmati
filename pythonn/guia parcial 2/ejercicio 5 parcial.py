def num_int():
    num_list = []
    while True:
        try:
            num = (int(input("Indique una cantidad de números que sean enteros y positivos (Para salir del programa use -1): ")))
            if num > 0:
                num_list.append(num)
                continue
            elif num == -1: 
                break
            else:
                print("Ingrese solo números positivos")
        except ValueError:
            print ("Ingrese solamente números")
            continue
    return num_list

def num_mayor(num_list):
    for i in num_list:
        max_num = max(num_list)
    return max_num

def suma_par(num_list):
    suma_par = 0
    for i in num_list:
        if i % 2 == 0:
            suma_par = suma_par + i
    return suma_par

def suma_impar(num_list):
    suma_impar = 0
    for i in num_list:
        if i % 2 != 0:
            suma_impar = suma_impar + i
    return suma_impar

def total_sum(num_list):
    suma_total = 0
    for i in num_list:
        suma_total = sum(num_list)
    return suma_total

def promedio(num_list):
    return sum(num_list)/len(num_list)

        

num_list = num_int()
prom = promedio(num_list)
suma_par(num_list)
suma_impar(num_list) 

print("La lista de números es la siguiente",num_list)
print("La suma de los pares es",(suma_par(num_list)))
print("La suma de los impares es",(suma_impar(num_list)))
print("La suma de todos los números es", (total_sum(num_list)))
print("El promedio de los números en la lista es de",round((promedio(num_list)),2))
print("El mayor de los ingresados corresponde a", (num_mayor(num_list)))

if num_mayor(num_list) > prom:
    print('El numero',(num_mayor(num_list)),'es MAYOR al promedio')
if num_mayor(num_list) < prom:
    print('El numero',(num_mayor(num_list)),'es MENOR al promedio')
if num_mayor(num_list) == prom:
    print('El numero' (num_mayor(num_list)),'es IGUAL al promedio')
    
