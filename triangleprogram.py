import math, turtle
from tkinter import *
from tkinter import messagebox

top = Tk()
rat = Toplevel(top)
rat.title("Triangle Checker")
ct = Toplevel(top)
ct.title("Cos Angle Checker")
ratcanvas = Canvas(rat, width = 600, height = 400)
ratcanvas.pack(side = TOP)

rat_t = turtle.RawTurtle(ratcanvas)
rat_t.hideturtle()
rat_t.speed(0)

ctcanvas = Canvas(ct, width = 600, height = 400)
ctcanvas.pack(side = TOP)

ct_t = turtle.RawTurtle(ctcanvas)
ct_t.hideturtle()

top.deiconify()
ct.withdraw()
rat.withdraw()

def rat_calculate():
	try:
		A = float(A_in.get())
		B = float(B_in.get())
		C = float(C_in.get())
		D = 90
		E = float(B_Angle_in.get())
		F = float(C_Angle_in.get())
	except ValueError:
		messagebox.showinfo("Error", "Please enter a interger")

	if (A == 0 and B > 0 and C > 0):
		output = round(math.sqrt((float(B)**2) + (float(C)**2)),2)
		A_in.delete(0,END)
		A_in.insert(0,str(output))
		angle_B = round(math.degrees(math.atan(float(B)/float(C))),2)
		B_Angle_in.delete(0,END)
		B_Angle_in.insert(0,str(angle_B))
		angle_C = 90 - angle_B
		C_Angle_in.delete(0,END)
		C_Angle_in.insert(0,str(angle_C))
		# draw(float(output),float(B),float(C),float(angle_B),float(angle_C))
		
	elif B == 0 and A > 0 and C > 0:
		output = round(math.sqrt((float(A)**2) - (float(C)**2)),2)
		B_in.delete(0,END)
		B_in.insert(0,str(output))
		angle_B = round(math.degrees(math.acos(float(C)/float(A))),2)
		B_Angle_in.delete(0,END)
		B_Angle_in.insert(0,str(angle_B))
		angle_C = 90 - angle_B
		C_Angle_in.delete(0,END)
		C_Angle_in.insert(0,str(angle_C))
		A_Angle_in.delete(0,END)
		A_Angle_in.insert(0,str(90))
		
	elif C == 0 and A > 0 and B > 0:
		output = round(math.sqrt((float(A)**2) - (float(B)**2)),2)
		C_in.delete(0,END)
		C_in.insert(0,str(output))
		angle_B = round(math.degrees(math.asin(float(B)/float(A))),2)
		B_Angle_in.delete(0,END)
		B_Angle_in.insert(0,str(angle_B))
		angle_C = 90 - angle_B
		C_Angle_in.delete(0,END)
		C_Angle_in.insert(0,str(angle_C))
		A_Angle_in.delete(0,END)
		A_Angle_in.insert(0,str(90))

	# E = angle B , F = angle C
	elif E > 0 and A > 0: 
		#input, angle B and hyp,a 
		angle_C = (90-float(E))
		side_B = round(float(A)*math.sin(math.radians(float(E))),2)
		side_C = round(float(A)*math.cos(math.radians(float(E))),2)
		C_Angle_in.delete(0,END)
		C_Angle_in.insert(0,str(angle_C))
		B_in.delete(0,END)
		B_in.insert(0,str(side_B))
		C_in.delete(0,END)
		C_in.insert(0,str(side_C))

	elif E > 0 and B > 0:
		#input, angle B and adj,b 
		angle_C = (90-float(E))
		side_A = round(float(B)/math.sin(math.radians(float(E))),2)
		side_C = round(float(B)/math.tan(math.radians(float(E))),2)
		C_Angle_in.delete(0,END)
		C_Angle_in.insert(0,str(angle_C))
		A_in.delete(0,END)
		A_in.insert(0,str(side_A))
		C_in.delete(0,END)
		C_in.insert(0,str(side_C))

	elif E > 0 and C > 0: 
		#input, angle B and opp,c
		angle_C = (90-float(E))
		side_A = round(float(C)/math.cos(math.radians(float(E))),2)
		side_B = round(float(C)*math.tan(math.radians(float(E))),2)
		C_Angle_in.delete(0,END)
		C_Angle_in.insert(0,str(angle_C))
		A_in.delete(0,END)
		A_in.insert(0,str(side_A))
		B_in.delete(0,END)
		B_in.insert(0,str(side_B))

	elif F > 0 and A > 0:
		#input,  angle c and hyp,a
		angle_B = (90-float(F))
		side_B = round(float(A)*math.cos(math.radians(float(F))),2)
		side_C = round(float(A)*math.sin(math.radians(float(F))),2)
		B_Angle_in.delete(0,END)
		B_Angle_in.insert(0,str(angle_B))
		B_in.delete(0,END)
		B_in.insert(0,str(side_B))
		C_in.delete(0,END)
		C_in.insert(0,str(side_C))

	elif F > 0 and B > 0:
		#input,  angle c and adj,b
		angle_B = (90-float(F))
		side_A = round(float(B)/math.cos(math.radians(float(F))),2)
		side_C = round(float(B)*math.tan(math.radians(float(F))),2)
		B_Angle_in.delete(0,END)
		B_Angle_in.insert(0,str(angle_B))
		A_in.delete(0,END)
		A_in.insert(0,str(side_A))
		C_in.delete(0,END)
		C_in.insert(0,str(side_C))

	elif F > 0 and C > 0:
		#input,  angle c and opp,c
		angle_B = (90-float(F))
		side_A = round(float(C)/math.sin(math.radians(float(F))),2)
		side_B = round(float(C)/math.tan(math.radians(float(F))),2)
		B_Angle_in.delete(0,END)
		B_Angle_in.insert(0,str(angle_B))
		A_in.delete(0,END)
		A_in.insert(0,str(side_A))
		B_in.delete(0,END)
		B_in.insert(0,str(side_B))
	else:
		messagebox.showinfo("Error", "Please enter two unknowns")

