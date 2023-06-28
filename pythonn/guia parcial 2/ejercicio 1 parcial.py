def cantidad():
    while True:
        try:
            num = (int(input("Digite la cantidad de números a ingresar: \n")))
            if num < 0:
                print ("Solamente se permiten números positivos")
                continue
            else:
                break
        except ValueError:
            print ("Digite solamente números")
            continue
    return num

def pedir(num):
    listaa = []
    for i in range(num):
        num = int(input("Ingrese un número: "))
        listaa.append(num)
    return listaa

def par(listaa):
    par = 0
    for i in listaa:
        if i % 2 == 0:
            par = par + i
    return par

def impar(listaa):
    impar = 0
    for i in listaa:
        if i % 2 != 0:
            impar = impar + i
    return impar
  
        
num = cantidad()
listaa= pedir(num)


print ("El resultado de la suma par es:",par(listaa))
print ("El resultado de la suma impar es:",impar(listaa))
print ("El resultado de la suma total es:",sum(listaa))

