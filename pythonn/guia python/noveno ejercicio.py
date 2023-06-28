print("##### EJERCICIO NUEVE #####")
num = [4,3,8,12,6,10,14,3,6]

print(num)

del num [-1]

print (num)



num.insert (0,2)

print (num)


num_no_repeat = []

for i in num:
    if i not in num_no_repeat:
        num_no_repeat.append (i)

print (num_no_repeat)



list_ordenados = sorted(num)

print (list_ordenados)

MA = sum(num) / len(num)
print (round(MA, 2))



if len(list_ordenados) % 2 == 0:
    mediana_pos_1 = (len(list_ordenados) / 2) -1
    mediana_pos_2 = mediana_pos_1 + 1

    mediana = (list_ordenados[mediana_pos_1] + list_ordenados[mediana_pos_2]) / 2
else:
    mediana_pos_1 = (len(list_ordenados) // 2)
    mediana = list_ordenados[mediana_pos_1]

print (mediana)
