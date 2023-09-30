import pgzrun
import pygame
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

enemy1 = Actor("enemyblack1")
enemy2 = pygame.Surface((100, 100))
enemy_rect = enemy2.get_rect(center=(100, 100))
enemy3 = Actor(enemy_rect)
enemy1.x = randint(50, 950)


def draw():
    screen.clear()
    player.draw()
    enemy1.draw()

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


def on_key_down():
    if keyboard.space:
        bullet = Actor("bullet")
        bullet.angle = 90
        bullet.x = player.x
        bullet.y = player.top
        player.bullets.append(bullet)


pgzrun.go()
