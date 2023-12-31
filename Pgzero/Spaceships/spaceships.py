import pgzrun
from random import randint
from pgzhelper import *

# settings
WIDTH = 1000
HEIGHT = 600
TITLE = "Space Game"

game_over = False

# actors
player = Actor("player", (500, 550))
player.speed = 4
player.bullet_speed = 5
player.bullets = []
player.bullet_powerup = False

enemies = []  # each enemy has a cooldown and a bullet list
upgrades = []  # holds our powerups
# create 10 enemy actors
for i in range(10):
    enemy = Actor("enemyblack1")
    enemy.cooldown = 60
    enemy.bullets = []
    enemy.drop_chance = randint(0, 100)
    enemy.x = i * 100 + 50
    # add enemy to the enemies list
    enemies.append(enemy)


def enemy_ai():
    for enemy in enemies:
        enemy.cooldown -= 1
        if enemy.cooldown <= 0:
            enemy.cooldown = 60
            rand = randint(1, 5)
            if rand < 4:
                enemy.y += 50
            else:
                bullet = Actor("bullet")
                bullet.angle = 180
                bullet.speed = randint(1, 4)
                bullet.pos = enemy.pos
                enemy.bullets.append(bullet)


def move_enemy_bullets():
    for enemy in enemies:
        for bullet in enemy.bullets:
            bullet.y += bullet.speed


def bound_player():
    if player.left < 0:
        player.left = 0
    if player.top <= 0:
        player.top = 0
    if player.right >= WIDTH:
        player.right = WIDTH
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT


def move_player():
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


def draw():
    screen.clear()
    if not game_over:
        player.draw()

        # draw all enemies in the list
        for enemy in enemies:
            enemy.draw()
            for bullet in enemy.bullets:
                bullet.draw()

        # draws all bullets in the list
        for bullet in player.bullets:
            bullet.draw()

        for drop in upgrades:
            drop.draw()

    else:
        screen.draw.text("Game Over", (450, 300), fontsize=45)


def update():
    move_player()
    enemy_ai()
    move_enemy_bullets()
    bound_player()
    global game_over
    
    for powerup in upgrades:
        powerup.y += 3
        if player.colliderect(powerup):
            # give the player a powerup
            player.bullet_powerup = True
            # remove the power from the list
            upgrades.remove(powerup)
            
    # move the bullets
    for i, bullet in enumerate(player.bullets):
        if player.bullet_powerup:
            bullet.move_forward(player.bullet_speed)
        else:
            # moves the one bullet
            bullet.y -= player.bullet_speed
        if bullet.y <= 0:
            player.bullets.remove(bullet)
    # ------collisions------
    # bullet and enemy
    for enemy in enemies:
        if enemy.collidelist(player.bullets) != -1:
            player.bullets.pop(0)
            add_powerup(enemy.pos, enemy.drop_chance)
            enemies.remove(enemy)
        if player.collidelist(enemy.bullets) != -1:
            game_over = True


def add_powerup(pos, drop_chance):
    if drop_chance < 20:
        drop = Actor("bolt", pos)
        upgrades.append(drop)


def on_key_down():
    if keyboard.space:
        if player.bullet_powerup:
            for i in range(3):
                bullet = Actor("bullet")
                bullet.x = player.x
                bullet.y = player.top
                bullet.angle = i * 45 + 45
                player.bullets.append(bullet)
        else:
            bullet = Actor("bullet")
            bullet.angle = 90
            bullet.x = player.x
            bullet.y = player.top
            # add bullet to list
            player.bullets.append(bullet)


pgzrun.go()
