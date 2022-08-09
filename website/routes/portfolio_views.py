#!/usr/bin/env python

# File for roots of the website

import json

from flask_login import login_required, current_user

from flask import Blueprint, render_template, request, flash, url_for

from .. import db
from ..models.models import User, Kyros
from ..services import RunKyros


portfolio_views = Blueprint("portfolio_views", __name__)

@portfolio_views.route("/", methods = ["GET", "POST"])
def home():
	if request.method == "POST":
		if current_user.is_authenticated:
			note = request.form.get("note")
			if len(note) < 1:
				flash("Note is too short!", category = "error")
			else:
				NewNote = Note(data = note, user_id = current_user.id)
				db.session.add(NewNote)
				db.session.commit()
				flash("Note added", category = "success")
		else:
			flash("Sign-in to Add Notes")

	return render_template("portfolio-base-1-home.html", user = current_user) # passes current_user to home.html

@portfolio_views.route("/kyros", methods = ["GET", "POST"])
def kyros_demo():
	# Endpoint for the kyros demo

	img = None

	if request.method == "POST":
		# For Form Submissions

		# Changes the Values Such that they Match with the displayed Values
		formdata = dict(request.form)
		if "vert" in formdata:
			if current_user.is_authenticated:
				formdata = json.loads(current_user.Kyros_Settings[0].settings)
				BonusSettings = {
					"turtle": True,
					"x": float(request.form["hori"]),
					"y": float(request.form["vert"]),
					"first": False
				}

				img, BoxRange = RunKyros(args = formdata, BonusSet = BonusSettings)

				formdata["BoxRange"] = BoxRange

				current_user.UpdateKyrosSettings(json.dumps(formdata))
				
			else:
				flash("Not Signed IN!")
		else:
			# Cleans up the values a bit to match the displayed values from html
			for key, power in [("MaxI", 2), ("SizeX", 2), ("RateOfColorChange", 3)]:
				formdata[key] = power ** float(formdata[key])
			for key, divisor in [("ci", 100), ("cj", 100)]:
				formdata[key] = float(formdata[key]) / divisor
			if current_user.is_authenticated:
				current_user.UpdateKyrosSettings(json.dumps(formdata))
			img, _ = RunKyros(dict(formdata))

	return render_template("portfolio-program-001-kyros.html", user = current_user, image=img)

@portfolio_views.route("/mnist", methods = ["GET"])
def mnist_demo():
	# Function for mnist classification endpoint
	return render_template("portfolio-program-002-mnist.html", user = current_user)