def ct_calculate():
	try:
		A = float(ct_A_in.get())
		B = float(ct_B_in.get())
		C = float(ct_C_in.get())
		D = float(ct_Angle_A_in.get()) #angle a
		E = float(ct_Angle_B_in.get()) #angle b
		F = float(ct_Angle_C_in.get()) #angle c

		if D >0 and E > 0 and F > 0:
			messagebox.showinfo("Error", "At least 1 side must be given")
			return
		if (A) >0 and (B) > 0 and (C) > 0:
			angle_A = round(math.degrees(math.acos((B**2 + C**2 - A**2)/(2.0 * B * C))),2)
			angle_B = round(math.degrees(math.acos((C**2 + A**2 - B**2)/(2.0 * C * A))),2)
			angle_C = round(math.degrees(math.acos((B**2 + A**2 - C**2)/(2.0 * B * A))),2)
			ct_set(str(A),str(B),str(C),str(angle_A),str(angle_B),str(angle_C))

		elif (A) >0 and (B) > 0 and (D) > 0:
			angle_B = round(math.degrees(math.asin((B*math.sin(math.radians(D)))/A)),2)
			angle_C = 180 - D - angle_B
			side_C = round(A*math.sin(math.radians(angle_C))/(math.sin(math.radians(D))),2)
			ct_set(str(A),str(B),str(side_C),str(D),str(angle_B),str(angle_C))

		elif (A) >0 and (B) > 0 and (E) > 0:
			angle_A = round(math.degrees(math.asin((A*math.sin(math.radians(E)))/B)),2)
			angle_C = 180 - E - angle_A
			side_C = round(A*math.sin(math.radians(angle_C))/(math.sin(math.radians(angle_A))),2)
			ct_set(str(A),str(B),str(side_C),str(angle_A),str(E),str(angle_C))

		elif (A) >0 and (B) > 0 and (F) > 0:
			side_C = round(math.sqrt((A**2 + B**2)-2*A*B*math.cos(math.radians(F))),2)
			angle_A = round(math.degrees(math.acos((B**2 + side_C**2 - A**2)/(2.0 * B *side_C))),2)
			angle_B = round(math.degrees(math.acos((A**2 + side_C**2 - B**2)/(2.0 * A *side_C))),2)
			ct_set(str(A),str(B),str(side_C),str(angle_A),str(angle_B),str(F))

		elif (A) >0 and (C) > 0 and (D) > 0:
			angle_C = round(math.degrees(math.asin((C*math.sin(math.radians(D)))/A)),2)
			angle_B = 180 - D - angle_C
			side_B = round(A*math.sin(math.radians(angle_B))/(math.sin(math.radians(D))),2)
			ct_set(str(A),str(side_B),str(C),str(D),str(angle_B),str(angle_C))
			
		elif (A) >0 and (C) > 0 and (E) > 0:
			side_B = round(math.sqrt((A**2 + C**2)-2*A*C*math.cos(math.radians(E))),2)
			angle_A = round(math.degrees(math.acos((side_B**2 + C**2 - A**2)/(2.0 * side_B *C))),2)
			angle_C = round(math.degrees(math.acos((side_B**2 + A**2 - C**2)/(2.0 * side_B *A))),2)
			ct_set(str(A),str(side_B),str(C),str(angle_A),str(E),str(angle_C))
			
		elif (A) >0 and (C) > 0 and (F) > 0:
			angle_A = round(math.degrees(math.asin((A*math.sin(math.radians(F)))/C)),2)
			angle_B = 180 - F - angle_A
			side_B = round(C*math.sin(math.radians(angle_B))/(math.sin(math.radians(F))),2)
			ct_set(str(A),str(side_B),str(C),str(angle_A),str(angle_B),str(F))

		elif (B) >0 and (C) > 0 and (D) > 0:
			side_A = round(math.sqrt((B**2 + C**2)-2*B*C*math.cos(math.radians(D))),2)
			angle_B = round(math.degrees(math.acos((side_A**2 + C**2 - B**2)/(2.0 * side_A * C))),2)
			angle_C = round(math.degrees(math.acos((side_A**2 + B**2 - C**2)/(2.0 * side_A * B))),2)
			ct_set(str(side_A),str(B),str(C),str(D),str(angle_B),str(angle_C))
			
		elif (B) >0 and (C) > 0 and (E) > 0:
			angle_C = round(math.degrees(math.asin((C*math.sin(math.radians(E)))/B)),2)
			angle_A = 180 - E - angle_C
			side_A = round(B*math.sin(math.radians(angle_A))/(math.sin(math.radians(E))),2)
			ct_set(str(side_A),str(B),str(C),str(angle_A),str(E),str(angle_C))
		
		elif (B) >0 and (C) > 0 and (F) > 0:
			angle_B = round(math.degrees(math.asin((B*math.sin(math.radians(F)))/C)),2)
			angle_A = 180 - F - angle_B
			side_A = round(B*math.sin(math.radians(angle_A))/(math.sin(math.radians(angle_B))),2)
			ct_set(str(side_A),str(B),str(C),str(angle_A),str(angle_B),str(F))	

		elif (D) >0 and (E) > 0 and (A) > 0:
			angle_C = 180 - D - E
			side_B = round(A*math.sin(math.radians(E))/(math.sin(math.radians(D))),2)	
			side_C = round(A*math.sin(math.radians(angle_C))/(math.sin(math.radians(D))),2)	
			ct_set(str(A),str(side_B),str(side_C),str(D),str(E),str(angle_C))
			
		elif (D) >0 and (E) > 0 and (B) > 0:
			angle_C = 180 - D - E
			side_A = round(B*math.sin(math.radians(D))/(math.sin(math.radians(E))),2)	
			side_C = round(B*math.sin(math.radians(angle_C))/(math.sin(math.radians(E))),2)	
			ct_set(str(side_A),str(B),str(side_C),str(D),str(E),str(angle_C))
			
		elif (D) >0 and (E) > 0 and (C) > 0:
			angle_C = 180 - D - E
			side_A = round(C*math.sin(math.radians(D))/(math.sin(math.radians(angle_C))),2)	
			side_B = round(C*math.sin(math.radians(E))/(math.sin(math.radians(angle_C))),2)	
			ct_set(str(side_A),str(side_B),str(C),str(D),str(E),str(angle_C))
		
		elif (D) >0 and (F) > 0 and (A) > 0:
			angle_B = 180 - D - F
			side_B = round(A*math.sin(math.radians(angle_B))/(math.sin(math.radians(D))),2)	
			side_C = round(A*math.sin(math.radians(F))/(math.sin(math.radians(D))),2)	
			ct_set(str(A),str(side_B),str(side_C),str(D),str(angle_B),str(F))
		
		elif (D) >0 and (F) > 0 and (B) > 0:
			angle_B = 180 - D - F
			side_A = round(B*math.sin(math.radians(D))/(math.sin(math.radians(angle_B))),2)	
			side_C = round(B*math.sin(math.radians(F))/(math.sin(math.radians(angle_B))),2)	
			ct_set(str(side_A),str(B),str(side_C),str(D),str(angle_B),str(F))
			
		elif (D) >0 and (F) > 0 and (C) > 0:
			angle_B = 180 - D - F
			side_A = round(C*math.sin(math.radians(D))/(math.sin(math.radians(F))),2)	
			side_B = round(C*math.sin(math.radians(angle_B))/(math.sin(math.radians(F))),2)	
			ct_set(str(side_A),str(side_B),str(C),str(D),str(angle_B),str(F))
	
		elif (E) >0 and (F) > 0 and (A) > 0:
			angle_A = 180 - E - F
			side_B = round(A*math.sin(math.radians(E))/(math.sin(math.radians(angle_A))),2)	
			side_C = round(A*math.sin(math.radians(F))/(math.sin(math.radians(angle_A))),2)	
			ct_set(str(A),str(side_B),str(side_C),str(angle_A),str(E),str(F))
			
		elif (E) >0 and (F) > 0 and (B) > 0:
			angle_A = 180 - E - F
			side_A = round(B*math.sin(math.radians(angle_A))/(math.sin(math.radians(E))),2)
			side_C = round(B*math.sin(math.radians(F))/(math.sin(math.radians(E))),2)
			ct_set(str(side_A),str(B),str(side_C),str(angle_A),str(E),str(F))
		
		elif (E) >0 and (F) > 0 and (C) > 0:
			angle_A = 180 - E - F
			side_A = round(C*math.sin(math.radians(angle_A))/(math.sin(math.radians(F))),2)
			side_B = round(C*math.sin(math.radians(E))/(math.sin(math.radians(F))),2)
			ct_set(str(side_A),str(side_B),str(C),str(angle_A),str(E),str(F))
		else:
			messagebox.showinfo("Error", "Please enter three unknowns")

	except ValueError:
		messagebox.showinfo("Error", "The specified values do not match a valid triangle.")
		messagebox.showinfo("Error", "Please input intergers not strings")

