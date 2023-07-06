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
    nuevo_usuario_id = Usuarios.registrar_uno( nuevo_usuario )
    return redirect(f"/usuario/{nuevo_usuario_id}")

@app.route("/formulario/usuario/<int:id>" , methods = ['GET'])
def desplegar_formulario_editar_usuario( id ):
    data = {
        "id" : id
    }
    usuario_actual = Usuarios.selecciona_uno( data )

    return render_template("editar_usuario.html", usuario_actual = usuario_actual)

@app.route( "/actualizar/usuario/<int:id>", methods = ['POST'] )
def actualizar_usuario(id):
    data = {
        "id" : id,
        "nombre" : request.form["nombre"],
        "apellido" : request.form["apellido"],
        "email" : request.form["email"]
    }
    #Actualizar con sesion una vez que se hizo el login
    Usuarios.actualiza_uno(data)
    return redirect("/usuarios")

@app.route( "/eliminar//<int:id>")
def eliminar_usuario(id):
    data = {
        "id" : id
    }
    Usuarios.elimina_uno( data )
    return redirect( "/usuarios")

@app.route( "/usuario/<int:id>", methods = ['GET'])
def ver_usuario(id):
    data = {
        "id" : id
    }
    usuario_actual = Usuarios.selecciona_uno( data )

    return render_template("ficha_usuario.html", usuario_actual = usuario_actual)

            
if __name__ == "__main__":
    app.run(debug=True)
