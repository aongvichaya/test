from tkinter import *


def say_hi():
    print("hi there, everyone!")

root = Tk()

frame = Frame(root)
frame.pack()

q = Button(frame, text="QUIT", fg="red", command=frame.quit)
q.pack(side=LEFT)

hi = Button(frame, text="Hello", command=say_hi)
hi.pack(side=LEFT)

root.mainloop()