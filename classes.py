from random import randint
import pygame
import difficulty
from pygame.locals import *
from gestion_fenetre import *

class Balle:

    def __init__(self,x=randint(25,75),y=randint(25,75),dx=2,dy=2,taille=10):
        self.taille=taille
        self.x=x  # position X
        self.y=y  # position Y
        self.dx=dx  # vitesse déplacement axe X
        self.dy=dy  # vitesse déplacement axe Y
    
    def set_pos(x,y) :
        if x != None : self.x=x
        if y != None: self.y=y
    
    def avancer(self):
        self.x=self.x+self.dx
        self.y=self.y+self.dy
    
    def tracer(self,fenetre):
        tracerBalle(fenetre,self)
        
    def collisions(self,raquette,dimensions_fenetre) :
        if self.x < 0 or self.x > dimensions_fenetre[0]-self.taille :
            self.x-=self.dx
            self.dx*=-1
        if self.y < 0 :
            self.y-=self.dy
            self.dy*=-1
        if self.y > dimensions_fenetre[1]-self.taille :
            difficulty.lives -= 1
            self.y-=self.dy
            self.dy*=-1
        if self.y+self.taille >= raquette.y and self.y <= raquette.y+raquette.hauteur and self.x >= raquette.x and self.x <= raquette.x+raquette.largeur :
            self.y-=self.dy
            self.dy*=-1


class Raquette:

    def __init__(self,x,y,largeur=50,hauteur=5):
        self.x=x
        self.y=y
        self.hauteur=hauteur
        self.largeur=largeur
    
    def tracer(self, fenetre) :
        tracerRaquette(fenetre,self)
    
    def move_horizontal(self,speed) :
        self.x+=speed
    
    def move_vertical(self,speed) :
        self.y+=speed

class InputBox :

    def __init__(self, x, y, size, base_color="BLACK", selected_color="RED", text_color="BLACK", font_path="Monocraft.otf") :
        self.text = " "
        self.font = pygame.font.Font(font_path, size)
        self.box = pygame.Rect(x, y, *self.font.size(self.text))
        self.base_color=base_color
        self.selected_color=selected_color
        self.text_color=text_color
        self.selected=False
    
    def render(self, fenetre) :
        if self.selected :
            pygame.draw.rect(fenetre, self.selected_color, self.box, 2)
        else :
            pygame.draw.rect(fenetre, self.base_color, self.box, 2)
        if self.text != " " :
            text = self.font.render(self.text, False, self.text_color)
            fenetre.blit(text, (self.box.x, self.box.y))
        actualiserAffichage(fenetre,self.box)
    
    def handle(self,fenetre,event) :
        if event.type == MOUSEBUTTONDOWN :
            if self.box.collidepoint(event.pos) and event.button == 1 :
                self.selected = True
                pygame.key.start_text_input()
            else :
                self.selected = False
                pygame.key.stop_text_input()
        
        if self.selected :
            if event.type == TEXTINPUT :
                self.text += event.text
                self.box.width,self.box.height = self.font.size(self.text)

            if event.type == KEYDOWN :
                if event.key == K_BACKSPACE :
                    self.text = self.text[:-1]
                    self.box.width,self.box.height = self.font.size(self.text)

        self.render(fenetre)

    def get_text(self) :
        return self.text