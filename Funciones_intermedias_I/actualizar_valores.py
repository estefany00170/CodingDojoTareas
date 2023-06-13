# 1.Actualizar valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15 #Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
print(x)

estudiantes[0]['last_name'] = 'Bryant' #Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
print(estudiantes)

directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes)

z[0]['y'] = 30   #Cambia el valor 20 en z a 30.
print(z)

        