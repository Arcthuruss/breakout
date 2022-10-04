from balle_pygame import *
from pygame.locals import *
from random import choice
from time import sleep
import random
vitesse=0.01
largeur_fenetre = 1920
hauteur_fenetre = 1080
alive = True
pygame.font.init()
pygame.mixer.init()
font = pygame.font.Font("Monocraft.otf", 100)
pygame.mixer.music.load("sounds/musics/"+choice(["pvz_sam","Bury_the_light"])+".ogg")

class Balle:
    def __init__(self,x=50,y=20,dx=2,dy=2,taille=10):
        self.taille=taille
        self.x=x #position X
        self.y=y #position Y
        self.dx=dx #vitesse déplacement axe X
        self.dy=dy #vitesse déplacement axe Y
        self.texture = pygame.image.load("textures/vergil_face.jpg")
        
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
            global alive
            alive = False
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
balle=Balle(1,1)
raquette=Raquette()
pygame.mixer.music.play()
while alive:
    effacer(fenetre)
    balle.avancer()
    balle.collisions(raquette)
    balle.tracer()
    raquette.tracer()
    actualiserAffichage(fenetre)
    sleep(vitesse)
    pygame.event.get()
    #for event in pygame.event.get(): #détection evenement
    #    if event.type==MOUSEMOTION: #evenement sur la souris
    #        balle.x=event.pos[0] #balle placée sur le X de la souris
    #        balle.y=event.pos[1] #balle placée sur le Y de la souris
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        raquette.move_horizontal(5)
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        raquette.move_horizontal(-5)
    if pygame.key.get_pressed()[pygame.K_UP]:
        raquette.move_vertical(-5)
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        raquette.move_vertical(5)

text = font.render('RIP BOZO', False, BLACK)
fenetre.blit(text, (69, 69))
asset = pygame.image.load("textures/chair.jpeg")
fenetre.blit(asset, (100, 200))
for i in range(23) :
    gif = pygame.image.load(f"textures/gifs/sam_smile/frame_{i}_delay-0.1s.gif")
    fenetre.blit(gif, (750, 50))
    sleep(0.1)
    actualiserAffichage(fenetre)
sleep(2.5)