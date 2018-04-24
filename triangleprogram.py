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
rat_equation_data, ct_equation_data = "Please enter data to the calculator", "Please enter data to the calculator",
ctcanvas = Canvas(ct, width = 600, height = 400)
ctcanvas.pack(side = TOP)

ct_t = turtle.RawTurtle(ctcanvas)
ct_t.hideturtle()

top.deiconify()
ct.withdraw()
rat.withdraw()

def rat_calculate():
	global rat_equation_data
	try:
		A = float(A_in.get())
		B = float(B_in.get())
		C = float(C_in.get())
		D = 90
		E = float(B_Angle_in.get()) #angle_B
		F = float(C_Angle_in.get())	#angle_C
		
		if (A == 0 and B > 0 and C > 0):
			A = round(math.sqrt((float(B)**2) + (float(C)**2)),2)
			angle_B = round(math.degrees(math.atan(float(B)/float(C))),2)
			angle_C = 90 - angle_B
			rat_set(A,B,C,D,angle_B,angle_C)
			rat_draw(float(A),float(B),float(C),90,float(angle_B),float(angle_C))
			equation(True, 'Side A = sqrt({0}**2 + {1}**2)'.format(B,C), 'angle_B = atan(float({0})/float({1})'.format(angle_B,angle_C), 'angle C = 90 - {0}'.format(angle_B))

		elif B == 0 and A > 0 and C > 0:
			B = round(math.sqrt((float(A)**2) - (float(C)**2)),2)
			angle_B = round(math.degrees(math.acos(float(C)/float(A))),2)
			angle_C = 90 - angle_B
			rat_set(A,B,C,D,angle_B,angle_C)
			rat_draw(float(A),float(B),float(C),90,float(angle_B),float(angle_C))
			equation(True, 'Side B = sqrt({0}**2 - {1}**2)'.format(A,B), 'angle_B = acos(float({0})/float({1})'.format(C,A), 'angle C = 90 - {0}'.format(angle_B))
			
		elif C == 0 and A > 0 and B > 0:
			C = round(math.sqrt((float(A)**2) - (float(B)**2)),2)
			angle_B = round(math.degrees(math.asin(float(B)/float(A))),2)
			angle_C = 90 - angle_B
			rat_set(A,B,C,D,angle_B,angle_C)
			rat_draw(float(A),float(B),float(C),90,float(angle_B),float(angle_C))
			equation(True, 'Side C = sqrt({0}**2 - {1}**2)'.format(A,B), 'angle_B = asin(float({0})/float({1})'.format(B,A), 'angle C = 90 - {0}'.format(angle_B))

		elif E > 0 and A > 0: 
			angle_C = (90-float(E))
			B = round(float(A)*math.sin(math.radians(float(E))),2)
			C = round(float(A)*math.cos(math.radians(float(E))),2)
			angle_B = E
			rat_set(A,B,C,D,angle_B,angle_C)
			rat_draw(float(A),float(B),float(C),90,float(angle_B),float(angle_C))
			equation(True, 'Side B = {0}*sin({1})'.format(A,E), 'Side C = {0}*cos({1})'.format(A,E), 'angle_C = 90-{0}'.format(E))

		elif E > 0 and B > 0:
			angle_C = (90-float(E))
			A = round(float(B)/math.sin(math.radians(float(E))),2)
			C = round(float(B)/math.tan(math.radians(float(E))),2)
			angle_B = E
			rat_set(A,B,C,D,angle_B,angle_C)
			rat_draw(float(A),float(B),float(C),90,float(angle_B),float(angle_C))
			equation(True, 'Side A = {0}*sin({1})'.format(B,E), 'Side C = {0}*tan({1})'.format(B,E), 'angle_C = 90-{0}'.format(E))

		elif E > 0 and C > 0: 
			angle_C = (90-float(E))
			A = round(float(C)/math.cos(math.radians(float(E))),2)
			B = round(float(C)*math.tan(math.radians(float(E))),2)
			angle_B = E
			rat_set(A,B,C,D,angle_B,angle_C)
			rat_draw(float(A),float(B),float(C),90,float(angle_B),float(angle_C))
			equation(True, 'Side A = {0}*cos({1})'.format(C,E), 'Side B = {0}*tan({1})'.format(C,E), 'angle_C = 90-{0}'.format(E))

		elif F > 0 and A > 0:
			angle_B = (90-float(F))
			B = round(float(A)*math.cos(math.radians(float(F))),2)
			C = round(float(A)*math.sin(math.radians(float(F))),2)
			angle_C = F
			rat_set(A,B,C,D,angle_B,angle_C)
			rat_draw(float(A),float(B),float(C),90,float(angle_B),float(angle_C))
			equation(True, 'Side B = {0}*cos({1})'.format(A,F), 'Side C = {0}*sin({1})'.format(A,F), 'angle B = 90-{0}'.format(F))

		elif F > 0 and B > 0:
			angle_B = (90-float(F))
			A = round(float(B)/math.cos(math.radians(float(F))),2)
			C = round(float(B)*math.tan(math.radians(float(F))),2)
			angle_C = F
			rat_set(A,B,C,D,angle_B,angle_C)
			rat_draw(float(A),float(B),float(C),90,float(angle_B),float(angle_C))
			equation(True, 'Side A = {0}*cos({1})'.format(B,F), 'Side C = {0}*tan({1})'.format(B,F), 'angle B = 90-{0}'.format(F))

		elif F > 0 and C > 0:
			angle_B = (90-float(F))
			A = round(float(C)/math.sin(math.radians(float(F))),2)
			B = round(float(C)/math.tan(math.radians(float(F))),2)
			angle_C = F
			rat_set(A,B,C,D,angle_B,angle_C)
			rat_draw(float(A),float(B),float(C),90,float(angle_B),float(angle_C))
			equation(True, 'Side A = {0}*sin({1})'.format(C,F), 'Side B = {0}*tan({1})'.format(C,F), 'angle B = 90-{0}'.format(F))
		else:
			messagebox.showinfo("Error", "Please enter two unknowns")

	except ValueError:
		messagebox.showinfo("Error", "The specified values do not match a valid triangle.")
		messagebox.showinfo("Error", "Please input intergers not strings")

	

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
			ct_draw(A,B,C,angle_A,angle_B,angle_C)
			equation(False, 'Angle A = acos({1}**2 + {2}**2 - {0}**2)/(2.0 * {1} * {2})'.format(A,B,C), 
				'Angle B = acos({2}**2 + {0}**2 - {1}**2)/(2.0 * {2} * {0})'.format(A,B,C), 
				'Angle C = acos(({1}**2 + {0}**2 - {2}**2)/(2.0 * {1} * {0})'.format(A,B,C))

		elif (A) >0 and (B) > 0 and (D) > 0:
			angle_B = round(math.degrees(math.asin((B*math.sin(math.radians(D)))/A)),2)
			angle_C = 180 - D - angle_B
			side_C = round(A*math.sin(math.radians(angle_C))/(math.sin(math.radians(D))),2)
			ct_set(str(A),str(B),str(side_C),str(D),str(angle_B),str(angle_C))
			ct_draw(A,B,side_C,D,angle_B,angle_C)
			equation(False, 'Angle B = asin({0}*sin(({1})/{2})'.format(B,D,A), 'Angle C = 180 - {0} - {1}'.format(D,angle_B), 
				'Side C = {0}sin({1})/(sin({2})'.format(A,angle_C,D))

		elif (A) >0 and (B) > 0 and (E) > 0:
			angle_A = round(math.degrees(math.asin((A*math.sin(math.radians(E)))/B)),2)
			angle_C = 180 - E - angle_A
			side_C = round(A*math.sin(math.radians(angle_C))/(math.sin(math.radians(angle_A))),2)
			ct_set(str(A),str(B),str(side_C),str(angle_A),str(E),str(angle_C))
			ct_draw(A,B,side_C,angle_A,E,angle_C)
			equation(False, 'Angle A = asin({0}*sin(({1})/{2})'.format(A,E,B), 'Angle C = 180 - {0} - {1}'.format(E,angle_A), 
				'Side C = {0}sin({1})/(sin({2})'.format(A,angle_C,angle_A))

		elif (A) >0 and (B) > 0 and (F) > 0:
			side_C = round(math.sqrt((A**2 + B**2)-2*A*B*math.cos(math.radians(F))),2)
			angle_A = round(math.degrees(math.acos((B**2 + side_C**2 - A**2)/(2.0 * B *side_C))),2)
			angle_B = round(math.degrees(math.acos((A**2 + side_C**2 - B**2)/(2.0 * A *side_C))),2)
			ct_set(str(A),str(B),str(side_C),str(angle_A),str(angle_B),str(F))
			ct_draw(A,B,side_C,angle_A,angle_B,F)
			equation(False, 'Side C = sqrt({0}**2 + {1}**2)-2*{0}*{1}*math.cos({2})'.format(A,B,F),
				'Angle A = acos({1}**2 + {2}**2 - {0}**2)/(2.0 * {1} * {2})'.format(A,B,C), 
				'Angle B = acos({2}**2 + {0}**2 - {1}**2)/(2.0 * {2} * {0})'.format(A,B,C))

		elif (A) >0 and (C) > 0 and (D) > 0:
			angle_C = round(math.degrees(math.asin((C*math.sin(math.radians(D)))/A)),2)
			angle_B = 180 - D - angle_C
			side_B = round(A*math.sin(math.radians(angle_B))/(math.sin(math.radians(D))),2)
			ct_set(str(A),str(side_B),str(C),str(D),str(angle_B),str(angle_C))
			ct_draw(A,side_B,C,D,angle_B,angle_C)
			equation(False, 'Angle C = asin({0}*sin(({1})/{2})'.format(C,D,A), 'Angle B = 180 - {0} - {1}'.format(D,angle_C), 
				'Side B = {0}sin({1})/(sin({2})'.format(A,angle_B,D))
			
		elif (A) >0 and (C) > 0 and (E) > 0:
			side_B = round(math.sqrt((A**2 + C**2)-2*A*C*math.cos(math.radians(E))),2)
			angle_A = round(math.degrees(math.acos((side_B**2 + C**2 - A**2)/(2.0 * side_B *C))),2)
			angle_C = round(math.degrees(math.acos((side_B**2 + A**2 - C**2)/(2.0 * side_B *A))),2)
			ct_set(str(A),str(side_B),str(C),str(angle_A),str(E),str(angle_C))
			ct_draw(A,side_B,C,angle_A,E,angle_C)
			equation(False, 'Side B = sqrt({0}**2 + {1}**2)-2*{0}*{1}*cos({2})'.format(A,C,E), 
				'Angle A = acos({1}**2 + {2}**2 - {0}**2)/(2.0 * {1} * {2})'.format(A,side_B,C), 
				'Angle C = acos(({1}**2 + {0}**2 - {2}**2)/(2.0 * {1} * {0})'.format(A,side_B,C))
			
		elif (A) >0 and (C) > 0 and (F) > 0:
			angle_A = round(math.degrees(math.asin((A*math.sin(math.radians(F)))/C)),2)
			angle_B = 180 - F - angle_A
			side_B = round(C*math.sin(math.radians(angle_B))/(math.sin(math.radians(F))),2)
			ct_set(str(A),str(side_B),str(C),str(angle_A),str(angle_B),str(F))
			ct_draw(A,side_B,C,angle_A,angle_B,F)
			equation(False, 'Angle A = asin({0}*sin(({1})/{2})'.format(A,F,C), 'Angle B = 180 - {0} - {1}'.format(F,angle_A), 
				'Side B = {0}sin({1})/(sin({2})'.format(C,angle_B,F))

		elif (B) >0 and (C) > 0 and (D) > 0:
			side_A = round(math.sqrt((B**2 + C**2)-2*B*C*math.cos(math.radians(D))),2)
			angle_B = round(math.degrees(math.acos((side_A**2 + C**2 - B**2)/(2.0 * side_A * C))),2)
			angle_C = round(math.degrees(math.acos((side_A**2 + B**2 - C**2)/(2.0 * side_A * B))),2)
			ct_set(str(side_A),str(B),str(C),str(D),str(angle_B),str(angle_C))
			ct_draw(side_A,B,C,D,angle_B,angle_C)
			equation(False, 'Side A = sqrt({0}**2 + {1}**2)-2*{0}*{1}*cos({2})'.format(B,C,D), 
				'Angle B = acos({1}**2 + {2}**2 - {0}**2)/(2.0 * {1} * {2})'.format(B,side_A,C), 
				'Angle C = acos(({1}**2 + {0}**2 - {2}**2)/(2.0 * {1} * {0})'.format(B,side_A,C))
			
		elif (B) >0 and (C) > 0 and (E) > 0:
			angle_C = round(math.degrees(math.asin((C*math.sin(math.radians(E)))/B)),2)
			angle_A = 180 - E - angle_C
			side_A = round(B*math.sin(math.radians(angle_A))/(math.sin(math.radians(E))),2)
			ct_set(str(side_A),str(B),str(C),str(angle_A),str(E),str(angle_C))
			ct_draw(side_A,B,C,angle_A,E,angle_C)
			equation(False, 'Angle C = asin({0}*sin(({1})/{2})'.format(C,E,B), 'Angle A = 180 - {0} - {1}'.format(E,angle_C), 
				'Side A = {0}sin({1})/(sin({2})'.format(B,angle_A,E))
		
		elif (B) >0 and (C) > 0 and (F) > 0:
			angle_B = round(math.degrees(math.asin((B*math.sin(math.radians(F)))/C)),2)
			angle_A = 180 - F - angle_B
			side_A = round(B*math.sin(math.radians(angle_A))/(math.sin(math.radians(angle_B))),2)
			ct_set(str(side_A),str(B),str(C),str(angle_A),str(angle_B),str(F))
			ct_draw(side_A,B,C,angle_A,angle_B,F)
			equation(False, 'Angle B = asin({0}*sin(({1})/{2})'.format(B,F,C), 'Angle A = 180 - {0} - {1}'.format(F,angle_B), 
				'Side A = {0}sin({1})/(sin({2})'.format(B,angle_A,angle_B))

		elif (D) >0 and (E) > 0 and (A) > 0:
			angle_C = 180 - D - E
			side_B = round(A*math.sin(math.radians(E))/(math.sin(math.radians(D))),2)	
			side_C = round(A*math.sin(math.radians(angle_C))/(math.sin(math.radians(D))),2)	
			ct_set(str(A),str(side_B),str(side_C),str(D),str(E),str(angle_C))
			ct_draw(A,side_B,side_C,D,E,angle_C)
			equation(False,'Angle C = 180 - {0} - {1}'.format(D,E), 'Side B = {0}*sin({1})/(sin({2})'.format(A,E,D), 
				'Side C = {0}*sin({1})/(sin({2})'.format(A,angle_C,D))
			
		elif (D) >0 and (E) > 0 and (B) > 0:
			angle_C = 180 - D - E
			side_A = round(B*math.sin(math.radians(D))/(math.sin(math.radians(E))),2)	
			side_C = round(B*math.sin(math.radians(angle_C))/(math.sin(math.radians(E))),2)	
			ct_set(str(side_A),str(B),str(side_C),str(D),str(E),str(angle_C))
			ct_draw(side_A,B,side_C,D,E,angle_C)
			equation(False,'Angle C = 180 - {0} - {1}'.format(D,E), 'Side A = {0}*sin({1})/(sin({2})'.format(B,D,E), 
				'Side C = {0}*sin({1})/(sin({2})'.format(B,angle_C,E))
			
		elif (D) >0 and (E) > 0 and (C) > 0:
			angle_C = 180 - D - E
			side_A = round(C*math.sin(math.radians(D))/(math.sin(math.radians(angle_C))),2)	
			side_B = round(C*math.sin(math.radians(E))/(math.sin(math.radians(angle_C))),2)	
			ct_set(str(side_A),str(side_B),str(C),str(D),str(E),str(angle_C))
			ct_draw(side_A,side_B,C,D,E,angle_C)
			equation(False,'Angle C = 180 - {0} - {1}'.format(D,E), 'Side A = {0}*sin({1})/(sin({2})'.format(C,D,angle_C), 
				'Side C = {0}*sin({1})/(sin({2})'.format(C,E,angle_C))
		
		elif (D) >0 and (F) > 0 and (A) > 0:
			angle_B = 180 - D - F
			side_B = round(A*math.sin(math.radians(angle_B))/(math.sin(math.radians(D))),2)	
			side_C = round(A*math.sin(math.radians(F))/(math.sin(math.radians(D))),2)	
			ct_set(str(A),str(side_B),str(side_C),str(D),str(angle_B),str(F))
			ct_draw(A,side_B,side_C,D,angle_B,F)
			equation(False,'Angle B = 180 - {0} - {1}'.format(D,F), 'Side B = {0}*sin({1})/(sin({2})'.format(A,angle_B,D), 
				'Side C = {0}*sin({1})/(sin({2})'.format(A,F,D))
		
		elif (D) >0 and (F) > 0 and (B) > 0:
			angle_B = 180 - D - F
			side_A = round(B*math.sin(math.radians(D))/(math.sin(math.radians(angle_B))),2)	
			side_C = round(B*math.sin(math.radians(F))/(math.sin(math.radians(angle_B))),2)	
			ct_set(str(side_A),str(B),str(side_C),str(D),str(angle_B),str(F))
			ct_draw(side_A,B,side_C,D,angle_B,F)
			equation(False,'Angle B = 180 - {0} - {1}'.format(D,F), 'Side A = {0}*sin({1})/(sin({2})'.format(B,D,angle_B), 
				'Side C = {0}*sin({1})/(sin({2})'.format(B,F,angle_B))
			
		elif (D) >0 and (F) > 0 and (C) > 0:
			angle_B = 180 - D - F
			side_A = round(C*math.sin(math.radians(D))/(math.sin(math.radians(F))),2)	
			side_B = round(C*math.sin(math.radians(angle_B))/(math.sin(math.radians(F))),2)	
			ct_set(str(side_A),str(side_B),str(C),str(D),str(angle_B),str(F))
			ct_draw(side_A,side_B,C,D,angle_B,F)
			equation(False,'Angle B = 180 - {0} - {1}'.format(D,F), 'Side A = {0}*sin({1})/(sin({2})'.format(C,D,F), 
				'Side B = {0}*sin({1})/(sin({2})'.format(C,angle_B,F))
	
		elif (E) >0 and (F) > 0 and (A) > 0:
			angle_A = 180 - E - F
			side_B = round(A*math.sin(math.radians(E))/(math.sin(math.radians(angle_A))),2)	
			side_C = round(A*math.sin(math.radians(F))/(math.sin(math.radians(angle_A))),2)	
			ct_set(str(A),str(side_B),str(side_C),str(angle_A),str(E),str(F))
			ct_draw(A,side_B,side_C,angle_A,E,F)
			equation(False,'Angle B = 180 - {0} - {1}'.format(E,F), 'Side B = {0}*sin({1})/(sin({2})'.format(A,E,angle_A), 
				'Side C = {0}*sin({1})/(sin({2})'.format(A,F,angle_A))
			
		elif (E) >0 and (F) > 0 and (B) > 0:
			angle_A = 180 - E - F
			side_A = round(B*math.sin(math.radians(angle_A))/(math.sin(math.radians(E))),2)
			side_C = round(B*math.sin(math.radians(F))/(math.sin(math.radians(E))),2)
			ct_set(str(side_A),str(B),str(side_C),str(angle_A),str(E),str(F))
			ct_draw(side_A,B,side_C,angle_A,E,F)
			equation(False,'Angle A = 180 - {0} - {1}'.format(E,F), 'Side A = {0}*sin({1})/(sin({2})'.format(B,angle_A,E), 
				'Side C = {0}*sin({1})/(sin({2})'.format(C,F,E))
		
		elif (E) >0 and (F) > 0 and (C) > 0:
			angle_A = 180 - E - F
			side_A = round(C*math.sin(math.radians(angle_A))/(math.sin(math.radians(F))),2)
			side_B = round(C*math.sin(math.radians(E))/(math.sin(math.radians(F))),2)
			ct_set(str(side_A),str(side_B),str(C),str(angle_A),str(E),str(F))
			ct_draw(side_A,side_B,C,angle_A,E,F)
		else:
			messagebox.showinfo("Error", "Please enter three unknowns")

	except ValueError:
		messagebox.showinfo("Error", "The specified values do not match a valid triangle.")
		messagebox.showinfo("Error", "Please input intergers not strings")

