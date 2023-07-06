# importar la función que devolverá una instancia de una conexión
from app_usuarios.config.mysqlconnection import connectToMySQL
from app_usuarios import BASE_DE_DATOS
# modelar la clase después de la tabla friend de nuestra base de datos
class Usuarios:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.tiempo_creacion = data['tiempo_creacion']
        self.tiempo_actualizacion = data['tiempo_actualizacion']
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def obtener_todos(cls):
        query = "SELECT * FROM usuarios;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        resultado = connectToMySQL('bd_usuarios').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de usuarios
        usuarios = []
        
        for usuario in resultado:
            usuarios.append( cls(usuario) )
        return usuarios
    
    @classmethod
    def registrar_uno( cls, data ):
        query = """
                INSERT INTO usuarios ( nombre, apellido, email )
                VALUES ( %(nombre)s, %(apellido)s, %(email)s );
                """
        resultado = connectToMySQL( BASE_DE_DATOS ).query_db( query, data )
        return resultado
    
    @classmethod
    def elimina_uno( cls, data ):
        query = """
                DELETE FROM usuarios
                WHERE id = %(id)s;
                """
        return connectToMySQL( BASE_DE_DATOS ).query_db(query, data)
    
    @classmethod
    def selecciona_uno(cls,data):
        query = """
                SELECT * FROM usuarios
                WHERE id = %(id)s;
                """
        resultado = connectToMySQL( BASE_DE_DATOS ).query_db(query,data )
        usuario_actual = Usuarios( resultado[0] ) #tener presente para la ruta
        return usuario_actual

    @classmethod
    def actualiza_uno( cls, data ):
        query = """
                UPDATE usuarios
                SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s
                WHERE id = %(id)s; 
                """
        return connectToMySQL( BASE_DE_DATOS ).query_db(query, data)