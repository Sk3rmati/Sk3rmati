print("##### EJERCICIO UNO #####")

num1=(int(input("Digite el primer numero: \n")))
num2=(int(input("Digite el segundo numero: \n")))
num3=(int(input("Digite el tercero numero: \n")))

if num1>=num2 and num1>=num3:
    print(f"El numero mayor es: {num1}")

elif num2>=num1 and num2>=num3:
    print(f"El numero mayor es: {num2}")

elif num3>=num1 and num3>=num2:
    print(f"El numero mayor es: {num3} ")

