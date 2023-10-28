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

enemies = [[], [], []]  # each enemy has a cooldown and a bullet list
random_formation = randint(0, len(enemies) - 1)
# create 10 enemy actors
for i in range(10):
    enemy = Actor("enemyblack1")
    enemy.cooldown = 60
    enemy.bullets = []
    enemy.x = i * 100 + 50
    # add enemy to the enemies list
    enemies[0].append(enemy)
for i in range(10):
    enemy = Actor("enemyblue2")
    enemy.cooldown = 60
    enemy.bullets = []
    enemy.x = i * 100 + 50
    # add enemy to the enemies list
    enemies[1].append(enemy)
for i in range(10):
    enemy = Actor("enemygreen1")
    enemy.cooldown = 60
    enemy.bullets = []
    enemy.x = i * 100 + 50
    # add enemy to the enemies list
    enemies[2].append(enemy)


def enemy_ai():
    global random_formation
    for enemy in enemies[random_formation]:
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
    global random_formationaaa 
    for enemy in enemies[random_formation]:
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
    global random_formation
    screen.clear()
    player.draw()

    # draw all enemies in the list
    for enemy in enemies[random_formation]:
        enemy.draw()
        for bullet in enemy.bullets:
            bullet.draw()

    # draws all bullets in the list
    for bullet in player.bullets:
        bullet.draw()


def update():
    global random_formation
    move_player()
    enemy_ai()
    move_enemy_bullets()
    bound_player()
    if len(enemies[random_formation]) == 0:
        random_formation = randint(0, len(enemies) - 1)
    # move the bullets
    for bullet in player.bullets:
        bullet.y -= player.bullet_speed
        if bullet.y <= 0:
            player.bullets.remove(bullet)
    # ------collisions------
    # bullet and enemy
    for enemy in enemies[random_formation]:
        if enemy.collidelist(player.bullets) != -1:
            player.bullets.pop(0)
            enemies[random_formation].remove(enemy)


def on_key_down():
    if keyboard.space:
        bullet = Actor("bullet")
        bullet.angle = 90
        bullet.x = player.x
        bullet.y = player.top
        # add bullet to list
        player.bullets.append(bullet)


pgzrun.go()
