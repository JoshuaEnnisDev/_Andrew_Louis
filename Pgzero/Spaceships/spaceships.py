import pgzrun
from random import randint

# settings
WIDTH = 1000
HEIGHT = 600
TITLE = "Space Game"

# actors
player = Actor("player", (500, 550))
player.speed = 4
player.bullet_speed = 5
player.bullets = []

enemies = []
# create 10 enemy actors
for i in range(10):
    enemy = Actor("enemyblack1")
    enemy.x = randint(50, 950)
    # add enemy to the enemies list
    enemies.append(enemy)


def draw():
    screen.clear()
    player.draw()
    
    # draw all enemies in the list
    for enemy in enemies:
        enemy.draw()
        
    # draws all bullets in the list    
    for bullet in player.bullets:
        bullet.draw()


def update():
    # move up
    if keyboard.w:
        player.y = player.y - player.speed
    # move left
    if keyboard.a:
        player.x -= player.speed
    # move right
    if keyboard.d:
        player.x += player.speed
    # move down
    if keyboard.s:
        player.y += player.speed
    # move the bullets
    for bullet in player.bullets:
        bullet.y -= player.bullet_speed
        if bullet.y <= 0:
            player.bullets.remove(bullet)
    #------collisions------
    # bullet and enemy
    for enemy in enemies:
        if enemy.collidelist(player.bullets) != -1:
            player.bullets.pop(0)
            enemies.remove(enemy)


def on_key_down():
    if keyboard.space:
        bullet = Actor("bullet")
        bullet.angle = 90
        bullet.x = player.x
        bullet.y = player.top
        # add bullet to listy=
        player.bullets.append(bullet)


pgzrun.go()
