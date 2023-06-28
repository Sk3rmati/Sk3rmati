print("##### EJERCICIO MATI #####")
#pedir lados de un cuadrado y en eso sacar el perimetro y el area, con 2 decimales en el resultado

lado1=(float(input("Ingrese el lado del cuadrado:\n")))

perimetrolado= (lado1 + lado1 + lado1 + lado1) 
perimetroladoo=round(perimetrolado,2)
areac= (lado1 * lado1)
areaac=round(areac,2)


print(f"El perimetro es: {perimetroladoo} y el area es: {areaac}")
