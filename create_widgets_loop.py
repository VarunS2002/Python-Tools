from tkinter import *

top = Tk()

boxes = []
values = []


def print_values():
    for x in range(0, 5):
        values.append(boxes[x].get())
    print(values)


b = Button(top, text="Print Values", command=print_values)
b.pack()

for i in range(0, 5):
    boxes.append(i)
    boxes[i] = Entry(top, bd=2)
    boxes[i].pack()

top.mainloop()
