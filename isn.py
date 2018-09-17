 #s!/usr/bin/python
from tkinter import *
import random
global listMob
global listStuff
listMob = []
liststuff = []

#Constructeur de mob
class basicMob:

	def __init__(self, nom, hp, x, y):
		
		self.nom = nom
		self.hpMob = hp
		self.loot = random.randint(x, y)
		appndmob(self)

#Constructeur de stuff
class stuff:
	def __init__(self,nom,dmg,x):

		self.nom = nom
		self.dmgstuff = dmg
		self.cost = x
		appndstuff(self)

#Ajouter chaques mobs crées a sa lite
def appndmob(x):
	global listMob
	listMob.append(x.nom)
	
#Ajouter chaques stuffs crées a sa lite	
def appndstuff(x):
	global liststuff
	liststuff.append(x.nom)	
	
	
def affstuff(x):
	print("Vous venez de faire l'acquisition de", x.nom , "et il vous permet de faire", x.dmgstuff , "dégats suplémentaires. Il vous coûtera la maudite somme de", x.cost , "coins !")

fs = stuff("Gloire du juste",25,5000)
ts = stuff("Yeezy750",2000,300)
qs = stuff("dildoverdose",2001,301)
js = stuff("Léna",2002,302)

listlong2 = len(liststuff)-1
print()
s = random.randint(0,listlong2)
if liststuff[s] == "fs":
	affstuff(fs)
elif liststuff[s] == "ts":
	affstuff(ts)
elif liststuff[s] == "qs":
	affstuff(qs)
elif liststuff[s] == "js":
	affstuff(js)

def affichage():

	root = Tk()
	canvas = Canvas(root, width=1920, height=1080, background='white')
	ligne1 = canvas.create_line(350, 0, 350, 1080)
	ligne2 = canvas.create_line(350,420,1920,420)
	rectan1 = canvas.create_rectangle(0, 0, 351, 1080,fill='grey')
	rectan2 = canvas.create_rectangle(351, 700, 1920,1080,fill='yellow')
	rectan3 = canvas.create_rectangle(352, 0, 1920,699,fill='green',tags="click")
	canvas.tag_bind("click","<Button-1>",clicked)
	canvas.pack()

	root.mainloop()



def clicked(*args):
	print("+1")

def mob(x):
	print('Le mob ', x.nom , ' possède ', x.hpMob , 'HP et looteras ', x.loot , ' coins !')


fm = basicMob("Gargantua", 100, 5, 20)
sm = basicMob("Trivador", 250, 50, 300)
tm = basicMob("Vadot", 1000, 300, 1500)
pm = basicMob("Théo le bg du 13",2800,5000,25000) 

listlong = len(listMob)-1
print()
p = random.randint(0,listlong)
if listMob[p] == "fm":
	mob(fm)
elif listMob[p] == "sm":
	mob(sm)
elif listMob[p] == "tm":
	mob(tm)
elif listMob[p] == "pm":
	mob(pm)
affichage()
