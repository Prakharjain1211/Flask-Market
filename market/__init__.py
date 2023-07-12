from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '9c8d96d7f41b5327904f5bb8'
db = SQLAlchemy(app)
app.app_context().push()
from market import routes