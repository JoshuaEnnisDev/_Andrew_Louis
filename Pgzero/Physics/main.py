import pgzrun
import math

# x, y, width, height
WIDTH = 800
HEIGHT = 600

shield_color = (70, 100, 120)

player = Actor("ufoblue")
player.pos = (WIDTH // 2, HEIGHT // 2)
shield = Rect(player.right, player.top, 10, 100)
laser = Actor("laserblue13", anchor=("center", "center"))


def draw():
    screen.clear()
    #screen.draw.filled_rect(shield, shield_color)
    #screen.draw.filled_rect(Rect(player.right, player.top, 10, 100), shield_color)
    player.draw()
    laser.draw()


def on_mouse_move(pos):
    player.angle = player.angle_to(pos)
    laser.center = (math.cos(player.right), math.sin(player.top))
    print(player.topleft)

def update():
    pass
   


pgzrun.go()