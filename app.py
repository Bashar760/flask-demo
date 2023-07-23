# """Simple Flask Project"""

# source: https://www.youtube.com/watch?v=0Qxtt4veJIc&list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz&index=1

# import logging
from wsgiref.validate import validator
from flask import Flask, render_template, flash, request, redirect, url_for
from markupsafe import escape

# from flask_bootstrap import Bootstrap

# Load forms libraries
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
# Bootstrap(app)

# Create CSRF Token to be used by FORMS
app.secret_key = "please_use_a_COMPLEX_secret_key"
#  OR
# app.config['SECRET_KEY'] = "please_use_a_COMPLEX_secret_key"


# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What is you name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


# FIELDS TYPES
# BooleanField
# DateField
# DateTimeField
# DecimalField
# FileField
# HiddenField
# MultipleField
# FieldList
# FloatField
# FormField
# IntegerField
# PasswordField
# RadioField
# SelectField
# SelectMultipleFie1d
# SubmitField
# StringField
# TextAreaFie1d

# VALIDATORS
# DataRequired
# Email
# EqualTo
# InputRequired
# IPAddress
# Length
# MacAddress
# NumberRange
# Optional
# Regexp
# UUID
# AnyOf
# NoneOf


@app.route("/hello")
def hello():
    return "Hello, World"


@app.route("/")
def index():
    pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    context = {"name": "Bashar", "lname": "Horanieh", "pizza": pizza}
    return render_template("index.html", context=context)


@app.route("/user/<name>")
def user(name):
    # Always escape untrusted variables
    return f"Hello, {escape(name).capitalize()}!"

@app.route("/log")
def log():
    # app.logger.debug('A value for debugging')
    # app.logger.warning('A warning occurred (%d apples)', 42)
    # app.logger.error('An error occurred')
    return render_template("index.html")


@app.route("/name", methods=["GET", "POST"])
def name():
    name = None
    form = NamerForm()

    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        flash("You were successfully logged in", "success")

    return render_template("name.html", name=name, form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run()

# PS D:/flask> set FLASK_ENV=development
# PS D:/flask> set FLASK_App=app.py

# Following command will refresh the server automatically

# PS D:/flask> flask --app example_app.py --debug run

# Following two commands can be used to save Powershell history

# PS D:/flask> Get-History | Export-Csv history.csv
# PS D:/flask> Get-History | Out-File history.txt
