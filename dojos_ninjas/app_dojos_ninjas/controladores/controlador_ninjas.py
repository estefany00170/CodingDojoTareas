from flask import render_template, session, request, redirect
from app_dojos_ninjas import app
from app_dojos_ninjas.modelos.modelo_dojos import Dojos
from app_dojos_ninjas.modelos.modelo_ninjas import Ninjas

@app.route("/ninjas", methods = ['GET'])
def desplegar_formulario_ninja():
    lista_dojos = Dojos.seleccionar_todos()

    return render_template("formulario_ninjas.html", lista_dojos = lista_dojos)

@app.route("/nuevo/ninja", methods = ['POST'])
def agregar_ninja():

    Ninjas.crear_uno( request.form )
    return redirect("/dojos")  