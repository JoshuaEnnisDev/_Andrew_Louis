import pgzrun
import random
from pgzhelper import Actor

# x, y, width, height
WIDTH = 800
HEIGHT = 600

shield_color = (70, 100, 120)

player = Actor("ufoblue")
player.pos = (WIDTH // 2, HEIGHT // 2)
shield = Rect(player.right, player.top, 10, 100)
laser = Actor("laserblue13", anchor=("center", "center"))
laser.scale = 2

enemies = []


def make_enemy():
    enemy = Actor("bomb")
    enemy.x = random.randint(-100, WIDTH + 100)
    if enemy.x < 0 or enemy.x > WIDTH:
        enemy.y = random.randint(0, HEIGHT)
    elif enemy.x > 0 and enemy.x < WIDTH:
        enemy.y = random.choice([-100, HEIGHT + 100])
    enemies.append(enemy)
    clock.unschedule(make_enemy)


def draw():
    screen.clear()
    #screen.draw.filled_rect(shield, shield_color)
    #screen.draw.filled_rect(Rect(player.right, player.top, 10, 100), shield_color)
    player.draw()
    laser.draw()
    for enemy in enemies:
        enemy.draw()


def on_mouse_move(pos):
    player.angle = player.angle_to(pos)
    laser.angle = player.angle + 90
    laser.rotate_with(player, 50)


def update():
    clock.schedule(make_enemy, 1.0)
    for enemy in enemies:
        enemy.move_towards(player, 3)
        if enemy.colliderect(laser):
            enemies.remove(enemy)
            print("You dont lose")
        elif enemy.colliderect(player):
            enemies.remove(enemy)
            print("You lose")
        


pgzrun.go()