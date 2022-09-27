from balle_pygame import *
from pygame.locals import *
from time import sleep
import random
vitesse=0.01
largeur_fenetre = 800
hauteur_fenetre = 600

class Balle:
    def __init__(self,x=50,y=20,dx=-3,dy=2,taille=10):
        self.taille=taille
        self.x=x #position X
        self.y=y #position Y
        self.dx=dx #vitesse déplacement axe X
        self.dy=dy #vitesse déplacement axe Y
        
    def avancer(self):
        self.x=self.x+self.dx
        self.y=self.y+self.dy
    
    def tracer(self):
        tracerBalle(fenetre,self)
        
fenetre = ouvrir_fenetre(largeur_fenetre, hauteur_fenetre)
balle=Balle(largeur_fenetre//2,hauteur_fenetre//4)
while True:
    effacer(fenetre)
    balle.avancer()
    balle.tracer()
    actualiserAffichage(fenetre)
    sleep(vitesse)
    for event in pygame.event.get(): #détection evenement
        if event.type==MOUSEMOTION: #evenement sur la souris
            balle.x=event.pos[0] #balle placée sur le X de la souris
            balle.y=event.pos[1] #balle placée sur le Y de la souris
