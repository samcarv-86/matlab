from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I've clicked a button!")
    myLabel.pack()

myButton = Button(root, text="Click Me!",command=myClick,fg="blue",bg="red")
myButton.pack()

root.mainloop()