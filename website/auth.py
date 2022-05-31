from flask import Blueprint, render_template



auth = Blueprint("auth", __name__)

@auth.route("/templates/login.html")
def login():
  return render_template("login.html")

@auth.route("/logout")
def logout():
  return "you have logged out"

@auth.route("/templates/signup.html")
def sign_up():
  return render_template("signup.html")