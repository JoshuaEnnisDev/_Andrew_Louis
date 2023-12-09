import pgzrun
import random
from pgzhelper import Actor

# Bases everywhere but ther dirt path

# Screen Setup
WIDTH = 1920
HEIGHT = 1080
TITLE = "Tower Defense"

# Create actors
floor = Actor("td1920x1080")
base = Actor("base1", (500, 200))

# an empty list to hold turret actors
turrets = []

# a list with image names
enemy_images = ["person1", "person2", "person3", "person4"]
# an empty to hold enemy actors
enemies = []


# turret needs a range, bullet list
def create_turret():
    # create a turret actor
    turret = Actor("turret_green")
    turret.bullets = []
    # add the turret actor to the turrets list
    turrets.append(turret)


# built in only runs when any mouse button is pressed (event handler)
def on_mouse_down(pos):
    print(pos)


# draw function built in to pgzero
def draw():
    floor.draw()
    base.draw()
    for turret in turrets:
        turret.draw()
    for enemy in enemies:
        enemy.draw()


# main built in too pygame zero runs 60 a second
def update():
    pass


pgzrun.go()