while True:
    try:
        num = int(input("Digite un numero entero:\n "))
        if num < 1:
            print("Digite un valor igual o mayor a 1")
            continue
        else:
            break
    except ValueError:
        print("Digite un numero valido")
print()

# Gestiona la impresion de las lineas
ls = 1
for i in range(num):
    listaa = []
    suma = 0
    L = 0

    # Realiza los calculos que se imprimiran por linea.
    while L <= i:
        suma += ls
        listaa.append(str(ls))
        ls += 2
        L += 1

    strngg = ' + '.join(listaa)

    print(f'{i+1}**3 = {suma} ➜  {strngg} = {suma}')