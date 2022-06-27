import pygame,help,random
coins = 10000
upgrade=0
naemnik1=False
randi=2
randy=0
upgrade_coins=10
knopka1=pygame.Rect(100,500,175,50)
knopka2=pygame.Rect(1000,0,175,50)
naem1=pygame.Rect(960,540,575,50)
def naim1():
    global naemnik1
    naemnik1=True

def tipo_def():
    global coins, upgrade_coins,upgrade,randy,randi
    if coins >= upgrade_coins:
        upgrade += 1
        randi += 2
        randy += 2
        coins -= upgrade_coins
        upgrade_coins += int(upgrade_coins / 10)
        if upgrade == 17:
            upgrade_coins = 1152
        if upgrade == 18:
            upgrade_coins = 39

            randi += 12
            randy += 12
        print('upgrade ' + str(upgrade))
