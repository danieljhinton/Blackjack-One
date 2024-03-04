import random

# Card data

suits = ('♠', '♥', '♦', '♣')

ranks = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')

values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10,
          'J':10, 'Q':10, 'K':10, 'A':11}    # Make A 1 or 11

# Card class

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank}{self.suit}'
    
