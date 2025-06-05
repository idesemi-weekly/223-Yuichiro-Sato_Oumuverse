from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/toppage")
def toppage():
    return render_template("toppage.html")