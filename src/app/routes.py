from flask import render_template,url_for
from app import app

@app.route("/")
def homepage():
    return render_template ("index.html")
   