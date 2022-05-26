import tkinter as tk

class Learning_Assistance():

  def __init__(self, master):
      self.master = master

  def login(self):
    Login_Frame = tk.Frame(self.master, height=1000, width=1000, bg="#90FFC8")
    Login_Frame.pack()