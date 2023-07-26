# """Simple Flask Project"""

# source: https://www.youtube.com/watch?v=0Qxtt4veJIc&list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz&index=1
# source: https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX


# import logging
from enum import unique
from wsgiref.validate import validator
from flask import Flask, render_template, flash, request, redirect, url_for, session
from markupsafe import escape

# Load forms libraries
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from admin.another_prg import admin

app = Flask(__name__)
app.register_blueprint(admin, url_prefix="/admin")

# Refer to Flask CONFIG Documentation: https://flask.palletsprojects.com/en/2.3.x/config/
# Create CSRF Token to be used by FORMS, Sessions and Cookies
app.secret_key = "please_use_a_COMPLEX_secret_key"
#  OR
# app.config['SECRET_KEY'] = "please_use_a_COMPLEX_secret_key"

# Optionally define session lifetime otherwise
# session will be terminated when browser is closed
app.permanent_session_lifetime = timedelta(minutes=5)

# Point database url to local directory
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

# Initialize database
db = SQLAlchemy(app)

# Create model
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<Name: {self.name!r}>"

"""
Create model using shell
(venv) PS D:\flask> flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
"""

# Create a Form Class
class UserForm(FlaskForm):
    name = StringField("Name?", validators=[DataRequired()])
    email = StringField("Email?", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/user/add", methods=["GET", "POST"])
def add_user():
    name = None
    form = UserForm()

    # Validate Form
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()

        form.name.data = ""
        form.email.data = ""

        flash("User added successfully", "success")

    return render_template("add_user.html", form=form, name=name)


# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What is you name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

"""
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
"""

@app.route("/hello")
def hello():
    return "Hello, World"


@app.route("/")
def home():
    pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    context = {"name": "Bashar", "lname": "Horanieh", "pizza": pizza}
    return render_template("index.html", context=context)


@app.route("/players/<name>")
def players(name):
    # Always escape untrusted variables
    return f"Hello, {escape(name).capitalize()}!"


# @app.route("/admin")
# def admin():
#     # Enter the name of the FUNCTION to redirect to
#     return redirect(url_for("home"))


@app.route("/log")
def log():
    # app.logger.debug('A value for debugging')
    # app.logger.warning('A warning occurred (%d apples)', 42)
    # app.logger.error('An error occurred')
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        # session.permanent = True
        # user = request.form.get("name")
        user = request.form["name"]
        session["user"] = user
        # flash("Successfully logged in", "success")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        
        return render_template("login.html")


@app.route("/logout")
def logout():
    flash("Successfully logged out", "success")
    session.pop("user", None)
    session.pop("email", None)
    return render_template("login.html")


@app.route("/user", methods=["GET", "POST"])
def user():
    email = None
    
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
        else:
            if "email" in session:
                email = session["email"]
                
            
        return render_template("user.html", name=user, email=email)
    else:
        flash("You are not logged in!")
        # return render_template("login.html")
        return redirect(url_for("login"))


@app.route("/name", methods=["GET", "POST"])
def name():
    name = None
    form = NamerForm()

    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        flash("You request was completed..")

    return render_template("name.html", name=name, form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    db.create_all()
    app.run()


"""
# app.run(debug=True)
# PS D:/flask> set FLASK_ENV=development
# PS D:/flask> set FLASK_App=app.py
# PS D:/flask> flask --debug run
# db.create_all()
# Following two commands can be used to save Powershell history

# PS D:/flask> Get-History | Export-Csv history.csv
# PS D:/flask> Get-History | Out-File history.txt
"""
