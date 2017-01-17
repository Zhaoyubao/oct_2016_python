from flask import Flask, render_template, redirect, request
from connection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'postsdb')
queries = {
        "show_all_posts" : "SELECT * FROM posts ORDER BY created_at DESC",
        "insert_post" : "INSERT INTO posts (description, created_at, updated_at) VALUES (:description, NOW(), NOW())"
}

@app.route('/')
def index():
    query = queries['show_all_posts']
    posts = mysql.query_db(query)
    return render_template('index.html', posts=posts)

@app.route('/posts/create', methods=['POST'])
def create():
    print request.form['post']
    query = queries['insert_post']
    data = {'description' : request.form['post']}
    mysql.query_db(query, data)
    query = queries['show_all_posts']
    posts = mysql.query_db(query)
    return render_template('partials/posts.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
