import pgzrun
import random
from pgzhelper import Actor

# Screen Setup
WIDTH = 1920
HEIGHT = 1080
TITLE = "Tower Defense"

# Create actors
floor = Actor("td1920x1080")
base = Actor("base1")

# an empty list
turrents = []

# a list with image names
enemy_images = ["person1", "person2", "person3", "person4"]

pgzrun.go()