import pygame, help, models, textures

coins = 0
def a____s():
    global coins
    okno_ne_oret = pygame.event.get()
    for i in okno_ne_oret:
        if i.type == pygame.MOUSEBUTTONDOWN and i.button == pygame.BUTTON_LEFT:
            coins+=1
            print(coins)