def rat_set(a,b,c,d,e,f):
	A_in.delete(0,END)
	A_in.insert(0,str(a))
	B_in.delete(0,END)
	B_in.insert(0,str(b))
	C_in.delete(0,END)
	C_in.insert(0,str(c))
	A_Angle_in.delete(0,END)
	A_Angle_in.insert(0,str(d))
	B_Angle_in.delete(0,END)
	B_Angle_in.insert(0,str(e))
	C_Angle_in.delete(0,END)
	C_Angle_in.insert(0,str(f))

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

def rat_draw(a,b,c,d,e,f):
	rat_t.clear()
	rat_t.speed(0)
	rat_t.up()
	rat_t.goto(0,-150)
	# rat_t.write("Home = ", True, align="center", font=("Arial", 10, "normal"))
	rat_t.penup()

	if b > c :
		hyp = (350/b) * a
		base = (350/b) *b
		opp = (350/b) * c
	elif c > b or b == c:
		hyp = (300/c) * a
		base = (300/c) *b
		opp = (300/c) * c
	
	x = base/2
	rat_t.pendown()
	rat_t.forward(x) 
	rat_t.left(d)
	rat_t.forward(opp)
	rat_t.left(90+f)
	rat_t.forward(hyp)
	rat_t.left(90+e)
	rat_t.forward(x)
	rat_t.penup()
	triangle_label(hyp,base,opp,d,e,f)

