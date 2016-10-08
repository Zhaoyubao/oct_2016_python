from flask import Flask, render_template, redirect, request, session, flash
from connection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "\xec\x03H\x9fZ\\I^\x98\x9d1\x9d\xf8\xd0\xa9\xb8\xa8iC'K\xa32#"
db = MySQLConnector(app, "usersdb")
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile('.*\s')
queries = {
    "select_user" : "SELECT * FROM users WHERE email=:email",
    "add_user" : "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first, :last, :email, :pw, NOW(), NOW())"
}

@app.route('/')
def index():
    if 'user' in session:
        return redirect('/success')
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    user = request.form
    errors = validate("register", user)
    if not errors:
        pw_hash = bcrypt.generate_password_hash(user['pw'])
        query = queries['add_user']
        data = {
            'first' : user['first_name'],
            'last' : user['last_name'],
            'email' : user['email'],
            'pw' : pw_hash
        }
        db.query_db(query, data)
        query = queries['select_user']
        data = {'email' : user['email']}
        session['user'] = db.query_db(query, data)[0]
        return redirect('/success')
    else:
        generate_flashes(errors)
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    user = request.form
    errors = validate("login", user)
    if not errors:
        query = queries['select_user']
        data = {'email' : user['email']}
        session['user'] = db.query_db(query, data)[0]
        return redirect('/success')
    else:
        generate_flashes(errors)
        return redirect('/')

@app.route('/success')
def success():
    return render_template('success.html', user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

# helper functions
def validate(type, input):
    errors = []
    if type == "register":
        fname = input['first_name']
        lname = input['last_name']
        email = input['email']
        pw = input['pw']
        if not fname:
            errors.append(("Please enter your first name!","fname_error"))
        elif len(fname) < 2 or not fname.isalpha():
            errors.append(("First name is invalid!","fname_error"))
        if not lname:
            errors.append(("Please enter your last name!","lname_error"))
        elif len(lname) < 2 or not lname.isalpha():
            errors.append(("Last name is invalid!","lname_error"))
        if not email:
            errors.append(("Please enter your email!","email_error"))
        elif not EMAIL_REGEX.match(email):
            errors.append(("Email is invalid!","email_error"))
        if not pw:
            errors.append(("Please create a new password.","pw_error"))
        elif PW_REGEX.match(pw) or len(pw) < 8:
            errors.append(("Please create a new password as per the criteria.","pw_error"))
        if not pw == input['confirm_pw']:
            errors.append(("The passwords entered don't match.","confirm_error"))

        query = queries['select_user']
        data = {'email' : email}
        user = db.query_db(query, data)
        if user:
            errors.append(("Email address already exists!","reg_error"))

    elif type == "login":
        user = db.query_db(queries['select_user'], {'email' : input['email']})
        if user:
            if not bcrypt.check_password_hash(user[0]['pw_hash'], input['pw']):
                errors.append(("Incorrect password!","login_pw_error"))
        else:
            errors.append(("Email address doesn't exist!","login_user_error"))
    return errors

def generate_flashes(error_list):
    for error in error_list:
        flash(error[0], error[1])

if __name__ == '__main__':
    app.run(debug=True)
