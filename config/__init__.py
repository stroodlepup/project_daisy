__author__ = 'stroodlepup'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# DEFAULT APPLICATION PROPERTIES
APP_NAME="DAISY"
DATABASE_USERNAME="stroodlepup"
DATABASE_PASSWORD="arcreactor"
DATABASE_HOST="localhost"
DATABASE_NAME="project_daisy"


# DATABASE STRINGS
MYSQL_STRING= 'mysql://'+ DATABASE_USERNAME +':'+DATABASE_PASSWORD+'@'+DATABASE_HOST+'/'+DATABASE_NAME
POSTGRESQL_STRING= 'postgresql://'+DATABASE_USERNAME+':'+DATABASE_PASSWORD+'@'+DATABASE_HOST+'/'+DATABASE_NAME

# DATABASE ACCESS FOR HEROKU
HEROKU_STRING= 'postgresql://xyfmhyseuygdge:koKeu9q-v8x3O0W9GQHNxDsX5l@ec2-107-21-114-132.compute-1.amazonaws.com/d7fkne5j602151'

# INSTANCES
app = Flask(__name__)
app.template_folder='../views'
app.static_folder='../assets'
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL_STRING
app.config['SQLALCHEMY_ECHO'] = True
app.debug=True
db=SQLAlchemy(app)

# ADDING CONTROLLERS
from controllers import *
from models import *

db.create_all()
db.session.commit()