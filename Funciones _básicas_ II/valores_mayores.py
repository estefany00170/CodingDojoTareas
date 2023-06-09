"""Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva que contenga solo los valores
de la lista original que sean mayores que su segundo valor. Imprime cuántos valores son y luego devuelve la lista nueva. 
Si la lista tiene menos de 2 elementos, has que la función devuelva False
Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False """

def valores_mayores_segundo(lista):
    nueva_lista = []

    if len( lista ) >= 2:
        for i in lista:
            if i > lista[1]:
                nueva_lista.append(i)
        print( len(nueva_lista) )
        if len(nueva_lista) < 2:
            return False
        else:
            return nueva_lista

lista1= valores_mayores_segundo([5, 2, 3, 2, 1, 4])
lista2= valores_mayores_segundo([3,2,1])
lista3= valores_mayores_segundo([10,4,5,3,10])

print(lista1)
print(lista2)
print(lista3)