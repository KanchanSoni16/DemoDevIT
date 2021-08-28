from flask import Flask, render_template, request
from pymysql import connections
import os
import boto3
from config import *

app = Flask(__name__)

region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}
table = 'enquiry'


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('AddEnquiry.html')


@app.route("/addenquiry", methods=['POST'])
def AddEnquiry():
    name = request.form['name']
    email = request.form['email']
    cont_no = request.form['cont_no']
    Details = request.form['Details']
    

    insert_sql = "INSERT INTO enquiry VALUES (%s, %s, %s, %s)"
    
    print("Data inserted in MySQL RDS... ")
        return render_template('EnquiryOutput.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
