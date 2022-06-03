#Model.py is a file that the primary use is as a Datebase for the Homework stored
#we setup database here
from . import db #the current folder, importing the object "db" in the init.py
# from flask_login import UserMixin, a model for login, not using right now..


#creating a instance(object) that inhertant the db.Model and creating a "schema" with the value wanted to store"

class user_homework(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  homework = db.Column(db.String(10000))
  #We can store other things, due date and such, time created.

