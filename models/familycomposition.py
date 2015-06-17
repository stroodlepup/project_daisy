__author__ = 'stroodlepup'
from config import db

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