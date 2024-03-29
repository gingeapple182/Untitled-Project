from enum import Enum
import pygame
import random

class Suits(Enum): # define suits
  CLUB = 0
  SPADE = 1
  HEART = 2
  DIAMOND = 3

class Card: # define value and image of each card
  suit = None
  value = None
  image = None

  def __init__(self, suit, value):
    self.suit = suit
    self.value = value
    self.image = pygame.image.load('SnapPy/images/' + self.suit.name + '-' + str(self.value) + '.svg')

class Deck: 
  cards = None

  def __init__(self): # set up the values for each suit within the deck
    self.cards = []
    for suit in Suits:
      for value in range(1,14):
        self.cards.append(Card(suit, value))

  def shuffle(self): # shuffle the whole deck
    random.shuffle(self.cards)

  def deal(self): # take the last card from the deck and return it
    return self.cards.pop()

  def length(self): # count how many cards remain
    return len(self.cards)

class Pile:
  cards = None

  def __init__(self):
    self.cards = []

  def add(self, card): #add the card to the pile
    self.cards.append(card)

  def peek(self): # return the top of the pile, if no cards, return none
    if (len(self.cards) >0):
      return self.cards[-1]
    else:
      return None
    
  def popAll(self): #return all cards on the pile for the winner
    return self.cards
  
  def clear(self): # clear pile for next round
    self.cards = []

  def isSnap(self): # check if snap call is valid
    if (len(self.cards) > 1):
      return (self.cards[-1].value == self.cards[-2].value)
    return False
  
class Player:
  hand = None
  flipKey = None
  snapKey = None
  name = None

  def __init__(self, name, flipKey, snapKey):
    self.hand = []
    self.flipKey = flipKey # flip card onto pile
    self.snapKey = snapKey # press snap
    self.name = name

  def draw(self, deck): # draw a card from deck, and add it to hand
    self.hand.append(deck.deal())

  def play(self): # plays card from hand
    return self.hand.pop(0)
  
  