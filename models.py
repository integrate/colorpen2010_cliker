import pygame,help,random
coins = 0
upgrade=0
naemnik1=False
randi=2
randy=0
zena_naemnika1=10000
naemnik_level1=1
givz_namnik1=0
upgrade_coins=10
knopka1=pygame.Rect(100,500,175,50)
knopka2=pygame.Rect(1000,0,175,50)
naem1=pygame.Rect(960,540,575,50)
def naim1():
    global naemnik1,coins,zena_naemnika1,givz_namnik1,naemnik_level1
    if coins >= zena_naemnika1:
        coins -= zena_naemnika1
        naemnik1=True
        zena_naemnika1+=int(zena_naemnika1*0.02)
        givz_namnik1 +=naemnik_level1
        naemnik_level1+=1


def tipo_def():
    global coins, upgrade_coins,upgrade,randy,randi
    if coins >= upgrade_coins:
        upgrade += 2
        randi += upgrade
        randy += upgrade
        coins -= upgrade_coins
        upgrade_coins += int(upgrade_coins / 10)
        if upgrade == 17:
            upgrade_coins = 1152
        if upgrade == 18:
            upgrade_coins = 39

            randi += 12
            randy += 12
        print('upgrade ' + str(upgrade))
