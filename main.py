from flask import Flask, session, render_template, redirect, request, g, url_for
import os
import sys
import MySQLdb

from frontend import signup_sql

import db
conn = db.conn
db   = db.db


app = Flask(__name__)

name = "Mahesh"

#index page
@app.route('/')
def index():
    return render_template('index.html', name=name)

#404
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

#signin
@app.route('/signin')
def signin():
    return render_template('signin.html')

#signup
@app.route('/signup')
def signup():
    return render_template('signup.html', error="")

#dashboard
@app.route('/dashb', methods=['POST'])
def dashb():
    strEmail = request.form['strEmail']
    strFName = request.form['strFName']
    strLName = request.form['strLName']
    strPassw1= request.form['strPassw1']
    strPassw2= request.form['strPassw2']

    if strPassw1==strPassw2:
        #submit sql data
        signup_done = signup_sql(strEmail, strFName, strLName, strPassw1, strPassw2)

        if (signup_done == True):
            return render_template('signup.html', error="User Signup Successful, <a href='/signin.html'>Signin</a>",
                                strEmail=strEmail,
                                strFName=strFName,
                                strLName= strLName,
                                strPassw1=strPassw1,
                                strPassw2=strPassw2)
        else:
            return render_template('signup', error="Signup Error, Try Again")

    else:
        return render_template('signup.html',error="Password Not Matched, Try Again")


if __name__ == "__main__":
    app.run()
