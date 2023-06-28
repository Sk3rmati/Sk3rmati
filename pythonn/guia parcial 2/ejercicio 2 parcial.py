def names():
    names_list = []
    while True:
        try:
            name = (str(input("Introduce un nombre (o 'exit' para salir): ")))
            if name == 'exit':
                break
            elif name.isalpha() == False:
                print ("No se permiten números")
                continue
            else:
                name = name.replace(" ","")
                if name:
                    names_list.append(name)
        except: ValueError
    return names_list
    

def names_count(names_list):
    letters_total = 0
    for i in names_list:
       letters_total += len(i)
    return letters_total




names_list = names()
letters_total = names_count(names_list)

print ("La lista de nombres ingresados es la siguiente:",names_list)
print ("La cantidad de letras totales en la lista es de:",letters_total)

