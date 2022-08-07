#!/usr/bin/env python

# File for database information

from .. import db # imports db variable from __init__.py
from flask_login import UserMixin
from datetime import datetime

class Note(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	data = db.Column(db.String(10000))
	date = db.Column(db.DateTime(timezone = True), default = datetime.now)
	# To use the Foreign key, you must pass a valid Userid to allow the note object to be created
	# It is referencing the class through a lowercase `user` because of sql
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class User(db.Model, UserMixin): # User Model
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(150), unique = True)
	password = db.Column(db.String(150))
	FirstName = db.Column(db.String(150))
	# Stores a list of notes that belong to a user
	# Caps for referencing other data is inconsistent, suck it up
	notes = db.relationship("Note")
