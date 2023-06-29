from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET'] )
def obtener_tabla():
    usuarios_lista = [
    {'nombre' : 'Michael', 'apellido' : 'Choi'},
    {'nombre' : 'John', 'apellido' : 'Supsupin'},
    {'nombre' : 'Mark', 'apellido' : 'Guillen'},
    {'nombre' : 'KB', 'apellido' : 'Tonel'}
]


    return render_template("index.html", usuarios = usuarios_lista)

if __name__=="__main__":
    app.run(debug=True)