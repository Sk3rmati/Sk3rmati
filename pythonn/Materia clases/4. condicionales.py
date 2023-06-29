licencia = True
edad = 20
automovil = False


if licencia==True:
    print("Puedo conducir porque tengo licencia\n")
else:
    print("No tengo licencia para conducir\n")



    

if edad >= 18:
    print("Puedo conducir porque soy mayor de edad\n")
else:
    print("No puedo conducir soy menor de edad\n")


if licencia and edad >= 18:
    print("Puedo conducir porque soy mayor de edad y tengo licencia")
elif automovil:
    print("Tengo automovil, pero no tengo licencia ni la edad necesaria")
else:
    print("No puedo conducir no tengo ni la edad, ni licencia ni automovil")