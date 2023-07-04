from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = '123secreto'

@app.route('/', methods = ['GET'])
def formulario_registro_ver():
    
    return render_template('formulario_registro.html')

@app.route('/process', methods = ['POST'])
def formulario_registro_rellenar():
        
    session['nombre'] = request.form['nombre']
    session['lenguaje'] = request.form['lenguaje']
    session['dojos'] = request.form['dojos']
    session['comentarios'] = request.form['comentarios']
    return redirect( "/resultado" )

@app.route('/resultado', methods = ['GET'])
def resultado_formulario():
    
    return render_template("resultado_registro.html")



if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración
