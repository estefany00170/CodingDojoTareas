"""Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2"""

def imprimir_devolver(lista):
    print(lista[0])
    return lista[1]
print(imprimir_devolver([1, 2]))
print(imprimir_devolver([4, 5]))