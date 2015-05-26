__author__ = 'stroodlepup'
from flask_sqlalchemy import SQLAlchemy
#from __init__ import db
db=None

class loginhistory(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    login=db.Column(db.DateTime,nullable=False)
    logout=db.Column(db.DateTime,nullable=False)

    def __init__(self,):
        self.id
        self.login
        self.logout

    def __repr__(self):
        return '<Timestamp %r>' % self.login +"-"+ self.logout