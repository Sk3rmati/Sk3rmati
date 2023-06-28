print("##### EJERCICIO 3 #####")

hora_diu=12000
hora_noct=16000

dom_diu= 14000
dom_noct=19000

empleado1={
    "Lunes":hora_noct,
    "Martes":hora_noct,
    "Miercoles":hora_noct,
    "Jueves":hora_diu,
    "Viernes":hora_diu
}

empleado1["Semanal1"]=(hora_diu+hora_diu+hora_noct+hora_noct+hora_noct)*10


empleado2={
    "Martes":hora_noct,
    "Miercoles":hora_noct,
    "Jueves":hora_noct,
    "Domingo":dom_diu
}

empleado2["Semanal2"]=(hora_noct+hora_noct+hora_noct+dom_diu)*10


empleado3={
    "Miercoles":hora_diu,
    "Jueves":hora_diu,
    "Viernes":hora_diu,
    "Sabado":hora_noct,
    "Domingo":dom_noct
}
empleado3["Semanal3"]=(hora_diu+hora_diu+hora_diu+hora_noct+dom_noct)*10

print(empleado1)
print(empleado2)
print(empleado3)