from random import randint 

name = input("Namn")
player_life = 100
zombie_life = 100

while player_life > 0 or zombie_life > 0:
    player_life -= randint(1, 2)
    zombie_life -= randint(1, 6)

