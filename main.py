from commandlist import *
from tkinter import *
from tkinter import ttk
from functools import partial #execute code before return WT????

basic_geometry = "800x450" 

root = Tk()
root.title("Monday")
root.geometry("800x450")





class Elder():
  def __init__(self, master):
    self.master = master

class Learning_User(Elder):
  def __init__ (self, master):
    super().__init__(self)
    return 


  def Daily_Check_In(self, master):
    master = Tk()
    master.title("Daily Check In")
    master.geometry(basic_geometry)

  

  def Plan_Page(self, master):
    master = Tk()
    master.title("Your Plan")
    master.geometry(basic_geometry)


  def Homework_Page(self, master):
    master = Tk()
    master.title("Your HW Today")
    master.geometry(basic_geometry)


  def Time_Management_Page(self, master):
    master = Tk()
    master.title("Time is Money")
    master.geometry(basic_geometry)

  def Priorty_Page(self, master):
    master = Tk()
    master.title("Focus")
    master.geometry(basic_geometry)

  def GradeCalculator_Page(self, master):
    master = Tk()
    master.title("Good Luck")
    master.geometry(basic_geometry)





  def Home_Page(self, master):
    master.destroy()
    master= Tk()
    master.title("Monday")
    master.geometry("800x450")

    i = 1
    go_Plan_Page = Button(master, text="Plans\nfor Today", command= lambda: Learning_User.Plan_Page(self, master)).grid(column=i, row=2)
    go_Homework_page = Button(master, text="Input \nHomework", command= lambda: Learning_User.Homework_Page(self, master)).grid(column=i+1, row=2, rowspan=2)
    go_Time_Management_page = Button(master, text="Manage \nTime", command= lambda: Learning_User.Time_Management_Page(self, master)).grid(column=i+2, row=2, rowspan=2)
    go_Priorty_page = Button(master, text="Priorty\nList", command=  lambda: Learning_User.Priorty_Page(self, master)).grid(column=i+3, row=2, rowspan=2)
    # go_Focus_page = Button(master, text="Focus\nList", command="").grid(column=4, row=2, rowspan=2)
    go_Grade_Calculater = Button(master, text="Grade\nCalculater", command= lambda: Learning_User.GradeCalculator_Page(self, master)).grid(column=i+4, row=2, rowspan=2)

    # estimate_time = 0
    # Hw_Completion_extimated_time = Label(
    #   master,
    #   text="Here is your estimated time: " + str(estimate_time),
    # ).grid(column=1, row=1)



  def Welcome_P2(self, master):
    
    master.destroy()

    master = Tk()
    master.title("Monday")
    master.geometry("800x450")

    grade_weighing = Label(master, text="Please Enter Each Classes Weighing")
    grade_weighing.grid(column=1, row=1)
    #get entry from input privously.

    done = Button(master, text="Done", command= lambda: Learning_User.Home_Page(self, master))
    done.grid(column=1, row=4)

    return


  def Welcome(self, master):

    welcome_Msg = "Welcome to Twincodetoes' Learning Assistance"
    Welcome_Label = Label(master, text=welcome_Msg)
    Welcome_Label.grid(column=1, row=1, columnspan=3)

    goal_Label = Label(master, text="What do you want to achieve using \n this Learning Assistance? \n Please Select One")
    goal_Label.grid(column=1, row=2, columnspan=1)
    goal_option_dict = {
      "Get Higher Grades": 1,
      "Stay Ahead" : 2,
      "Learn how to Learn" :3,
      "Time Management" :4,
    }
    goal_option = StringVar()
    goal_dropD = OptionMenu(master, goal_option, *goal_option_dict)
    goal_dropD.grid(column=3, row=2)
    print(goal_option)

    class_Label = Label(master, text="Please Enter the Class you are taking,\n separated by a comma")
    class_Label.grid(column=1, row=3)

    e_class = Entry(master)
    e_class.insert(END, "Physics 11, Chemistry 12, etc.")
    e_class.grid(column=2, row=3)
    def get_value():
      class_list = e_class.get()
      class_list_to_list = class_list.split(",")
      with open("classlistdata.txt", "w") as classlist:
          classlist.write(class_list)
          classlist.close()
      print(class_list_to_list[1])
      print(class_list)
      return
    Submit_Button = ttk.Button(master, text="Submit", command= lambda: get_value()).grid(column=3, row=4)


  
    

    welcome_Done = Button(master, text="Next", width=10, command= lambda: Learning_User.Welcome_P2(self, master))
    welcome_Done.grid(column=1, row=5)








    # Finished_Btn = Button(master, text="quit", width=10, command=partial(commands.calloutpress))
    # Finished_Btn.grid(column=2, row=3)
    



    return print("Welcome Func Finished")



  









firstpage = Learning_User(root)

firstpage.Daily_Check_In(root)
firstpage.Welcome(root)


root.mainloop()



