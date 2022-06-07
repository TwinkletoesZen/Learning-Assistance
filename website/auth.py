from flask import Blueprint, render_template, request, flash

#importing Database
from . import models
from . import db


auth = Blueprint("auth", __name__)

@auth.route("/templates/login.html", methods=["GET", "POST"])
def login():
  return render_template("login.html")

@auth.route("/logout")
def logout():
  return "you have logged out"

@auth.route("/templates/signup.html", methods=["GET", "POST"])
def sign_up():
  if request.method == "POST":
    user_sign_up_email = request.form.get("email")
    user_sign_up_pw1 = str(request.form.get("password1"))
    user_sign_up_pw2 = str(request.form.get("password2"))

    #getting the classes
    user_classes = request.form.get("classes")
    user_classes_list = user_classes.split(",")
    #storing it in DB
    store_user_classes_list = models.classes(classes = user_classes)
    # db.session.add(store_user_classes_list)
    # db.session.commit()

    if len(user_sign_up_email) < 3:
      flash("Email need to be greater than 3", category="bad")
    elif len(user_sign_up_pw1) < 8:
      flash("You need the length 8 for a password", category="bad")
    elif user_sign_up_pw1 != user_sign_up_pw2:
      flash("Password don't match", category="bad")
    else:
      flash ("hell yeah, Account created, You are now a better student", category="good")

    
  return render_template("signup.html")