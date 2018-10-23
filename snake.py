import pygame
import sys
import random
import time


class snake():
    def __init__(self):
        self.position = [100,50]
        self.corps = [[100,50],[90,50],[80,50]]
        self.direction = "droite"
        self.modifdir = self.direction
        
    def modifdirection(self,dir):
        if dir=="droite" and not self.direction=="gauche":
            self.direction="droite"
        if dir=="gauche" and not self.direction=="droite":
            self.direction="gauche"
        if dir=="haut" and not self.direction=="bas":
            self.direction="haut"
        if dir=="bas" and not self.direction=="haut":
            self.direction="bas"
        if dir=="droite" and self.direction=="gauche":
            mort()
        if dir=="gauche" and self.direction=="droite":
           mort()
        if dir=="haut" and self.direction=="bas":
            mort()
        if dir=="bas" and  self.direction=="haut":
            mort()
            
    def bouge(self,pommePos):
        if self.direction == "droite":
            self.position[0] += 10
        if self.direction == "gauche":
            self.position[0] -= 10
        if self.direction == "haut":
            self.position[1] -= 10
        if self.direction == "bas":
            self.position[1] += 10
            
        self.corps.insert(0,list(self.position))
        
        if self.position == pommePos:
            return 1
        else:
            self.corps.pop()
            return 0
            
    def verifCollision(self):
        if self.position[0] > 490 or self.position[0] < 0:
            return 1
        elif self.position[1] > 490 or self.position[1] < 0:
            return 1
            
        for PCorps in self.corps[1:]:
            if self.position == PCorps:
                return 1
        return 0
     
        
    def PosTete(self):
        return self.position
      
        
    def PosCorps(self):
        return self.corps
      
        
class generateurPomme():
    def __init__(self):
        self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
        self.manger = False
        
        
    def apparition(self):
        if self.manger == True:
            self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
            self.manger = False
        return self.position
        
    def affichagepomme(self,x):
        self.manger = x
        
        
root = pygame.display.set_mode((500,500))
pygame.display.set_caption("SNAKER")
fps = pygame.time.Clock()
difficulte = 15
score = 0
Snake = snake()
gp = generateurPomme()

def mort():
    pygame.init()
    root.fill(pygame.Color(0,0,0))
    font=pygame.font.Font(None, 24)
    text = font.render("Votre score: ",1,(255,255,255))
    text2 =font.render(str(score),1,(255,255,255))
    root.blit(text, (100,200))
    root.blit(text2, (210,200))
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()
        
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mort()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Snake.modifdirection('droite')
            elif event.key == pygame.K_LEFT:
                Snake.modifdirection('gauche')
            elif event.key == pygame.K_UP:
                Snake.modifdirection('haut')
            elif event.key == pygame.K_DOWN:
                Snake.modifdirection('bas')
    pommePos = gp.apparition()
    if (Snake.bouge(pommePos)==1):
        score += 1
        gp.affichagepomme(True)
        
    root.fill(pygame.Color(255,255,255))
    for pos in Snake.PosCorps():
        pygame.draw.rect(root, pygame.Color(0,255,0),pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(root, pygame.Color(255,0,0),pygame.Rect(pommePos[0],pommePos[1],10,10))
    if(Snake.verifCollision()==1):
        mort()
    pygame.display.set_caption("SNAKER | Score : "+str(score))
    pygame.display.flip()
    fps.tick(difficulte)
    
            
    
        
        
