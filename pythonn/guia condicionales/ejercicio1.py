lista=("La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion democratica")

lista_sub1 = lista.split()

lista_sub2 = lista_sub1.count("Universidad") + lista_sub1.count("universidad")
lista_sub3= str(lista_sub2)

tupla=tuple(lista_sub3)
print(tupla)
print(type(tupla))


