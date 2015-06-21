__author__ = 'stroodlepup'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import APP_NAME, DATABASE_HOST, DATABASE_NAME, DATABASE_USERNAME, DATABASE_PASSWORD, MYSQL_STRING, POSTGRESQL_STRING, HEROKU_STRING
# INSTANCES
app = Flask(__name__)
app.template_folder='../views'
app.static_folder='../assets'
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL_STRING
app.config['SQLALCHEMY_ECHO'] = True
app.debug=True
db=SQLAlchemy(app)

# ADDING CONTROLLERS
from models import *
from controllers import *

db.create_all()
db.session.commit()