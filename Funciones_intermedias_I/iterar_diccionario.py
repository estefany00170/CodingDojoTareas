"""Iterar a través de un diccionarios con valores de lista
Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, 
imprima el nombre de cada clave junto con el tamaño de su lista,
y luego imprima los valores asociados dentro de la lista de cada clave."""

dojo = {'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
        'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
        }

def printInfo(some_dict):
    for key, values in some_dict.items(): #el .items() devuelve una vista de los pares clave-valor del diccionario
            print(f"{len(values)} {key}")
            for i in values:
                print(i)
            print()
        





printInfo(dojo)

