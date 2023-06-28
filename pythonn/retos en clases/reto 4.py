nombre1= input ("¿Cual es el nombre del primer paciente?\n")
edad1= input(int("¿Cual es la edad del primer paciente?\n"))
peso1= input (float("¿Cual es el peso del primer paciente?\n"))
estatura1= input (float("¿Cual es la estatura del primer paciente?\n"))

tupla1=tuple(nombre1+edad1+peso1+estatura1)


nombre2= input ("¿Cual es el nombre del segundo paciente?\n")
edad2= input (int("¿Cual es la edad del segundo paciente?\n"))
peso2= input (float("¿Cual es el peso del segundo paciente?\n"))
estatura2= input (float("¿Cual es la estatura del segundo paciente?\n"))

tupla2=tuple(nombre2+edad2+peso2+estatura2)


nombre3= input ("¿Cual es el nombre del tercer paciente?\n")
edad3= input (int("¿Cual es la edad del tercer paciente?\n"))
peso3= input (float("¿Cual es el peso del tercer paciente?\n"))
estatura3= input (float("¿Cual es la estatura del tercer paciente?\n"))

tupla3=tuple(nombre3+edad3+peso3+estatura3)

tupla4=(tupla1+tupla2+tupla3)

print(tupla4)


