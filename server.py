from flask import Flask, request, render_template, redirect
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'friendsdb')
# an example of running a query
print mysql.query_db("SELECT * FROM friends")
@app.route('/')
def index():
    return render_template('index.html')
app.run(debug=True)
