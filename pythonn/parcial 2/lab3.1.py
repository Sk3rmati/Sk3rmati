print("##### PRIMER EJERCICIO PARCIAL DOS #####")

#Determinar si una palabra ingresada por teclado es una palíndromo.

pal=(input("Introduzca una palabra siendo esta palíndromo\n")) 

pal.lower() 

pal2=pal[-1] 

pal2.lower()


if pal2 != pal[0]:
    print(f"La palabra {pal} no es un palíndromo")
    
else:
    print(f"La palabra {pal} es un palíndromo")






