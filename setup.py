#!/usr/bin/env python3

from setuptools import find_packages, setup

from pathlib import Path

setup(
	name="Base Website",
	packages=find_packages(include=["website"]),
	version="0.0.0",
	description="A Website Setup for Understanding the Fundamentals of website development",
	author="@some1and2",
	author_email='04x0xx@gmail.com',
	license="GPL-3.0",
	install_requires=["flask", "flask-login", "flask-sqlalchemy"],
	setup_requires=[],
	long_description = ( Path(__file__).parent / "README.md" ).read_text(),
	long_description_content_type='text/markdown'
)