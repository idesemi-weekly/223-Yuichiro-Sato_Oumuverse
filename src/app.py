import os
from datetime import datetime

import pytz
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import check_password_hash, generate_password_hash

load_dotenv()

if os.environ.get("SECRET_KEY"):
    print("SECRET_KEY=OK")
else:
    print("SECRET_KEY=NG")

app = Flask(__name__)
csrf = CSRFProtect(app)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
if not app.config["SECRET_KEY"]:
    print(
        "警告: SECRET_KEYが設定されていません。安全なキーを環境変数に設定してください。"
    )
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(3000), nullable=False)
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(pytz.timezone("Asia/Tokyo")),
    )
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    author = db.relationship("User", back_populates="posts")


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(128))
    posts = db.relationship(
        "Post", back_populates="author", cascade="all, delete-orphan", lazy="dynamic"
    )


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/mypost", methods=["GET", "POST"])
@login_required
def mypost():
    if request.method == "GET":
        posts = Post.query.filter_by(user_id=current_user.id).all()
        return render_template("mypost.html", posts=posts)


@app.route("/everyonepost", methods=["GET", "POST"])
@login_required
def everyonepost():
    if request.method == "GET":
        posts = Post.query.all()
        return render_template("everyonepost.html", posts=posts)


@app.route("/")
def top():
    return render_template("top.html")


@app.route("/newpost", methods=["GET", "POST"])
@login_required
def newpost():
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")

        post = Post(title=title, body=body, user_id=current_user.id)

        db.session.add(post)
        db.session.commit()
        return redirect("/mypost")
    else:
        return render_template("newpost.html")


@app.route("/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit(id):
    post = Post.query.get(id)

    if post is None:
        return redirect("/mypost")

    if post.user_id != current_user.id:
        return redirect("/mypost")

    if request.method == "GET":
        return render_template("edit.html", post=post)

    else:
        post.title = request.form.get("title")
        post.body = request.form.get("body")

        db.session.commit()
        return redirect("/mypost")


@app.route("/<int:id>/delete", methods=["GET"])
@login_required
def delete(id):
    post = Post.query.get(id)

    if post is None:
        return redirect("/mypost")

    if post.user_id != current_user.id:
        return redirect("/mypost")

    db.session.delete(post)
    db.session.commit()
    return redirect("/mypost")


@app.route("/admin")
@login_required
def admin():

    admin_user = os.environ.get("ADMIN_USERNAME")

    if not admin_user or current_user.username != admin_user:
        return redirect("/")

    users = User.query.all()
    return render_template("admin.html", users=users)


@app.route("/admin/reset_password/<int:user_id>", methods=["POST"])
@login_required
def reset_password_admin(user_id):

    admin_user = os.environ.get("ADMIN_USERNAME")

    if not admin_user or current_user.username != admin_user:
        return redirect("/")

    user_to_reset = User.query.get(user_id)
    new_password = request.form.get("new_password")

    if not new_password or len(new_password) < 8:
        users = User.query.all()
        return render_template(
            "admin.html",
            users=users,
            error="Passwordは8文字以上必要です",
            error_user_id=user_id,
        )

    if user_to_reset and new_password:
        user_to_reset.password = generate_password_hash(
            new_password, method="pbkdf2:sha256"
        )
        db.session.commit()

    return redirect("/admin")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            return render_template(
                "signup.html", error="このUsernameは既に使用されています"
            )

        if not username or not password:
            return render_template("signup.html", error="UsernameとPasswordは必須です")

        if len(password) < 8:
            return render_template("signup.html", error="Passwordは8文字以上必要です")

        user = User(
            username=username,
            password=generate_password_hash(password, method="pbkdf2:sha256"),
        )

        db.session.add(user)
        db.session.commit()
        return redirect("/login")
    else:
        return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect("/mypost")
        else:
            return render_template(
                "login.html", error="UsernameまたはPasswordが正しくありません。"
            )
    else:
        return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")
