#01 - OPERADORES ARITMETICOS

#Se declaran variables para proceder al uso de operadores
a = 2
b = 6
c= 10
d = 30

#Operaciones comunes
print("suma entre dos números", a + b) 
print("multiplicación entre dos números", c*a)
print("Números elevados", b**a)
print("Resta de números", d - c)
print("División de números", d/a)

#Operaciones con flotantes
T= 2
D = 6

#Por consecuencia

V = T * D

#Declarando variables de tipo compleja

c1 = 4 + 3j
print(type(c1))

#Creando un número complejo con complex

c2 = complex(3, -5)
print("el numero complejo es:" ,c2)

print(c2.real) #Se obtiene la parte real del número complejo
print(c2.imag) #Se obtiene la parte imaginaria del número complejo

#¿Se puede multiplicar un String con un número entero?

print("Una cadena de texto" * 5)

#Y lo siguiente?
#print("Hola" * 3.5 * 2) - error
#Si el resultado da 7 (número entero), ¿Por qué da error?

#¿y esta operación de suma?
print("Hola + 18") #Se puede pero solo con la función String

#02. OPERADORES DE COMPARACIÓN

#Comparando términos numéricos

a = 1
b = 2
c = 3
d = 4

print("Comparando números")
#print(a == b) #b igual a
print(a != b) #es distinto a
print(a < b) #b es mayor que a
print(b < a) #a es mayor que b
print(c > d) #c es mayor que d
print(c < d) #d es mayor que c
print("\n")

#Comparando cadenas de caracteres

animal_doméstico = "perro"
animal_salvaje = "tigre"

print("Comparando cadenas de carácteres")
print(animal_doméstico == animal_salvaje)
print(animal_doméstico != animal_salvaje)
print(animal_doméstico > animal_salvaje)
print(animal_doméstico < animal_salvaje)

#TAREA COMPARAR CADENAS DE TEXTO Y AVERIGUAR POR QUÉ DA TRUE O FALSE

#BUCLES

#if es "Si"
#else es "Sino"
#elif es "Sino si"

#Da TRUE porque lo lee siguiendo el ASCII (Valor número de cada letra)

#COMPARANDO TÉRMINOS NÚMERICOS ASCII
print ("comparando números")

bencina = False
encendido = True
edad = 20

#Utilizando el operador AND
if bencina and encendido:
    print("El auto puede avanzar")
else:
    print("El auto no puede avanzar")

#Utilizando el operador OR
if bencina or encendido:
    print("El auto puede avanzar")
else:
    print("El auto no puede avanzar")

#Utilizando el operador NOT junto al AND
if not bencina and encendido:
    print("El auto puede avanzar") #El NOT invierte el True o False en la variable (En este caso "bencina")
else: 
    print("El auto no puede avanzar")

#Utilizando el operador NOT junto al OR
if not bencina and encendido:
    print("El auto puede avanzar")
else:
    print("El auto no puede avanzar")

#Utilizando el operador NOT junto al AND y OR
if not bencina or (encendido and edad >= 17):
    print("El auto puede avanzar")
else: 
    print("El auto no puede avanzar")