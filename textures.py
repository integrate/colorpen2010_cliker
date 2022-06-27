import pygame, help, models, models

pygame.init()
screen = pygame.display.set_mode([1920, 1080])
pygame.display.set_caption("Жизнь попрошайки")
zagryschaem_shrift = pygame.font.SysFont('arial', 35, True)
cveta = [243, 30, 15]
fon = pygame.image.load('cliker_kartinki/pereylok1.jpg')
fon = help.izmeni_kartinku(fon, 1920, 1080, [255, 255, 255], 20)
# загружаем картинку фона

dengi = pygame.image.load('cliker_kartinki/coin_PNG36887.png')
dengi = help.izmeni_kartinku(dengi, 50, 50, [255, 255, 255], 20)
d = ','
bomj = pygame.image.load('cliker_kartinki/BOMJ.png')
bomj = help.izmeni_kartinku(bomj, 350, 350, [255, 255, 255], 20)
d = ','

if models.naemnik1 == True:
        rabothi1=pygame.image.load('cliker_kartinki/lll2.jpg')
        screen.blit(rabothi1,[400,100])

def money():
    global cveta, fon
    if models.upgrade == 18:
        cveta = [243, 30, 15]
    rec = zagryschaem_shrift. render(str(models.upgrade_coins), True, [34, 54, 43])  # рисует картинку с ценой upgrade
    nemrobotnika1=zagryschaem_shrift.render("наём бродячего музыканта стои - 10000", True, [34, 54, 43],)
    recxit = zagryschaem_shrift.render('          X', True, [34, 54, 43])  # рисует картинку с ценой upgrade
    pygame.image.save(rec,'rec.png')
    monetkis = zagryschaem_shrift.render(str(models.coins), True, [34, 54, 43])
    skoko_polythis = zagryschaem_shrift.render('за щелчок даётся - ' + str(models.randy) + d + str(models.randi), True,[34, 54, 43],[255,255,255])
    if models.upgrade == 17:
        cveta = [103, 30, 176]  # фиолетовый
        rec = zagryschaem_shrift.render(str(1152), True,[34, 54, 43])  # создаёт картинку с  ценой upgrade

    if models.upgrade == 18:
        fon = pygame.image.load('cliker_kartinki/metro-london-foto1.jpg')
        fon = help.izmeni_kartinku(fon, 1920, 1080, [255, 255, 255], 20)

    screen.blit(fon, [0, 0])
    pygame.draw.rect(screen, cveta, models.knopka1)  # рисует кнопку 1
    pygame.draw.rect(screen, cveta, models.knopka2)  # рисует кнопку 2
    pygame.draw.rect(screen, cveta, models.naem1)  # рисует надпись покупки бродячего
    screen.blit(monetkis, [60, 5])
    screen.blit(recxit,models.knopka2)
    screen.blit(rec, models.knopka1)  # рисует натписи на кнопке апгрэйд
    screen.blit(nemrobotnika1, models.naem1)
    screen.blit(skoko_polythis, [550, 500])
    screen.blit(dengi, [0, 1])
    screen.blit(bomj, [0, 730])
    pygame.display.flip()
    screen.fill([255, 255, 255])
