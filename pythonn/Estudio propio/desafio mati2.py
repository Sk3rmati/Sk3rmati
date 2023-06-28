print("##### EJERCICIO DOS MATI #####")

cadena=(str(input("Ingrese una frase:\n"))).lower()

cadena_sep=cadena.split()
print(cadena_sep)

dict = {}

for i in cadena_sep:
    if i not in dict:
        count= cadena_sep.count(i)
        dict[i] = count

print(dict)



