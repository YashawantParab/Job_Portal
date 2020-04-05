# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 10:28:08 2019

@author: yasha
"""

import tkinter as tkr


master = tkr.Tk()
master.geometry("200x100")
master.title("Dropdown List")


tkr.Label(master, text = "Basic Dropdown list").grid(row= 0)
# Create a Tkinter variable 
var = tkr.StringVar()
# Dictionary with options
set1 =tkr.OptionMenu(master, var, "C", "C++", "Python")

set1.configure(font= ("Arial",25))
set1.grid(row = 1, column = 0)

#Activate
listData= tkr.mainloop()

print(listData)