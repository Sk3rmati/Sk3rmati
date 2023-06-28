print("##### EJERCICIO OCHO #####")

mes=(str(input("Ingrese un mes del año para determinar su estación\n"))).lower()

if mes=="enero" or mes=="febrero" or mes=="marzo":
    print(f"{mes} pertenece a la estación de año verano.")

elif mes=="abril" or mes=="mayo" or mes=="junio":
    print(f"{mes} pertenece a la estación del año otoño.")

elif mes=="julio" or mes=="agosto" or mes=="septiembre":
    print(f"{mes} pertenece a la estación del año invierno.")

elif mes=="octubre" or mes=="noviembre" or mes=="diciembre":
    print(f"{mes} pertenece a la estación del año primavera.")

else:
    print("No es un mes")
