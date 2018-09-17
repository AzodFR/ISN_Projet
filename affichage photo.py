 #s!/usr/bin/python
from tkinter import *
import random
global listMob
global liststuff
import os
listMob = []
liststuff = []

#Constructeur de mob
class basicMob:

	def __init__(self, nom, hp, x, y,pic):
		
		self.nom = nom
		self.hpMob = hp
		self.loot = random.randint(x, y)
		self.pic = pic
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
	
#Provisoir pour vérifier les stuffs crées	
def affstuff(x):
	print("Vous venez de faire l'acquisition de", x.nom , "et il vous permet de faire", x.dmgstuff , "dégats suplémentaires. Il vous coûtera la maudite somme de", x.cost , "coins !")
#Création de stuffs + mobs basiques
fs = stuff("Gloire du juste",25,5000)
ts = stuff("Yeezy750",2000,300)
qs = stuff("dildoverdose",2001,301)
js = stuff("Léna",2002,302)
fm = basicMob("Gargantua", 100, 5, 20, "gargantua.png")
sm = basicMob("Trivador", 250, 50, 300, "trivador.png")
tm = basicMob("Vadot", 1000, 300, 1500, "vadot.png")
pm = basicMob("Théo le bg du 13",2800,5000,25000, "vadot.png") 

#Choix aléatoire d'un mob a partir de la liste
def choixMob():
	listlong = len(listMob)-1
	print()
	p = random.randint(0,listlong)
	if listMob[p] == "Gargantua":
		mob(fm)
	elif listMob[p] == "Trivador":
		mob(sm)
	elif listMob[p] == "Vadot":
		mob(tm)
	elif listMob[p] == "Théo le bg du 13":
		mob(pm)
    
#Choix aléatoire d'un stuff a partir de la liste 
def choixStuff():
	listlong2 = len(liststuff)-1
	print()
	s = random.randint(0,listlong2)
	if liststuff[s] == "Gloire du juste":
		affstuff(fs)
	elif liststuff[s] == "Yeezy750":
		affstuff(ts)
	elif liststuff[s] == "dildoverdose":
		affstuff(qs)
	elif liststuff[s] == "Léna":
		affstuff(js)

#Affichage des PV du mob
def mob(x):
	global txt
	global canvas
	print('Le mob ', x.nom , ' possède ', x.hpMob , 'HP et looteras ', x.loot , ' coins !')
	canvas.delete(txt)
	txt = canvas.create_text(800, 100, text=x.hpMob, font="Arial 32 italic", fill="black")
	print(x.pic)
	

#Fenêtre principal
def affichage():
	global p
	root = Tk()
	global canvas
	canvas = Canvas(root, width=1920, height=1080, background='white')
	ligne1 = canvas.create_line(350, 0, 350, 1080)
	ligne2 = canvas.create_line(350,420,1920,420)
	rectan1 = canvas.create_rectangle(0, 0, 351, 1080,fill='grey')
	rectan2 = canvas.create_rectangle(352, 500, 1920,1080,fill='yellow', tags="boutique")
	rectan3 = canvas.create_rectangle(352, 0, 1920,499,fill='green',tags="click")
	global txt
	txt = canvas.create_text(800,100, text="", font="Arial 32 italic", fill="black")

	choixMob()
	#Affichage du mob selon la fonction choixMob utilisé
	if listMob[p] == "Gargantua":
	
		photo = PhotoImage(file="gargantua.png")
		canvas.create_image(680, 155, anchor=NW, image=photo)
	elif listMob[p] == "Trivador":
		
		photo = PhotoImage(file="trivador.png")
		canvas.create_image(680, 155, anchor=NW, image=photo)
	elif listMob[p] == "Vadot":
		
		photo = PhotoImage(file="vadot.png")
		canvas.create_image(680, 155, anchor=NW, image=photo)
	elif listMob[p] == "Théo le bg du 13":
		
		photo = PhotoImage(file="gargantua.png")
		canvas.create_image(680, 155, anchor=NW, image=photo)
	#Bind du rectangle vert à la fonction clicked
	canvas.tag_bind("click","<Button-1>",clicked)
	canvas.tag_bind("boutique","<Button-1>",boutique)
	canvas.pack()

	root.mainloop()


#Provisoir -> Calculera les dégats du joueur et y déduira des PV du mob
def clicked(*args):
	print("+1")

def boutique(*args):
	boutique = Tk()
	label = Label(boutique, text="BOUTIQUE", bg="yellow")
	label.pack()
	boutique.mainloop()

affichage()
