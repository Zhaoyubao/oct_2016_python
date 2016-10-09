from flask import Flask, render_template, redirect, request, session, flash
from connection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "\xec\x03H\x9fZ\\I^\x98\x9d1\x9d\xf8\xd0\xa9\xb8\xa8iC'K\xa32#"
db = MySQLConnector(app, "walldb")
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile('.*\s')
queries = {
    "user" : {
        "select" : "SELECT * FROM users WHERE email=:email",
        "create" : "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first, :last, :email, :pw, NOW(), NOW())"
    },
    "message" : {
        "select" : "SELECT users.id AS user_id, messages.id AS msg_id, first_name, last_name, message, TIMESTAMPDIFF(MINUTE, messages.created_at, NOW()) AS time_offset, TIMESTAMPDIFF(MINUTE, messages.created_at, NOW()) AS offset, DATE_FORMAT(messages.created_at, '%M %D %Y') AS msg_created FROM users JOIN messages ON messages.user_id = users.id ORDER BY messages.created_at DESC",
        "create" : "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())",
        "select_del" : "SELECT * FROM messages WHERE TIMESTAMPDIFF(MINUTE, messages.created_at, NOW()) <= 30 and id =:id",
        "delete" : "DELETE FROM messages WHERE id = :id"
    },
    "comment" : {
        "select" : "SELECT user_id, comments.id AS com_id, message_id AS msg_id, first_name, last_name, comment, TIMESTAMPDIFF(MINUTE, comments.created_at, NOW()) AS time_offset, TIMESTAMPDIFF(MINUTE, comments.created_at, NOW()) AS offset, DATE_FORMAT(comments.created_at, '%M %D %Y') AS comment_created FROM users JOIN comments ON users.id = comments.user_id ORDER BY comments.created_at",
        "create" : "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:id, :msg_id, :comment, NOW(), NOW())",
        "select_del" : "SELECT * FROM comments WHERE TIMESTAMPDIFF(MINUTE, comments.created_at, NOW()) <= 30 and id =:id",
        "delete" : "DELETE FROM comments WHERE id = :id"
    }
}

@app.route('/')
def index():
    if 'user' in session:
        return redirect('/wall')
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    user = request.form
    errors = validate("register", user)
    if not errors:
        pw_hash = bcrypt.generate_password_hash(user['pw'])
        query = queries['user']['create']
        data = {
            'first' : user['first_name'].capitalize(),
            'last' : user['last_name'].capitalize(),
            'email' : user['email'],
            'pw' : pw_hash
        }
        db.query_db(query, data)
        query = queries['user']['select']
        data = {'email' : user['email']}
        session['user'] = db.query_db(query, data)[0]
        return redirect('/wall')
    else:
        generate_flashes(errors)
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    user = request.form
    errors = validate("login", user)
    if not errors:
        query = queries['user']['select']
        data = {'email' : user['email']}
        session['user'] = db.query_db(query, data)[0]
        return redirect('/wall')
    else:
        generate_flashes(errors)
        return redirect('/')
# ================================================================================
@app.route('/wall')
def wall():
    query = queries['message']['select']
    messages = db.query_db(query)
    time_offset(messages)
    query = queries['comment']['select']
    comments = db.query_db(query)
    time_offset(comments)
    return render_template('wall.html', user=session['user'], messages=messages, comments=comments)

def time_offset(data_list):
    if data_list:
        for item in data_list:
            offset = item['offset']
            if offset >= 10080:       # 7 days
                item['offset'] = ""
            elif offset >= 1440:      # 24 hours
                item['offset'] = "a day ago" if offset/1440 == 1 else str(offset/1440)+" days ago"
            elif offset >= 60:        # 60 minutes
                item['offset'] = "an hour ago" if offset/60 == 1 else str(offset/60)+" hours ago"
            else:
                item['offset'] = "a minute ago" if offset <= 1 else str(offset)+" minutes ago"

@app.route('/message', methods=['POST'])
def create_msg():
    message = request.form['message']
    if not message or message.isspace():
        flash("Please enter your message!")
    else:
        query = queries['message']['create']
        data = {'user_id': session['user']['id'], 'message': message}
        db.query_db(query, data)
    return redirect('/wall')

@app.route('/message/<id>/delete')
def delete_msg(id):
    query = queries['message']['select_del']
    data = {'id': id}
    msg = db.query_db(query, data)
    if not msg:
        flash("You're not allowed to delete your message that was made more than 30 minutes!")
    else:
        flash("Message deleted!")
        query = queries['message']['delete']
        data = {'id': id}
        db.query_db(query, data)
    return redirect('/wall')

@app.route('/comment/<msg_id>', methods=['POST'])
def create_com(msg_id):
    comment = request.form['comment']
    if not comment or comment.isspace():
        flash("Please enter your comment!")
    else:
        query = queries['comment']['create']
        data = {
                'id': session['user']['id'],
                'msg_id': msg_id,
                'comment': comment
        }
        db.query_db(query, data)
    return redirect('/wall')

@app.route('/comment/<id>/delete')
def delete_com(id):
    query = queries['comment']['select_del']
    data = {'id': id}
    comment = db.query_db(query, data)
    if not comment:
        flash("You're not allowed to delete your comment that was made more than 30 minutes!")
    else:
        flash("Comment deleted!")
        query = queries['comment']['delete']
        data = {'id': id}
        db.query_db(query, data)
    return redirect('/wall')

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

        query = queries['user']['select']
        data = {'email' : email}
        user = db.query_db(query, data)
        if user:
            errors.append(("Email address already exists!","reg_error"))

    elif type == "login":
        user = db.query_db(queries['user']['select'], {'email' : input['email']})
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
