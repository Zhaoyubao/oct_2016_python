from flask import Flask, render_template, redirect, request, session
from random import randint

app = Flask(__name__)
app.secret_key = "\x9eh\xb7;)\x10\xf0{\xb7\xf1\x95\xbb?Y*\xd4\x83Q\xfa\xa8\x14\x99s\x96"

@app.route('/')
def index():
    if 'random' not in session:
        session['random'] = randint(1,100)
    if 'guess' not in session:
        session['guess'] = 0
    if 'counter' not in session:
        session['counter'] = 0
    print "Random:", session['random']
    return render_template("index.html")

@app.route('/process', methods = ['POST'])
def process():
    if request.form['number']:
        session['guess'] = int(request.form['number'])
        session['counter'] += 1
    return redirect('/')

@app.route('/restart')
def restart():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
