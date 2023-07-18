# """Simple Flask Project"""

# source: https://www.youtube.com/watch?v=0Qxtt4veJIc&list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz&index=1

from flask import Flask, render_template, flash, request, redirect, url_for
from markupsafe import escape
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "please_use_a_COMPLEX_secret_key"


@app.route("/")
def index():
    return "Index Page STR"


@app.route("/hello")
def hello():
    return "Hello, World"


@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello, {escape(name)}!"


@app.route("/message")
def index_page():
    flash("Good", "Success")
    flash("Warning", "Warning")
    flash("Error", "Error")
    # return redirect(url_for('index'))
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)

