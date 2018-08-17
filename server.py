from flask import Flask, request, render_template, redirect
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'friendsdb')


@app.route('/')
def index():
    
    # an example of running a query
    friends = mysql.query_db("SELECT * FROM friends")
    return render_template('index.html', friends=friends)


@app.route('/process', methods=['POST'])
def process():
    query = 'INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) Values ( :first, :last, :occupation, now(), now())'
    data = {
        'first': request.form['first_name'],
        'last': request.form['last_name'],
        'occupation': request.form['occupation']
    }
    mysql.query_db(query,data)

    return redirect('/')

app.run(debug=True)
