from flask import render_template,url_for
from app.navigation import navigation_items
from app import app

@app.route("/")
def homepage():
    return render_template("index.html", navigation=navigation_items, page_url="homepage")

@app.route("/login-adm")
def loginADM():
    return render_template("login-adm.html")

# Páginas de conteúdo

@app.route("/sprints")
def sprints():
    return render_template("placeholder.html", page_url="sprints")

@app.route("/product-owner")
def productOwner():
    return render_template("placeholder.html", page_url="productOwner")

@app.route("/scrum-master")
def scrumMaster():
    return render_template("placeholder.html", page_url="scrumMaster")

@app.route("/dev-team")
def devTeam():
    return render_template("placeholder.html", page_url="devTeam")