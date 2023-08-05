from pgzrun import go
from random import randint
import pygame

WIDTH = 600
HEIGHT = 400

pygame.mouse.set_visible(False)

timer = 60

hole = Actor('hole', (100, 100))
hole2 = Actor('hole', (300, 100))
hole3 = Actor('hole', (500, 100))

slime = Actor('slime')
hammer = Actor('hammer')


def draw():
    screen.fill((100, 150, 120))
    hole.draw()
    hole2.draw()
    hole3.draw()
    slime.draw()
    hammer.draw()


def on_mouse_down(pos):
    hammer.angle -= 45
    if slime.collidepoint(pos):
        slime.image = 'slime_hurt'


def on_mouse_up():
    hammer.angle += 45


def on_mouse_move(pos):
    hammer.pos = pos


def update():
    global timer
    timer -= 1

    if timer <= 0:
        timer = 60

        slime.image = 'slime'
        rand = randint(1, 3)
        if rand == 1:
            slime.x = hole.x
            slime.y = hole.y - 20
            animate(slime, tween='end_elastic', pos=(slime.x, slime.y - 50))
        elif rand == 2:
            slime.x = hole2.x
            slime.y = hole2.y
            animate(slime, pos=(slime.x, slime.y - 50))
        elif rand == 3:
            slime.x = hole3.x
            slime.y = hole3.y
            animate(slime, pos=(slime.x, slime.y - 50))


go()
