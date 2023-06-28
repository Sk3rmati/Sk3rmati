print("##### EJERCICIO CINCO #####")

nota1=(float(input("Ingrese la primera nota:\n")))
nota2=(float(input("Ingrese la segunda nota:\n")))
nota3=(float(input("Ingrese la tercera nota:\n")))

promedio= (nota1 * 0.3) + (nota2 * 0.4) + (nota3 * 0.3)
promedior= round(promedio,1)

if promedior>=6.0:
    print (f"Tu promedio es: {promedior}, aprobaste con distinción, felicidades.")

elif promedior>=4.0 and promedior<=5.9:
    print(f"Tú promedio es: {promedior}, aprobaste, felicidades.")

elif promedior>1.0 and promedior<=3.9:
    print(f"Tu promedio es: {promedior} , reprobaste la asignatura")

else:
    print(f"Tu promedio es:{promedior}, a lo cual no es un promedio correcto.")
