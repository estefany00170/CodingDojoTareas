from flask import Flask, render_template, session, request, url_for, redirect

app = Flask(__name__)
app.secret_key = '123'

@app.route('/', methods = ['GET', 'POST'])
def increase_counter():
    if 'counter' not in session:
        session['counter'] = 0
    if request.method == 'POST':
        session['counter'] += 1
    return render_template('index.html')

@app.route('/increase_2', methods = ['GET'])
def increase_counter_two():
    if 'counter' in session:
        session['counter'] += 2
    return render_template('index.html')

@app.route('/form', methods = ['POST'])
def increase_counter_form():
    increase = int(request.form['increase'])
    if 'counter' in session:
        session['counter'] += increase
    return redirect(url_for('increase_counter'))

@app.route('/destroy_session', methods = ['POST'])
def destroy_session():
    session.clear()		# borra todas las claves
    return render_template('index.html')



if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración
