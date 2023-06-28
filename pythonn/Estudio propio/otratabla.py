print("##### EJERCICIO 2 TABLA DE MULTIPLICAR #####")

numero=(int(input("Digite un numero para hacer su tabla de multiplicar:\n")))
multiplicacion=1

while multiplicacion <= 9:
    multiplicacion += 1
    resultado= numero * multiplicacion
    print(f"{numero} x {multiplicacion} = {resultado}")
