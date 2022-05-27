import pygame, help, models, textures,random,models
def a____s():
    okno_ne_oret = pygame.event.get()
    for i in okno_ne_oret:
        if i.type == pygame.MOUSEBUTTONDOWN and i.button == pygame.BUTTON_LEFT:
            models.coins += random.randint(models.randy,models.randi)
        if i.type == pygame.MOUSEBUTTONDOWN and i.button == pygame.BUTTON_LEFT:
            x = i.pos[0]
            y = i.pos[1]
            if models.knopka1.collidepoint(x,y):
                if models.coins>=models.upgrade_coins:
                    models.upgrade += 1
                    models.randi+=2
                    models.randy+=2
                    models.upgrade_coins+=int(models.upgrade_coins/10)
                    models.coins-=models.upgrade_coins
                    print('upgrade '+str(models.upgrade))