def saludar():
    nombre = input("Escribe tu nombre:\n")
    saludo = f"¡Hola, {nombre}!"
    return saludo

print(saludar())

def sumatoria(resultado):
    a=int(input("Digita el primer numero:\n"))
    b=(int(input("Digita el segundo numero:\n")))
    c=int(input("Digita el tercer numero:\n"))
    resultado= (a*b)/c
    return resultado



digito=int(input("Digite un numero cualquiera entero:\n"))

print(( digito + sumatoria(resultado=True)))