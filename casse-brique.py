from balle_pygame import *
from pygame.locals import *
from time import sleep
import random
vitesse=0.01
largeur_fenetre = 800
hauteur_fenetre = 600

class Balle:
    def __init__(self,x=50,y=20,dx=2,dy=2,taille=10):
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
        
    def collisions(self,raquette) :
        if balle.x < 0 or balle.x > largeur_fenetre-self.taille :
            balle.dx*=-1
        if balle.y < 0 :
            balle.dy*=-1
        if balle.y > hauteur_fenetre-self.taille :
            exit()
        if balle.y+balle.taille >= raquette.y and balle.y <= raquette.y+raquette.hauteur and balle.x >= raquette.x and balle.x <= raquette.x+raquette.largeur :
            balle.dy*=-1

class Raquette:
    def __init__(self,x=largeur_fenetre//2,y=hauteur_fenetre-5,largeur=50,hauteur=5):
        self.x=x
        self.y=y
        self.hauteur=hauteur
        self.largeur=largeur
    
    def tracer(self) :
        tracerRaquette(fenetre,self)
    
    def move_horizontal(self,speed) :
        self.x+=speed
    
    def move_vertical(self,speed) :
        self.y+=speed

fenetre = ouvrir_fenetre(largeur_fenetre, hauteur_fenetre)
balle=Balle(largeur_fenetre//2,hauteur_fenetre//4)
raquette=Raquette()
while True:
    effacer(fenetre)
    balle.avancer()
    balle.collisions(raquette)
    balle.tracer()
    raquette.tracer()
    actualiserAffichage(fenetre)
    sleep(vitesse)
    for event in pygame.event.get(): #détection evenement
        if event.type==MOUSEMOTION: #evenement sur la souris
            balle.x=event.pos[0] #balle placée sur le X de la souris
            balle.y=event.pos[1] #balle placée sur le Y de la souris
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        raquette.move_horizontal(5)
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        raquette.move_horizontal(-5)
    if pygame.key.get_pressed()[pygame.K_UP]:
        raquette.move_vertical(-5)
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        raquette.move_vertical(5)