#COMPARANDO TÉRMINOS NÚMERICOS ASCII
print ("Comparando números")

bencina = False
encendido = True
edad = 18

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

#WHILE 

edad = 18
num = 0

#BUCLES INFINITOS

while edad < 18:
    print("Edad inválida")

#¿Que hace este bucle?

while num <= 100:
    print(num)
    num += 2
    #Es lo mismo a num = num + 2
print("Primer bucle finalizado")