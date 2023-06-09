"""Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)"""

suma = 0
def primero_mas_longitud(lista):
    suma =  lista[0] + len(lista)
    return suma
x = [1, 2, 3, 4, 5]
y = [10,9,8,7]
print(primero_mas_longitud(x))
print(primero_mas_longitud(y))