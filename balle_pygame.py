import pygame

NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
BLUE=(0,0,255)
RED=(255,0,0)
GREEN=(0,255,0)

def ouvrir_fenetre(largeur, hauteur):
    """
    créé un objet fenetre de taille donnée en paramètre
    Parametre:
        largeur: integer
        hauteur: integer
    Sortie:
        objet fenetre
    """
    fenetre = pygame.display.set_mode((largeur, hauteur))
    fenetre.fill(BLANC)
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
    pygame.draw.rect(fenetre, NOIR, (brique.x, brique.y, brique.taille, brique.taille))

def tracerBalle(fenetre, balle):
    """
    Trace une balle dans la fenetre
    Parametre:
        fenetre: objet fenetre
        raquette: objet balle
    Sortie:
        rien
    """
    pygame.draw.rect(fenetre, RED, (balle.x, balle.y, balle.taille, balle.taille))
    
def actualiserAffichage(fenetre):
    """
    Actualise l'affichage
    Parametre:
        fenetre: objet fenetre
    Sortie:
        rien
    """
    pygame.display.update()
    
    
def effacer(fenetre):
    """
    Efface la fenetre
    Parametre:
        fenetre: objet fenetre
    Sortie:
        rien
    """
    fenetre.fill(BLANC)
    
def fermer_fenetre():
    """
    Termine l'affichage
    Parametre:
        Aucun
    Sortie:
        rien
    """
    pygame.quit()
