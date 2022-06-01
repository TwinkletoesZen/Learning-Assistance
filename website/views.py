from flask import Blueprint, render_template, redirect, url_for, request, session
# from flask_sqlalchemy import SQLAlchemy

views = Blueprint('views', __name__)
# views.secret_key = "test"

@views.route("/templates/index.html")
def home():
  return render_template("index.html")

@views.route("/templates/Time.html")
def Time():
  timeuntilsleep = 0
  timetocompleteallwork = ""
  freetimeavaliable = 0




  return render_template("Time.html", time_to_complete_all_work=timetocompleteallwork, free_time_avaliable=freetimeavaliable, time_until_sleep=str(timeuntilsleep))




@views.route("/templates/Homework.html", methods=["GET", "POST"])
def Homework():
  global list_of_HW
  list_of_HW = ""
  if request.method == "POST":
    addedHW = request.form.get("addHW")
    list_of_HW = addedHW.split(",")
    session["all_HW"] = addedHW

    print(session["all_HW"])
  else:
    print("Failed")

  if "all_HW" in session:
    addedHW = session["all_HW"]
    list_of_HW = addedHW.split(",")
    # if request.method == "POST":
    #   newlyaddedhw = request.form.get("addHW")
    #   newlyaddedlist = newlyaddedhw.split(",")
    #   list_of_HW.append(newlyaddedlist)
    # else:
  #     print("Can't Append Item")
  # else:
    print("can't find session")
  return render_template("Homework.html", list_of_HW = list_of_HW)

@views.route("/templates/Priority.html")
def Priority():
  return render_template("Priority.html")


@views.route("/") #Redirect must come after the Directed Code
def root():
  return redirect(url_for("views.home"))