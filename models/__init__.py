__author__ = 'stroodlepup'
from flask_sqlalchemy import SQLAlchemy
from controllers import application

db = SQLAlchemy(application.app)


class communityprofile(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lastname = db.Column(db.String(30), nullable=False)
    firstname = db.Column(db.String(30), nullable=False)
    middlename = db.Column(db.String(30), nullable=False)
    nickname = db.Column(db.String(15), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)

    def __init__(self, lastname, firstname, middlename, nickname, birthdate):
        self.lastname = lastname
        self.firstname = firstname
        self.middlename = middlename
        self.nickname = nickname
        self.birthdate = birthdate

    def __repr__(self):
        return '<Name %r>' % self.lastname + "," + self.firstname + " " + self.middlename


class familycomposition(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    relationship = db.Column(db.String(20), nullable=False)
    attainment = db.Column(db.String(45), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    occupation = db.Column(db.String(35), nullable=False)

    def __init__(self, name, age, relationship, attainment, status, occupation):
        self.name = name
        self.age = age
        self.relationship = relationship
        self.attainment = attainment
        self.status = status
        self.occupation = occupation

    def __repr__(self):
        return '<Name %r>' % self.name

db.create_all()
db.session.commit
