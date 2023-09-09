# gives up access to pgzero
from pgzrun import go

# basic setup
WIDTH = 800
HEIGHT = 600
TITLE = 'WMD Clicker'

total_destruction = 0

# actors
bomb = Actor('bomb')
bomb.x = WIDTH / 2
bomb.y = HEIGHT / 2
bomb.destruction = 1

button_red = Actor('buttonred', (100, 550))
button_red.cost = 10


# draw function automatically called 60 times per second
def draw():
    bomb.draw()
    button_red.draw()
    screen.draw.text(f"Destruction: {total_destruction}", (20, 20))


def reset_button(button, image):
    button.image = image


# gets called 60 times per second
def update():
    screen.fill((25, 103, 105))


# only called when mouse is clicked
def on_mouse_down(pos):
    global total_destruction
    if bomb.collidepoint(pos):
        bomb.image = 'bombflash'
        total_destruction += bomb.destruction

    if button_red.collidepoint(pos) and total_destruction >= 10:
        button_red.image = "buttonred_pressed"
        bomb.destruction += 1
        total_destruction -= 10


def on_mouse_up(pos):
    if bomb.collidepoint(pos):
        bomb.image = 'bomb'

    if button_red.collidepoint(pos):
        button_red.image = "buttonred"


# last line
go()
