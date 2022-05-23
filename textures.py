import pygame,help,models,events,models
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
    pygame.draw.rect(screen,[243,30,154],models.knopka1)
    rec = zagryschaem_shrift.render('upgrade - 10', True, [34, 54, 43])
    monetkis=zagryschaem_shrift.render(str(models.coins), True, [34, 54, 43])
    skoko_polythis = zagryschaem_shrift.render('0-2 за щелчок', True, [34, 54, 43])
    screen.blit(fon, [0, 45])
    screen.blit(monetkis, [60, 5])
    screen.blit(rec, models.knopka1)
    screen.blit(skoko_polythis, [550, 500])
    screen.blit(dengi, [0, 1])
    pygame.display.flip()
    screen.fill([255, 255, 255])