def triangle_label(a,b,c,d,e,f):
	t = '''
	Hypotenuse
	  Side A
	'''
	t2 = '''
	Opposite
	  Side C
	'''
	t3 = '''
	Adjacent
	  Side B
	'''
	t4 = 'hello'
	x = a/2
	y = b/2
	q = b/4
	z = c/2
	rat_t.goto(0,-170)
	rat_t.penup()
	rat_t.right(90)
	rat_t.forward(30)
	rat_t.write(t3 ,False, align="center", font=("Arial", 10, "normal"))
	rat_t.backward(30)
	rat_t.left(90)
	
	rat_t.forward(y)
	rat_t.write("Angle A", False, align="center", font=("Arial", 10, "normal"))
	rat_t.left(d)
	rat_t.forward(z)
	rat_t.write(t2, False, align="center", font=("Arial", 10, "normal"))
	rat_t.forward(z+30)
	# rat_t.forward(z+30)
	rat_t.write("Angle B", False, align="center", font=("Arial", 10, "normal"))
	rat_t.left(90+f)
	rat_t.forward(x)
	rat_t.write(t, False, align="center", font=("Arial", 10, "normal"))
	rat_t.forward(x+30)
	rat_t.write("Angle C", False, align="center", font=("Arial", 10, "normal"))
	rat_t.left(90+e)
	
	rat_t.forward(y)

