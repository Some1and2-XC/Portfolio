#!/usr/bin/env python

# File for roots of the website

import json

from flask_login import login_required, current_user

from flask import Blueprint # Blueprints lets you split up views into multiple files cleanly
from flask import render_template
from flask import request
from flask import flash

from .. import db


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

@portfolio_views.route("/kyros", methods = ["GET"])
def kyros_demo():
	return render_template("portfolio-program-001-kyros.html", user = current_user)
