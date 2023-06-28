#### Hacer lista de nombre, edad, materias, juegos y mascotas ####
print("#### TEST 1 ####")

vida={"Matias":{"edad":18, "materias": ["Habilidades comunicativas", "Programacion","Matematicas"],
               "Juegos": ("Minecraft", "Roblox"), "Mascotas":["Hera", "Tobi","Punto"] }, 
               "Karla":{"edad":14, "materia": "lenguaje", "juego":"roblox" }}

##print(vida)
#Agregas datos colocando primero lista, clave de la lista + nueva palabra clave.
#colocas un =, para  colocar los datos que tendra dentro de la lista.
vida["Matias"]["Diferencia de edad con Karla"] = int((vida["Matias"]["edad"]) - int(vida["Karla"]["edad"]))
vida["Karla"]["Diferencia de edad con Matias"] = int((vida["Karla"]["edad"]- int(vida["Matias"]["edad"])))
print(vida) # en este print se dara a conocer las nuevas llaves del diccionario "Matias"
#Ya que hay una lista dentro de otra y asi.
#Se debe agregar el int si operaras numeros, sino saldra error, o float si sera con decimales, se puede colocar round
#ej: round((int("lista"["Llave"][valor])) / round((int("otralista"["otrallave"][otrovalor]1)))


