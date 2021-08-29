from flask import Flask, render_template, request
from pymysql import mysql.connections
import os
import boto3
from config import *

app = Flask(__name__)

region = customregion

db_conn = mysql.connections.Connection(
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
    full_name = request.form['full_name']
    mail = request.form['mail']
    cont_no = request.form['cont_no']
    Details = request.form['Details']
    
mycursor = db_conn.cursor()
  sql = "INSERT INTO enquiry (full_name, mail , cont_no ,Details ) VALUES (%s, %s ,%s , %s) "
    val = (full_name, mail , cont_no ,Details )
mycursor.execute(sql, val)
db_conn.commit()

   return render_template('EnquiryOutput.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
