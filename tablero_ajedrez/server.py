from flask import Flask, render_template
app = Flask(__name__)

color_1 = "red"
color_2 = "black"

@app.route('/', methods = ['GET'])
def tablero_ocho_ocho():
    num_rows = 8
    num_columnas = 8
    return render_template("index.html", columnas= num_columnas, row=num_rows, color1= color_1, color2= color_2)

@app.route('/<int:x>', methods = ['GET'])
def tablero_ocho_x(x):
    num_rows = 8
    return render_template("index.html", columnas=x, row= num_rows, color1 = color_1, color2= color_2)

@app.route('/<int:x>/<int:y>', methods= ['GET'] )
def tablero_x_y(x,y):
    return render_template("index.html", columnas=x, row= y,color1= color_1, color2= color_2)

@app.route('/<int:x>/<int:y>/<color1>', methods= ['GET'] )
def tablero_x_y_color1(x, y, color1):
    return render_template("index.html", columnas=x, row= y, color1=color1,color2= color_2 )

@app.route('/<int:x>/<int:y>/<color1>/<color2>', methods= ['GET'] )
def tablero_x_y_color1_color2(x, y , color1, color2):
    return render_template("index.html", columnas=x, row= y, color1=color1, color2=color2 )
    
# colors = [[color1 if (row+columnas) %2 == 0 else color2 for columnas in range(num_columnas)] for row in range(num_rows)]

if __name__=="__main__":
    app.run(debug=True)