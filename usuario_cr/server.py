from flask import render_template, redirect, request
from app_usuarios import app
from app_usuarios.modelos.modelo_usuarios import Usuarios




@app.route( "/usuarios", methods = ['GET'] )
def desplegar_usuarios():
    # llamar al método de clase obtener_todos para obtener todos los usuarios
    usuarios = Usuarios.obtener_todos()
    print(usuarios)
    return render_template("leer_todo.html", usuarios=usuarios)


@app.route('/formulario/usuario', methods = ['GET'])
def formulario_registro():
    return render_template("crear.html")


@app.route( '/nuevo/usuario', methods = ['POST'] )
def registrar_usuario():
    nuevo_usuario = {
        "nombre" : request.form['nombre'],
        "apellido" : request.form['apellido'],
        "email" : request.form['email']
        }
    Usuarios.registrar_uno( nuevo_usuario )
    return redirect( '/usuarios' )

            
if __name__ == "__main__":
    app.run(debug=True)