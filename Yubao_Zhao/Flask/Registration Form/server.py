from flask import Flask, render_template, redirect, request, session, flash
import re

app = Flask(__name__)
app.secret_key = "\xc2\xe6X]0gG\x96\x8d\xf0&\x8a\xb8\xb4\xf1 \xb5\xe7\xb5\n\xd9\xfb\xe9\x8b"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
SPACE_REGEX = re.compile('.*\s.*')
PW_REGEX = re.compile(r'.*?[A-Z]+.*?[0-9]+|.*?[0-9]+.*?[A-Z]')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    errors = validate(request.form)
    if not errors:
        msg = "Congratulations {}! You have registered successfully!".format(request.form['fname'].capitalize())
        flash(msg, "success")
    else:
        generate_flashes(errors)
    return redirect('/')

# Helper functions
def validate(user):
    errors = []
    if not ''.join(user['fname'].split(' ')):
        errors.append(("Please enter your first name!","fname_error"))
    elif not user['fname'].isalpha():
        errors.append(("First name is not valid!","fname_error"))

    if not ''.join(user['lname'].split(' ')):
        errors.append(("Please enter your first name!","lname_error"))
    elif not user['lname'].isalpha():
        errors.append(("Last name is not valid!","lname_error"))

    if not ''.join(user['email'].split(' ')):
        errors.append(("Please enter your email!","email_error"))
    elif not EMAIL_REGEX.match(user['email']):
        errors.append(("Email is not valid!","email_error"))

    if not ''.join(user['pw'].split(' ')):
        errors.append(("Please create a new password.","pw_error"))
    elif not PW_REGEX.match(user['pw']) or len(user['pw']) <= 8 or SPACE_REGEX.match(user['pw']):
        errors.append(("Password is not valid!","pw_error"))

    if user['confirm_pw'] != user['pw']:
        errors.append(("The passwords do not match.","confirm_error"))
    return errors

def generate_flashes(error_list):
    for error in error_list:
        flash(error[0], error[1])

if __name__ == "__main__":
    app.run(debug=True)
