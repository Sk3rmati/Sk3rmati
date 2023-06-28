print("##### TERCERO EJERCICIO PARCIAL DOS #####")

#Se cuenta con dos sets: el primero contiene las temperaturas mínimas tomadas el mes de
#Mayo en Osorno. El segundo set contiene las temperaturas máximas: 

temp_min = {9, 5, 2, 7, 6, 1}
temp_max = {12, 14, 11, 10, 15,9}

#Comprobar si el grado 9 esta en ambas temperaturas

print(f"El grado que esta en ambas temperaturas es:{temp_min & temp_max}")

#Comprobar si al menos la temperatura 6°C y 17°C está en alguno de los sets}

if 6 in temp_min and 17 not in temp_max:
    print("Hubieron 6° en temperaturas minimas en Osorno")

if not 17 in temp_max:
    print("No hubieron 17° en mayo, en la ciudad de Osorno")


#Elevar a 4° todas las temperaturas dentro de los sets


temp_min={(9**4), (5**4), (2**4), (7**4), (6**4), 1} #No elevo el 1 por que da 1 XD


temp_max={(12**4), (14**4), (11**4), (10**4), (15**4),(9**4)}




print(f"Las temperaturas minimas fueron elevadas 4 veces a lo cual ahora son:{temp_min}")
print(f"Las temperaturas maximas fueron elevadas 4 veces a lo cual ahora son:{temp_max}")

#Unir ambos sets en uno solo

temperaturas=temp_min.union(temp_max)


print(temperaturas)
print(type(temperaturas))

