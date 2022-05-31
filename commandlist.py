from tkinter import *
from tkinter import ttk


class commands():



  def calloutpress():
    print("Pressed")
    return

  def checkpress():
    global pressed
    pressed = True
    return pressed == True

  
  def get_entry():
    Submit_Button = ""
    Submitted_Entry = Submit_Button.get()
    print(Submitted_Entry)