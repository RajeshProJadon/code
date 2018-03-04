# try:
#     import tkinter
# except ImportError: # pyhton2
#     import Tkinter as tkinter
import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('450x680')
mainWindow.mainloop()