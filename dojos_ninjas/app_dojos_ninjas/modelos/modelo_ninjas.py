from app_dojos_ninjas.config.mysqlconnection import connectToMySQL
from app_dojos_ninjas import BASE_DE_DATOS

class Ninjas: #Una clase para cada tabla
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.fecha_creacion = data['fecha_creacion']
        self.fecha_actualizacion = data['fecha_actualizacion']
        self.id_dojo = data['id_dojo']
        
    
    @classmethod
    def crear_uno(cls, data):
        query = """
                INSERT INTO ninjas(nombre, apellido, edad, id_dojo)
                VALUES (%(nombre)s, %(apellido)s,%(edad)s, %(id_dojo)s);
                """
        
        resultado = connectToMySQL( BASE_DE_DATOS ).query_db( query, data)

        return resultado
    
    @classmethod
    def elimina_uno( cls, data ):
        query = """
                DELETE FROM ninjas
                WHERE id = %(id)s;
                """
        return connectToMySQL( BASE_DE_DATOS ).query_db( query, data )

    @classmethod
    def selecciona_uno( cls, data):
        query = """
                SELECT * 
                FROM ninjas
                WHERE id = %(id)s;
                """
        resultado = connectToMySQL( BASE_DE_DATOS ).query_db( query, data )
        ninja_actual = Ninjas(resultado[0] )
        return ninja_actual
    
    @classmethod
    def actualiza_uno( cls, data ):
        query = """
                UPDATE ninjas
                SET nombre = %(nombre)s, apellido = %(apellido)s, edad = %(edad)s, id_dojo = %(id_dojo)s
                WHERE id = %(id)s; 
                """
        return connectToMySQL( BASE_DE_DATOS ).query_db(query, data)