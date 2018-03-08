import math
from tkinter import *
from tkinter import messagebox

top = Tk()
newcanvas = Canvas(top, width = 600, height = 400)
newcanvas.pack(side = TOP)
newcanvas.configure(background='black')

def close_window():
	top.destroy()

def calculate():
	#calculates the unknown side of the triangle
	A = A_in.get()
	B = B_in.get()
	C = C_in.get()
	if len(A) == 0:
		output = math.sqrt((int(B)**2) + (int(C)**2))
		messagebox.showinfo("Side A", str(output))
	elif len(B) == 0:
		output = math.sqrt((int(A)**2) - (int(C)**2))
		messagebox.showinfo("Side A", str(output))
	elif len(C) == 0:
		output = math.sqrt((int(A)**2) - (int(B)**2))
		messagebox.showinfo("Side A", str(output))

def clear():
	A_in.delete(0,END)
	A_in.insert(0,"")
	B_in.delete(0,END)
	B_in.insert(0,"")
	C_in.delete(0,END)
	C_in.insert(0,"")

box = Frame(top)
box.pack(side = BOTTOM)
Side_A = Label(box,text = "Side A")
Side_A.grid(row = 1, column = 1)
Side_B = Label(box,text = "Side B")
Side_B.grid(row = 1, column = 2)
Side_C = Label(box,text = "Side C")
Side_C.grid(row = 1, column = 3)
A_in = Entry(box)
A_in.grid(row = 2, column = 1)
B_in = Entry(box)
B_in.grid(row = 2, column = 2)
C_in = Entry(box)
C_in.grid(row = 2, column = 3)
cal_button = Button(box,text = "Calculate", command = calculate)
cal_button.grid(row = 3, column = 2)
clear_botton = Button(box,text = "Clear", command = clear)
clear_botton.grid(row = 4, column = 2)

top.mainloop()
