

from flask import Blueprint, render_template, redirect, request_started, url_for, request, session
from flask_login import user_accessed
from flask_sqlalchemy import SQLAlchemy
from . import models
from . import db
# import time
import datetime
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


@views.route("/templates/Course.html", methods = ["GET", "POST"])
def Course():
  if request.method == "POST":
    user_enter_course = request.form.get("courses") #this has be the "input div" with the "id or Name" atr
    course_list = (user_enter_course).split(",")
    print(course_list)

    session["k_course_list"] = user_enter_course
    #check if table alr exist, if yes then just add, if not create
    global store_user_enter_course
    store_user_enter_course = models.course(course_name=user_enter_course, homework = None)
    db.session.add(store_user_enter_course)
    db.session.commit()


  return render_template("Course.html")

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
  global store_course_homework
  if "k_course_list" in session:
    all_Course = session["k_course_list"]
    list_of_Course = all_Course.split(",")

    
  
  # global each_course_hw

  if request.method == "POST":
    entered_hw = request.form.get("hw_in_MATH")
    entered_hw_list = entered_hw.split(",")
    print(len(entered_hw_list))

    session["k_hw_in_MATH"] = entered_hw
    store_user_enter_course.homework = entered_hw
    db.session.add(store_user_enter_course)
    db.session.commit()
    # for each_course_hw in list_of_Course:
    #   entered_hw = request.form.get(f"hw_in{each_course_hw}")
    #   session[f"k_homework_in_{each_course_hw}"] = entered_hw

    #   store_user_enter_course.homework = entered_hw
    #   #   hw = request.form.get(f"hw_in_{each_course_hw}")
    #   # store_course_homework = models.course(course_name = each_course_hw, homework = entered_hw)
    #   #   session[f"k_{each_course_hw}"] = hw
    #   db.session.add(store_user_enter_course)
    #   db.session.commit()
    
    





  # if request.method == "POST":
  #   addnewHW = request.form.get("addNHW")
  #   newHWList = addnewHW.split(",")
  #   list_of_HW = list_of_HW + newHWList
  # else:
  #   pass
  return render_template("Homework.html", list_of_Course = list_of_Course)



@views.route("/templates/Time.html")
def Time():

  if "k_hw_in_MATH" in session:
    entered_hw_list = session["k_hw_in_MATH"]
    
    year_now = 2022
    month_now = 6
    day_now = 13

    time_now = datetime.datetime.now()
    bed_time = datetime.datetime(year_now, month_now, day_now, 23)
    homework_time = ((len(entered_hw_list)-1)* 2)
    print(len(entered_hw_list))
    print(entered_hw_list)
    print(homework_time)
    work_time = datetime.datetime(year_now, month_now, day_now, homework_time)
    free_time = datetime.datetime(year_now, month_now, day_now, homework_time+12)
    
  


    timeuntilsleep= (bed_time - time_now)
    timetocompleteallwork = (work_time).strftime("%H:%M:%S")
    freetimeavaliable = bed_time - free_time
    print(freetimeavaliable)
  else:
    timeuntilsleep = "0"
    timetocompleteallwork = "0"
    freetimeavaliable = "0"




  return render_template(
    "Time.html",
    time_to_complete_all_work=timetocompleteallwork, free_time_avaliable=freetimeavaliable, 
    time_until_sleep=str(timeuntilsleep),



  )


@views.route("/templates/Priority.html")
def Priority():
  hw = models.course.query.all()
  print(hw)

  # if  in session:
  #   for each_course_hw in list_of_Course:
  #     hw = session[f"k_homework_in_{each_course_hw}"]
  #     list_of_all_HW += [hw]
    # all_hw_list = all_hw.split(",")


  #Need to calculate class weighing and sort by large to small
  #first one is Urgent_HW
  #next use for loop to print the other


  return render_template("Priority.html", allhw = hw) 




@views.route("/templates/Setting.html")
def Setting():
  if "k_course_list" in session:
    all_Course = session["k_course_list"]
    listofclass= all_Course.split(",")
  
  return render_template("Setting.html", listofclass = listofclass )


#Redirecting user, when they Just Entered the IP
@views.route("/") #Redirect must come after the Directed Code
def root():
  return redirect(url_for("views.home"))