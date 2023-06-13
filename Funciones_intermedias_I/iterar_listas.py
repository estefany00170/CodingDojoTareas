estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]



def iterateDictionary(some_list):
    for i in some_list:
        for key, value in i.items():
            print(f"{key} - {value}" , end=" , ")
        print("")

iterateDictionary(estudiantes)