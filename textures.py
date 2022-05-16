import pygame,help,models
screen = pygame.display.set_mode([1300, 1000])
screen.fill([255,255,255])
pygame.display.set_caption("Жизнь попрошайки")
# загружаем картинку фона
fon = pygame.image.load('cliker_kartinki/BOMJ.png')
fon=help.izmeni_kartinku(fon,200,200,[255,255,255],20)
screen.blit(fon,[0, 1])
pygame.display.flip()



pygame.image.load('cliker_kartinki/coin_PNG36887.png')