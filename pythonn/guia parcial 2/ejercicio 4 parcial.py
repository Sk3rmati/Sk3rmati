def product_mont():
    product_price = 0
    while True:
        try:
            product = int(input("Introduzca la cantidad de dinero que cuesta el producto: "))
            if product % 10 != 0:
                print('Ingrese un monto multiplo de 10.')
                continue
            if product < 0: 
               print("No puede ser un valor negativo") 
               continue
            elif product == 0:
                print("¿Cómo algo que se va a pagar puede valer $0 pesos?")
                continue
            else:
                product_price += product
                print ("El coste de su producto corresponde a: $", product_price ,)
                break
        except ValueError:
            print ("Ingrese un valor válido")
            continue
    return product_price

def change(product_price):
    while True:
        change = 0
        pay = (int(input("Ingrese el monto a pagar: ")))
        if pay % 10 != 0:
            print('Ingresa un monto multiplo de 10.')
            continue
        if pay < product_price:
            print ("No puedes pagar menos de lo que vale el producto")
        elif pay > product_price:
            change = pay - product_price
            break
        else:
            change = pay - product_price
            print("Al pagar el precio justo del producto no tienes vuelto")
            break
    return change

def change_dev(change):
    cash = [20000,10000,5000,2000,1000,500,100,50,10]
    cash_list = []
    aux = []
    for i in cash:
        if change // i > 0:
            aux.append(i)
            aux.append(change // i)
            cash_list.append(aux)
            change -= i * aux[1]
            aux = []
    return cash_list

def desglose(cash_list):
    for i in cash_list:
        print('>>',i[0], 'x', i[1])
            
    
product_price = product_mont()
vuelto = change(product_price)
cash_list = change_dev(vuelto)



print ("Su vuelto es de $",vuelto)
desglose(cash_list)
 
