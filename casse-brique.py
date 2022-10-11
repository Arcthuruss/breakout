from gestion_fenetre import *
from pygame.locals import *
from classes import *
import difficulty
from random import choice, randint
from time import sleep
import menu

pygame.mixer.init()
pygame.mixer.music.load("sounds/musics/"+choice(["pvz_sam","Bury_the_light"])+".ogg")
        

fenetre = ouvrir_fenetre(largeur_fenetre, hauteur_fenetre)
balle=Balle()
raquette=Raquette(largeur_fenetre//2,hauteur_fenetre-20)
#shut the fuck up 
pygame.mixer.music.play()
while difficulty.lives :
    effacer(fenetre)
    balle.avancer()
    balle.collisions(raquette,(largeur_fenetre, hauteur_fenetre))
    balle.tracer(fenetre)
    raquette.tracer(fenetre)
    actualiserAffichage(fenetre)
    print(f"{difficulty.lives=}")
    #sleep(vitesse)
    clock.tick(difficulty.speed)
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
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        menu.pause(fenetre)

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