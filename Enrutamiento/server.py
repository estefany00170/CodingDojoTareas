from flask import Flask
app = Flask(__name__)

@app.route('/', methods = ['GET'] )
def mensaje_holaMundo():
    return "Hola Mundo!"

@app.route('/dojo', methods = ['GET'] )
def mensaje_dojo():
    return '¡Dojo!'

@app.route('/say/<name>', methods = ['GET'])
def mensaje_say(name):
    return "¡Hola, " + name

@app.route('/repeat/<int:num>/<string:name>', methods = ['GET'])
def mensaje_repeat(num, name):
    return f"{name * num}"

@app.errorhandler(404)
def page_not_found(e):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez.", 404

if __name__=="__main__":    
    app.run(debug=True) 
