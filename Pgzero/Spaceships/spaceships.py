import pgzrun

# settings
WIDTH = 1000
HEIGHT = 600
TITLE = "Space Game"

# actors
player = Actor("player", (500, 550))
player.speed = 4


def draw():
    screen.clear()
    player.draw()


def update():
    if keyboard.w:
        player.y = player.y - player.speed
    if keyboard.a:
        player.x -= player.speed


pgzrun.go()
