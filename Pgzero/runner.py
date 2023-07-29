from pgzrun import go

WIDTH = 800
HEIGHT = 400

#Actors
snail = Actor('snail/snail1')
snail.midbottom = (700,305)
snail_timer = 30

player = Actor('player/player_walk_1')
player.midbottom = (60,305)
gravity = 0

def animinate_snail():
  if snail.image == 'snail/snail1':
    snail.image = 'snail/snail2'
  else:
    snail.image = 'snail/snail1'

def draw():
  screen.blit('sky', (0,0))
  screen.blit('ground', (0,300))
  screen.draw.text("Score: ", (375, 30), color='black', fontsize=35)
  snail.draw()
  player.draw()
  
def on_key_down(key):
  global gravity
  if keyboard.space and player.bottom >= 300: #1
    gravity = -20

def update():
  global gravity
  clock.schedule(animinate_snail, 0.5)
 
  gravity += 1
  player.y += gravity
  snail.x -= 4
  
  if player.midbottom[1] > 300:
    player.midbottom= (60, 305)
  
  if snail.right < 0:
    snail.left = 800
  
  

go()