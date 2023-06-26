from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play', methods = ['GET'])
def home():
    boxes = ''
    for i in range(3):
        boxes += '<div  style="background-color: aqua;"  class="box"></div>'
    return render_template("index.html", boxes=boxes)


@app.route('/play/<int:x>', methods = ['GET'])
def play(x):
    boxes = ''
    for i in range(x):
        boxes += '<div style="background-color: aqua;" class="box"></div>'
    return render_template("index.html", boxes=boxes)

@app.route('/play/<int:x>/<color>')
def play_color(x, color):
    boxes = ''
    for i in range(x):
        boxes += f'<div style="background-color: {color}!important;" class="box"></div>'
    return render_template("index.html", boxes=boxes)

if __name__=="__main__":
    app.run(debug=True)