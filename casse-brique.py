from gestion_fenetre import *
from pygame.locals import *
from classes import *
import difficulty
from random import choice, randint
from time import sleep
import menu

caption = "Casse-Brique : " + splash_text + " | " + difficulty.difficulty

pygame.mixer.init()
if splash_text == "Ambasing" :
    pygame.mixer.music.load("sounds/musics/Ambatukam.ogg")
else :
    music=choice(["pvz_sam","Bury_the_light"])
    pygame.mixer.music.load("sounds/musics/"+music+".ogg")

fenetre = ouvrir_fenetre(largeur_fenetre, hauteur_fenetre, caption)

menu.start(fenetre)

balle=Balle(200,100)
raquette=Raquette(largeur_fenetre//2,hauteur_fenetre-40)

briques = []#Brique(150,50,10,5,1),Brique(110,10,5,10,2),Brique(170,10,10,10,3),Brique(125,25,30,5,4)]

#shut the fuck up 
if music=="Bury_the_light":
	pygame.mixer.music.play(loops=1,start=difficulty.music_timer,fade_ms=0)
else:
    pygame.mixer.music.play()
while difficulty.lives :
	effacer(fenetre)
	lives_counter=font.render('Vies : '+ str(difficulty.lives), True, RED, WHITE)
	fenetre.blit(lives_counter, (0, 0))
	balle.avancer()
	balle.collisions(raquette,briques,(largeur_fenetre, hauteur_fenetre))
	balle.tracer(fenetre)
	raquette.tracer(fenetre)
	tracerTouteBrique(fenetre,briques)
	actualiserAffichage(fenetre)
	clock.tick(difficulty.speed)
	pygame.event.get()
	if pygame.key.get_pressed()[pygame.K_RIGHT]:
		raquette.move_horizontal(5)
	if pygame.key.get_pressed()[pygame.K_LEFT]:
		raquette.move_horizontal(-5)
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