def ct_set(a,b,c,d,e,f):
	ct_A_in.delete(0,END)
	ct_A_in.insert(0,str(a))
	ct_B_in.delete(0,END)
	ct_B_in.insert(0,str(b))
	ct_C_in.delete(0,END)
	ct_C_in.insert(0,str(c))
	ct_Angle_A_in.delete(0,END)
	ct_Angle_A_in.insert(0,str(d))
	ct_Angle_B_in.delete(0,END)
	ct_Angle_B_in.insert(0,str(e))
	ct_Angle_C_in.delete(0,END)
	ct_Angle_C_in.insert(0,str(f))


def clear():
	A_in.delete(0,END)
	A_in.insert(0,str(0))
	B_in.delete(0,END)
	B_in.insert(0,str(0))
	C_in.delete(0,END)
	C_in.insert(0,str(0))
	A_Angle_in.delete(0,END)
	A_Angle_in.insert(0,str(90))
	B_Angle_in.delete(0,END)
	B_Angle_in.insert(0,str(0))
	C_Angle_in.delete(0,END)
	C_Angle_in.insert(0,str(0))
	ct_A_in.delete(0,END)
	ct_A_in.insert(0,str(0))
	ct_B_in.delete(0,END)
	ct_B_in.insert(0,str(0))
	ct_C_in.delete(0,END)
	ct_C_in.insert(0,str(0))
	ct_Angle_A_in.delete(0,END)
	ct_Angle_A_in.insert(0,str(0))
	ct_Angle_B_in.delete(0,END)
	ct_Angle_B_in.insert(0,str(0))
	ct_Angle_C_in.delete(0,END)
	ct_Angle_C_in.insert(0,str(0))

	rat_t.clear()
	ct_t.clear()

