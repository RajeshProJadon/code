import sys
import tkinter as tk


win = tk.Tk()

win.title("this is title window")
lbl = tk.Label(win, text = "Enter your application name: ").grid(column = 0, row=0)
def click():
    print("Hi," + name.get())

name = tk.StringVar()
nameEntered = tk.Entry(win, width = 12, textvariable = name).grid(column = 0, row = 1)  
# Button widget  
button = tk.Button(win, text = "submit", command = click).grid(column = 1, row = 1)  
win.mainloop()
