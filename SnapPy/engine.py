from enum import Enum
import pygame
from models import *

class GameState(Enum):
  PLAYING = 0 # main state of the game
  SNAPPING = 1 # when the pplayer calls snap
  ENDED = 2 # when game is over

class SnapEngine:
  deck = None
  player1 = None
  player2 = None
  pile = None
  state = None
  currentPlayer = None
  result = None

  def __init__(self): # set up each aspect of the snap feature
    self.deck = Deck()
    self.deck.shuffle()
    self.player1 = Player("Player 1", pygame.K_q, pygame.K_w)
    self.player2 = Player("Player 2", pygame.K_o,pygame.K_p)
    self.pile = Pile()
    self.deal()
    self.currentPlayer = self.player1
    self.state = GameState.PLAYING

  def deal(self): # split deck in half for each player
    half = self.deck.length() // 2
    for i in range(0, half):
      self.player1.draw(self.deck)
      self.player2.draw(self.deck)

  def switchPlayer(self): 
    if self.currentPlayer == self.player1:
      self.currentPlayer = self.player2
    else:
      self.currentPlayer = self.player1

  def winRound(self, player): # add pile to winners hand 
    self.state = GameState.SNAPPING
    player.hand.extend(self.pile.popAll())
    self.pile.clear()

  def play(self, key):
    if key == None:
      return

    if self.state == GameState.ENDED:
      return
    
    if key == self.currentPlayer.flipKey: # check if current player is pressing their key for flipping
      self.pile.add(self.currentPlayer.play())
      self.switchPlayer()

    snapCaller = None
    nonSnapCaller = None
    isSnap = self.pile.isSnap()

    if (key == self.player1.snapKey): # check who called snap
      snapCaller = self.player1
      nonSnapCaller = self.player2
    elif (key == self.player2.snapKey):
      snapCaller = self.player2
      nonSnapCaller = self.player1

    if isSnap and snapCaller: # if snap accurate, assign win to caller
      self.winRound(snapCaller)
      self.result = {
        "winner": snapCaller,
        "isSnap": True,
        "snapCaller": snapCaller
      }
      self.winRound(snapCaller)
    elif not isSnap and snapCaller: # if snap false, assign win to nonSnapCaller
      self.result = {
        "winner": nonSnapCaller,
        "isSnap": False,
        "snapCaller": snapCaller
      }
      self.winRound(nonSnapCaller)

    if len(self.player1.hand) == 0: # assign winner
      self.result = {
        "winner": self.player2,
      }
      self.state = GameState.ENDED
    elif len(self.player2.hand) == 0:
      self.result = {
        "winner": self.player1,
      }
      self.state = GameState.ENDED
