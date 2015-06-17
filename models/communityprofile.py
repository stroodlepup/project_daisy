__author__ = 'stroodlepup'
from config import db

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