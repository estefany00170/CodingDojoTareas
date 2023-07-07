from flask import Flask

app = Flask( __name__)    # Crea una nueva instancia de la clase Flask llamada "app"
app.secret_key = "esto es secreto"

BASE_DE_DATOS = "esquemas_dojos_y_ninjas"