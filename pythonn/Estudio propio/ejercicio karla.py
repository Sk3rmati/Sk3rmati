print("##### EJERCICIO KARLA #####")

#Karla jefa de empresa
#Ver sueldos de trabajadores, hay 4
#1-2 horas = 30.000
#3horas+ = 45.000
#1 hora equivale 10mil adicional al de las 3 horas
#1.- trabajó 1 hora dia.- lune martes miercoles
#2.- 3 horas.- toda la semana
#3.- 2 horas.- lunes
#4.- 7 horas.- 5 dias
#agregar semanal

hora=30000
hora3=45000
horad=10000

empleado1={"lunes":hora,
           "martes":hora,
           "miercoles":hora
           
}


empleado1["semanal1"]= hora * 3


empleado2={"lunes":hora3,
           "martes":hora3,
           "miercoles":hora3,
           "jueves":hora3,
           "viernes":hora3,
           "sabado":hora3,
           "domingo":hora3}

empleado2["semanal2"]=hora3*7

empleado3={"lunes":hora}

empleado3["semanal3"]=hora

empleado4={"lunes":hora3,
           "martes":hora3,
           "miercoles":hora3,
           "jueves":hora3,
           "viernes":hora3}

empleado4["semanal4"]=(hora3 * 5) + horad * 5

print(empleado1)
print(empleado2)
print(empleado3)
print(empleado4)


