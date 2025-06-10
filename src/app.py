#環境変数設定と起動コマンド
#export FLASK_APP=app.py
#flask run --debug

from flask import Flask
from flask import render_template , request ,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user,logout_user,login_required,LoginManager,UserMixin

from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import pytz
import os
from dotenv import load_dotenv

load_dotenv()

if os.environ.get("SECRET_KEY"):
    print("SECRET_KEY=OK")
else:
    print("SECRET_KEY=NG")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mypost.db'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY',os.urandom(24))
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    body = db.Column(db.String(3000),nullable=False)
    updated_at = db.Column(db.DateTime,nullable=False,default=datetime.now(pytz.timezone('Asia/Tokyo')))

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),unique=True)
    password = db.Column(db.String(128))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    

@app.route("/index",methods=['GET','POST'])
@login_required
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
@login_required
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
@login_required
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
@login_required
def delete(id):
    post = Post.query.get(id)

    db.session.delete(post)
    db.session.commit()
    return redirect('/index')


@app.route("/admin")
@login_required
def admin():
    return render_template("admin.html")

@app.route("/signup",methods=['GET','POST'])
def signup():
    if request.method == "POST":
        username = request.form.get('username')
        password =request.form.get('password')

        user = User(username=username,password=generate_password_hash(password,method='pbkdf2:sha256'))

        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    else:
        return render_template('signup.html')

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password =request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password,password):
            login_user(user)
            return redirect('/index')
        else:
            return render_template('login.html',error='UsernameまたはPasswordが正しくありません。')
    else:
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')