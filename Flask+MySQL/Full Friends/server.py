from flask import Flask, request, render_template, redirect, session, flash
from connection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = '\x87\xa0\x99\x0c\xc3LX"\xd1\xb2\xaf\x16\x91L\xad\xfet\xb9\xdd\xb5@\x10\x11\xc3'
db = MySQLConnector(app, 'friendsdb')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$')
queries = {
    "show_all" : "SELECT id, first_name, last_name, email, DATE_FORMAT(created_at, '%Y %b %d, %l:%i %p') AS updated FROM friends",
    "create" : "INSERT INTO friends (first_name, last_name, email, created_at) VALUES (:first, :last, :email, NOW())",
    "show_one" : "SELECT id, first_name, last_name, email FROM friends WHERE id =:id",
    "update" : "UPDATE friends SET first_name=:first_name, last_name=:last_name, email=:email, created_at=NOW() WHERE id=:id",
    "delete" : "DELETE FROM friends WHERE id=:id"
}

@app.route('/')
def index():
    friends = db.query_db(queries['show_all'])
    return render_template('index.html', friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    errors = validate("create", request.form)
    if not errors:
        query = queries['create']
        data = {
                'first': request.form['first_name'].capitalize(),
                'last': request.form['last_name'].capitalize(),
                'email': request.form['email']
        }
        db.query_db(query, data)
    else:
        generate_flashes(errors)
    return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
    query = queries['show_one']
    data = {'id': id}
    session['friend'] = db.query_db(query, data)[0]
    return render_template('edit.html', friend=session['friend'])

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    fname = ''.join(request.form['first_name'].split(' '))      #remove whitespace
    lname = ''.join(request.form['last_name'].split(' '))
    email = ''.join(request.form['email'].split(' '))
    errors = validate("update", request.form)
    if not errors and (fname or lname or email):
        data = session['friend']
        if fname:
            data['first_name'] = request.form['first_name'].capitalize()
        if lname:
            data['last_name'] = request.form['last_name'].capitalize()
        if email:
            data['email'] = request.form['email']
        db.query_db(queries['update'], data)
    else:
        generate_flashes(errors)
    url = "/friends/"+id+"/edit"
    return redirect(url)

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query = queries['delete']
    data = {'id': id}
    db.query_db(query, data)
    return redirect('/')

# Helper functions
def validate(type, input):
    errors = []
    first = ''.join(input['first_name'].split(' '))       # remove whitespace
    last = ''.join(input['last_name'].split(' '))
    email = ''.join(input['email'].split(' '))
    if type == "create":
        if not first:
            errors.append(("Please enter your first name!","fname_error"))
        elif not input['first_name'].isalpha():
            errors.append(("First name is not valid!","fname_error"))
        if not last:
            errors.append(("Please enter your last name!","lname_error"))
        elif not input['last_name'].isalpha():
            errors.append(("Last name is not valid!","lname_error"))
        if not email:
            errors.append(("Please enter your email!","email_error"))
        elif not EMAIL_REGEX.match(input['email']):
            errors.append(("Email is not valid!","email_error"))
    elif type == "update":
        if first and not input['first_name'].isalpha():
            errors.append(("First name is not valid!","fname_update_error"))
        if last and not input['last_name'].isalpha():
            errors.append(("Last name is not valid!","lname_update_error"))
        if email and not EMAIL_REGEX.match(input['email']):
            errors.append(("Email is not valid!","email_update_error"))
    return errors

def generate_flashes(error_list):
    for error in error_list:
        flash(error[0], error[1])

if __name__ == '__main__':
    app.run(debug=True)
