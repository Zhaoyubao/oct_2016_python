from flask import Flask, request, render_template, redirect, session, flash
from connection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = '\x87\xa0\x99\x0c\xc3LX"\xd1\xb2\xaf\x16\x91L\xad\xfet\xb9\xdd\xb5@\x10\x11\xc3'
db = MySQLConnector(app, 'emaildb')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$')
queries = {
        "show_all" : "SELECT id, email, DATE_FORMAT(created_at,'%b %D, %Y, %l:%i %p') AS created_at FROM emails",
        "create" : "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())",
        "delete" : "DELETE FROM emails WHERE id = :id"
}

@app.route('/')
def index():
    try:
        session['email']
    except:
        session['email'] = ""
    return render_template('index.html')

@app.route('/emails/create', methods=['POST'])
def create():
    session['email'] = request.form['email']
    if not EMAIL_REGEX.match(session['email']):
        flash("Email is not valid!","error")
        return redirect('/')
    query = queries['create']
    data = {'email': session['email']}
    db.query_db(query, data)
    return redirect('/emails')

@app.route('/emails')
def show_all():
    query = queries['show_all']
    emails = db.query_db(query)
    msg = "The email address you entered: %s is a VALID email address! Thank you!"% session['email']
    flash(msg,"success")
    return render_template('success.html', emails=emails)

@app.route('/emails/<id>/delete')
def delete(id):
    query = queries['delete']
    data = {'id': id}
    db.query_db(query, data)
    return redirect('/emails')

if __name__ == '__main__':
    app.run(debug=True)
