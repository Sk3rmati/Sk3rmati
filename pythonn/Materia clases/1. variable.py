##Introduccion a python
##principales variables
nombre = "matias"
edad = "18"
nombre1 = "javier"
print("hola soy" ,nombre)
print("hola soy" ,nombre ,"y tengo" ,edad)
print("hola soy" ,nombre ,nombre1 ,"y tengo" ,edad)

#más variables
import math
altura = 165
peso = 56
complejo = 1+ 4j

#lista con elemento especifico
##Los numeros negativos hacen que la lista sea del final hacia el inicio, pero solo en python.
##data_asig = 
##TUPLAS
grupo1= "daniel", "cristian", "felipe" ,200,100, "daniel"
print ("######## 05-TUPLAS ########")
print (type(grupo1))

##accediendo al primer elemento de la tupla
print(grupo1[0])

#consultando el elemento "daniel" cuantas veces se encuentra en la tupla
print("el elemento se repite" ,grupo1.count("daniel"))

#muestra el indice del primer elemento buscado
print("indice del elemento:" ,grupo1.index ("daniel"))

#index muestra la posicion de tal elemento

##reasignando el primer elemento de la tupla
#grupo1[0] = Constanza
#print(grupo1)
#la tupla no se puede modificar

#obteniendo poco de la tupla
grupo2 = ("pedro",100 ,"felipe", "diego",2020, "alejandro")
print("trozo de la tupla",grupo2[0:3])

#Entonces como no puedo modificar una tupla, ¿Que puedo hacer?
grupo1 = list(grupo1)
print("la tupla ahora es de tipo",type(grupo1),"\n")
print("\n")

#forma de inicializar un set
conjunto_vacio=set()
conjunto_vacio1={}
print(type(conjunto_vacio1))
conjunto_colores= set({"azul", "rojo", "verde"}) #utilizando funcion set
conjunto_animales= {"gato", "perro", "conejo"} #utilizando corchetes
print("###### 06-SETS #######")
print(type(conjunto_colores))
print(type(conjunto_animales))
print("El primer set contiene los siguientes colores", conjunto_colores)
print("El segundo set contiene los siguientes animales", conjunto_animales)

#print(conjunto_animales[2])
conjunto_colores.add("Celeste")
print("El set de colores lo conforman", conjunto_colores)
conjunto_animales.add("gato")
print("El set de animales lo conforman" ,conjunto_animales, "\n")


##dato numerico tip###
##print (f"ejemploo"(altura) "ya mi peso es de"(peso))##
##La f reemplaza las comas##

##len dice cantidad de elementos de una lista##
##Float imprime numeros enteros##
##bool evalua si es falso o verdadero##
### False = 0 "" None ###
### True = "False" y 1 ###
## para hacer una lista se ocupa (list) []  y se ocupa corchete para hacer una lista ##

##data_asig = asignar valor o en si datos ##
## con range sueles elegir desde donde comienza ##
## para colocar set se debe de ocupar llaves ##
##diccionario (clave/valor)##

##para colocar datos personales hay que empezar con un corchete "{} y finalizar con este mismo para que asi llegue a funcionar bien este mismo ##

