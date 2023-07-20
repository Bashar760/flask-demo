# """Simple Flask Project"""

# source: https://www.youtube.com/watch?v=0Qxtt4veJIc&list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz&index=1

# import logging
from flask import Flask, render_template, flash, request, redirect, url_for
from markupsafe import escape
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "please_use_a_COMPLEX_secret_key"


@app.route("/")
def index():
    return "String"


@app.route("/hello")
def hello():
    return "Hello, World"


@app.route("/hello/<name>")
def hello_name(name):
    # Always escape untrusted vars to prevent any unwanted behaviour
    return f"Hello, {escape(name).capitalize()}!"


@app.route("/message")
def index_page():
    # flash("Good", "Success")
    # flash("Warning", "Warning")
    # flash("Error", "Error")
    # return redirect(url_for('index'))
    
    # app.logger.debug('A value for debugging')
    # app.logger.warning('A warning occurred (%d apples)', 42)
    # app.logger.error('An error occurred')
    
    return render_template("index.html")


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
