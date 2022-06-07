#Model.py is a file that the primary use is as a Datebase for the Homework stored
#we setup database here
from . import db #the current folder, importing the object "db" in the init.py
# from flask_login import UserMixin, a model for login, not using right now..


#creating a instance(object) that inhertant the db.Model and creating a "schema" with the value wanted to store"

class user_homework(db.Model):
  id = db.Column(db.Integer, primary_key = True) #THIS IS IMPORTANT
  homework = db.Column(db.String(10000))
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



class classes(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  classes = db.Column(db.String(1000))
  # Weighing = db.Column(db.String(1000))


# class sign_up_form(db.Model):
#   id = db.Column(db.Integer, primary_key =True)



  