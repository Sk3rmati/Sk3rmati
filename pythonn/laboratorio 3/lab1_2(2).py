##Parte 2 (listas)##
a = [21,8,15,3,12]
b = [10,9,12,15,18]
c = [2,3,8,9,12]
newlist=[4,5,6]

suma=(a+b+c) ##Concatenar todas las listas e imprimir la lista obtenida.
print(suma)

suma.insert(-1,20)##Agregar el número 20 en la penúltima posición de la lista.
print(suma)

suma.sort(reverse=True)##Ordenar la lista de forma descendente. 
print(suma)

otralista=(suma, newlist) ##Insertar la lista [4,5,6] en la última posición de la lista ordenada
print(otralista)

otralista1=sum(suma+newlist)##Sumar todos los números dentro de la lista.
print(otralista1) 

otralista_prom=(otralista1/19)###Obtener el promedio simple de la lista
print(otralista_prom)




