# gives up access to pgzero
from pgzrun import go

# basic setup
WIDTH = 800
HEIGHT = 600
TITLE = 'WMD Clicker'

# gloabal variables
total_destruction = 0
auto_value = 0

# actors
bomb = Actor('bomb')
bomb.x = WIDTH / 2
bomb.y = HEIGHT / 2
bomb.destruction = 1
bomb.cost = 10

button_red = Actor('buttonred', (100, 550))
button_red.cost = 10

auto_button = Actor('buttonred', (200, 550))
auto_button.value = 0


# draw function automatically called 60 times per second
def draw():
    screen.fill((25, 103, 105))
    bomb.draw()
    button_red.draw()
    auto_button.draw()
    screen.draw.text(f"Destruction: {round(total_destruction)}", (20, 20))
    screen.draw.text("Click Increase", center=(button_red.x, button_red.y + 10))
    screen.draw.text(f"Cost: {button_red.cost}", center=(button_red.x, button_red.y + 20))


# gets called 60 times per second
def update(dt):
    global total_destruction
    total_destruction += auto_button.value * dt


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

    if auto_button.collidepoint(pos) and total_destruction >= 10:
        auto_button.image = "buttonred_pressed"
        auto_button.value += 1
        total_destruction -= 10


def on_mouse_up(pos):
    if bomb.collidepoint(pos):
        bomb.image = 'bomb'

    if button_red.collidepoint(pos):
        button_red.image = "buttonred"


# last line
go()
