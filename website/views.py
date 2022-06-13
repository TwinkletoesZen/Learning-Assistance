

from flask import Blueprint, render_template, redirect, request_started, url_for, request, session
from flask_login import user_accessed
from flask_sqlalchemy import SQLAlchemy
from . import models
from . import db
# from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
views = Blueprint('views', __name__)

# views.secret_key = "test"

global homework_in_course
homework_in_course = ""
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
  # global list_of_HW
  # list_of_HW = ""
  # global newHWList
  # newHWList = ""
  # if request.method == "POST":
  #   addedHW = request.form.get("addHW")
  #   list_of_HW = addedHW.split(",")
  #   session["all_HW"] = addedHW


  #   store_hw = models.user_homework(homework=addedHW)
  #   db.session.add(store_hw) #what do these do again? #for this to work, we need to have a session stored
  #   db.session.commit()



  #   print(session["all_HW"])
  # else:
  #   pass

  # # bruh = store_hw.query

  # if "all_HW" in session:
  #   addedHW = session["all_HW"]
  #   list_of_HW = addedHW.split(",")
  #   # if request.method == "POST":
  #   #   newlyaddedhw = request.form.get("addHW")
  #   #   newlyaddedlist = newlyaddedhw.split(",")
  #   #   list_of_HW.append(newlyaddedlist)
  #   # else:
  # #     print("Can't Append Item")
  # else:
  #   print("can't find session")



#Bridge between Cuorse Page and homework page
  global list_of_Course
  if "k_course_list" in session:
    all_Course = session["k_course_list"]
    list_of_Course = all_Course.split(",")

    
  
  # global each_course_hw
  if request.method == "POST":
    for each_course_hw in list_of_Course:
      entered_hw = request.form.get(f"hw_in{each_course_hw}")
      session[f"k_homework_in_{each_course_hw}"] = entered_hw
      #   hw = request.form.get(f"hw_in_{each_course_hw}")
      #   store_course_homework = models.course(course_name = each_course_hw, homework = hw)
      #   session[f"k_{each_course_hw}"] = hw
      #   db.session.add(store_course_homework)
      #   db.session.commit()
    
    





  # if request.method == "POST":
  #   addnewHW = request.form.get("addNHW")
  #   newHWList = addnewHW.split(",")
  #   list_of_HW = list_of_HW + newHWList
  # else:
  #   pass
  return render_template("Homework.html", list_of_Course = list_of_Course)



@views.route("/templates/Priority.html")
def Priority():
  list_of_all_HW = []
  
  if  in session:
    for each_course_hw in list_of_Course:
      hw = session[f"k_homework_in_{each_course_hw}"]
      list_of_all_HW += [hw]
    # all_hw_list = all_hw.split(",")


  #Need to calculate class weighing and sort by large to small
  #first one is Urgent_HW
  #next use for loop to print the other


  return render_template("Priority.html", allhw = list_of_all_HW) 


@views.route("/templates/Course.html", methods = ["GET", "POST"])
def Course():
  if request.method == "POST":
    user_enter_course = request.form.get("courses") #this has be the "input div" with the "id or Name" atr
    course_list = (user_enter_course).split(",")
    print(course_list)

    session["k_course_list"] = user_enter_course
    store_user_enter_course = models.course(course_name=user_enter_course, homework = "0")
    db.session.add(store_user_enter_course)
    db.session.commit()


  return render_template("Course.html")


@views.route("/templates/Setting.html")
def Setting():
  listofclass = ["hI", "2"]
  return render_template("Setting.html", listofclass = listofclass )


#Redirecting user, when they Just Entered the IP
@views.route("/") #Redirect must come after the Directed Code
def root():
  return redirect(url_for("views.home"))