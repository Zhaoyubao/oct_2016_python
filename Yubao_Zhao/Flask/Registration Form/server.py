from flask import Flask, render_template, redirect, request, session, flash
import re

app = Flask(__name__)
app.secret_key = "\xc2\xe6X]0gG\x96\x8d\xf0&\x8a\xb8\xb4\xf1 \xb5\xe7\xb5\n\xd9\xfb\xe9\x8b"

NAME_REGEX = re.compile('^[a-zA-Z\s]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile(r'.*?[A-Z]+.*?[0-9]+|.*?[0-9]+.*?[A-Z]')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    pw = request.form['pw']
    confirm_pw = request.form['confirm_pw']
    valid = True
    if not ''.join(fname.split(' ')):
        flash("Please enter your first name!","fname_error")
        valid = False
    elif not NAME_REGEX.match(fname):
        flash("First name is not valid!","fname_error")
        valid = False

    if not ''.join(lname.split(' ')):
        flash("Please enter your last name!","lname_error")
        valid = False
    elif not NAME_REGEX.match(lname):
        flash("Last name is not valid!","lname_error")
        valid = False

    if not ''.join(email.split(' ')):
        valid = False
        flash("Please enter your email!","email_error")
    elif not EMAIL_REGEX.match(email):
        valid = False
        flash("Email is not valid!","email_error")

    if not ''.join(pw.split(' ')):
        valid = False
        flash("Please create a new password.","pw_error")
    elif not PW_REGEX.match(pw) or len(pw) <= 8:
        valid = False
        flash("Password is not valid!","pw_error")

    if not confirm_pw == pw:
        valid = False
        flash("The passwords entered don't match.","confirm_error")

    if valid:
        msg = "Congratulations {}! You have registered successfully!".format(fname.capitalize())
        flash(msg, "success")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
