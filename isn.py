#s!/usr/bin/python
from tkinter import *
import random
class basicMob:

	def __init__(self, nom, hp, x, y):
		
		self.nom = nom
		self.hpMob = hp
		self.loot = random.randint(x, y)

def affichage():

	root = Tk()
	canvas = Canvas(root, width=1920, height=1080, background='white')
	ligne1 = canvas.create_line(350, 0, 350, 1080)
	ligne2 = canvas.create_line(350,420,1920,420)
	rectan1 = canvas.create_rectangle(0, 0, 351, 1080,fill='grey')
	rectan2 = canvas.create_rectangle(351, 419, 1920,1080,fill='yellow')
	rectan3 = canvas.create_rectangle(352, 0, 1920,418,fill='green',tags="click")
	canvas.tag_bind("click","<Button-1>",clicked)
	canvas.pack()

	root.mainloop()



def clicked(*args):
	print("+1")

affichage()
def mob(x):
	print('Le mob ', x.nom , ' possède ', x.hpMob , 'HP et looteras ', x.loot , ' coins !')


fm = basicMob("Gargantua", 100, 5, 20)
sm = basicMob("Trivador", 250, 50, 300)
tm = basicMob("Vadot", 1000, 300, 1500)
listMob = ['fm', 'sm', 'tm']
listlong = len(listMob)-1
print(listlong)
p = random.randint(0,listlong)
if listMob[p] == "fm":
	mob(fm)
elif listMob[p] == "sm":
	mob(sm)
elif listMob[p] == "tm":
	mob(tm)
