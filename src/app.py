from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/toppage")
def toppage():
    return render_template("toppage.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/everyonepost")
def everyonepost():
    return render_template("everyonepost.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/mypost")
def mypost():
    return render_template("mypost.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")