def home():
	rat.withdraw()
	ct.withdraw()
	top.deiconify()

def goto_ct():
	top.withdraw()
	rat.withdraw()
	ct.deiconify()

def goto_rat():
	top.withdraw()
	ct.withdraw()
	rat.deiconify()

def draw(a,b,c,e,f):
	# rat_t.write("Side B", font=("Arial", 16, "normal")) #used to add text to turtle
	rat_t.penup()
	rat_t.goto(-200,-150)
	rat_t.pendown()
	hyp = 105 *a
	base = 105 *b
	opp = 105 *c
	rat_t.forward(base)
	rat_t.left(90)
	rat_t.forward(opp)
	rat_t.left(90+f)
	rat_t.forward(hyp)
	rat_t.left(90+e)
	return

box0 = Frame(top)
box0.pack()
b_1 = Button(box0, text = "Right Angle Triangle", command = goto_rat)
b_1.pack()
b_2 = Button(box0, text = "Cosine Triangle", command = goto_ct)
b_2.pack()
b_3 = Button(box0, text = "Help", command = quit)
b_3.pack()
b_4 = Button(box0, text = "Close", command = quit)
b_4.pack()

box = Frame(rat)
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

Angle_A = Label(box,text = "Angle A")
Angle_A.grid(row = 3, column = 1)
Angle_B = Label(box,text = "Angle B")
Angle_B.grid(row = 3, column = 2)
Angle_C = Label(box,text = "Angle C")
Angle_C.grid(row = 3, column = 3)

