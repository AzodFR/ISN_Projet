#s!/usr/bin/python
from tkinter import *
def affichage():

	root = Tk()
	canvas = Canvas(root, width=1920, height=1080, background='white')
	ligne1 = canvas.create_line(350, 0, 350, 1080)
	ligne2 = canvas.create_line(350,420,1920,420)
	rectan1 = canvas.create_rectangle(0, 0, 351, 1080,fill='grey')
	rectan2 = canvas.create_rectangle(351, 419, 1920,1080,fill='yellow')
	rectan3 = canvas.create_rectangle(352, 0, 1920,418,fill='green')
	canvas.focus_set()
	canvas.bind("<Key>", clavier)
	canvas.pack()
	print(root.winfo_pointerxy())
	root.mainloop()
def clavier(event):
    touche = event.keysym

affichage()