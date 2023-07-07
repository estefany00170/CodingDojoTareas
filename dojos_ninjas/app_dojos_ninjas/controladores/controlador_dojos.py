from flask import render_template, session, request, redirect
from app_dojos_ninjas import app
from app_dojos_ninjas.modelos.modelo_dojos import Dojos

@app.route("/dojos", methods = ['GET'])
def todos_dojos():
    lista_dojos = Dojos.seleccionar_todos()

    return render_template("dojos.html", lista_dojos = lista_dojos)

@app.route("/dojo/nuevo", methods = ['POST'])
def agregar_dojo():
    nuevo_dojo = {
        "nombre" : request.form['nombre']
    }
    Dojos.crear_uno( nuevo_dojo )
    return redirect("/dojos")  

@app.route("/dojo/<int:id>", methods = ['GET'])
def obtener_dojo(id):
    data = {
        "id" : id
    }
    informacion_dojo = Dojos.obtener_uno_con_ninjas( data )
    return render_template("dojo.html", informacion_dojo = informacion_dojo)
