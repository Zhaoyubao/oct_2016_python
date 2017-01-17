from flask import Flask, render_template, redirect
app = Flask(__name__)

turtles = {"blue":"leonardo.jpg", "orange":"michelangelo.jpg", "red":"raphael.jpg", "purple":"donatello.jpg"}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def show_all():
    ninjas = turtles
    return render_template("ninjas.html", ninjas=ninjas)

@app.route('/ninja/<color>')
def show_ninja(color):
    ninjas = {}
    if color in turtles:
        ninjas[color] = turtles[color]
    else:
        ninjas["megan"] = "notapril.jpg"
    return render_template("ninjas.html", ninjas=ninjas)

if __name__ == '__main__':
    app.run(debug=True)
