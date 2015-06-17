from config import app
from flask import request, session, redirect, url_for, render_template, jsonify
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
