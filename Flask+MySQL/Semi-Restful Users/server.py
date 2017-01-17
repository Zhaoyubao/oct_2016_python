from flask import Flask, render_template, redirect, request, url_for, flash
from connection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = 'Its A Secret'
mysql = MySQLConnector(app, 'friendsdb')
queries = {
        'show_all_users': "SELECT id, CONCAT_WS(' ', first_name, last_name) AS full_name, email, DATE_FORMAT(created_at,'%b %D, %Y') AS created FROM friends",
        'show_user': "SELECT id, CONCAT_WS(' ', first_name, last_name) AS full_name, email, DATE_FORMAT(created_at,'%b %D, %Y') AS created FROM friends WHERE id=:id",
        'select_user': "SELECT * FROM friends WHERE id=:id",
        'add_new_user': "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first, :last, :email, NOW(), NOW())",
        'update_user': "UPDATE friends SET first_name=:first, last_name=:last, email=:email, created_at=NOW(), updated_at=NOW() WHERE id=:id",
        'delete_user': "DELETE FROM friends WHERE id=:id"
}
name_regex = re.compile('^[A-Za-z\s]*$')
email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$')

@app.route('/users')
def index():
    query = queries['show_all_users']
    users = mysql.query_db(query)
    return render_template('index.html', users=users)

@app.route('/users/new')
def new():
    return render_template('new.html')

@app.route('/users/create', methods=['POST'])
def create():
    user = request.form
    if validate_create(user)[0]:
        return redirect('/users/new')
    query = queries['add_new_user']
    data = validate_create(user)[1]
    id = mysql.query_db(query, data)
    url = '/users/' + str(id)
    return redirect(url)

@app.route('/users/<id>/edit')
def edit(id):
    return render_template('edit.html', id=id)

@app.route('/users/<id>')
def show(id):
    query = queries['show_user']
    data = {'id': id}
    user = mysql.query_db(query, data)
    return render_template('show.html', user=user)

@app.route('/users/<id>', methods=['POST'])
def update(id):
    new_user = request.form
    old_user = mysql.query_db(queries['select_user'], {'id': id})
    if validate_update(new_user, old_user)[0]:
        url = '/users/' + id + '/edit'
    else:
        query = queries['update_user']
        data = validate_update(new_user, old_user)[1]
        data['id'] = id
        mysql.query_db(query, data)
        url = '/users/' + id
    return redirect(url)

@app.route('/users/<id>/destroy')
def destroy(id):
    query = queries['delete_user']
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/users')

#Help Functions
def validate_create(user):
    invalid = False
    first = ''.join(user['first_name'].split(' ')).capitalize()
    last = ''.join(user['last_name'].split(' ')).capitalize()
    email = ''.join(user['email'].split(' '))
    data = {
    'first': first,
    'last': last,
    'email': email
    }
    if len(first) < 1:
        invalid = True
        flash("Please enter the first name!","first_error")
    elif not name_regex.match(first):
        invalid = True
        flash("First name is not valid!","first_error")

    if len(last) < 1:
        invalid = True
        flash("Please enter the last name!","last_error")
    elif not name_regex.match(last):
        invalid = True
        flash("Last name is not valid!","last_error")

    if len(user['email']) < 1:
        invalid = True
        flash("Please enter your email!","email_error")
    elif not email_regex.match(user['email']):
        invalid = True
        flash("Email is not valid!","email_error")
    return (invalid, data)

def validate_update(new_user, old_user):
    invalid = False
    first = ''.join(new_user['first_name'].split(' ')).capitalize()
    last = ''.join(new_user['last_name'].split(' ')).capitalize()
    email = ''.join(new_user['email'].split(' '))
    data = {
    'first': first,
    'last': last,
    'email': email
    }
    if len(first) < 1:
        data['first'] = old_user[0]['first_name']
    elif not name_regex.match(first):
        invalid = True
        flash("First name is not valid!","first_error")

    if len(last) < 1:
        data['last'] = old_user[0]['last_name']
    elif not name_regex.match(last):
        invalid = True
        flash("Last name is not valid!","last_error")

    if len(email) < 1:
        data['email'] = old_user[0]['email']
    elif not email_regex.match(new_user['email']):
        invalid = True
        flash("Email is not valid!","email_error")

    if len(first) < 1 and len(last) < 1 and len(email) < 1:
        invalid = True
    return (invalid, data)

if __name__ == '__main__':
    app.run(debug=True)
