from flask import Flask, redirect
from flask_fileupload import FlaskFileUpload
from flask_login import LoginManager, UserMixin, login_user, logout_user

app = Flask(__name__)
app.config.from_object("config")
lm = LoginManager(app)
fue = FlaskFileUpload(app)


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id


@lm.user_loader
def load_user(user_id):
    return User(user_id)


@app.route("/login/")
def login():
    user = User("testuser")
    login_user(user)
    return redirect("/upload")


@app.route("/logout/")
def logout():
    logout_user()
    return redirect("/")
