import pygame, help, models, textures,random,models

def a____s():
    okno_ne_oret = pygame.event.get()
    for i in okno_ne_oret:
        if i.type == pygame.MOUSEBUTTONDOWN and i.button == pygame.BUTTON_LEFT:
            models.coins += random.randint(0, 2)
            print(models.coins)
