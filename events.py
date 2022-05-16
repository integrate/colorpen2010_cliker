import pygame, help, models, textures


def a____s():
    okno_ne_oret = pygame.event.get()
    for i in okno_ne_oret:
        if i.type == pygame.MOUSEBUTTONDOWN and i.button == pygame.BUTTON_LEFT:
            print('game_models_system:+1 money and i want go to toilet')
