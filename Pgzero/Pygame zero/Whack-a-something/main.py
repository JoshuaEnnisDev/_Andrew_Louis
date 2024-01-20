from pgzrun import go
from random import choice
import pygame

WIDTH = 1000
HEIGHT = 800

pygame.mouse.set_visible(False)

timer = 60

# make a list to hold all of our holes
holes = []

# creates 9 holes
for row in [0, 1, 2]:
    for col in [0, 1, 2, 3, 4]:
        hole = Actor('hole')
        hole.x = 100 + (col * 200)
        hole.y = 100 + (row * 120)
        # add to the list
        holes.append(hole)

slime = Actor('slime')
hammer = Actor('hammer')

score = 0
is_hit = False


def slime_animate():
    animate(slime, pos=(slime.x, slime.y - 30))
    clock.schedule_unique(slime_up, 1.0)


def slime_up():
    animate(slime, pos=(slime.x, slime.y + 30))


# functions that pgzero calls for us

def draw():
    screen.fill((100, 150, 120))
    screen.draw.text(f"Score:{score}", (500, 20), fontsize=35)
    for hole in holes:
        hole.draw()
    slime.draw()
    hammer.draw()


def on_mouse_down(pos):
    global score
    global is_hit
    hammer.angle -= 45
    if slime.collidepoint(pos) and not is_hit:
        is_hit = True
        slime.image = 'slime_hurt'
        score += 1


def on_mouse_up():
    hammer.angle += 45


def on_mouse_move(pos):
    hammer.pos = pos


def update():
    global timer
    global is_hit
    timer -= 1

    if timer <= 0:
        timer = 120
        is_hit = False
        slime.image = 'slime'
        # pick a random hole from the holes list
        hole = choice(holes)
        slime.x = hole.x
        slime.y = hole.y - 10
        slime_animate()


go()
