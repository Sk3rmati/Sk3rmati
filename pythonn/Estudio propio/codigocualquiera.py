print("##### EJERCICIO TRATANDO DE SEGUIR EL RETO EN CLASES #####")

##Pedir al usuario que digite una frase y en eso contado las palabras separadas dentro de una lista
#usando definiciones

def reto7():
   
   frase=((input("Ingrese alguna palabra u oración:\n")))
   palabras=frase.split()
   frase2={palabra: len(palabra) for palabra in palabras}
   return frase2

diccionario=reto7()
print(diccionario)

   








    