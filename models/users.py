__author__ = 'stroodlepup'
from flask_sqlalchemy import SQLAlchemy
#from __init__ import db
db=None

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username=db.Column(db.String(15),nullable=False)
    password = db.Column(db.String(30),nullable=False)
    accesslevel = db.Column(db.Integer,nullable=False)
    lastname = db.Column(db.String(30),nullable=True)
    firstname = db.Column(db.String(30),nullable=True)
    middlename = db.Column(db.String(30),nullable=True)
    nickname = db.Column(db.String(15),nullable=True)
    birthdate = db.Column(db.Date,nullable=True)
    email = db.Column(db.String(30),nullable=True)

    def __init__(self,username,password,accesslevel,lastname,firstname,middlename,nickname,birthdate,email):
        self.username=username
        self.password=password
        self.lastname=lastname
        self.firstname=firstname
        self.middlename=middlename
        self.nickname=nickname
        self.birthdate=birthdate
        self.email=email

    def __repr__(self):
        return '<User %r>' % self.username