from tkinter import *


def say_hi():
    print("hi there, everyone!")

root = Tk()

frame = Frame(root,height=5, bg="red", bd=3)
frame.pack()

q = Button(frame, text="QUIT", fg="red", command=frame.quit)
q.pack(side=LEFT)

hi = Button(frame, text="Hello", command=say_hi)
hi.pack(side=RIGHT)

root.mainloop()