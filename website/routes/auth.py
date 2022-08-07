#!/usr/bin/env python

from flask import Blueprint, render_template, request, flash, redirect, url_for
from ..models.models import User
from .. import db
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		email = request.form.get("email")
		password = request.form.get("Password")

		user = User.query.filter_by(email = email).first() # should only be one option but just in case
		if user:
			if check_password_hash(user.password, password):
				flash("Logged in successfully!", category = "success")
				login_user(user, remember = True)
				return redirect(url_for("views.home"))
			else:
				flash("Incorrect password, try again.", category = "error")
		else:
			flash("Email does not exist. ", category = "error")


	return render_template("login.html", user = current_user)

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
	if request.method == "POST":
		email = request.form.get("email")
		FirstName = request.form.get("FirstName")
		Password1 = request.form.get("Password1")
		Password2 = request.form.get("Password2")

		user = User.query.filter_by(email=email).first()
		if user:
			flash("Email already exists. ", category = "error")
		elif len(email) < 4:
			flash("Invalid Email", category = "error")
		elif len(FirstName) < 2:
			flash("Invalid Name: Name must be more than 1 character", category = "error")
		elif Password1 != Password2:
			flash("Passwords don't match", category = "error")
		elif len(Password1) < 7:
			flash("Password must be more than 6 characters", category = "error")
		else:
			New_User = User(email=email, FirstName = FirstName, password = generate_password_hash(Password1, method="sha256")) # sha hashes password before comiting to dtb
			db.session.add(New_User)
			db.session.commit()
			flash("Account Created!", category="success")
			login_user(New_User, remember = True)
			return redirect(url_for("views.home")) # Gets the url for "views.home" and redirects there

	if request.method == "GET":
		...

	return render_template("sign_up.html", user = current_user)

@auth.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(url_for("auth.login"))