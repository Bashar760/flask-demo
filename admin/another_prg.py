# Blueprint Docs: https://exploreflask.com/en/latest/blueprints.html

from flask import Blueprint, render_template

admin = Blueprint("another_prg", __name__, static_folder="static", template_folder="templates")

@admin.route("/home")
@admin.route("/")
def home():
    return render_template("blank.html")


@admin.route("/test")
def test():
    return "<hl>admin test</hl>"
