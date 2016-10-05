from flask import Flask, render_template, redirect, request, session
from random import randint
import time

app = Flask(__name__)
app.secret_key = "\x9eh\xb7;)\x10\xf0{\xb7\xf1\x95\xbb?Y*\xd4\x83Q\xfa\xa8\x14\x99s\x96"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = []
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process():
    data = {"farm": randint(10,20), "cave":randint(5,10), "house":randint(2,5), "casino":randint(-50,50)}
    building = request.form['building']
    gold = data[building]
    now = time.strftime("%Y/%m/%d %I:%M:%S %p")
    act = {}
    if gold > 0:
        act = {"status":"earn", "log":"Earned {} golds from the {}! ({})".format(gold, building, now)}
    elif gold < 0:
        act = {"status":"lost", "log":"Entered a casino and lost {} golds... Ouch.. ({})".format(-gold, now)}
    else:
        act = {"status":"null", "log":"Entered a casino and got nothing... ({})".format(now)}
    session['gold'] += gold
    session['activity'].append(act)
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
