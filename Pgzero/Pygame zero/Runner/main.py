from pgzrun import go

WIDTH = 800
HEIGHT = 400

#Actors
snail = Actor('snail/snail1')
snail.midbottom = (700,305)

#player variables
player = Actor('player/player_walk_1')
player.midbottom = (60,305)

#global variables
lives = 3
gravity = 0
game_over = False


def draw():
  
  if game_over == False:
    screen.blit('sky', (0,0))
    screen.blit('ground', (0,300))
    screen.draw.text("Score: ", (375, 30), color='black', fontsize=35)
    snail.draw()
    player.draw()
  else:
    screen.fill("red")
    screen.draw.text("Game Over!", (350, 200), color="black", fontsize = 50)
  
def on_key_down(key):
  global gravity
  if keyboard.space and player.bottom >= 305: 
    gravity = -20

def update():
  global gravity
  global lives
  global game_over
  
  if lives <= 0:
    game_over = True
  
  gravity += 1
  player.y += gravity
  snail.x -= 4
  
  if player.bottom >= 305:
    player.bottom= 305
  
  if snail.right < 0:
    snail.left = 800
    
  if player.colliderect(snail):
    snail.left = 800
    lives -= 1
    print(lives)
    
  
  
  

go()