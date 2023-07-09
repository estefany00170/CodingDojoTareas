from login_registro_app.config.mysqlconnection import connectToMySQL
from login_registro_app import BASE_DE_DATOS, EMAIL_REGEX, NOMBRE_REGEX
from flask import flash


class Usuarios: #Una clase para cada tabla
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['email']
        self.password = data['password']
        self.tiempo_creacion = data['tiempo_creacion']
        self.tiempo_actualizacion = data['tiempo_actualizacion']
        
        
    
    @classmethod
    def crear_uno(cls, data):
        query = """
                INSERT INTO usuarios(nombre, apellido, email, password)
                VALUES (%(nombre)s, %(apellido)s,%(email)s, %(password)s);
                """
        
        resultado = connectToMySQL( BASE_DE_DATOS ).query_db( query, data)

        return resultado
    
    @classmethod
    def obtener_uno_con_email( cls, data):
        query = """
                SELECT * 
                FROM usuarios
                WHERE email = %(email)s;
                """
        resultado = connectToMySQL( BASE_DE_DATOS ).query_db( query, data )
        
        if len( resultado ) == 0:
            return None
        else:
            return Usuarios(resultado[0] )

    
    @staticmethod
    def validar_registro( data ):
        es_valido = True
        #1.Nombre: solo letras, al menos 2 caracteres y que se haya enviado
        if len( data['nombre'] ) < 2:
            es_valido = False
            flash( "Tu nombre debe de contener al menos dos caracteres.", "error_nombre" )
        
        if not NOMBRE_REGEX.match( data['nombre'] ):
            es_valido = False
            flash( "Por favor proporciona un nombre valido (solo letras).", "error_nombre" )
        
        #2.Apellido: solo letras, al menos 2 caracteres y que se haya enviado
        if len( data['apellido'] ) < 2:
            es_valido = False
            flash( "Tu apellido debe de contener al menos dos caracteres.", "error_apellido" )
        
        if not NOMBRE_REGEX.match( data['apellido'] ):
            es_valido = False
            flash( "Por favor proporciona un apellido valido (solo letras).", "error_apellido" )
        
        #3.Correo electrónico: formato de correo electrónico válido, aún no existe en la base de datos y que se haya enviado
        if not EMAIL_REGEX.match( data['email'] ):
            es_valido = False
            flash( "Por favor proporciona un email valido (solo letras).", "error_email" )

        #4.Contraseña: al menos 8 caracteres y que se haya enviado
        if len( data['password'] ) < 8:
            es_valido = False
            flash("Tu contraseña debe tener al menos 8 caracteres","error_password")
        
        #5.Confirmación de contraseña: que coincida con la contraseña   
        if data['password'] != data['confirmacion_password']:
            es_valido = False
            flash( "Tus contraseñas deben coincidir", "error_password")

        return es_valido
    
        