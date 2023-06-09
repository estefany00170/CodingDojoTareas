"""Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor.
La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]"""

def longitud_valor(tamaño, valor):
    lista= []
    i = 1
    while i <= tamaño:
        lista.append( valor )
        i += 1
    return lista

resultado1= longitud_valor(4, 7)
resultado2= longitud_valor(6, 2)
print(resultado1)
print(resultado2)

    