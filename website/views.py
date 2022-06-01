from flask import Blueprint, render_template, redirect, url_for



views = Blueprint('views', __name__)


@views.route("/templates/index.html")
def home():
  return render_template("index.html")

@views.route("/templates/Time.html ")
def Time():
  return render_template("Time.html")

@views.route("/templates/Homework.html")
def Homework():
  return render_template("Homework.html")

@views.route("/templates/Priority.html")
def Priority():
  return render_template("Priority.html")


@views.route("/") #Redirect must come after the Directed Code
def root():
  return redirect(url_for("views.home"))