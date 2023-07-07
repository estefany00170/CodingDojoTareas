from app_dojos_ninjas.config.mysqlconnection import connectToMySQL
from app_dojos_ninjas import BASE_DE_DATOS
from app_dojos_ninjas.modelos.modelo_ninjas import Ninjas

class Dojos: #Una clase para cada tabla
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.fecha_creacion = data['fecha_creacion']
        self.fecha_actualizacion = data['fecha_actualizacion']
        self.ninjas = []
        
    @classmethod #Para cada query se necesita un metodo de clase
    def seleccionar_todos( cls ):
        query = """
                SELECT *
                FROM dojos;
                """ 
        resultado = connectToMySQL( BASE_DE_DATOS ).query_db( query )


        lista_dojos = []
        for renglon in resultado:
            lista_dojos.append( Dojos( renglon ) )
        return lista_dojos
    
    @classmethod
    def crear_uno(cls, data):
        query = """
                INSERT INTO dojos(nombre)
                VALUES (%(nombre)s);
                """
        
        resultado = connectToMySQL( BASE_DE_DATOS ).query_db( query, data)

        return resultado
    
    @classmethod
    def elimina_uno( cls, data ):
        query = """
                DELETE FROM dojos
                WHERE id = %(id)s;
                """
        return connectToMySQL( BASE_DE_DATOS ).query_db( query, data )

    @classmethod
    def selecciona_uno( cls, data):
        query = """
                SELECT * 
                FROM dojos
                WHERE id = %(id)s;
                """
        resultado = connectToMySQL( BASE_DE_DATOS ).query_db( query, data )
        dojo_actual = Dojos(resultado[0] )
        return dojo_actual
    
    @classmethod
    def actualiza_uno( cls, data ):
        query = """
                UPDATE dojos
                SET nombre = %(nombre)s
                WHERE id = %(id)s; 
                """
        return connectToMySQL( BASE_DE_DATOS ).query_db(query, data)
    
    @classmethod
    def obtener_uno_con_ninjas(cls, data):
        query = """
                SELECT *
                FROM dojos d LEFT JOIN ninjas n
                ON d.id = n.id_dojo
                WHERE d.id = %(id)s;
                """
        resultado = connectToMySQL(BASE_DE_DATOS).query_db(query, data)
        informacion_dojo = Dojos(resultado[0])

        for renglon in resultado:
            if renglon['n.nombre'] != None:
                datos_ninja = {
                    "nombre" : renglon['n.nombre'],
                    "apellido": renglon['apellido'],
                    "edad" : renglon['edad'],
                    "id" : renglon['n.id'],
                    "id_dojo":renglon['id_dojo'],
                    "fecha_creacion":renglon['n.fecha_creacion'],
                    "fecha_actualizacion":renglon['n.fecha_actualizacion']
                }
                ninja_actual = Ninjas( datos_ninja )
                informacion_dojo.ninjas.append(ninja_actual)
            return informacion_dojo

        