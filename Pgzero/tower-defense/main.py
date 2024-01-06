import pgzrun
import random
from pgzhelper import Actor


# Screen Setup
WIDTH = 1920
HEIGHT = 1080
TITLE = "Tower Defense"

# Create actors
floor = Actor("td1920x1080")


def is_on_path(x, y):
    if 110 < x < 380 and 570 < y < 1080:
        return True
    if 350 < x < 800 and 570 < y < 800:
        return True
    if 570 < x < 820 and 120 < y < 570:
        return True
    if 830 < x < 1250 and 120 < y < 350:
        return True
    if 1000 < x < 1250 and 120 < y < 600:
        return True
    if 1250 < x < WIDTH and 350 < y < 600:
        return True

    return False


# create bases
bases = []

for row in range(0, 16):
    for col in range(0, 30):
        base = Actor("base1")
        base.left = col * 64
        base.top = row * 64
        if not is_on_path(base.left, base.top):
            bases.append(base)


# an empty list to hold turret actors
turrets = []

# a list with image names
enemy_images = ["person1", "person2", "person3", "person4"]
# an empty list to hold enemy actors
enemies = []


def add_enemy():
    # get a random image from the enemy image list
    random_enemy = random.choice(enemy_images)
    # create an enemy actor
    enemy = Actor(random_enemy)
    enemy.x = 250
    enemy.y = 1000
    enemy.angle = 90
    # add this to the enemy list
    enemies.append(enemy)
    clock.unschedule(add_enemy)
    # debug to check size of enemy list
    # print(len(enemies))


def move_enemies():
    for enemy in enemies:
        enemy.move_forward(3)


# turret needs a range, bullet list
def create_turret():
    # create a turret actor
    turret = Actor("turret_green")
    turret.bullets = []
    # add the turret actor to the turrets list
    turrets.append(turret)


# _______________PGzero built in functions__________________________________ #
# built in only runs when any mouse button is pressed (event handler)
def on_mouse_down(pos):
    print(pos)


# draw function built in to pgzero
def draw():
    floor.draw()
    for turret in turrets:
        turret.draw()
    for enemy in enemies:
        enemy.draw()
    for base in bases:
        base.draw()


# main built in to pygame zero runs 60 a second
def update():
    # runs the function once per second
    clock.schedule(add_enemy, 1.0)
    move_enemies()


pgzrun.go()
