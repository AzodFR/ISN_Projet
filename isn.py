#s!/usr/bin/python
#Import du module
from tkinter import *
#Création de la fonction qui créer la page
def affichage():
	#root = la fenetre
	root = Tk()
	#Création de la "toile" sur la quelle on va afficher des choses
	canvas = Canvas(root, width=1920, height=1080, background='white')
	#Séparation en 3 de la fenêtre
	ligne1 = canvas.create_line(350, 0, 350, 1080)
	ligne2 = canvas.create_line(350,420,1920,420)
	#Ajout de couleur aux 3 parties
	rectan1 = canvas.create_rectangle(0, 0, 351, 1080,fill='grey')
	rectan2 = canvas.create_rectangle(351, 419, 1920,1080,fill='yellow')
	rectan3 = canvas.create_rectangle(352, 0, 1920,418,fill='green')
	canvas.focus_set()
	#En cours de création
	canvas.bind("<Key>", clavier)
	canvas.pack()
	print(root.winfo_pointerxy())
	#Boucle infini qui permet d'afficher tout ça
	root.mainloop()
#Fonction qui servira de detecter les clicks
def clavier(event):
    touche = event.keysym
#Appelle de la fonction pour lancer la fenêtre
affichage()
