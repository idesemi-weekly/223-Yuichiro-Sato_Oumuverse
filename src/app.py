from flask import Flask
from flask import render_template , request ,redirect
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
import pytz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mypost.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    body = db.Column(db.String(3000),nullable=False)
    updated_at = db.Column(db.DateTime,nullable=False,default=datetime.now(pytz.timezone('Asia/Tokyo')))


@app.route("/index",methods=['GET','POST'])
#@login_required
def index():
    if request.method == 'GET':
        posts = Post.query.all()
        return render_template("index.html",posts=posts)

@app.route("/mypost")
#@login_required
def mypost():
    return render_template("mypost.html")

@app.route("/everyonepost")
#@login_required
def everyonepost():
    return render_template("everyonepost.html")


@app.route("/toppage",methods=['GET','POST'])
#@login_required
def toppage():
    if request.method == "POST":
        title = request.form.get('title')
        body = request.form.get('body')

        post = Post(title=title,body=body)

        db.session.add(post)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template("toppage.html")

@app.route("/<int:id>/edit",methods=['GET','POST'])
#@login_required
def edit(id):
    post = Post.query.get(id)
    if request.method == "GET":
        return render_template('edit.html',post=post)

    else:
        post.title = request.form.get('title')
        post.body =request.form.get('body')

        db.session.commit()
        return redirect('/index')

@app.route("/<int:id>/delete",methods=['GET'])
#@login_required
def delete(id):
    post = Post.query.get(id)

    db.session.delete(post)
    db.session.commit()
    return redirect('/index')


@app.route("/admin")
#@login_required
def admin():
    return render_template("admin.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")