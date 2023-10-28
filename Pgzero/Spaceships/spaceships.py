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

enemies = []  # each enemy has a cooldown and a bullet list
# create 10 enemy actors
for i in range(10):
    enemy = Actor("enemyblack1")
    enemy.cooldown = 60
    enemy.bullets = []
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
    player.draw()

    # draw all enemies in the list
    for enemy in enemies:
        enemy.draw()
        for bullet in enemy.bullets:
            bullet.draw()

    # draws all bullets in the list
    for bullet in player.bullets:
        bullet.draw()


def update():
    move_player()
    enemy_ai()
    move_enemy_bullets()
    bound_player()
    # move the bullets
    for bullet in player.bullets:
        bullet.y -= player.bullet_speed
        if bullet.y <= 0:
            player.bullets.remove(bullet)
    # ------collisions------
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
        # add bullet to list
        player.bullets.append(bullet)


pgzrun.go()
