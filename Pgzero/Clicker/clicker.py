# gives up access to pgzero
from pgzrun import go

# basic setup
WIDTH = 800
HEIGHT = 600
TITLE = 'clicker'

# actors
bomb = Actor('bomb')
bomb.x = WIDTH / 2
bomb.y = HEIGHT / 2

count = 0


# draw function automatically called 60 times per second
def draw():
    bomb.draw()


# gets called 60 times per second
def update():
    screen.fill((25, 103, 105))


# only called when mouse is clicked
def on_mouse_down(pos):
    if bomb.collidepoint(pos):
        bomb.image = 'bombflash'


def on_mouse_up(pos):
    if bomb.collidepoint(pos):
        bomb.image = 'bomb'


# last line
go()
