from app_dojos_ninjas import app
from app_dojos_ninjas.controladores import controlador_dojos
from app_dojos_ninjas.controladores import controlador_ninjas


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

