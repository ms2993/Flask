from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy

application=Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketdb.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    application.run(port=5000,debug=True)