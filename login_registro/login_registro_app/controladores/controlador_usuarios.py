from flask import render_template, session, request, redirect, flash
from flask_bcrypt import Bcrypt
from login_registro_app import app
from login_registro_app.modelos.modelo_usuario import Usuarios

bcrypt = Bcrypt( app )

@app.route("/", methods = ['GET'])
def desplegar_login_registro():

    return render_template("login_registro.html")

@app.route("/crear/usuario", methods = ['POST'])
def nuevo_usuario():
    data = {
        **request.form
    }

    if Usuarios.validar_registro( data ) == False:
        return redirect("/")
    else:
        password_encriptado = bcrypt.generate_password_hash( data['password'] ) #cifra la contraseña con hash y guarda al usuario en la base de datos
        data['password'] = password_encriptado
        id_usuario = Usuarios.crear_uno( data )
        session['nombre'] = data['nombre']
        session['apellido'] = data['apellido']
        session['id_usuario'] = id_usuario

        return redirect('/dashboard')
    
@app.route( "/dashboard", methods = ['GET'] )
def desplegar_dashboard():
    #asegurar que despues de hacer Logout no se pueda acceder al dashboard
    if 'nombre' not in session:
        return redirect("/")
    else:
        return render_template("dashboard.html")

@app.route("/login", methods = ['POST'] )
def procesa_login():
    data = {
        "email" : request.form['email_login']
    }
    usuario = Usuarios.obtener_uno_con_email( data )

    if usuario == None:
        flash("Email inválido", "error_email_login")
        return redirect("/")
    else:
        if not bcrypt.check_password_hash( usuario.password, request.form['password_login'] ):
            flash("Credenciales incorrectas", "error_password_login")
            return redirect('/')
        else:
            session['nombre'] = usuario.nombre
            session['apellido'] = usuario.apellido
            session['id_usuario'] = usuario.id
            return redirect('/dashboard')

@app.route( "/logout", methods = ['POST'])
def procesa_logout():
    session.clear()
    return redirect("/")

        