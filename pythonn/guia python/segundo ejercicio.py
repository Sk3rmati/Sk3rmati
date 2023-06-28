print("##### EJERCICIO DOS #####")

nombre1=(str(input("Ingrese la primera palabra:\n")))
nombre2=(str(input("Ingrese la segunda palabra:\n")))

if len(nombre1)>len(nombre2):
    print(f"La palabra '{nombre1}' contiene más caracteres.")
    print(f"La palabra '{nombre2}' contiene menos caracteres.")

elif len(nombre2)>len(nombre1):
    print(f"La palabra '{nombre2}' contiene más caracteres.")
    print(f"La palabra '{nombre1}' contiene menos caracteres.")

else:
    print("Ambas palabras contienen los mismos caracteres")