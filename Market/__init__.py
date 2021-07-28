from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy

application=Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketdata.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['SECRET_KEY'] = 'C\xa2\x16rP\x8b\xdd\xbd\x80K\xb7\xd4'
db = SQLAlchemy(application)

from Market import route