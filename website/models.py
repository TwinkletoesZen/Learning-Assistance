#Model.py is a file that the primary use is as a Datebase for the Homework stored
#we setup database here

from . import db #the current folder, importing the object "db" in the init.py
# from flask_login import UserMixin, a model for login, not using right now..
from flask_login import UserMixin
import sqlalchemy
# fr om sqlalchemy.sql import func
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship
#creating a instance(object) that inhertant the db.Model and creating a "schema" with the value wanted to store"






# class user_homework(db.Model):
#   id = db.Column(db.Integer, primary_key = True) #THIS IS IMPORTANT
#   homework = db.Column(db.String(10000))

  #sub field of which Class, connect with the "classes" db
  #ask for input on which class
  # initial_est_time_for_assignment = db.Column(db.Float)
  # average_assignment = db.Column(db.Float)
  # initial_est_time_for_quiz = db.Column(db.Float)
  # initial_est_time_for_exam = db.Column(db.Float)
  
  #We can store other things, due date and such, time created.
  #a field of the "classes"'s Id, (connection purposes)


#maybe separate quiz, hw, exam
#or just count Quiz, Exam as assignment
#compare actual time and est time.

#testing: Use two classes(Math and English), test to connect them
#give it inital data for the database
#then Algorithm can be accurate



class course(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  course_name = db.Column(db.String(1000)) #One to Many, with relation to "user_homework
  homework = db.Column(db.String(10000))
  # weight = db.Column(db.Integer)


  # def __init__(self, course_name):
  #   self.course_name = course_name

  # user_id = db.Column(db.Integer, db.ForeginKey("user.id"))
  #user.id, user a SQL thing, ID is the atr referencing

  #Connection to Homework
    #
  # Weighing = db.Column(db.String(1000))


# class sign_up_form(db.Model):
#   id = db.Column(db.Integer, primary_key =True)



# class User(db.Model, UserMixin):
#   id = db.Column(db.Integer, primary_key = True)
#   email = db.Column(db.String(150), unique=True)
#   password = db.Column(db.String(150))
#   # courses = db.relationship("Cources")
  #connection to Courses

  #Forigen Key that reference anothor "Column" 
