import pgzrun

# x, y, width, height
shield = Rect(0, 0, 50, 50)
shield_color = (70, 100, 120)

player = Actor("ufoblue")


def draw():
    screen.draw.filled_rect(shield, shield_color)
    player.draw()


pgzrun.go()