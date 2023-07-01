from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "Secret"

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    session['checkout'] = {
        "raspberry":request.form["raspberry"],
        "blackberry":request.form["blackberry"],
        "apple":request.form["apple"],
        "strawberry":request.form["strawberry"],
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "student_id":request.form["student_id"],
    }
    return redirect("/checkout")

@app.route('/checkout', methods=['GET'])
def show_checkout():

    if "checkout" not in session:
        return redirect("/")
    
    totalFrutas = int(session["checkout"]["apple"])+int(session["checkout"]["blackberry"])+int(session["checkout"]["raspberry"])+int(session["checkout"]["strawberry"])
    print("Cobrando a"+ session["checkout"]["first_name"]+ "por "+ str(totalFrutas)+ " frutas")
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():

    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    