def ct_draw(a,b,c,d,e,f):
	ct_t.clear()
	ct_t.speed(0)
	ct_t.up()
	ct_t.goto(0,-150)
	# rat_t.write("Home = ", True, align="center", font=("Arial", 10, "normal"))
	ct_t.penup()

	if b > c :
		hyp = (300/b) * a
		base = (300/b) *b
		opp = (300/b) * c
	elif c > b or b == c:
		hyp = (300/c) * a
		base = (300/c) *b
		opp = (300/c) * c
	
	x = base/2
	ct_t.pendown()
	ct_t.forward(x) 
	ct_t.left(180-d)
	ct_t.forward(opp)
	ct_t.left(180-e)
	ct_t.forward(hyp)
	ct_t.left(180-f)
	ct_t.forward(x)
	ct_t.penup()
	ct_triangle_label(hyp,base,opp,d,e,f)

def ct_triangle_label(a,b,c,d,e,f):
	if a > b and a > c:
		t = '''
		Hypotenuse
		  Side A
		'''
		t2 = '''
		Opposite
		  Side C
		'''
		t3 = '''
		Adjacent
		  Side B
		'''
	else:
		t = '''
      Opposite
      Side A
		'''
		t2 = '''
		Hypotenuse
		Side C
		'''
		t3 = '''
	Adjacent
	Side B
		'''
	t4 = 'hello'
	x = a/2
	y = b/2
	q = b/4
	z = c/2
	ct_t.goto(0,-170)
	ct_t.penup()
	ct_t.right(90)
	ct_t.forward(30)
	ct_t.write(t3 ,False, align="center", font=("Arial", 10, "normal"))
	ct_t.backward(30)
	ct_t.left(90)
	ct_t.forward(y)
	ct_t.write("Angle A", False, align="center", font=("Arial", 10, "normal"))
	ct_t.left(180-d)
	ct_t.forward(z)
	ct_t.write(t2, False, align="center", font=("Arial", 10, "normal"))
	ct_t.forward(z+30)
	# ct_t.forward(z+30)
	ct_t.write("Angle B", False, align="center", font=("Arial", 10, "normal"))
	ct_t.left(180-e)
	ct_t.forward(x+30)
	ct_t.write(t, False, align="center", font=("Arial", 10, "normal"))
	ct_t.forward(x)
	ct_t.write("Angle C", False, align="center", font=("Arial", 10, "normal"))
	ct_t.left(180-f)
	ct_t.forward(y)

