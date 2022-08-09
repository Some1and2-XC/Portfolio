#!/usr/bin/env python3

from flask import Blueprint # Blueprints lets you split up views into multiple files cleanly
from flask import render_template
from flask import request
from flask import flash

from .. import db

views = Blueprint("views", __name__)

@views.route("/", methods = ["GET"])
def home():
	return "<h1>Page not found</h1><a href=\"http://portfolio.localhost\">Go to `portfolio.localhost`</a>"