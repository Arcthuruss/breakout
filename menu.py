from gestion_fenetre import *
from time import sleep

difficulty = "Lunatic"

def pause(fenetre) :
    options = ["resume","quit"]
    cursor = 0
    while 1 :
        for i,v in enumerate(options) :
            text = font.render(v, False, RED if cursor == i else BLACK)
            x, y = largeur_fenetre//2, (hauteur_fenetre//3) * (i+1)
            fenetre.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))
        actualiserAffichage(fenetre)
        pygame.event.get()
        clock.tick(60)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            cursor+=1
            cursor %= len(options)
            sleep(0.1)
        if pygame.key.get_pressed()[pygame.K_UP]:
            cursor-=1
            if cursor < 0 : cursor=len(options)-1
            sleep(0.1)
        if pygame.key.get_pressed()[pygame.K_RETURN] :
            match options[cursor] :
                case "resume" :
                    return

                case "quit" :
                    exit()