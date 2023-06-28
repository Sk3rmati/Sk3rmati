print("##### EJERCICIO TRES #####")

a=(float(input("Ingrese el primer lado del triangulo:\n")))
b=(float(input("Ingrese el segundo lado del triangulo:\n")))
c=(float(input("Ingrese el tercer lado del triangulo:\n")))

p= (a+b+c) / 2
area= p * (p-a) * (p-b) * (p-c)


if a>b and a>c:
    print("Es un triangulo Escaleno")
    print(f"El area es: {area}")

elif b>a and b>c:
     print("Es un triangulo Escaleno")
     print(f"El area es: {area}")

elif c>a and c>b:
     print("Es un triangulo Escaleno")
     print(f"El area es: {area}")
     
elif a==b and a!=c or a!=b and a==c:
    print("Es un triangulo Isosceles")
    print(f"El area es: {area}")

elif b==a and b!=c or b!=a and b==c:
    print("Es un triangulo Isosceles")
    print(f"El area es: {area}")

elif c==a and c!=b or c!=a and c==b:
    print("Es un triangulo Isosceles")
    print(f"El area es: {area}")

else:
    print("Es un triangulo Equilatero")
    print(f"El area es: {area}")