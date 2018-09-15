#s!/usr/bin/python
#Importation des modules
import random
from tkinter import *
global point
global x
global txt
global multp
global cost
global aze
global txt2
global price
global cost

aze = 0
multp = 0
x = 1
point = 0
cost = [15, 30, 45, 60, 75, 100, 150, 180, 250, 325, 400, 500, 650, 800, 1000, 1200, 1500, 1800, 2500, 3000]
price = cost[aze]
#Création fenêtre
root = Tk()
root.title('Clicker Game !')
def click():
	global point
	global x
	global txt
	global multp
	global txt2
	canvas.delete(txt)
	canvas.delete(txt2)

	
	point = point + x + multp
	print (x)
	print (point)
	txt = canvas.create_text(170, 100, text=point, font="Arial 16 italic", fill="blue")
	canvas.pack()
def buy():
	global point
	global multp
	global cost
	global aze
	global txt
	global txt2
	global txt4
	global txt5
	global price
	price = cost[aze]
	if point >= price :
		canvas.delete(txt)
		canvas.delete(txt4)
		canvas.delete(txt5)
		canvas.delete(txt2)
		point = point - price
		multp = multp + 1
		aze = aze + 1
		txt = canvas.create_text(170, 100, text=point, font="Arial 16 italic", fill="blue")
		txt5 = canvas.create_text(210, 280, text=multp, font="Arial 8 italic", fill="blue")
		price = cost[aze]
		txt4 = canvas.create_text(80, 280, text=price, font="Arial 8 italic", fill="blue")

		canvas.pack()
	else :
		canvas.delete(txt2)
		txt2 = canvas.create_text(200, 10, text="No enought points !", font="Arial 16 italic", fill="red")
		canvas.pack()


canvas = Canvas(root, width=1080, height=920, background='white')
txt = canvas.create_text(170, 100, text=point, font="Arial 16 italic", fill="blue")
txt2 = canvas.create_text(150, 10, text="No enought points !", font="Arial 16 italic", fill="white")
txt3 = canvas.create_text(50, 280, text="COST:", font="Arial 8 italic", fill="blue")
txt6 = canvas.create_text(180, 280, text="BONUS: +", font="Arial 8 italic", fill="blue")
txt5 = canvas.create_text(210, 280, text=multp, font="Arial 8 italic", fill="blue")
txt4 = canvas.create_text(80, 280, text=price, font="Arial 8 italic", fill="blue")
bouton=Button(root, text="HIT !", command=click)
bouton2=Button(root, text="BUY + 1", command=buy)
bouton.pack()
bouton2.pack()
canvas.pack()

root.mainloop()
