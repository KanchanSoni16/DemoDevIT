from flask import Flask, render_template, request
import pymysql
from config import *

app = Flask(__name__)

region = customregion

db_conn = pymysql.connect(
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
    details = request.form['details']
    sql = "INSERT INTO enquiry (name, email, cont_no, Details) VALUES (%s, %s, %s, %s)"
    print(db_conn)
    mycursor = db_conn.cursor()
    print(mycursor)
    try: 
        mycursor.execute(sql, (full_name,mail,cont_no,details))
        db_conn.commit()
    except Exception as e:
        print("Rolling back the commit.".format(e))
        print(e)
        db_conn.rollback()
    finally:
        db_conn.close()
    return render_template('EnquiryOutput.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
