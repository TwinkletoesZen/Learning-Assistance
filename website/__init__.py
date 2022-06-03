from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy() #creating a object of the class "SQLAlchemy"
DB_NAME = "database.db"#what is this?

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'ILoveTanya0313'
  app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}" #the database is located at this place.
  
  #initlize Db
  db.init_app(app)




  from .views import views
  from .auth import auth

  app.register_blueprint(views, url_prefix = "/")
  app.register_blueprint(auth, url_prefix = "/")


  from .models import user_homework #making the model run, before database creation
  
  create_database(app)


  return app
  

#creating our database:

def create_database(app):
  #checking if the db alr have exist
  if not path.exists("website/" + DB_NAME): #if data doesn't exist
    db.create_all(app=app)
