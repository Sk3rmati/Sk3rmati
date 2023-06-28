print("#### 01.- DECLARANDO UNA FUNCION SIMPLE #####")

def hola():
    print ("BUENAS CHAVALES, COMO ESTAN??")

hola()

print("##### 02.- DECLARANDO UNA FUNCION Y UTILIZANDO #####")

def concatenar(lista1,lista2):
    return lista1 + lista2

lista1= [1,2,3]
lista2= [4,5,6]

#concatenar()
print(concatenar(lista1,lista2));


print("##### 03.- DECLARANDO UNA FUNCION MULTIPLICACION #####")

def multiplicacion (num1, num2):
    return num1*num2

print(multiplicacion(50,50))

print("##### 04-FUNCIONES SUMA Y RESTA (POR TECLADO) #####")

def suma (num1, num2):
   return num1 + num2

print(suma(6,3))
print(suma(123,456))

def resta(num1, num2):
    return num1 - num2

print(resta(3,4))
print(resta(2313,21312))

#Ahora con imput

def multiply (a,b):
    return a * b

a = int(input("Digite su primer número:\n "))
b = int(input("Digite su segundo número:\n "))

print("El resultado de su multiplicación es:", multiply(a,b))






    
