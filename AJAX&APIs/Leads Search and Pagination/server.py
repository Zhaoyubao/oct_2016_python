from flask import Flask, render_template, request
from connection import MySQLConnector
import math
app = Flask(__name__)
mysql = MySQLConnector(app, 'lead_gen_business')
queries = {
        'leads_count' : "SELECT count(*) AS count FROM leads WHERE CONCAT_WS(' ', first_name, last_name) LIKE :name AND registered_datetime BETWEEN :from_date AND :to_date",
        'show_leads_pagination' : "SELECT * FROM leads WHERE CONCAT_WS(' ', first_name, last_name) LIKE :name AND registered_datetime BETWEEN :from_date AND :to_date LIMIT :start_row, :rows"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show/<page>', methods=['post'])
def show(page):
    data = {
            'from_date': request.form['from_date'],
            'to_date': request.form['to_date']
    }
    name = ''.join(request.form['name'].split(' '))
    if name:
        data['name'] = '%'+name+'%'
    else:
        data['name'] = '%'
    query = queries['leads_count']
    count = mysql.query_db(query, data)[0]['count']

    rows = 10
    if count > rows:
        pages = int(math.ceil(count/float(rows)))
        start_row = (int(page)-1)*rows
        if page == pages:
            rows = -1
        data['start_row'] = start_row
        data['rows'] = rows
    else:
        pages = 0
        data['start_row'] = 0
        data['rows'] = count
    query = queries['show_leads_pagination']
    leads = mysql.query_db(query, data)
    return render_template('partials/leads.html', leads=leads, pages=pages, page=int(page))

if __name__ == '__main__':
    app.run(debug=True)
