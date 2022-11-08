from gestion_fenetre import *
from pygame.locals import *
from classes import *
import difficulty
from random import choice, randint
from time import sleep
from pattern_handler import *
import menu
import tkinter as tk
from PIL import ImageTk, Image
caption = "Casse-Brique : " + splash_text + " | " + difficulty.difficulty

def watiPopup(icon,title,path):
    popup = tk.Tk()
    popup.wm_title(title)
    popup.geometry("250x150")
    label = tk.Label(popup)
    label.pack(side="top", fill="x", pady=10)
    img = ImageTk.PhotoImage(Image.open(path))
    label = tk.Label(popup, image = img)
    label.pack(fill = "both", expand = "yes")
    B1 = tk.Button(popup, text="OK", command = popup.destroy)
    B1.pack()
    popup.mainloop()

pygame.mixer.init()
if splash_text == "Ambasing" :
    pygame.mixer.music.load("sounds/musics/Ambatukam.ogg")
else :
    music=choice(["pvz_sam","Bury_the_light"])
    pygame.mixer.music.load("sounds/musics/"+music+".ogg")

fenetre = ouvrir_fenetre(largeur_fenetre, hauteur_fenetre, caption)

menu.start(fenetre)

balle=Balle(400,400)
raquette=Raquette(largeur_fenetre//2,hauteur_fenetre-40)

briques = read_pattern(2,'Lunatic')

#shut the fuck up 
if music=="Bury_the_light":
	pygame.mixer.music.play(loops=1,start=difficulty.music_timer,fade_ms=0)
else:
    pygame.mixer.music.play()
while difficulty.lives :
	effacer(fenetre)
	lives_counter=font_vies.render('Vies : '+ str(difficulty.lives), True, RED, WHITE)
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
# THE PETER ALERT IS REAL !!!!!!!!!!!!!
if menu.difficulty == "Easy":
    watiPopup("","Peter Alert","./textures/petah.jpeg", )
text = font.render('RIP BOZO', False, BLACK, WHITE)
fenetre.blit(text, (69, 69))
asset = pygame.image.load("textures/chair.jpeg")
fenetre.blit(asset, (100, 200))
for i in range(23) :
	gif = pygame.image.load(f"textures/gifs/sam_smile/frame_{i}_delay-0.1s.gif")
	fenetre.blit(gif, (750, 50))
	sleep(0.1)
	actualiserAffichage(fenetre)
sleep(2.5)