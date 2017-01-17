from flask import Flask, render_template, redirect, request
from connection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'notesdb')
queries = {
        "show_all_notes" : "SELECT * FROM notes ORDER BY created_at DESC",
        "insert_note" : "INSERT INTO notes (title, description, created_at, updated_at) VALUES (:title, '', NOW(), NOW())",
        "update_note" : "UPDATE notes SET title=:title, description=:description, created_at=NOW(), updated_at=NOW() WHERE id=:id",
        "delete_note" : "DELETE FROM notes WHERE id = :id"
}

@app.route('/')
def index():
    query = queries['show_all_notes']
    notes = mysql.query_db(query)
    return render_template('index.html', notes=notes)

@app.route('/notes/show')
def show():
    query = queries['show_all_notes']
    notes = mysql.query_db(query)
    return render_template('partials/notes.html', notes=notes)

@app.route('/notes/create', methods=['POST'])
def create():
    print "Title:",request.form['title']
    query = queries['insert_note']
    data = {'title' : request.form['title']}
    mysql.query_db(query, data)
    return redirect('/notes/show')

@app.route('/notes/<id>/update', methods=['POST'])
def update(id):
    print "Update:Request.form",request.form
    query = queries['update_note']
    data = {
            'id' : id,
            'title': request.form['title'],
            'description': request.form['description']
    }
    mysql.query_db(query, data)
    return redirect('/notes/show')

@app.route('/notes/<id>/delete', methods=['GET'])
def delete(id):
    print "Delete ID:", id
    query = queries['delete_note']
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/notes/show')

if __name__ == '__main__':
    app.run(debug=True)
