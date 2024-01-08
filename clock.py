#from tkinter import *

#import time

#main_window = Tk()
#[create a label named clock, set font options etc.]
#clock = Label(main_window, font=('arial', 100, 'bold'), bg='green')
#[Place clock label into main window]
#clock.pack(fill=BOTH, expand=1)
#[define a user defined function tick()
 #we will call this function again and again after
 #200 milli seconds]
#def tick():
   # [ get time in a string s]
   # s = time.strftime('%H:%M:%S')
    #[if need to update time (after 1 second)
       #then update otherwise pass]
   # if s != clock["text"]:
        #clock["text"] = s
    #[call tick function after 200 milliseconds]
   # clock.after(200, tick)

#[ start tick function]
#tick()
#[ start mainloop to start GUI of the program
#main_window.mainloop()

#4.Adding Menus to Python 3 tkinter GUI Programs
# Python Menu Program to show
# File and Edit Menue
# When an option clicked
# Option Label is shown in title of
# application window

from tkinter import *

# Menu click handling functions for File menu
def new():
    main_window.title("'New' is selected")
def open1():
    main_window.title ("'Open' is selected")
def save():
    main_window.title("'Save' is selected")
def exit1():
    main_window.destroy()


# Menu click handling functions for Edit menu
def cut():
    main_window.title("'Cut' is selected")
def copy():
    main_window.title("'Copy' is selected")
def paste():
    main_window.title("'Paste' is selected")

# create main window 
main_window = Tk()
# set size and position of main window 
main_window.geometry("300x300+550+350")
# create menu bar 
menubar = Menu(main_window)
# create file menu
file = Menu(menubar, tearoff = 0)
# create file menu commands New,Open,Save,Exit 
file.add_command(label="New", command = new)
file.add_command(label = "Open", command = open1)
file.add_command(label = "Save", command = save)
file.add_command(label = "Exit", command = exit1)
# add file menu to menu bar
menubar.add_cascade(label = "File", menu = file)
# create edit menu
edit = Menu(menubar, tearoff=0)
# create edit menu commands Cut,Copy,Paste
edit.add_command(label = "Cut", command = cut)
edit.add_command(label = "Copy", command = copy)
edit.add_command(label = "Paste", command = paste)
# add edit menu to menu bar
menubar.add_cascade(label = "Edit", menu = edit)
# attach menubar to main window
main_window.config(menu = menubar)
# start mainloop(), start GUI
main_window.mainloop()
