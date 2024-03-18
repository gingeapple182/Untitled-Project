from enum import Enum
import pygame
from models import *

class GameState(Enum):
  PLAYING = 0 #main state of the game
  SNAPPING = 1 #when the pplayer calls snap
  ENDED = 2 #when game is over

class SnapEngine:
  deck = None
  player1 = None
  player2 = None
  pile = None
  state = None
  currentPlayer = None
  result = None

  def __init__(self):
    self.deck = Deck()
    self.deck.shuffle()
    self.player1 = Player("Player 1", pygame.K_q, pygame.K_w)
    self.player2 = Player("Player 2", pygame.K_o,pygame.K_p)
    self.pile = Pile()
    self.deal()
    self.currentPlayer = self.player1
    self.state = GameState.PLAYING