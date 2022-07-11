from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '793f0563db6e1716dc0dfb8f'
db = SQLAlchemy(app)

from market import routes