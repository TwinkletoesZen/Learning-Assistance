from flask import Blueprint, render_template, request, flash
from requests import session

#importing Database
from . import models
from . import db
from .models import User

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

    # #getting the courses
    # user_courses_form = request.form.get("courses")
    # user_courses_list = user_courses_form.split(",")
    # #storing it in DB

    # for each_course_name in user_courses_list:
    #   store_user_courses_list = models.Cources(course_name = each_course_name)
    #   # db.session.add(store_user_courses_list)
    #   # db.session.commit()

    if len(user_sign_up_email) <  3:
      flash("Email need to be greater than 3", category="bad")
    elif len(user_sign_up_pw1) < 8:
      flash("You need the length 8 for a password", category="bad")
    elif user_sign_up_pw1 != user_sign_up_pw2:
      flash("Password don't match", category="bad")
    else:
      flash ("hell yeah, Account created, You are now a better student", category="good")

    
  return render_template("signup.html")