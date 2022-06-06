from flask import Blueprint, render_template, redirect, url_for, request, session
from flask_login import user_accessed
from flask_sqlalchemy import SQLAlchemy
from . import models
from . import db
# from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
views = Blueprint('views', __name__)

# views.secret_key = "test"



#Home Page
@views.route("/templates/index.html")
def home():
  user = "Sean"
  return render_template("index.html", user = user)



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
  global newHWList
  newHWList = ""
  if request.method == "POST":
    addedHW = request.form.get("addHW")
    list_of_HW = addedHW.split(",")
    session["all_HW"] = addedHW


    store_hw = models.user_homework(homework=addedHW)
    db.session.add(store_hw)
    db.session.commit()



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

  # if request.method == "POST":
  #   addnewHW = request.form.get("addNHW")
  #   newHWList = addnewHW.split(",")
  #   list_of_HW = list_of_HW + newHWList
  # else:
  #   pass
  return render_template("Homework.html", list_of_HW = list_of_HW)



@views.route("/templates/Priority.html")
def Priority():
  urgent_homework = "test"

  #Need to calculate class weighing and sort by large to small
  #first one is Urgent_HW
  #next use for loop to print the other


  return render_template("Priority.html", Priority = f"Finish {urgent_homework}")




@views.route("/templates/Setting.html")
def Setting():
  listofclass = ["hI", "2"]
  return render_template("Setting.html", listofclass = listofclass )


#Redirecting user, when they Just Entered the IP
@views.route("/") #Redirect must come after the Directed Code
def root():
  return redirect(url_for("views.home"))