##Las tuplas son como las listas solo que estan no pueden ser modificadas, además que las listas se pueden transformar
#en estas mismas.
tuplaa = ("Mati", "Diego", "Cristian", "Nelson","Alberto")
print(type(tuplaa))
##Para hacer una tupla debes usar parentesis, sino ocupar el codigo "tuple"

#Se puede ordenar una tupla con Sorted (str)
tuplaordenada = sorted(tuplaa)
print(tuplaordenada) ##Se ordena de forma alfabetica

print(type(tuplaa))##Se vuelve a verificar que sea una tupla

alumnos = [("Diego", 6.2, 6.0), ("Cristian", 5.2, 6.8), ("Minecraft", 4.3, 5.7)] #Creando una lista con str y float
alumnos2=tuple(alumnos) ##Transformando a tupla
print(alumnos2)
print(type(alumnos2)) #Verificar si se transformó en una tupla

for estudiantes in alumnos2:
    print(estudiantes)

promedios = [] #Creando una lista

for i in alumnos2:
    nombre = i[0]
    labs1   = i[1]
    labs2   = i[2]
    promedio = round((labs1 * 0.6) + (labs2 * 0.4),3)
    promedios.append((nombre, promedio))

print(promedios)

