from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name:")

# Create a Label Widget
myLabel1 = Label(root, text="Hello world!")
myLabel2 = Label(root, text="My name is John")

# Showing it on the screen
# myLabel1.grid(row="0", column="0")
# myLabel2.grid(row="1", column="0")
# myLabel1.pack()
# myLabel2.pack()

i = 4


def myClick():
	global i
	myLabel = Label(root, text=e.get())
	# myLabel.grid(row=i, column="0")
	myLabel.pack()
	i += 1


myButton = Button(root, text="Click me!", command=myClick, fg="blue", bg="#000000")
# myButton.grid(row="1", column="1")
myButton.pack()

root.mainloop()

