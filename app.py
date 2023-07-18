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

# Following two commands will refresh the server automatically
# PS D:/flask/> set FLASK_ENV=development
# PS D:/flask/> set FLASK_App=app.py

"""

Source: https://www.youtube.com/watch?v=3O4ZmH5aolg&list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz&index=3

(venv) PS D:\flask> deactivate

PS D:/flask/> cd ~
PS C:/Users/BASHAR> 
PS C:/Users/BASHAR> md .ssh
PS C:/Users/BASHAR/.ssh> ssh-keygen.exe
Generating public/private rsa key pair.
Enter file in which to save the key (C:/Users/BASHAR/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in C:/Users/BASHAR/.ssh/id_rsa.
Your public key has been saved in C:/Users/BASHAR/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:r2QQvWthzQwIsWBSamO7RtB5EI5WaMzAsx/TLk4XHcQ bashar@Bashar-PC
The key's randomart image is:
+---[RSA 3072]----+
|B.Boo.o.         |
| #.+ o E         |
|==* + + +        |
|=.o+ o o *       |
| o. + o S +      |
|. .+ o o +       |
| oo o   = .      |
|.  .   + .       |
|        .        |
+----[SHA256]-----+

PS C:/Users/BASHAR/.ssh> dir

    Directory: C:/Users/BASHAR/.ssh

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---          17/07/2023  7:29 PM           2602 id_rsa
-a---          17/07/2023  7:29 PM            571 id_rsa.pub

PS C:/Users/BASHAR/.ssh> cat id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCikGtAXeSZnoH1UD3Yd
LdRJtnZRV9RDjWOneuR8Csl2UiOnNT6NmeOA0cqFFFwNmtYVxSEjXsUBO
naTV9O1PkDv3aZuBrplXNc7MkrhEJA9qdXstCUgmvjv1XSWYs1in0zsvs
BR6AwYQhjZcyP7Us870PF38KYsdKr+x3nUotHx3SoowijQMv/qL1ljLL6
Nakv4opqzSqFxKtJavpaBbhDC7E6IcsKYt9Ks6XgTefFs8/dktX08fKaY
E4RrXIxZysR3+ZgtlKY3PepfzbkKEjvmrAuRImJZP4TKqmr6xcSpDoRDZ
QeW824IVt9ta5L91Op0Uw6N5n1hSAlVUuygYI0+wiZbUiNx97X554HbXt
IWN4nAej9/Z9Os6NcA6Ujkw1PnQUcFkIHhDuyxggkhIlDHVUoz5u1pRTp
GmwgvzsQWOwe593K2vVLl0fvTuT9C6bdgu9thnZv48bCgO/B7MIw8FBhU
outxmjGaHM0fQhvYaXeUDwh7gXJN++2Q+tv4fE= bashar@Bashar-PC


Create an .gitignore file as per the following example:
    .gitignore

    venv/
    .vscode/
    __pycache__
    presentation1.pptx

Setup Git for Version Control
Activate environment again then run the following commands:

(venv) PS D:\flask> git config --global user.name "Bashar"
(venv) PS D:\flask> git config --global user.email "bashar750@gmail.com"
(venv) PS D:\flask> git config --global push.default matching
(venv) PS D:\flask> git config --global alias.co checkout
(venv) PS D:\flask> git init

Turn on Version Control

(venv) PS D:\flask> git add .
(venv) PS D:\flask> git commit -am "Initial commit"

You can push an existing repository from the command line

(Note: run the following command if you received the following error message error: remote origin already exists.)
(venv) PS D:\flask> git remote remove origin


(venv) PS D:\flask> git remote add origin https://github.com/Bashar760/flask-demo.git
(venv) PS D:\flask> git branch -M main
(venv) PS D:\flask> git push -u origin main

"""
