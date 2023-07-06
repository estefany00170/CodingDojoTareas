from flask import Flask

app = Flask(__name__)
app.secret_key = "concesionario"

BASE_DE_DATOS = "bd_usuarios"