A_Angle_in = Entry(box)
A_Angle_in.grid(row = 4, column = 1)
B_Angle_in = Entry(box)
B_Angle_in.grid(row = 4, column = 2)
C_Angle_in = Entry(box)
C_Angle_in.grid(row = 4, column = 3)

cal_button = Button(box,text = "Calculate", command = lambda:rat_calculate())
cal_button.grid(row = 5, column = 2)
clear_botton = Button(box,text = "Clear", command = clear)
clear_botton.grid(row = 6, column = 2)
close_button = Button(box, text = "Close", command = quit)
close_button.grid(row = 7, column = 2)
change_button = Button(box, text = "Cosine Triangle", command = goto_ct)
change_button.grid(row = 8, column = 2)
home_button = Button(box, text = "Home", command = home)
home_button.grid(row = 9, column = 2)

box1 = Frame(ct)
box1.pack(side = BOTTOM)
Side_A = Label(box1,text = "Side A")
Side_A.grid(row = 1, column = 1)
Side_B = Label(box1,text = "Side B")
Side_B.grid(row = 1, column = 2)
Side_C = Label(box1,text = "Side C")
Side_C.grid(row = 1, column = 3)

ct_A_in = Entry(box1)
ct_A_in.grid(row = 2, column = 1)
ct_B_in = Entry(box1)
ct_B_in.grid(row = 2, column = 2)
ct_C_in = Entry(box1)
ct_C_in.grid(row = 2, column = 3)

Angle_A = Label(box1,text = "Angle A")
Angle_A.grid(row = 3, column = 1)
Angle_B = Label(box1,text = "Angle B")
Angle_B.grid(row = 3, column = 2)
Angle_C = Label(box1,text = "Angle C")
Angle_C.grid(row = 3, column = 3)

ct_Angle_A_in = Entry(box1)
ct_Angle_A_in.grid(row = 4, column = 1)
ct_Angle_B_in = Entry(box1)
ct_Angle_B_in.grid(row = 4, column = 2)
ct_Angle_C_in = Entry(box1)
ct_Angle_C_in.grid(row = 4, column = 3)

cal_button = Button(box1,text = "Calculate", command = lambda:ct_calculate())
cal_button.grid(row = 5, column = 2)
clear_botton = Button(box1,text = "Clear", command = clear)
clear_botton.grid(row = 6, column = 2)
close_button = Button(box1, text = "Close", command = quit)
close_button.grid(row = 7, column = 2)
change_button = Button(box1, text = "Right angle triange", command = goto_rat)
change_button.grid(row = 8, column = 2)
home_button = Button(box1, text = "Home", command = home)
home_button.grid(row = 9, column = 2)

clear()
top.mainloop()
