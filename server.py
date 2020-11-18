from flask import Flask, redirect, request, url_for, render_template
from datetime import datetime
import sqlite3

app = Flask(__name__)

@app.route("/FlaskApp/login-success")
def loginSuccess():
	return render_template("login-success.html")

@app.route("/FlaskApp/register", methods=["GET", "POST"])
def register():

	if request.method == "POST":
		fname = request.form.get('firstname')
		mname = request.form.get('middlename')
		lname = request.form.get('lastname')
		email = request.form.get('email')
		password = request.form.get('password')
		datetoday = datetime.today().strftime('%Y-%m-%d')

		con = sqlite3.connect("tinderClone.db")
		cur = con.cursor();

		cur.execute("INSERT INTO users VALUES (40599,?,?,?,?)", (fname+mname+lname, email, password, datetoday))

		con.commit();
		con.close();

		return redirect(url_for("loginSuccess"))
	return render_template("register.html")

if __name__ == "__main__":
	app.run(debug = True)