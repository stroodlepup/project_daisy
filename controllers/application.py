from sqlalchemy.orm import backref

__author__ = 'stroodlepup'
from flask import Flask, request, session, redirect, url_for, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy


APP_NAME="DAISY"
DATABASE_USERNAME="stroodlepup"
DATABASE_PASSWORD="arcreactor"
DATABASE_HOST="localhost"
DATABASE_NAME="project_daisy"

app = Flask(__name__, static_folder='../assets', template_folder= '../views')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+ DATABASE_USERNAME +':'+DATABASE_PASSWORD+'@'+DATABASE_HOST+'/'+DATABASE_NAME
app.config['SQLALCHEMY_ECHO'] = True

db=SQLAlchemy(app)

# DB ORM CLASSES. EDIT AT OWN RISK

class communityprofile(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lastname = db.Column(db.String(30), nullable=False)
    firstname = db.Column(db.String(30), nullable=False)
    middlename = db.Column(db.String(30), nullable=False)
    nickname = db.Column(db.String(15), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    familycomposition = db.relationship("familycomposition", backref="familycomp", lazy="dynamic")

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
    communityprofile_id=db.Column(db.Integer,db.ForeignKey("communityprofile.id"),nullable=False)
    name = db.Column(db.String(45), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    relationship = db.Column(db.String(20), nullable=False)
    attainment = db.Column(db.String(45), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    occupation = db.Column(db.String(35), nullable=False)

    def __init__(self,source_id , name, age, relationship, attainment, status, occupation):
        self.name = name
        self.communityprofile_id=source_id
        self.age = age
        self.relationship = relationship
        self.attainment = attainment
        self.status = status
        self.occupation = occupation

    def __repr__(self):
        return '<Name %r>' % self.name

# DB SESSION

db.create_all()
db.session.commit()


# ROUTING 

@app.route('/')
def redirector():
	if not session.get('logged_in'):
		return redirect(url_for("login"))
	else:
		return redirect(url_for("home"))

@app.route('/home')
def home():
	error=None
	return render_template("home.html",error=error)

@app.route('/admin')
def admin():
	if not session.get('logged_in'):
		return redirect(url_for("login"))
	else:
		return "True"

@app.route('/login', methods=["GET", "POST"])
def login():
	error=None
	if request.method == "POST":
		if request.form["username"] != "LOL" and request.form["password"] != "pass":
			error="Login Error. Try Again"
			return render_template("login.html", error = error)
		else:
			return redirect(url_for("home"))
	return render_template("login.html", error = error)

@app.route('/communityprofile')
def communityProfile():
    error=None
    if session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template("communityprofile.html",error=error)

@app.route('/communityprofile/profile/add', methods=["POST"])
def addCommunityProfile():
    error=None
    if session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        entry=communityprofile(request.form['lastname'],request.form['firstname'],request.form['middlename'],request.form['nickname'],request.form['birthdate'])
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('communityProfile'), error=error)

@app.route('/communityprofile/profile/get', methods=['GET', 'POST'])
def getCommunityProfile():
    error=None
    if session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        if request.method == "POST":

            return jsonify()
        elif request.method == "GET":
            return jsonify()

@app.route('/communityprofile/familycomposition/add', methods=['POST'])
def addfamilycomposition():
    error=None
    if session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        entry=familycomposition
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('communityProfile'), error=error)

# ERROR ROUTES

if __name__ == '__main__':
    app.run(debug=True)
    print 'start'