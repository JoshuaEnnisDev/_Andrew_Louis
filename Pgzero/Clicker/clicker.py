# gives up access to pgzero
from pgzrun import go

# basic setup
WIDTH = 800
HEIGHT = 600
TITLE = 'clicker'

total_destruction = 0

# actors
bomb = Actor('bomb')
bomb.x = WIDTH / 2
bomb.y = HEIGHT / 2
bomb.destruction = 1

bomb_upgrade = Actor('buttonred', (100, 550))
bomb_upgrade.disabled = False


# draw function automatically called 60 times per second
def draw():
    bomb.draw()
    bomb_upgrade.draw()
    screen.draw.text(f"Destruction: {total_destruction}", (20, 20))


# gets called 60 times per second
def update():
    screen.fill((25, 103, 105))


# only called when mouse is clicked
def on_mouse_down(pos):
    global total_destruction
    if bomb.collidepoint(pos):
        bomb.image = 'bombflash'
        total_destruction += bomb.destruction

def on_mouse_up(pos):
    if bomb.collidepoint(pos):
        bomb.image = 'bomb'


# last line
go()