def gtfo():
	top.destroy()

def equation(condition,x,y,z):
	global rat_equation_data,ct_equation_data
	if condition == True:
		rat_equation_data = '''{0}
						       {1}
						   	{2}'''.format(x,y,z)
	elif condition == False:
		ct_equation_data = '''{0}
						       {1}
						   	{2}'''.format(x,y,z)

def rat_show_equations():
	global rat_equation_data
	messagebox.showinfo("Equations", "{0}".format(rat_equation_data))
	rat_equation_data = "Please enter data to the calculator"

def ct_show_equations():
	global ct_equation_data
	messagebox.showinfo("Equations", "{0}".format(ct_equation_data))
	ct_equation_data = "Please enter data to the calculator"

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
rat_equation_button = Button(box, text = "Equations", command = lambda:rat_show_equations())
rat_equation_button.grid(row = 7, column = 2)
change_button = Button(box, text = "Cosine Triangle", command = goto_ct)
# change_button.grid(row = 8, column = 2)
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
ct_equation_button = Button(box1, text = "Equations", command = lambda:ct_show_equations())
ct_equation_button.grid(row = 7, column = 2)
change_button = Button(box1, text = "Right angle triange", command = goto_rat)
# change_button.grid(row = 8, column = 2)
home_button = Button(box1, text = "Home", command = home)
home_button.grid(row = 9, column = 2)

def main():
	clear()
	top.mainloop()

if __name__ == '__main__':
	main()
