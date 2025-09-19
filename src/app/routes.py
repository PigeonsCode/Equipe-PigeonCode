from flask import render_template,url_for
from app import app

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/login-adm")
def loginADM():
    return render_template("login-adm.html")