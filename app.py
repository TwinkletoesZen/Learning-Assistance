from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/templates/index.html")
def home():
  return render_template("index.html")

@app.route("/templates/Time.html")
def Time():
  return render_template("Time.html")

@app.route("/templates/Homework.html")
def Homework():
  return render_template("Homework.html")

@app.route("/templates/Priority.html")
def Priority():
  return render_template("Priority.html")


@app.route("/") #Redirect must come after the Directed Code
def root():
  return redirect(url_for("home"))

if __name__ == "__main__":
  app.run(debug=True)
