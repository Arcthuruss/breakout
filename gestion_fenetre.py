import pygame
import difficulty
from random import choice

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE=(0,0,255)
RED=(255,0,0)
GREEN=(0,255,0)

largeur_fenetre = 960
hauteur_fenetre = 540

clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.Font("Monocraft.otf", 100)

with open("splash_texts.txt",'r',encoding='utf-8') as f:
    splash_texts=f.read().split('\n')
caption = "Casse-Brique : " + choice(splash_texts) + " | " + difficulty.difficulty
icon = pygame.image.load("textures/vergil_face.jpg")

def ouvrir_fenetre(largeur, hauteur):
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
    pygame.draw.rect(fenetre, BLACK, (brique.x, brique.y, brique.taille, brique.taille))

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