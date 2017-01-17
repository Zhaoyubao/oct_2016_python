from flask import Flask, render_template, redirect, request, flash
app = Flask(__name__)
app.secret_key = "thisisasecret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def show_user():
    name = request.form['username']
    comment = request.form['comment']
    valid = True
    if not ''.join(name.split(' ')):
        valid = False
        flash("Please enter your name!")
    if not ''.join(comment.split(' ')):
        valid = False
        flash("Please enter your comment!")
    elif len(comment) > 120:
        valid = False
        flash("Sorry,comment should no more than 120 characters!")
    if not valid:
        return redirect('/')
    return render_template("result.html", user=request.form)

if __name__ == '__main__':
    app.run(debug=True)
