diccionario={
    'ID':14,
    'Nombre': 'Los Rios',
    'Superficie':18.429,
    'Habitantes':404.432,


    '#ID':12,
    '#Nombre': "Magallanes",
    '#Superficie':1382.291,
    '#Habitantes':166.533
     }
             
print(diccionario)

densidad1= (404432/18429)
diccionario.setdefault("Densidad", densidad1)
densidad2= (166533/1382291)
diccionario.setdefault("#Densidad", densidad2)

diccionario.setdefault("Capital", "Valdivia" )
diccionario.setdefault("#Capital", "Punta Arenas")

comuna=["Río Bueno", "La Unión", "Paillaco"]
diccionario.setdefault("Comunas", comuna)

comuna2= ["Cabo de Hornos ", " Puerto Williams ", " Porvenir"]
diccionario.setdefault("#Comunas", comuna2)

tupla1=("Ranco", "Valdivia")
diccionario.setdefault("Provincia",  tupla1)
tupla2=("Antártica Chilena","Magallanes", "Tierra del Fuego", "Última Esperanza")
diccionario.setdefault("#Provincia", tupla2)


print(diccionario)

