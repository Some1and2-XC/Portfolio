#!/usr/bin/env python

from os import path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

website_url = "localhost:80"

db = SQLAlchemy()
DBNAME = "database.dtb"

def create_app():
	app = Flask(__name__)

	app.config["SERVER_NAME"] = website_url
	app.config["SECRET_KEY"] = "tyfhcgceahovukb"
	app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DBNAME}"
	db.init_app(app)

	from .routes.views import views
	from .routes.auth import auth

	app.register_blueprint(views, subdomain = "portfolio") # Registers views with the app
	app.register_blueprint(auth, subdomain = "portfolio") # Registers auth with the app

	from .models.models import User, Note # runs to define parameters for database

	create_database(app = app)

	login_manager = LoginManager()
	login_manager.login_view = "auth.login"
	login_manager.init_app(app) # tells which app we are using

	@login_manager.user_loader
	def load_user(id): # Tells flask how to load a user
		return User.query.get(int(id)) # Looks for primary key by default so `.get` doesn't need to specify `id = int(id)`

	return app

def create_database(app): # Should probably add some check to see if the database actually works etc
	if not path.exists(f"website/{DBNAME}"):
		db.create_all(app = app)
		print("Created Database!")