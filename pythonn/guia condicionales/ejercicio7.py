facts = 1
facts_lista = []

while True:
    try:
        num = int(input("Digite un número entero: \n"))
        if num < 0:
            print("Digite un número entero positivo")
            continue
        else:
            break
    except:
        print('Ingresa un número valido')

if num == 0:
    print('El factorial de 0 es: 1')
    print('\n0! = 1')

else:
    for i in range(1, num+1):
        facts = facts * i

    for j in range(num, 0, -1):
        j = str(j)
        facts_lista.append(j)
    
    print('El factorial de', num, 'es:', facts)
    facts_list_str = ' * '.join(facts_lista)
    print(f'\n{num}! = {facts_list_str} = {facts}')