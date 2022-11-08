import pygame
from random import choice

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE=(0,0,255)
RED=(255,0,0)
GREEN=(0,255,0)

#Cool color collection !!
HP1=(250, 77, 65)
HP2=(250, 111, 65)
HP3=(250, 142, 65)
HP4=(250, 210, 65)
HP5=(182, 250, 65)
HP6=(96, 250, 65)
HP7=(65, 250, 133)
HP8=(65, 250, 198)
HP9=(65, 182, 250)
JinxIsBlack=(0,0,0)

BRICK_THEME = [HP1,HP2,HP3,HP4,HP5,HP6,HP7,HP8,HP9,JinxIsBlack]


largeur_fenetre = 960
hauteur_fenetre = 540

clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.Font("Monocraft.otf", 100)
font_vies = pygame.font.Font("Monocraft.otf", 20)

with open("splash_texts.txt",'r',encoding='utf-8') as f:
    splash_text=choice(f.read().split('\n'))
icon = pygame.image.load("textures/vergil_face.jpg")

def ouvrir_fenetre(largeur, hauteur, caption):
	"""
	créé un objet fenetre de taille donnée en paramètre
	Parametre:
		largeur: integer
		hauteur: integer
	Sortie:
		objet fenetre
	"""
	pygame.display.set_icon(icon)
	pygame.display.set_caption(caption)
	fenetre = pygame.display.set_mode((largeur, hauteur), pygame.SCALED)
	fenetre.fill(WHITE)
	pygame.display.update()
	return fenetre

def tracerRaquette(fenetre, raquette):
	"""
	trace une raquette dans la fenetre
	Parametre:
		fenetre: objet fenetre
		raquette: objet raquette
	Sortie:
		rien
	"""
	pygame.draw.rect(fenetre, BLUE, (raquette.x, raquette.y, raquette.largeur, raquette.hauteur))
	
def tracerBrique(fenetre, brique):
	"""
	Trace une brique dans la fenetre
	Parametre:
		fenetre: objet fenetre
		brique: objet brique
	Sortie:
		rien
	"""
	pygame.draw.rect(fenetre, BRICK_THEME[brique.lives-1], (brique.x, brique.y, brique.largeur, brique.hauteur))

def tracerBalle(fenetre, balle):
	"""
	Trace une balle dans la fenetre
	Parametre:
		fenetre: objet fenetre
		raquette: objet balle
	Sortie:
		rien
	"""
	pygame.draw.circle(fenetre, GREEN, (balle.x+balle.taille//2, balle.y+balle.taille//2), balle.taille//2)
	
def actualiserAffichage(fenetre,rectangle=None):
	"""
	Actualise l'affichage
	Parametre:
		fenetre: objet fenetre
	Sortie:
		rien
	"""
	pygame.display.update(rectangle)
	
	
def effacer(fenetre):
	"""
	Efface la fenetre
	Parametre:
		fenetre: objet fenetre
	Sortie:
		rien
	"""
	fenetre.fill(WHITE)
	
def fermer_fenetre():
	"""
	Termine l'affichage
	Parametre:
		Aucun
	Sortie:
		rien
	"""
	pygame.quit()

def tracerTouteBrique(fenetre, liste_briques) :
	[[tracerBrique(fenetre,brick) for brick in ligne if not brick.disabled] for ligne in liste_briques]