from pgzrun import go #first line
from random import randint

WIDTH = 600
HEIGHT = 400

hole = Actor('hole', (100,100))
hole2 = Actor('hole', (300, 100))
hole3 = Actor('hole', (500, 100))

timer = 60

slime = Actor('slime')

def draw():
  screen.fill((100,150,120))
  hole.draw()
  hole2.draw()
  hole3.draw()
  slime.draw()
  
def on_mouse_down(pos):
  if slime.collidepoint(pos):
    slime.image = 'slime_hurt'

def update():
  global timer
  timer -= 1
  
  if timer <= 0:
    timer = 60
    slime.image = 'slime'
    rand = randint(1,3)
    if rand == 1:
      slime.x = hole.x
    elif rand == 2:
      slime.x = hole2.x
    elif rand == 3:
      slime.x = hole3.x

go() #last line