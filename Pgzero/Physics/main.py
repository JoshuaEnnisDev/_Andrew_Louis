import pgzrun

# x, y, width, height

shield_color = (70, 100, 120)

player = Actor("ufoblue")
shield = Rect(player.right, player.top, 50, 50)


def draw():
    screen.draw.filled_rect(shield, shield_color)
    player.draw()


pgzrun.go()