#!/usr/bin/env python

# File for database information

from .. import db # imports db variable from __init__.py
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin): # User Model
	__tablename__ = "user"
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(150), unique = True)
	password = db.Column(db.String(150))
	FirstName = db.Column(db.String(150))
	# Stores a list of notes that belong to a user
	# Caps for referencing other data is inconsistent, suck it up
	auth_lvl = 0
	Kyros_Settings = db.relationship("Kyros")

	def UpdateKyrosSettings(self, data):
		if len(self.Kyros_Settings) != 0:
			toremove = Kyros.query.filter_by(id = self.Kyros_Settings[0].id).first()
			db.session.delete(toremove)
		settings = Kyros(user = self.id, settings = str(data))
		db.session.add(settings)
		db.session.commit()


class Kyros(db.Model): # Model For Fractals
	__tablename__ = "kryos"
	id = db.Column(db.Integer, primary_key = True)
	user = db.Column(db.Integer, db.ForeignKey("user.id"))
	settings = db.Column(db.String(400), default="{}")