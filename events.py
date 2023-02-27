import pygame, help, models, textures,random,models
TIMER_COINS=pygame.event.custom_type()#номер события
pygame.time.set_timer(TIMER_COINS,1000,1)#запускаем таймер
def a____s():
    okno_ne_oret = pygame.event.get()
    for i in okno_ne_oret:
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN and i.button == pygame.BUTTON_LEFT:
            models.coins += random.randint(models.randy,models.randi)
        if i.type == pygame.MOUSEBUTTONDOWN and i.button == pygame.BUTTON_LEFT:
            x = i.pos[0]
            y = i.pos[1]
            if models.knopka1.collidepoint(x,y):
                models.tipo_def()
            if models.knopka2.collidepoint(x,y):
                exit()
            if models.naem1.collidepoint(x,y):
                models.naim1()
        if i.type == TIMER_COINS:
            pygame.time.set_timer(TIMER_COINS, 1000, 1)  # запускаем таймер
        if models.naemnik1 == True:
            if i.type == TIMER_COINS:
                models.coins+=models.givz_namnik1