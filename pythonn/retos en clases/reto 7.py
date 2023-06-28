print("##### RETO EN CLASES 7 #####")

#Escribir una funcion que reciba una frase por teclado y devuelva un diccionario con las palabras
#que contiene y su longitud.

def reto7():
   
   frase=((input("Ingrese alguna oración:\n")))
   palabras=frase.split()
   return {palabra: len(palabra) for palabra in palabras}

diccionario=reto7()
print(diccionario)


