import pygame
from models import *
from engine import *

pygame.init()
bounds = (1024, 768) 
window = pygame.display.set_mode(bounds) # creates window with dimensions set in bounds
pygame.display.set_caption("SnapPy") # window/game name

gameEngine = SnapEngine()

cardBack = pygame.image.load('SnapPy/images/BACK.png') # load and scale card back image to match the rest of the cards
cardBack = pygame.transform.scale(cardBack, (int(238*0.8), int(332*0.8))) 

def renderGame(window):
  window.fill((15,0,169)) # fill background
  font = pygame.font.SysFont('comicsans',60, True) # set system font

  window.blit(cardBack, (100, 200)) # load cardback into pile locations
  window.blit(cardBack, (700, 200))

  text = font.render(str(len(gameEngine.player1.hand)) + " cards", True, (255,255,255)) # card counts
  window.blit(text, (100, 500))

  text = font.render(str(len(gameEngine.player2.hand)) + " cards", True, (255,255,255))
  window.blit(text, (700, 500))

  topCard = gameEngine.pile.peek() # show top card of pile
  if (topCard != None):
    window.blit(topCard.image, (400, 200))

  if gameEngine.state == GameState.PLAYING: # text to show current state of game to player
    text = font.render(gameEngine.currentPlayer.name + " to flip", True, (255,255,255))
    window.blit(text, (20,50))

  if gameEngine.state == GameState.SNAPPING: 
    result = gameEngine.result
    if result["isSnap"] == True:
      message = "Winning Snap! by " + result["winner"].name
    else:
      message = "False Snap! by " + result["snapCaller"].name + ". " + result["winner"].name + " wins!"
    text = font.render(message, True, (255,255,255))
    window.blit(text, (20,50))

  if gameEngine.state == GameState.ENDED:
    result = gameEngine.result
    message = "Game Over! " + result["winner"].name + " wins!"
    text = font.render(message, True, (255,255,255))
    window.blit(text, (20,50))

run = True 
while run: # run game
  key = None;
  for event in pygame.event.get(): # check if anything is happening
    if event.type == pygame.QUIT: # end game when window closed
      run = False
    if event.type == pygame.KEYDOWN: # set event to key pressed
      key = event.key

  gameEngine.play(key)
  renderGame(window) 
  pygame.display.update() # update UI when events occur

  if gameEngine.state == GameState.SNAPPING: # create time delay suring snap before moving on
    pygame.time.delay(3000)
    gameEngine.state = GameState.PLAYING