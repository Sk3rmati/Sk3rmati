a = [10,80,15,30,20]
b = [20,45,80,20,10]
c = [20,35,60,90,20]

def valor_comun(a, b, c):
    valor = list(set(a) & set(b) & set(c))
    return valor


def sumaa(a, b, c):
    lista = a + b + c
    return lista


def no_repetir(lista):
    repeticion = list(set(lista))
    return repeticion


def orden_lista(noduplicar):
    orden_lista = sorted(noduplicar, reverse=True)
    return orden_lista


def reemplazoo(orden_lista):
    copia = orden_lista.copy()
    copia[6] = 100
    return copia

valor = valor_comun(a, b, c)
lista = sumaa(a, b, c)
noduplicar = no_repetir(lista)
orden_lista = orden_lista(noduplicar)
definitivo = reemplazoo(orden_lista)

print(f"Valor comun en las 3 listas: {valor}")
print(f"Concatenación (suma) de las 3 listas: {lista}")
print(f"Eliminar valores duplicados: {noduplicar}")
print(f"Ordenar la lista de forma descendente: {orden_lista}")
print(f"Reemplazar la posicion 7° por un 100: {definitivo}")