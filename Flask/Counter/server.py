from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "\x9eh\xb7;)\x10\xf0{\xb7\xf1\x95\xbb?Y*\xd4\x83Q\xfa\xa8\x14\x99s\x96"

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/add')
def add():
    session['count'] += 1
    return redirect("/")

@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
