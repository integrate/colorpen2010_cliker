import pygame,help,models,events
pygame.init()
screen = pygame.display.set_mode([1300, 1000])
pygame.display.set_caption("Жизнь попрошайки")
zagryschaem_shrift=pygame.font.SysFont('arial',35,True)
# загружаем картинку фона
fon = pygame.image.load('cliker_kartinki/BOMJ.png')
fon=help.izmeni_kartinku(fon,200,200,[255,255,255],20)
pygame.display.flip()

dengi=pygame.image.load('cliker_kartinki/coin_PNG36887.png')
dengi=help.izmeni_kartinku(dengi,50,50,[255,255,255],20)



def money():
    monetkis=zagryschaem_shrift.render(str(events.coins), True, [34, 54, 43])
    screen.blit(fon, [0, 45])
    screen.blit(monetkis, [60, 5])
    screen.blit(dengi, [0, 1])
    pygame.display.flip()
    screen.fill([255, 255, 255])