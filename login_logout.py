#Api for Login and validation 
from email import header
from lib2to3.pgen2 import token
from itsdangerous import base64_decode
from pymysql import NULL
from connect2db import *
from flask import Flask, jsonify, request, session
from pyrsistent import s #pip install flask-mysqldb
from flask_cors import CORS #pip install -U flask-cors      
from datetime import timedelta
from flask import jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash

import requests
import base64

import base64
from itsdangerous import base64_decode
app = Flask(__name__)

app.config['SECRET_KEY'] = 'this is a secret key'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)
CORS(app)
base = connectDB()

cursor = base.cursor()
cur = base.cursor()

@app.route('/login', methods=['POST'])
def login():
        Email_Id = request.json.get('Email_Id')
        Password = request.json.get('Password')
        # id = request.json.get('User_Id')
        #print(id)
        newtoken = Password
        token = newtoken.encode('ascii')
        base64_bytes = base64.b64encode(token)
        base64_message = base64_bytes.decode('ascii')
        value = base64_decode(base64_message)
        UserPass = value.decode('ascii')
        
        if len(Email_Id)==0 or len(Password)==0:

            resp = jsonify({'Message': "Email/Password can't be empty",'Status':"400"})
            resp.status_code = 400
            return resp
        if len(Password)!=0:
           cur.execute('SELECT * FROM users where email_id=%s', [Email_Id])
           res = cur.fetchall()
           #print(res)
           l = []
           for i in res:
              for j in i:
                 l.append(j)
           #print(l[2])Z
           stored_password = l[2]
           result = check_password_hash(stored_password, Password)
           if result == True:
                return jsonify({'Message': 'Succesfully Logged In', 'Role': l[9], 'Username':l[3],'User_Id': l[0], 'Status': "200 OK",'Token': base64_message})
           else:
               resp = jsonify({'Message': 'Bad Request - invalid email id or password','Status':'404'})
               resp.status_code = 400
               return resp
        else:
            return jsonify({'Message': 'Password must be not null'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

