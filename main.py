

from tkinter import *


root = Tk()
root.title("Learning Assistance")
root.geometry("1000x1000")

class Elder():
  def __init__(self, master):
    self.master = master


class commands():

  def calloutpress():
    print("Button Pressed")

class Learning_User(Elder):

  def __init__ (self, master):
    super().__init__(self)
    global LUPage
    LUPage = Canvas(master, width=300, height=300, bg="#7FA391").pack()

    return print("Canvas Loaded")

  def Welcome(self, master):
    Title_LUPage = Button(master, height=5, width=5, pady=10, command=commands.calloutpress).pack()

    return print("BTN Loaded")


  

firstpage = Learning_User(root)

firstpage.Welcome(LUPage)

root.mainloop()




