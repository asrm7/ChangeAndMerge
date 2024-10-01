from tkinter import *

class Grid( Frame ):
 def __init__(self):
  # starting the frame 
  Frame.__init__(self)
  self.master.title("Grid")
  self.master.geometry( "80x80" )
  
  # creating the labels and adding
  # grid() method
  for xrow in range(3):
   for xcolumn in range(3):
    Label(self.master, text=str(xrow)+','+str(xcolumn)).grid(row=xrow,column=xcolumn)
  
  mainloop()

Grid()
